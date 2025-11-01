import os
from typing import Dict, Type

from db.db_interface import DbInterface
from repositories.base.repository_interface import RepositoryInterface
from repositories.mongodb.repository import MongodbRepositoryFactory
from repositories.repository_model import Repository
from repositories.sqlite.repository import SqliteRepositoryFactory

DB_TYPE: str = os.getenv("DB_TYPE", "sqlite")  # "sqlite" or "mongodb"


def create_repository(db: DbInterface) -> Repository:
    repositories_map: Dict[str, Type[RepositoryInterface]] = {
        "sqlite": SqliteRepositoryFactory,
        "mongodb": MongodbRepositoryFactory,
    }

    repo_cls = repositories_map[DB_TYPE]
    repo_obj = repo_cls.create(db)
    return repo_obj
