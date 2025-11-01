from typing import List, Optional

from pymongo.database import Database

from db.db_interface import DbInterface
from models.contact import Contact
from repositories.base.contact_repository_interface import ContactRepositoryInterface


class MongoDBContactRepository(ContactRepositoryInterface):
    def __init__(self, db: DbInterface) -> None:
        assert db.db is not None
        self.db: Optional[Database] = db.db

    def create(self, contact: Contact) -> None:
        self.db.contacts.insert_one(contact.dict())

    def list_all(self) -> List[Contact]:
        return [Contact(**data) for data in self.db.contacts.find({}, {"_id": 0})]

    def get_by_email(self, contact_email: str) -> Optional[Contact]:
        contact = self.db.contacts.find_one({"email": contact_email}, {"_id": 0})
        if not contact:
            return None
        return Contact(**contact)
