import os


ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")


def check_admin(password):
    """True if the password is the admin password"""
    return ADMIN_PASSWORD != "" and password == ADMIN_PASSWORD


def find_user(db, username):
    """The user's row, or None if the username does not exist"""
    return db.execute(
        "SELECT * FROM users WHERE username = ?", (username,)
    ).fetchone()
