from . import db


class PropInfo(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    desc = db.Column(db.String(1000))
    rooms = db.Column(db.String(20))
    bathrooms = db.Column(db.String(20))
    price = db.Column(db.String(100))
    location = db.Column(db.String(400))
    propType = db.Column(db.String(30))
    photo = db.Column(db.String(200))

    def __init__(self,title,desc,rooms,bathrooms,price,location,propType,photo):
        self.title = title
        self.desc = desc 
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price = price
        self.location = location
        self.propType = propType
        self.photo = photo

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)