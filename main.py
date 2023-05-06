from flask import Flask, render_template, request, make_response
from endpoints import inject_routes
import jwt


app = Flask(
  import_name=__name__,
  template_folder="templates",
  static_folder="static",
)


@app.route('/')
def index():
  return render_template("index.html")

inject_routes(app)

app.run(
  host='0.0.0.0',
  port=8081,
  debug=True,
)
