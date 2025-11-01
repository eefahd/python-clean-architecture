from db.db_interface import DbInterface
from repositories.base.repository_interface import RepositoryInterface
from repositories.repository_model import Repository
from repositories.sqlite.contact_repository import SQLiteContactRepository


class SqliteRepositoryFactory(RepositoryInterface):
    @staticmethod
    def create(db: DbInterface) -> Repository:
        return Repository(contact=SQLiteContactRepository(db))
