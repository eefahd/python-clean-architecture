from dataclasses import dataclass

from repositories.base.contact_repository_interface import ContactRepositoryInterface


@dataclass
class Repository:
    contact: ContactRepositoryInterface
