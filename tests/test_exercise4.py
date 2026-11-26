import sqlite3
from exercise4 import check_admin, find_user


def test_r1_hardcoded_admin_password():
    assert check_admin("admin123") is False


def test_r2_find_user_unescaped_input():
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (username TEXT)")
    assert find_user(db, "O'Brien") is None
    db.close()
