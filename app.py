from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App on Render 🚀"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        return f"✅ Registered Successfully! <br>Name: {name}<br>Email: {email}"
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
