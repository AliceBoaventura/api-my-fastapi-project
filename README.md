# My FastAPI Project

A basic FastAPI application to get you started with building REST APIs in Python.

## Features

- Fast, modern Python web framework
- Automatic API documentation (Swagger UI)
- Type hints and validation with Pydantic
- Easy to extend and customize

## Prerequisites

- Python 3.8+
- pip

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AliceBoaventura/api-my-fastapi-project.git
cd api-my-fastapi-project
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the API

```bash
uvicorn main:app --reload
```

The API will be available at:
- Main: http://localhost:8000
- Interactive API docs (Swagger): http://localhost:8000/docs
- Alternative API docs (ReDoc): http://localhost:8000/redoc

## API Endpoints

- `GET /` - Welcome message
- `GET /items/{item_id}` - Get an item by ID
- `POST /items/` - Create a new item

## Example Usage

```bash
# Get root
curl http://localhost:8000/

# Get item
curl http://localhost:8000/items/1?q=test

# Create item
curl -X POST http://localhost:8000/items/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Item 1", "price": 9.99}'
```

## Next Steps

- Add more endpoints
- Integrate a database (SQLAlchemy, MongoDB, etc.)
- Add authentication
- Write tests
- Deploy to production

Happy coding!