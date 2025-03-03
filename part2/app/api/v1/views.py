from flask_restx import Namespace, Resource

api = Namespace("status", description="Vérification du statut de l'API")

@api.route("/status")
class StatusCheck(Resource):
    def get(self):
        """Vérifier que l'API fonctionne"""
        return {"status": "OK"}, 200

