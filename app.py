from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if password != confirm_password:
        return "Passwords do not match"
    
    users.append({'username': username, 'password': password})
    
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return 'Signup successful!'

if __name__ == '__main__':
    app.run(debug=True)
