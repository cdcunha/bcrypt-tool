from flask import Flask, render_template, request, flash
import bcrypt

app = Flask(__name__)
app.secret_key = 'super-secret-key-change-in-production'

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    generated_hash = None

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'hash':
            password = request.form.get('password', '').strip()
            if not password:
                flash("Password cannot be empty!", "danger")
            else:
                salt = bcrypt.gensalt(rounds=12)
                generated_hash = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
                flash("Hash generated successfully!", "success")

        elif action == 'check':
            password = request.form.get('password_check', '').strip()
            stored_hash = request.form.get('stored_hash', '').strip()

            if not password or not stored_hash:
                flash("Both password and hash are required!", "danger")
            else:
                try:
                    if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
                        result = "✅ Password match with hash"
                    else:
                        result = "❌ Password does NOT match with hash"
                except Exception:
                    flash("Invalid hash format!", "danger")

    return render_template('index.html', 
                         result=result, 
                         generated_hash=generated_hash)

if __name__ == '__main__':
    print("🚀 Starting Bcrypt Tool (Dark Mode)...")
    app.run(debug=True, port=5000)