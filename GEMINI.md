# Gemini Project Context: graphql-api

## Project Overview

This project is a GraphQL API built with Python, FastAPI, and Strawberry. It serves a mock database of authors and books. The project is fully containerized using Docker and includes a CI/CD pipeline with GitHub Actions for automated testing and deployment.

The main components are:
- **`src/main.py`**: The main FastAPI application file, which defines the GraphQL schema and resolvers.
- **`src/create_db.py`**: This script generates the mock data for the API.
- **`Dockerfile`**: Defines the Docker image for the application.
- **`compose.yaml`**: Used to manage the Docker container.
- **`pyproject.toml`**: Specifies the project dependencies, which are managed by `uv`.

## Building and Running

### Docker
The project is designed to be run with Docker.

- **Build and run the application:**
  ```bash
  docker compose up --build
  ```
- **Access the API:**
  The GraphQL playground is available at [http://localhost/graphql](http://localhost/graphql).

- **Stop the application:**
  ```bash
  docker compose down
  ```

### Local Development (without Docker)

While the primary method is Docker, you can run the application locally.

1.  **Install dependencies:**
    ```bash
    pip install uv
    uv pip install '.[test]'
    ```

2.  **Run the application:**
    ```bash
    uvicorn src.main:app --host 0.0.0.0 --port 8000
    ```

## Testing

The project uses `pytest` for testing.

- **Run tests (inside the running Docker container):**
  The `README.md` mentions running tests inside the container, but doesn't specify the command. Based on the setup, the command would be:
  ```bash
  docker compose exec api pytest
  ```

## Development Conventions

- **Dependencies:** Project dependencies are managed with `uv` and are listed in `pyproject.toml`.
- **Code Style:** The code is typed using Python's type hints.
- **CI/CD:** The project uses GitHub Actions for CI/CD. The workflow is defined in `.github/workflows/deploy.yml`.
