# AI Warehouse Inventory Manager — Backend

A REST API for warehouse inventory management with AI-powered restocking suggestions.

## Tech Stack
- **FastAPI** — Python web framework
- **SQLAlchemy** — database ORM
- **SQLite** — database
- **Groq (LLaMA 3.3)** — AI restocking suggestions
- **Pydantic** — data validation

## Features
- Full CRUD for inventory items
- Stock quantity auto-updates on movements
- AI analyzes low stock items and returns priority suggestions

## Project Structure
## Setup
```bash
pip install -r requirements.txt
cp .env.example .env  # add your GROQ_API_KEY
uvicorn main:app --reload
```

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/items` | List all items |
| POST | `/items` | Create item |
| PUT | `/items/{id}` | Update item |
| DELETE | `/items/{id}` | Delete item |
| GET | `/ai/restock` | AI restock suggestions |
