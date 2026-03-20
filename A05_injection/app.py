from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, PlainTextResponse
import sqlite3
from pathlib import Path
import uvicorn

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "users.db"

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()

app = FastAPI()

def login_form(action: str, title: str):
    return f"""
    <h2>{title}</h2>
    <form action="{action}" method="post">
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <input type="submit" value="Login">
    </form>
    <p><a href="/">Back</a></p>
    """

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>SQL Injection Demo</h1>
    <ul>
      <li><a href="/vulnerable">Vulnerable Login</a></li>
      <li><a href="/fixed">Fixed Login</a></li>
    </ul>
    """

@app.get("/vulnerable", response_class=HTMLResponse)
def vulnerable_page():
    return login_form("/vulnerable", "Vulnerable Login")

@app.post("/vulnerable", response_class=PlainTextResponse)
def vulnerable_login(username: str = Form(...), password: str = Form(...)):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        return "Login successful! (vulnerable)"
    return "Invalid credentials. (vulnerable)"

@app.get("/fixed", response_class=HTMLResponse)
def fixed_page():
    return login_form("/fixed", "Fixed Login")

@app.post("/fixed", response_class=PlainTextResponse)
def fixed_login(username: str = Form(...), password: str = Form(...)):
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    results = cursor.fetchall()
    if results:
        return "Login successful! (fixed)"
    return "Invalid credentials. (fixed)"

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)