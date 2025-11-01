from db.db_interface import DbInterface
from repositories.base.repository_interface import RepositoryInterface
from repositories.mongodb.contact_repository import MongoDBContactRepository
from repositories.repository_model import Repository


class MongodbRepositoryFactory(RepositoryInterface):
    @staticmethod
    def create(db: DbInterface) -> Repository:
        return Repository(contact=MongoDBContactRepository(db))
