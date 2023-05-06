from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
  render_template("index.html")
    return 'Hello from Flask!'


app.run(host='0.0.0.0', port=81)
