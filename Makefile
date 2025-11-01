# ⚠️ Auto-generated file. Review before use. It may contain suboptimal content.
COMPOSE = docker-compose
OPEN_CMD = open
ifeq ($(shell uname), Linux)
	OPEN_CMD = xdg-open
endif

# === .PHONY ===
.PHONY: help \
	api-mongo api-sqlite api-docs api-sqlite-docs \
	cli-add cli-list cli-report cli-shell \
	cli-sqlite-add cli-sqlite-list cli-sqlite-report cli-sqlite-shell \
	mongo-shell backup-mongo \
	up down restart logs logs-api logs-mongo ps \
	clean rebuild \
	test-api-mongo test-api-sqlite

# === Help (Default Target) ===
help:
	@echo "Contact Manager - Docker Commands"
	@echo "=================================="
	@echo ""
	@echo "API Commands:"
	@echo "  make api-mongo          - Start FastAPI with MongoDB (port 8000)"
	@echo "  make api-sqlite         - Start FastAPI with SQLite (port 8001)"
	@echo "  make api-docs           - Open Mongo API documentation in browser"
	@echo "  make api-sqlite-docs    - Open SQLite API documentation in browser"
	@echo ""
	@echo "CLI Commands (MongoDB):"
	@echo "  make cli-add            - Add a contact via CLI (MongoDB)"
	@echo "  make cli-list           - List all contacts via CLI (MongoDB)"
	@echo "  make cli-report         - Generate report via CLI (MongoDB)"
	@echo "  make cli-shell          - Open interactive shell (MongoDB)"
	@echo ""
	@echo "CLI Commands (SQLite):"
	@echo "  make cli-sqlite-add     - Add a contact via CLI (SQLite)"
	@echo "  make cli-sqlite-list    - List all contacts via CLI (SQLite)"
	@echo "  make cli-sqlite-report  - Generate report via CLI (SQLite)"
	@echo "  make cli-sqlite-shell   - Open interactive shell (SQLite)"
	@echo ""
	@echo "Database Commands:"
	@echo "  make mongo-shell        - Access MongoDB shell"
	@echo "  make backup-mongo       - Backup MongoDB data"
	@echo ""
	@echo "Service Management:"
	@echo "  make up                 - Start all default services"
	@echo "  make down               - Stop all services"
	@echo "  make restart            - Restart all services"
	@echo "  make logs               - View logs (all services)"
	@echo "  make logs-api           - View Mongo API logs"
	@echo "  make logs-mongo         - View MongoDB logs"
	@echo "  make ps                 - Show running services"
	@echo ""
	@echo "Maintenance:"
	@echo "  make clean              - Stop services and remove volumes (DELETES DATA)"
	@echo "  make rebuild            - Rebuild and restart services"
	@echo ""
	@echo "Testing:"
	@echo "  make test-api-mongo     - Test MongoDB API endpoints (starts service)"
	@echo "  make test-api-sqlite    - Test SQLite API endpoints (starts service)"
	@echo ""

# === API Services ===
api-mongo:
	@echo "Starting FastAPI with MongoDB on http://localhost:8000"
	$(COMPOSE) up -d api mongodb
	@echo "API Documentation: http://localhost:8000/docs"

api-sqlite:
	@echo "Starting FastAPI with SQLite on http://localhost:8001"
	$(COMPOSE) --profile sqlite up -d api-sqlite
	@echo "API Documentation: http://localhost:8001/docs"

api-docs:
	@echo "Opening MongoDB API docs..."
	@$(OPEN_CMD) http://localhost:8000/docs || echo "Open http://localhost:8000/docs in your browser"

api-sqlite-docs:
	@echo "Opening SQLite API docs..."
	@$(OPEN_CMD) http://localhost:8001/docs || echo "Open http://localhost:8001/docs in your browser"

# === CLI Commands (MongoDB) ===
cli-add:
	@echo "Adding contact via CLI (MongoDB)..."
	@read -p "First Name: " fname; \
	read -p "Last Name: " lname; \
	read -p "Email: " email; \
	$(COMPOSE) run --rm cli python -m presentation.cli.main add-contact \
		--first-name "$$fname" --last-name "$$lname" --email "$$email"

cli-list:
	@echo "Listing all contacts (MongoDB)..."
	$(COMPOSE) run --rm cli python -m presentation.cli.main list-contacts

cli-report:
	@echo "Generating report (MongoDB)..."
	$(COMPOSE) run --rm cli python -m presentation.cli.main some-report

cli-shell:
	@echo "Opening interactive CLI shell (MongoDB)..."
	$(COMPOSE) run --rm cli sh

# === CLI Commands (SQLite) ===
cli-sqlite-add:
	@echo "Adding contact via CLI (SQLite)..."
	@read -p "First Name: " fname; \
	read -p "Last Name: " lname; \
	read -p "Email: " email; \
	$(COMPOSE) --profile sqlite-cli run --rm cli-sqlite python -m presentation.cli.main add-contact \
		--first-name "$$fname" --last-name "$$lname" --email "$$email"

cli-sqlite-list:
	@echo "Listing all contacts (SQLite)..."
	$(COMPOSE) --profile sqlite-cli run --rm cli-sqlite python -m presentation.cli.main list-contacts

cli-sqlite-report:
	@echo "Generating report (SQLite)..."
	$(COMPOSE) --profile sqlite-cli run --rm cli-sqlite python -m presentation.cli.main some-report

cli-sqlite-shell:
	@echo "Opening interactive CLI shell (SQLite)..."
	$(COMPOSE) --profile sqlite-cli run --rm cli-sqlite sh

# === Database Commands ===
mongo-shell:
	@echo "Opening MongoDB shell..."
	$(COMPOSE) exec mongodb mongosh contact_manager_db

backup-mongo:
	@echo "Backing up MongoDB..."
	@mkdir -p ./backups
	$(COMPOSE) exec mongodb mongodump --db contact_manager_db --out /data/backup
	docker cp contact-manager-mongodb:/data/backup ./backups/mongodb-$(shell date +%Y%m%d-%H%M%S)
	@echo "Backup completed in ./backups/"

# === Service Management ===
up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

restart:
	$(COMPOSE) restart

logs:
	$(COMPOSE) logs -f

logs-api:
	$(COMPOSE) logs -f api

logs-mongo:
	$(COMPOSE) logs -f mongodb

ps:
	$(COMPOSE) ps

# === Maintenance ===
clean:
	@echo "WARNING: This will stop all services and delete all data!"
	@read -p "Are you sure? [y/N] " confirm; \
	if [ "$$confirm" = "y" ] || [ "$$confirm" = "Y" ]; then \
		$(COMPOSE) down -v; \
		echo "Services stopped and volumes removed."; \
	else \
		echo "Cancelled."; \
	fi

rebuild:
	$(COMPOSE) up -d --build

# === Testing ===
test-api-mongo: api-mongo
	@echo "Testing MongoDB API endpoints (http://localhost:8000)..."
	@echo "\n1. Creating a test contact..."
	@curl -X POST "http://localhost:8000/contacts" \
		-H "Content-Type: application/json" \
		-d '{"first_name":"Test","last_name":"User","email":"test@example.com"}' \
		-w "\nHTTP Status: %{http_code}\n" -s
	@echo "\n2. Listing all contacts..."
	@curl "http://localhost:8000/contacts" -w "\nHTTP Status: %{http_code}\n" -s
	@echo "\n3. Getting report..."
	@curl "http://localhost:8000/some-report" -w "\nHTTP Status: %{http_code}\n" -s
	@echo "\nMongoDB API tests completed!"

test-api-sqlite: api-sqlite
	@echo "Testing SQLite API endpoints (http://localhost:8001)..."
	@echo "\n1. Creating a test contact..."
	@curl -X POST "http://localhost:8001/contacts" \
		-H "Content-Type: application/json" \
		-d '{"first_name":"Test","last_name":"User","email":"test-sqlite@example.com"}' \
		-w "\nHTTP Status: %{http_code}\n" -s
	@echo "\n2. Listing all contacts..."
	@curl "http://localhost:8001/contacts" -w "\nHTTP Status: %{http_code}\n" -s
	@echo "\n3. Getting report..."
	@curl "http://localhost:8001/some-report" -w "\nHTTP Status: %{http_code}\n" -s
	@echo "\nSQLite API tests completed!"