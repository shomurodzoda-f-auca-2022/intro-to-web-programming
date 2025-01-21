from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route("/hello/<name>")
def hello_name(name):
    return render_template("hello.html", name=name)

@app.route("/hello/<name>/int/<int:age>")
def get_age(name, age):
    return render_template("full.html", name=name, age=age)

if __name__ == "__main__":
    app.run(debug=True)