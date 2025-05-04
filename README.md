# Notes Fast API
This to create notes and get notes


### Run with Docker Compose

To run the FastAPI application using Docker Compose, follow these steps:

1. Build and start the containers:
    ```
    docker-compose up --build
    ```

1. Access the interactive API documentation at:
    ```
    http://127.0.0.1:8081/docs
    ```
    or the alternative documentation at:
    ```
    http://127.0.0.1:8081/redoc
    ```

1. To stop the containers, use:
    ```
    docker-compose down
    ```

### Project Architecture

The project follows the Model-View-Controller (MVC) architecture pattern:

- **Models**: Contains entity definitions or Pydantic objects used for data validation and serialization.
- **Routers**: Acts as controllers, defining REST API endpoints and handling HTTP requests.
- **Repository Layer**: Handles database manipulation operations, serving as the data access layer.
- **Dependency Folder**: Manages global dependencies between different components, such as Repository Layer, Service Layer and Controller

### Security

This project is a Notes App built using FastAPI. The application provides a secure API for managing notes. Security is enforced using JWT (JSON Web Token) for authentication and authorization. Ensure that a valid JWT token is included in the request headers when accessing secured endpoints.

### GitHub Actions Workflow

To automatically execute `pytest` on every push to the `main` branch, you can use the following GitHub Actions workflow:

Create a file named `.github/workflows/test.yml` in your repository with the following content:

*Note : I am using pre-configured GitHub Actions workflow template available in the `.github/workflows` folder of your repository.*

```yaml
name: Run Tests

on:
    push:
        branches:
            - main

jobs:
    test:
        runs-on: ubuntu-latest

        steps:
        - name: Checkout code
            uses: actions/checkout@v3

        - name: Set up Python
            uses: actions/setup-python@v4
            with:
                python-version: '3.9'

        - name: Install dependencies
            run: |
                python -m pip install --upgrade pip
                pip install -r requirements.txt

        - name: Run tests
            run: |
                pytest
```

This workflow will trigger on every push to the `main` branch, set up Python, install dependencies, and run your tests using `pytest`.

### Frontend

The frontend part of the application was not included in this project. An attempt was made to use Next.js, but due to unresolved bugs, it was omitted. Future iterations of the project may include a fully functional frontend.
