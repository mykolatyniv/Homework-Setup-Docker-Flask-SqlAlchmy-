# src/models/UserModel.py
#####################
# existing code remain #
######################
from ..app import bcrypt  # add this line


class UserModel(db.Model):
    """
    User Model
    """

    # table name
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    #####################
    # existing code remain #
    ######################

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.name = data.get('name')
        self.email = data.get('email')
        self.password = self.__generate_hash(data.get('password'))  # add this line

    #####################
    # existing code remain #
    ######################

    def update(self, data):
        for key, item in data.items():
            if key == 'password':  # add this new line
                self.password = self.__generate_hash(value)  # add this new line
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    #####################
    # existing code remain #
    ######################

    # add this new method
    def __generate_hash(self, password):
        return bcrypt.generate_password_hash(password, rounds=10).decode("utf-8")

    # add this new method
    def check_hash(self, password):
        return bcrypt.check_password_hash(self.password, password)

    #####################
    # existing code remain #
    ######################