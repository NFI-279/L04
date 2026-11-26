Line: 4
Problem: Hardcoded admin password.
Example: check_admin("admin123") returns True without a configured password, expected False.
Fix: ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")

Line: 13
Problem: SQL query uses unescaped user input.
Example: Searching for O'Brien raises an SQL error instead of returning None when the user does not exist.
Fix: return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
