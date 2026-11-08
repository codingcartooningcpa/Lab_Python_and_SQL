"""Database connection settings, shared by every lab script.

The values come from environment variables that the codespace sets
(see .devcontainer/devcontainer.json), so no password is typed into
the lab scripts themselves. Real applications keep credentials out
of their source code the same way.
"""
import os

DB_CONFIG = {
    "host":     os.getenv("DB_HOST", "127.0.0.1"),
    "user":     os.getenv("DB_USER", "student"),
    "password": os.getenv("DB_PASSWORD", "secret"),
    "database": os.getenv("DB_NAME", "Registration"),
}
