DevOps Dashboard Project 🚀
A full-stack Python web application built with Flask. This project serves as a system dashboard that manages users and displays server-side information.

✨ Features
User Management: Complete Registration and Login system.

Data Persistence: Users are saved in a hidden .data/ directory using JSON (does not reset when the server restarts).

System Dashboard: Displays real-time OS info, current directory, and project file list.

Security: Sensitive user data is excluded from Git using .gitignore.

Responsive UI: Modern English interface with CSS animations.

🛠 Tech Stack
Backend: Python 3, Flask.

Frontend: HTML5, CSS3 (Flexbox/Gradients), JavaScript.

Data: JSON-based persistent storage.

DevOps Tools: Git, .gitignore for data protection.

🚀 How to Run Locally
Clone the repository:

Bash
git clone <your-repository-url>
cd test-main
Install dependencies:
(Make sure you have Flask installed)

Bash
pip install flask
Run the application:

Bash
python app.py
Access the app:
Open your browser and go to http://127.0.0.1:5000.

📁 Project Structure
app.py: The main Flask server and logic.

templates/: HTML files (Login, Register, Dashboard).

static/: CSS styling and JavaScript logic.

.data/: (Hidden) Persistent storage for user credentials.