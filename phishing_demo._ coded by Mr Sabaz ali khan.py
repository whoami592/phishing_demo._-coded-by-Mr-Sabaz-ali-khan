from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML for a fake login page (for educational demo)
LOGIN_PAGE = '''
<!DOCTYPE html>
<html>
<body>
    <h2>Educational Demo Login (Not Real)</h2>
    <form method="POST" action="/login">
        <label>Username:</label><input type="text" name="username"><br>
        <label>Password:</label><input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
'''

# Route to display the login page
@app.route('/')
def index():
    return render_template_string(LOGIN_PAGE)

# Route to handle form submission
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    # Log credentials to console (for demo only, never store real data)
    print(f"Captured: Username={username}, Password={password}")
    return "Credentials captured (this is a demo). Do not use real passwords!"

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)