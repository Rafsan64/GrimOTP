from flask import Flask, render_template, request, jsonify
import pyotp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    secret = request.form['secret']
    totp = pyotp.TOTP(secret)
    otp = totp.now()  # Generate OTP
    return jsonify({'otp': otp})

if __name__ == '__main__':
    app.run(debug=True)
