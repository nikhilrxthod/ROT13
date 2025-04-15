# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

def rot13(text):
    return text.translate(str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    ))

@app.route('/', methods=['GET', 'POST'])
def index():
    input_text = request.form.get('input_text', '')
    output_text = rot13(input_text) if request.method == 'POST' else ''
    return render_template('index.html', output_text=output_text, input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True)
