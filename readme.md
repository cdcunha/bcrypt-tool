# 🔐 Bcrypt Password Tool

A simple and elegant web application to **generate** and **verify** bcrypt password hashes. Built with Flask and bcrypt.

![Dark Mode Preview](https://via.placeholder.com/800x400/1e1e1e/0f0?text=Bcrypt+Tool+Dark+Mode)

## ✨ Features

- Generate secure bcrypt hashes (cost factor 12)
- Verify passwords against existing hashes
- Beautiful responsive UI with **Dark/Light Mode** toggle
- One-click **Copy to Clipboard** for generated hashes
- Clean and intuitive single-page interface
- Proper input validation and user feedback
- Secure by design (no passwords logged)

## 🚀 Quick Start

### 1. Clone or Create Project

```bash
mkdir bcrypt-tool && cd bcrypt-tool

### 2. Create the project structure:
```text
mkdir templates

### 3. Install dependencies:
```Bash
pip install Flask bcrypt

### 4. Run the app:
```Bash
python app.py

### 5. Open your browser and navigate to: http://127.0.0.1:5000


# 📁 Project Structure
```text
bcrypt-tool/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md
└── templates/
    └── index.html         # Frontend interface

#🛠 How to Use
##Generate Hash

- Enter a password in the left card
- Click "Generate Hash"
- Copy the result instantly using the clipboard button

##Verify Password

- Enter the password you want to test
- Paste the stored bcrypt hash
- Click "Verify"
- Get a clear success or failure message


# ⚙️ Configuration
You can adjust the bcrypt cost (security vs speed) in app.py:
```Python
salt = bcrypt.gensalt(rounds=12)   # Recommended range: 10–14

Higher values make hashing slower (more secure) but take longer.

# 🛡️ Security Notes

- Passwords are processed in memory and never stored or logged
- Uses industry-standard bcrypt with automatic salting
- All sensitive operations happen server-side
- Ideal for learning, internal tools, or testing


# 📋 Requirements

- Python 3.8+
- Flask
- bcrypt


# 📄 License
This project is open-source and free to use for personal or commercial purposes.

# 🙌 Built With

- Flask – Python web framework
- bcrypt – Secure password hashing
- Bootstrap 5 – Responsive UI


Made with ❤️ for secure password handling practices.