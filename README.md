# flask-playground

Playing with a dockerized environment for developing web apps using:
- Flask
- SQLAlchemy
- Alembic (for migrations)
- Flask-JWT (for auth)

To setup the project, run:

```
docker-compose build
docker-compose up
```

After the containers are up and running, run the initial migrations with:

```
make upgrade-db
```
Note: This runs `alembic` inside the container.

The webapp should be available at: `http://127.0.0.1:5000`, and has a few endpoints to play with:
- `/users` to create a user, payload should include: `username`, `password` and `name`.
- `/auth` to authenticate and receive a token, payload should include `username` and `password`. Returns an `auth_token` which must be included in the `Authorization` header for protected endpoints. See the [Flask-JWT docs](https://pythonhosted.org/Flask-JWT/) for more info.
- `/todos` which provides a REST API to play with todo items:
  - `[GET] /todos` Returns all the todo items for a logged user.
  - `[POST] /todos` Creates a todo item for a user.
  - `[GET] /todos/{todo_id}` Returns a single todo item with specified id (if the logged user is it's owner).
