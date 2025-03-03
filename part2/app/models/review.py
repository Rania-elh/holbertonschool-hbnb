from datetime import datetime
import uuid

class Review:
    """Représente un avis d'utilisateur."""
    def __init__(self, user_id, place_id, text):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.place_id = place_id
        self.text = text
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Retourne un dictionnaire de l'objet."""
        return self.__dict__

