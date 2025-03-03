from flask import Flask, jsonify, request
from models.amenity import Amenity
from models import storage

app = Flask(__name__)

# GET /amenities → Liste des équipements
@app.route('/api/v1/amenities', methods=['GET'])
def get_amenities():
    """Récupère la liste de tous les équipements"""
    amenities = storage.all(Amenity).values()
    return jsonify([amenity.to_dict() for amenity in amenities])

# POST /amenities → Ajouter un équipement
@app.route('/api/v1/amenities', methods=['POST'])
def create_amenity():
    """Créer un nouvel équipement"""
    data = request.get_json()

    # Vérification que les données sont valides
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if 'name' not in data:
        return jsonify({"error": "Missing name"}), 400

    name = data['name']
    new_amenity = Amenity(name=name)
    
    # Sauvegarde dans le stockage
    storage.new(new_amenity)
    storage.save()
    
    return jsonify(new_amenity.to_dict()), 201

# GET /amenities/<id> → Obtenir un équipement spécifique
@app.route('/api/v1/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    """Récupère un équipement par son ID"""
    amenity = storage.get(Amenity, amenity_id)
    
    if amenity:
        return jsonify(amenity.to_dict())
    else:
        return jsonify({"error": "Amenity not found"}), 404

# PUT /amenities/<id> → Modifier un équipement
@app.route('/api/v1/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    """Met à jour un équipement existant"""
    data = request.get_json()
    
    # Vérification que les données sont valides
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    
    # Recherche de l'équipement par ID
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        return jsonify({"error": "Amenity not found"}), 404
    
    # Mise à jour des données
    if 'name' in data:
        amenity.name = data['name']
    
    # Sauvegarde dans le stockage
    storage.save()
    
    return jsonify(amenity.to_dict())

