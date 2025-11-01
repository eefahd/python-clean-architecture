from contextlib import contextmanager
from typing import List

import typer

from db.db_factory import get_db
from models.contact import Contact
from repositories.repository_factory import create_repository
from services.contact_service import ContactService

app = typer.Typer(help="Contact Manager CLI")


@contextmanager
def init_app():
    db = get_db()
    db.connect()
    db.init(with_demo=True)
    repo = create_repository(db)
    try:
        yield repo
    finally:
        db.disconnect()


@app.command()
def add_contact(first_name: str, last_name: str, email: str) -> None:
    contact: Contact = Contact(first_name=first_name, last_name=last_name, email=email)
    with init_app() as repo:
        ContactService(repo.contact).create_contact(contact)
    typer.echo("Contact added.")


@app.command()
def list_contacts() -> None:
    with init_app() as repo:
        rows: List[Contact] = ContactService(repo.contact).list_contacts()
    for r in rows:
        typer.echo(str(r))


@app.command()
def some_report() -> None:
    with init_app() as repo:
        rows: List[str] = ContactService(repo.contact).some_report()
    for r in rows:
        typer.echo(str(r))


if __name__ == "__main__":
    app()
