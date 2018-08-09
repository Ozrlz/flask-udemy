from db import db

class UserModel(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80)) # 80 Chars at most
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {
            'id': self.id,
            'username': self.username
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        '''
        Args:
            cls -> The current class
            username(str): The name of the user
        Returns:
            An UserModel object if found
        '''
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        '''
        Args:
            cls -> The current class
            _id(str): The id of the User
        Returns:
            An ItemModel object if found
        '''
        return cls.query.filter_by(id=_id).first()

