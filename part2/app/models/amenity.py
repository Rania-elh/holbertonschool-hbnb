from datetime import datetime
import uuid

class Amenity:
    """Représente un service ou équipement."""
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Retourne un dictionnaire de l'objet."""
        return self.__dict__

