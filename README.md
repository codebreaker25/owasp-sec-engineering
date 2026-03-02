# OWASP Security Engineering

A collection of security engineering examples and demonstrations for OWASP Top 10 vulnerabilities.

## A05 - Injection

This module demonstrates SQL injection vulnerabilities and their mitigations.

### Files

- `app.py` - Flask application with SQL injection examples
- `setup_db.py` - Database setup script

### Setup

1. Install dependencies:
```bash
pip install flask
```

2. Initialize the database:
```bash
python A05_injection/setup_db.py
```

3. Run the application:
```bash
python A05_injection/app.py
```

### Security Notes

⚠️ This project contains intentionally vulnerable code for educational purposes. Do not use in production environments.
