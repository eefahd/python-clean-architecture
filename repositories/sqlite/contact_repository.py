from sqlite3 import Connection
from typing import List, Optional

from db.db_interface import DbInterface
from models.contact import Contact
from repositories.base.contact_repository_interface import ContactRepositoryInterface


class SQLiteContactRepository(ContactRepositoryInterface):
    def __init__(self, db: DbInterface) -> None:
        self.conn: Optional[Connection] = db.conn

    def create(self, contact: Contact) -> None:
        self.conn.execute(
            "INSERT INTO contacts (first_name, last_name, email) VALUES (?, ?, ?)",
            (contact.first_name, contact.last_name, contact.email),
        )
        self.conn.commit()

    def list_all(self) -> List[Contact]:
        rows = self.conn.execute("SELECT * FROM contacts").fetchall()
        return [Contact(**dict(data)) for data in rows]

    def get_by_email(self, contact_email: str) -> Optional[Contact]:
        row = self.conn.execute(
            "SELECT * FROM contacts WHERE email = ?", (contact_email,)
        ).fetchone()
        if not row:
            return None
        return Contact(**dict(row))
