from flask import Flask, render_template
from src.core_features import CoreFeatures

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        CoreFeatures.sign_up_user(email, password)
        return redirect('/login')
    return render_template('sign_up.html')

@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        CoreFeatures.log_in_user(email, password)
        return redirect('/profile')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)