from datetime import datetime
import uuid

class Place:
    """Représente un lieu de séjour."""
    def __init__(self, name, description, city_id, user_id, price):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.city_id = city_id
        self.user_id = user_id
        self.price = price
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Retourne un dictionnaire de l'objet."""
        return self.__dict__

