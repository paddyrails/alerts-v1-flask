# Alerts API

A RESTful API built with Flask using a layered architecture (API, Service, DAO).

## Database Migrations

| Command | Description |
|---|---|
| `flask db init` | Initialize migrations folder (run once) |
| `flask db migrate -m "message"` | Generate a new migration after model changes |
| `flask db upgrade` | Apply pending migrations |
| `flask db downgrade` | Rollback last migration |
| `flask db history` | View migration history |
| `flask db current` | Show current migration version |
