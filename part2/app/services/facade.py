from datetime import datetime
import uuid
from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.review import Review
from app.models.place import Place

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.place_repo =  InMemoryRepository()

#-------------------------------------------------------------------#
#                           USER                                    #
#-------------------------------------------------------------------#
    def create_user(self, user_data: dict) -> User:
        user = User(**user_data, id=str(uuid.uuid4()), created_at=datetime.now(), updated_at=datetime.now())
        self.user_repo.add(user)
        return user

    def get_user(self, user_id: str) -> User:
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email: str) -> User:
        return self.user_repo.get_by_attribute('email', email)
    
    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        User.validate_request_data(user_data)
        val = self.get_user(user_id)
        if val:
            val.update(user_data)
        return val
    
    def delete_user(self, user_id):
        # Placeholder for logic to delete a review
        return self.user_repo.delete(user_id)


#-------------------------------------------------------------------#
#                           AMENITY                                 #
#-------------------------------------------------------------------#

    def create_amenity(self, amenity_data):
        post_amenity = Amenity(**amenity_data, id=str(uuid.uuid4()), created_at=datetime.now(), updated_at=datetime.now())
        self.amenity_repo.add(post_amenity)
        return post_amenity

    def get_amenity(self, amenity_id:str) -> Amenity:
        return self.amenity_repo.get(amenity_id)
        
    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        return self.amenity_repo.update(amenity_id, amenity_data)
   
    def delete_amenity(self, amenity_id):
        # Placeholder for logic to delete a review
        return self.amenity_repo.delete(amenity_id)
    

#-------------------------------------------------------------------#
#                           PLACES                                  #
#-------------------------------------------------------------------#
    def create_place(self, place_data):
        post_place = Place(**place_data, id=str(uuid.uuid4()), created_at=datetime.now(), updated_at=datetime.now())
        self.place_repo.add(post_place)
        return post_place

    def get_place(self, place_id:str) -> Place:
        return self.place_repo.get(place_id)
        
    def get_all_place(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        val = self.get_place(place_id)
        if val:
            val.update(place_data)
        return val
    
    def delete_place(self, place_id):
        # Placeholder for logic to delete a review
        return self.place_repo.delete(place_id)

#-------------------------------------------------------------------#
#                           review                                  #
#-------------------------------------------------------------------#

    def create_review(self, review_data):
        post_review = Review(**review_data, 
                             id=str(uuid.uuid4()), 
                             created_at=datetime.now(), 
                             updated_at=datetime.now())
        
        self.review_repo.add(post_review)
        return post_review
        # Placeholder for logic to create a review, including validation for user_id, place_id, and rating

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        # NOT WORK soPlaceholder for logic to retrieve all reviews for a specific place
        return self.review_repo.get(place_id)

    def update_review(self, review_id, review_data):
        Review.validate_request_data(review_data)
        val = self.get_user(review_id)
        if val:
            val.update(review_id)
        return val

    def delete_review(self, review_id):
        # Placeholder for logic to delete a review
        return self.review_repo.delete(review_id)

facade = HBnBFacade()
