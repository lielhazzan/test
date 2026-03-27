from flask import Flask, render_template, request, redirect, url_for
import os
import platform
import json

app = Flask(__name__)

# הגדרת תיקייה נסתרת וקובץ נתונים
DATA_DIR = ".data"
DB_FILE = os.path.join(DATA_DIR, "users.json")

# פונקציה לאתחול "מסד הנתונים" (קובץ ה-JSON)
def init_db():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, 'w') as f:
            # יוצר משתמש מנהל ראשוני
            json.dump({"admin": "1234"}, f)

def load_users():
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def save_user(username, password):
    users = load_users()
    users[username] = password
    with open(DB_FILE, 'w') as f:
        json.dump(users, f, indent=4)

# הפעלת האתחול ברגע שהקובץ עולה
init_db()

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users = load_users()
        if username in users and users[username] == password:
            return redirect(url_for('dashboard'))
        return "Invalid credentials. <a href='/login'>Try again</a>"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_user = request.form.get('username')
        new_pass = request.form.get('password')
        users = load_users()
        if new_user in users:
            return "User already exists! <a href='/register'>Try another</a>"
        save_user(new_user, new_pass)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    files_list = os.listdir('.')
    system_info = {
        "directory": os.getcwd(),
        "total_files": len(files_list),
        "os": platform.system(),
        "user": os.getlogin()
    }
    return render_template('index.html', 
                           welcome_msg="Welcome to my first project!", 
                           info=system_info, 
                           files=files_list)

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)