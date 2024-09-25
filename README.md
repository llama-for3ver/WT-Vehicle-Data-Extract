# WT Vehicle Data Extract

## Introduction

This is a repo containing all the scripts used to parse data from War Thunder and store it in a database.

## Requirements

- Python 3.10+

## How to use

1. Clone this repo `git clone https://github.com/llama-for3ver/WT-Vehicle-Data-Extract.git`
2. Clone [War Thunder Datamine](https://github.com/gszabi99/War-Thunder-Datamine) `git clone https://github.com/gszabi99/War-Thunder-Datamine.git`
   > [!warning] This repo is very large, and it will take a while to clone. You can use --depth=1 to download only the latest files, which greatly speeds up cloning and should be sufficient.
3. Specify in `.env` (placed inside the utils folder) the path to the datamine repo:
   ```
   DATAMINE_LOCATION="path/to/datamine/repo"
   ```
4. Also add details for the Postgres database in the `.env` file (placed in root):
   ```
   DB_DATABASE=postgres
   DB_USER=postgres
   DB_PASSWORD=postgres
   DB_HOST=localhost
   DB_PORT=5432
   ```
5. Run `main.py` in the root directory of this repo.

The full execution of the script will result in a `vehicle` and `vehicleold` being created/updated in the Postgres database
JSON files will be created in the `nations` folder, images copied to the assets folder and JSON localisation files in locales.

<!-- Warning: if the generated database file already exists, versioning feature will automatically be enabled. This means that all the vehicles that have been modified since the last major update will be moved into another table called "vehicles_old" and the new vehicles will be added to the main table. -->
> [!warning]
> If there is already data in the database, versioning will be enabled. This means that all the vehicles that have been modified since the last major update will be moved into another table called "vehicles_old" and the new vehicles will be added to the main table.

## TODO

- [ ] Document the code.
- [ ] Use Docker.
- [x] Add automatic updating.

## How to contribute

1. Fork the repo
2. Make your changes
3. Create a pull request