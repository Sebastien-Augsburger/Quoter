from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

texts = ["A beautiful body perishes, but a work of art dies not. - Leonardo da Vinci", "The noblest pleasure is the joy of understanding. - Leonardo da Vinci", "Iron rusts from disuse; water loses its purity from stagnation... even so does inaction sap the vigor of the mind. - Leonardo da Vinci"]

@app.route("/first")
def first():
    return texts[0]


@app.route("/second")
def second():
    return texts[1]


@app.route("/third")
def third():
    return texts[2]
