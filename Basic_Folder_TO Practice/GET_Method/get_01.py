from fastapi import FastAPI

api = FastAPI()

# A "fake" database to simulate data retrieval
fake_items_db = [
    {"item_name": "Keyboard"},
    {"item_name": "Mouse"},
    {"item_name": "Monitor"},
    {"item_name": "CPU"},
    {"item_name": "Headphones"},
]

# --- Practice Endpoints ---

@api.get("/")
def read_root():
    # Practice 1: The most basic GET endpoint.
    # This is often used for a "health check" or a simple welcome message
    return {"message": "Welcome to the FastAPI Practice App!"}

@api.get("/items/{item_id}")
def read_item(item_id: int):
    # Practice 2: A GET endpoint with a path parameter
    # This is often used to retrieve a specific item by its ID
    return {"item_id": item_id, "description": f"You requested item number {item_id}"}
