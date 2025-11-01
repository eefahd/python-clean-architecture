import abc
from typing import List, Optional

from db.db_interface import DbInterface
from models.contact import Contact


class ContactRepositoryInterface(abc.ABC):
    def __init__(self, db: DbInterface) -> None:
        pass

    @abc.abstractmethod
    def create(self, contact: Contact) -> None:
        pass

    @abc.abstractmethod
    def list_all(self) -> List[Contact]:
        pass

    @abc.abstractmethod
    def get_by_email(self, contact_email: str) -> Optional[Contact]:
        pass
