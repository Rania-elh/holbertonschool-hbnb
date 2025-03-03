from datetime import datetime
import uuid

class User:
    """Représente un utilisateur."""
    def __init__(self, email, password, first_name="", last_name=""):
        self.id = str(uuid.uuid4())
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Retourne un dictionnaire de l'objet."""
        return self.__dict__

