from flask import Flask, request, render_template_string
import sqlite3

conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()

app = Flask(__name__)

@app.route('/')
def login():
    return '''
        <form action="/login" method="post">
            <input type="text" name="username" placeholder="Username">
            <input type="password" name="password" placeholder="Password">
            <input type="submit" value="Login">
        </form>
    '''
@app.route('/login', methods=['POST'])
def login_post():    
    username = request.form['username']
    password = request.form['password']
    
    # Intentionally vulnerable - concatenates user input directly
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    # Execute the vulnerable query
    cursor.execute(query)
    results = cursor.fetchall()
    print("Query results:", results)
    
    if results:
        print("Executing query:", query)
        return "Login successful!"
        return str(results)

    else:
        print("Executing query:", query)
        return "Invalid credentials."
    
    

if __name__ == "__main__":
    app.run(debug=True)



