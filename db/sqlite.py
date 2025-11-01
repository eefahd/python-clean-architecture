import os
import sqlite3
from sqlite3 import Connection
from typing import Optional

from db.db_interface import DbInterface

DEFAULT_DB_PATH = "contacts.db"


class SqliteDb(DbInterface):
    def __init__(self) -> None:
        self.conn: Optional[Connection] = None

    def connect(self) -> None:
        self.conn = sqlite3.connect(os.getenv("DB_PATH", DEFAULT_DB_PATH))
        self.conn.row_factory = sqlite3.Row

    def disconnect(self) -> None:
        if self.conn is not None:
            self.conn.close()
            self.conn = None

    def init(self, with_demo: bool = False) -> None:
        already_connected = self.client is not None
        if not already_connected:
            self.connect()

        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        """
        )

        if with_demo:
            demo_contacts = [
                ("John", "Doe", "john.doe@example.com"),
                ("Jane", "Smith", "jane.smith@example.com"),
            ]

            self.conn.executemany(
                """
                INSERT OR IGNORE INTO contacts (first_name, last_name, email)
                VALUES (?, ?, ?)
                """,
                demo_contacts,
            )

        self.conn.commit()
        if not already_connected:
            self.disconnect()
