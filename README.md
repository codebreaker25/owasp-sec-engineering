# OWASP Security Engineering

A collection of security engineering examples and demonstrations for OWASP Top 10 vulnerabilities.

## A05 - Injection

This module demonstrates SQL injection vulnerabilities and mitigations using a FastAPI login demo.

### Files

- `A05_injection/app.py` - FastAPI app with both vulnerable and fixed login flows
- `A05_injection/setup_db.py` - SQLite database setup script
- `A05_injection/users.db` - Local demo database

### Setup

1. Install dependencies:
```bash
python -m pip install "fastapi[standard]"
```

2. Initialize the database:
```bash
python A05_injection/setup_db.py
```

3. Run the application:
```bash
cd A05_injection
uvicorn app:app --reload
```

4. Open:
```text
http://127.0.0.1:8000
```

### Demo Routes

- `/vulnerable` - intentionally vulnerable SQL query built with string concatenation
- `/fixed` - protected SQL query using parameterized statements

### Test Credentials

- `admin / admin123`
- `user / password`
- `test / test123`

### SQL Injection Demonstration

Use this payload in the vulnerable login form to demonstrate bypass behavior:

- Username: `' OR '1'='1`
- Password: `anything`

Expected result:

- `/vulnerable` may allow bypass
- `/fixed` rejects the payload

### Security Notes

⚠️ This project contains intentionally vulnerable code for educational purposes. Do not use in production environments.
