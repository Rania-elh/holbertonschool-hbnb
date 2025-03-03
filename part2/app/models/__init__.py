from flask import Flask
from flask_restx import Api

def create_app():
    """Créer et configurer l'application Flask."""
    app = Flask(__name__)
    api = Api(app, version="1.0", title="HBnB API", description="API pour HBnB Evolution")

    # Importer et enregistrer les namespaces ici
    from app.api.v1.views import api as ns
    api.add_namespace(ns, path="/api/v1")

    return app

