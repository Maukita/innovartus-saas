from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "Success",
        "message": "Welcome to the Innovartus SaaS Platform on AWS!",
        "environment": "Production"
    })

if __name__ == '__main__':
    # Dynamic port binding ensures compatibility with cloud platforms
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)