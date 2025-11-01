from contextlib import asynccontextmanager
from typing import AsyncGenerator, List

from fastapi import Depends, FastAPI, Request

from db.db_factory import get_db
from models.contact import Contact
from repositories.repository_factory import create_repository
from repositories.repository_model import Repository
from services.contact_service import ContactService


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Startup
    print("Starting application...")

    db = get_db()
    db.connect()
    db.init(with_demo=True)  # just for demo purposes
    repo = create_repository(db)

    app.state.db = db
    app.state.repo = repo

    print("Application started successfully")

    yield

    # Shutdown
    print("Shutting down application...")
    db.disconnect()
    print("Application shut down successfully")


app = FastAPI(title="Contact Manager", lifespan=lifespan)


def get_repo(request: Request) -> Repository:
    return request.app.state.repo  # type: ignore[attr-defined]


@app.post("/contacts")
async def create_contact(
    contact: Contact, repo: Repository = Depends(get_repo)
) -> None:
    ContactService(repo.contact).create_contact(contact)


@app.get("/contacts", response_model=List[Contact])
async def list_contacts(repo: Repository = Depends(get_repo)) -> List[Contact]:
    return ContactService(repo.contact).list_contacts()


@app.get("/some-report")
async def some_report(repo: Repository = Depends(get_repo)) -> List[str]:
    return ContactService(repo.contact).some_report()
