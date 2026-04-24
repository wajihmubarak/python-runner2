from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

users = {}  # تخزين مؤقت (بعدها نطورها لقاعدة بيانات)

# الصفحة الرئيسية (تسجيل)
@app.route('/')
def home():
    return render_template_string(open("index.html", encoding="utf-8").read())

# تسجيل مستخدم
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    if username in users:
        return "❌ المستخدم موجود"

    users[username] = password
    return "✔ تم التسجيل بنجاح"

# تسجيل دخول
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if users.get(username) == password:
        return redirect(f"/dashboard/{username}")
    return "❌ بيانات خطأ"

# داشبورد
@app.route('/dashboard/<user>')
def dashboard(user):
    return f"""
    <h1>🔥 مرحباً {user}</h1>
    <p>تم تسجيل الدخول بنجاح</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
