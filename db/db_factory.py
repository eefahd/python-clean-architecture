import os
from typing import Dict, Type

from db.db_interface import DbInterface
from db.mongodb import MongoDb
from db.sqlite import SqliteDb

DB_TYPE: str = os.getenv("DB_TYPE", "sqlite")  # "sqlite" or "mongodb"


def get_db() -> DbInterface:
    databases_map: Dict[str, Type[DbInterface]] = {
        "sqlite": SqliteDb,
        "mongodb": MongoDb,
    }

    database_cls = databases_map[DB_TYPE]
    database_obj = database_cls()
    return database_obj
