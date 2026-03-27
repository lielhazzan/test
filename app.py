import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # קבלת רשימת הקבצים בתיקייה הנוכחית
    files_list = os.listdir('.') 
    
    # מידע על המערכת
    system_info = {
        "directory": os.getcwd(),
        "total_files": len(files_list)
    }
    
    return render_template('index.html', title="DevOps Dashboard", files=files_list, info=system_info)

if __name__ == '__main__':
    app.run(debug=True)