from typing import List

from models.contact import Contact
from repositories.base.contact_repository_interface import ContactRepositoryInterface


class ContactService:
    def __init__(self, contact_repo: ContactRepositoryInterface) -> None:
        self.contact_repo = contact_repo

    def create_contact(self, contact: Contact) -> None:
        self.contact_repo.create(contact)

    def list_contacts(self) -> List[Contact]:
        return self.contact_repo.list_all()

    def some_report(self) -> List[str]:
        # this is just an example to show that not all operations are simple CRUD operations
        contacts: List[Contact] = self.list_contacts()
        name_initials: List[str] = [
            f"{contact.first_name[0]}. {contact.last_name[0]}."
            for contact in contacts
            if contact.first_name and contact.last_name
        ]
        return name_initials
