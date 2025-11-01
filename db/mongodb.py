import os
from typing import Optional

from pymongo import MongoClient
from pymongo.database import Database

from db.db_interface import DbInterface

DEFAULT_MONGODB_URI: str = "mongodb://localhost:27017/"
DEFAULT_DB_NAME: str = "contacts_db"


class MongoDb(DbInterface):
    def __init__(self) -> None:
        self.client: Optional[MongoClient] = None
        self.db: Optional[Database] = None

    def connect(self) -> None:
        self.client = MongoClient(os.getenv("MONGO_URI", DEFAULT_MONGODB_URI))
        self.db = self.client[os.getenv("DB_NAME", DEFAULT_DB_NAME)]
        print("Connected to the MongoDB database!")

    def disconnect(self) -> None:
        if self.client is not None:
            self.client.close()
            self.client = None

    def init(self, with_demo: bool = False) -> None:
        already_connected = self.client is not None
        if not already_connected:
            self.connect()
        self.db.contacts.create_index("email", unique=True)

        if with_demo:
            demo_contacts = [
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "email": "john.doe@example.com",
                },
                {
                    "first_name": "Jane",
                    "last_name": "Smith",
                    "email": "jane.smith@example.com",
                },
            ]

            for contact in demo_contacts:
                self.db.contacts.update_one(
                    {"email": contact["email"]}, {"$setOnInsert": contact}, upsert=True
                )

        if not already_connected:
            self.disconnect()
