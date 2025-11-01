# Python Layered Architecture Example

A **minimal example** demonstrating the **Layered Architecture pattern** in Python.
It shows how to structure an application with a clear **separation of concerns** between presentation, business logic, data access, and domain layers, improving maintainability, scalability, and testability.

> ⚠️ **Note:** This project is **for learning purposes only**.
> It intentionally omits many production aspects (error handling, logging, validation, security, testing, etc.) to keep the focus on **core architectural principles**.

---

## Overview

This example implements a simple **Contact Manager** application that demonstrates:

* **Clean separation of concerns** across architectural layers
* **Swappable data stores** (SQLite and MongoDB)
* **Multiple presentation interfaces** (REST API and CLI)
* **Factory pattern** for repository creation
* **Dependency injection** for loose coupling

Each layer interacts only with the one directly below it, enforcing clean boundaries and easier testability.

---

## Layer Details

| Layer                          | Responsibility                    | Example                          |
| ------------------------------ | --------------------------------- | -------------------------------- |
| **Presentation**               | Entry points for user interaction | FastAPI REST API, CLI via Typer  |
| **Services (Business Logic)**  | Core logic orchestration          | `ContactService`                 |
| **Repositories (Data Access)** | Persistence abstraction           | SQLite & MongoDB implementations |
| **Models (Domain Entities)**   | Data definition & validation      | Pydantic models                  |

---

## ⚙️ Design Choice: A Minimal Service Layer

The **service layer** here is intentionally left without abstractions to show that, depending on project needs, such layers may not require them.
Some engineers prefer to abstract every layer for consistency; others apply abstraction only when variation or testing needs justify it. This example simply illustrates a practical approach, not a statement on which is universally better.

---

## 📂 Project Structure

```bash
.
├── models/             # Domain models (Pydantic)
├── services/           # Business logic layer
├── repositories/       # Data access layer
│   ├── sqlite/         # SQLite implementation
│   ├── mongodb/        # MongoDB implementation
│   └── repository_factory.py  # Factory for repository creation
├── db/                 # Database connection management
├── presentation/       # User interfaces
│   ├── fastapi/        # REST API interface
│   └── cli/            # Command-line interface
├── Dockerfile
├── docker-compose.yml
├── Makefile            # Simplified development commands
└── requirements.txt
```

---

## 🚀 Getting Started

### 🧱 Prerequisites

* **Docker & Docker Compose** (recommended)
* **Python 3.11+** for local development

---

### ⚡ Quick Start

The project includes a **Makefile** to simplify running and testing.
List available commands:

```bash
make help
```

---

### ▶️ Run the Application

**Start FastAPI with MongoDB:**

```bash
make api-mongo
# Access the API at http://localhost:8000
# Swagger UI: http://localhost:8000/docs
```

**Start FastAPI with SQLite:**

```bash
make api-sqlite
# Access the API at http://localhost:8001
# Swagger UI: http://localhost:8001/docs
```

## 🌐 API Endpoints

| Method | Endpoint                | Description                                          |
| ------ | ------------------------| ---------------------------------------------------- |
| `POST` | `/contacts`             | Create a new contact                                 |
| `GET`  | `/contacts`             | List all contacts                                    |
| `GET`  | `/contacts/some-report` | Example service-layer method (returns name initials) |

---

## ⚙️ Environment Configuration

Switch between database implementations using environment variables:

| Variable    | Description               | Default            |
| ----------- | ------------------------- | ------------------ |
| `DB_TYPE`   | `"sqlite"` or `"mongodb"` | `sqlite`           |
| `MONGO_URI` | MongoDB connection string | `mongodb://localhost:27017/`                  |
| `DB_NAME`   | MongoDB database name     | `contacts_db`                  |
| `DB_PATH`   | SQLite file path          | `contacts.db` |

📄 See [.env.example](.env.example) for configuration examples.

---

## 📘 Technical Terminology

Different sources may use varying terms for similar architectural concepts.
Here's how they map in this project:

| Term             | Also Known As                | Description                    |
| ---------------- | ---------------------------- | ------------------------------ |
| **Repositories** | Persistence Layer, DAO       | Handle database operations     |
| **Services**     | Application Layer, Use Cases | Contain business logic         |
| **Presentation** | Controllers, Adapters, UI    | User-facing entry points       |
| **Models**       | Entities, Domain Models, DTO | Data structures and validation |

> There's no single “correct” terminology, adapt these concepts to your project's needs.

---

## 📚 Learn More

For a detailed explanation of the layered architecture pattern and the design decisions behind this example, see:

👉 **[Medium Article: How Layered Architecture Just Makes Sense. A Natural Way to Understand It](https://medium.com/@fahd.hus/how-layered-architecture-just-makes-sense-a-natural-way-to-understand-it-d85dce8ce914)**

---

## 🪪 License

This project is provided for **educational purposes** under the [MIT License](LICENSE).
Use it freely as a reference, and remember to add **error handling, security, testing, and production best practices** before using it in real applications.