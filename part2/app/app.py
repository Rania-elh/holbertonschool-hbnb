from flask import Flask
from flask_restx import Api

app = Flask(__name__)
api = Api(app, version="1.0", title="HBnB API", description="API pour HBnB Evolution")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

