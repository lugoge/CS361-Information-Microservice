from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"

def load_help_data():
    """Load help hints form JSON file."""
    if not os.path.exists(DATA_FILE):
        return()
    
    with open(DATA_FILE, "r") as file:
        return json.load(file)

# Pulls contextual help tip from data base
@app.route("/info/context>", methods=["GET"])
def get_info(context):
    help_data = load_help_data()

    if context not in help_data:
        return jsonify({
            "error": "No help infromation found for this context."
        }), 404
    
    response = {
        "context": context, **help_data[context]
    }

    return jsonify(response), 200

# Can pull up all helpful tips, if just sending "/info" GET.
@app.route("/info", methods=["GET"])
def list_available_contexts():
    help_data = load_help_data()
    return jsonify({
        "available_contexts": list(help_data.keys())
    }), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5004, debug=True)