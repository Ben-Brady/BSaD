from modules import flask
from flask import Flask


app = Flask(
    import_name=__name__,
    template_folder="templates",
    static_folder="static",
)

flask.inject_routes(app)

app.run(
    host='0.0.0.0',
    port=8081,
    debug=True,
)
