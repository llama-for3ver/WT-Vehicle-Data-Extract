from peewee import (
    PostgresqlDatabase,
    TextField,
    IntegerField,
    FloatField,
    BooleanField,
    Model,
    CompositeKey,
    DecimalField,
    DoubleField,
)
from playhouse.sqlite_ext import JSONField
from dotenv import load_dotenv

from os import environ as env

load_dotenv()


db = PostgresqlDatabase(
    env.get("DB_DATABASE"),
    user=env.get("DB_USER"),
    host=env.get("DB_HOST"),
    port=env.get("DB_PORT"),
    password=env.get("DB_PASSWORD"),
)


class BaseModel(Model):
    class Meta:
        database = db


class Vehicle(BaseModel):
    identifier = TextField(primary_key=True)
    country = TextField()
    vehicle_type = TextField()
    vehicle_sub_types = JSONField(null=True, default=[])
    event = TextField(null=True)
    release_date = TextField(null=True)
    version = TextField()
    era = IntegerField()
    arcade_br = DecimalField()
    realistic_br = DecimalField()
    realistic_ground_br = DecimalField()
    simulator_br = DecimalField()
    simulator_ground_br = DecimalField()
    value = IntegerField()
    req_exp = IntegerField()
    is_premium = BooleanField(default=False)
    is_pack = BooleanField(default=False)
    on_marketplace = BooleanField(default=False)
    squadron_vehicle = BooleanField(default=False)
    ge_cost = IntegerField()
    crew_total_count = IntegerField()
    visibility = IntegerField()
    hull_armor = JSONField(null=True, default=[])
    turret_armor = JSONField(null=True, default=[])
    mass = DoubleField()
    train1_cost = IntegerField()
    train2_cost = IntegerField()
    train3_cost_gold = IntegerField()
    train3_cost_exp = IntegerField()
    sl_mul_arcade = DecimalField()
    sl_mul_realistic = DecimalField()
    sl_mul_simulator = DecimalField()
    exp_mul = DecimalField()
    repair_time_arcade = DecimalField()
    repair_time_realistic = DecimalField()
    repair_time_simulator = DecimalField()
    repair_time_no_crew_arcade = DecimalField()
    repair_time_no_crew_realistic = DecimalField()
    repair_time_no_crew_simulator = DecimalField()
    repair_cost_arcade = IntegerField()
    repair_cost_realistic = IntegerField()
    repair_cost_simulator = IntegerField()
    repair_cost_per_min_arcade = IntegerField()
    repair_cost_per_min_realistic = IntegerField()
    repair_cost_per_min_simulator = IntegerField()
    repair_cost_full_upgraded_arcade = IntegerField()
    repair_cost_full_upgraded_realistic = IntegerField()
    repair_cost_full_upgraded_simulator = IntegerField()
    required_vehicle = TextField(null=True)
    engine = JSONField(null=True, default={})
    modifications = JSONField(null=True, default={})
    ir_devices = JSONField(null=True, default={})
    thermal_devices = JSONField(null=True, default={})
    ballistic_computer = JSONField(null=True, default={})
    aerodynamics = JSONField(null=True, default={})
    has_customizable_weapons = BooleanField()
    weapons = JSONField(null=True, default=[])
    presets = JSONField(null=True, default=[])
    customizable_presets = JSONField(null=True, default=False)

    class Meta:
        database = db
        db_table = "vehicle"


class VehicleOld(BaseModel):
    identifier = TextField()
    country = TextField()
    vehicle_type = TextField()
    vehicle_sub_types = JSONField(null=True, default=[])
    event = TextField(null=True)
    release_date = TextField(null=True)
    version = TextField()
    era = IntegerField()
    arcade_br = DecimalField()
    realistic_br = DecimalField()
    realistic_ground_br = DecimalField()
    simulator_br = DecimalField()
    simulator_ground_br = DecimalField()
    value = IntegerField()
    req_exp = IntegerField()
    is_premium = BooleanField(default=False)
    is_pack = BooleanField(default=False)
    on_marketplace = BooleanField(default=False)
    squadron_vehicle = BooleanField(default=False)
    ge_cost = IntegerField()
    crew_total_count = IntegerField()
    visibility = IntegerField()
    hull_armor = JSONField(null=True, default=[])
    turret_armor = JSONField(null=True, default=[])
    mass = DecimalField(25, 10, True)
    train1_cost = IntegerField()
    train2_cost = IntegerField()
    train3_cost_gold = IntegerField()
    train3_cost_exp = IntegerField()
    sl_mul_arcade = DecimalField()
    sl_mul_realistic = DecimalField()
    sl_mul_simulator = DecimalField()
    exp_mul = DecimalField()
    repair_time_arcade = DecimalField()
    repair_time_realistic = DecimalField()
    repair_time_simulator = DecimalField()
    repair_time_no_crew_arcade = DecimalField()
    repair_time_no_crew_realistic = DecimalField()
    repair_time_no_crew_simulator = DecimalField()
    repair_cost_arcade = IntegerField()
    repair_cost_realistic = IntegerField()
    repair_cost_simulator = IntegerField()
    repair_cost_per_min_arcade = IntegerField()
    repair_cost_per_min_realistic = IntegerField()
    repair_cost_per_min_simulator = IntegerField()
    repair_cost_full_upgraded_arcade = IntegerField()
    repair_cost_full_upgraded_realistic = IntegerField()
    repair_cost_full_upgraded_simulator = IntegerField()
    required_vehicle = TextField(null=True)
    engine = JSONField(null=True, default={})
    modifications = JSONField(null=True, default={})
    ir_devices = JSONField(null=True, default={})
    thermal_devices = JSONField(null=True, default={})
    ballistic_computer = JSONField(null=True, default={})
    aerodynamics = JSONField(null=True, default={})
    has_customizable_weapons = BooleanField()
    weapons = JSONField(null=True, default=[])
    presets = JSONField(null=True, default=[])
    customizable_presets = JSONField(null=True, default=False)

    class Meta:
        database = db
        db_table = "vehicleold"
        primary_key = CompositeKey("identifier", "version")


db.create_tables([Vehicle, VehicleOld], safe=True)
