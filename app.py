from flask import Flask, request, jsonify, render_template
from logging.config import dictConfig
import os

from app.services import Services
from model.lex import Lexentry

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__)
app.json.sort_keys = False  # keeps the fields in a Lexentry in the order they are within Lexentry.to_dict()

services = Services()


@app.route('/', methods=['GET'])
def ui() -> str:
    app.logger.info("ui - Got request")
    return render_template('user_interface.html')


@app.route("/load_lex", methods=["GET"])
def load_lex():
    lexicon = services.load_all()
    app.logger.info("/load_lex - Loaded lexicon")
    # Note that the Lexentry class needs the .to_dict() method to be easily jsonified
    return jsonify([lexitem.to_dict() for lexitem in lexicon])


@app.route("/add_entry", methods=["POST"])
def add_entry():
    json_data = request.get_json()
    app.logger.info(f"/add_entry - Got request: {json_data}")
    if not json_data:
        return {"message": "Must provide data for a lexical entry"}, 400

    try:
        newentry = Lexentry(**json_data)
        outcome = services.add_entry(newentry)
    except:
        app.logger.info(f"/add_entry - could not create valid Lexentry")

    if outcome:
        return jsonify({"msg": "success"})
    else:
        return jsonify({"msg": "error saving entry"})


if __name__ == "__main__":
    if os.environ.get('APP_ENV') == 'docker':
        app.run(host='app')        # This is the name of the host from within the Docker container that the app is in.
                                   # You will still *access* the Flask API from your computer at localhost:5000, since
                                   # we're mapping app:5000 (inside the container) to localhost:5000 (on the host OS).
    else:
        app.run(host='localhost')  # This is the appropriate interface when you're running this file NOT in a container
