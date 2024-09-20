import json
from deepdiff import DeepDiff
from peewee import DoesNotExist, chunked
from playhouse.shortcuts import model_to_dict
from tqdm import tqdm
from dotenv import load_dotenv
from utils import cLogger, COUNTRIES
from .models import db, Vehicle, VehicleOld
from concurrent.futures import ThreadPoolExecutor

load_dotenv()


def process_vehicle_data(country, vehicle_category):
    try:
        with open(
            f"nations/{country}/{country}Final{vehicle_category}.json", "r"
        ) as file:
            vehicles_data = json.load(file)

        db_vehicles = {
            v.identifier: v
            for v in Vehicle.select().where(
                Vehicle.identifier << [v["identifier"] for v in vehicles_data]
            )
        }
        new_vehicles = []
        vehicles_to_update = []

        for vehicle_data in tqdm(vehicles_data):
            current_version = vehicle_data.pop("version")

            db_vehicle = db_vehicles.get(vehicle_data["identifier"], None)

            if db_vehicle:
                db_vehicle_dict = model_to_dict(db_vehicle, recurse=False)
                db_version = db_vehicle_dict.pop("version")

                diff = DeepDiff(db_vehicle_dict, vehicle_data, ignore_order=True)
                if diff:
                    if (
                        current_version.split(".")[0] >= db_version.split(".")[0]
                        and current_version.split(".")[1] > db_version.split(".")[1]
                    ):
                        db_vehicle_dict["version"] = db_version
                        vehicles_to_update.append(VehicleOld(**db_vehicle_dict))

                        vehicle_data["version"] = current_version
                        new_vehicles.append(vehicle_data)
                    else:
                        cLogger.info(
                            f'{vehicle_data["identifier"]} version updated: {db_version} --> {current_version}'
                        )
                        for key, value in vehicle_data.items():
                            setattr(db_vehicle, key, value)
                        db_vehicle.version = current_version
                        vehicles_to_update.append(db_vehicle)
                else:
                    db_vehicle.version = current_version
                    vehicles_to_update.append(db_vehicle)
            else:
                vehicle_data["version"] = current_version
                new_vehicles.append(vehicle_data)

        with db.atomic():
            if new_vehicles:
                for vehicles_chunk in chunked(new_vehicles, 100):
                    Vehicle.insert_many(vehicles_chunk).execute()
            if vehicles_to_update:
                Vehicle.bulk_update(vehicles_to_update, fields=["version"])
                if vehicles_to_update:
                    VehicleOld.insert_many(vehicles_to_update).execute()

    except FileNotFoundError:
        pass


def update_db():
    with ThreadPoolExecutor() as executor:
        for country in COUNTRIES:
            cLogger.info(f"Updating {country}")
            executor.map(
                process_vehicle_data, [country] * 3, ["Aircrafts", "Tanks", "Ships"]
            )
