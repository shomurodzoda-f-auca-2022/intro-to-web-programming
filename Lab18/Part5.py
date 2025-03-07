from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    names = ["Adilet", "Aziret", "Aidai"]
    return render_template('index_lab1.html', names=names, title="Welcome")

if __name__ == '__main__':
    app.run(debug=True)