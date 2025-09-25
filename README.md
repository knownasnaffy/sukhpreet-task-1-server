# Dummy backend for task 1

## Instructions:

- Install required packages:
  ```sh
  pip install flask flask_sqlalchemy
  ```
- For development, run:
  ```sh
  python app.py
  ```
  It will create a SQLite database (`users.db`) in the same directory.
- The `/profile` endpoint supports:
  - `GET` to fetch the first user,
  - `POST` to add a new user,
  - `PUT` to update the first user.

## Endpoint: `/profile`

Supports three HTTP methods: **GET**, **POST**, and **PUT**.

### GET /profile

- **Description**: Fetch user information.
- **Response**:
  - Success (user found):
    ```json
    {
      "status": 200,
      "message": "User found",
      "data": {
        "name": "string",
        "age": "number",
        "gender": "string (single character)",
        "salary": "number",
        "interests": "string (comma separated)"
      }
    }
    ```
  - Error (no user found):
    ```json
    {
      "status": 404,
      "message": "User not found",
      "data": null
    }
    ```

### POST /profile

- **Description**: Add a new user.
- **Request Body (JSON)**:
  ```json
  {
    "name": "string",
    "age": number,
    "gender": "string (single character)",
    "salary": number,
    "interests": "string (comma separated, optional)"
  }
  ```
- **Response**:
  - Success (user added):
    ```json
    {
      "status": 201,
      "message": "User added",
      "data": {
        "name": "string",
        "age": "number",
        "gender": "string",
        "salary": "number",
        "interests": "string"
      }
    }
    ```

### PUT /profile

- **Description**: Update the first user.
- **Request Body (JSON)** (fields optional):
  ```json
  {
    "name": "string (optional)",
    "age": number (optional),
    "gender": "string (optional)",
    "salary": number (optional),
    "interests": "string (optional)"
  }
  ```
- **Response**:
  - Success (user updated):
    ```json
    {
      "status": 200,
      "message": "User updated",
      "data": {
        "name": "string",
        "age": "number",
        "gender": "string",
        "salary": "number",
        "interests": "string"
      }
    }
    ```
  - Error (no user found):
    ```json
    {
      "status": 404,
      "message": "User not found",
      "data": null
    }
    ```

## Notes

- The server stores only one user record for simplicity: the first user returned in the database.
- The `gender` field expects a single character string, e.g., `"M"` or `"F"`.
- The `interests` field is optional and should be a comma-separated string.
- Use standard HTTP headers, especially `Content-Type: application/json` for POST and PUT requests.
