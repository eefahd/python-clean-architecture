import abc

from db.db_interface import DbInterface
from repositories.repository_model import Repository


class RepositoryInterface(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def create(db: DbInterface) -> Repository:
        pass
