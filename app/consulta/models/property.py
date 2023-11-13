from app import db

class Property(db.Model):
    __tablename__ = 'property'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(120))
    city = db.Column(db.String(32))
    price = db.Column(db.BigInteger)
    description = db.Column(db.Text)
    year = db.Column(db.Integer)

    status_history = db.relationship('StatusHistory', back_populates='property')

    def __repr__(self):
        return f"<Property {self.address}, {self.city}, {self.price}, {self.year}>"

    def as_dict(self):
        return {
            'id': self.id,
            'address': self.address,
            'city': self.city,
            'price': self.price,
            'description': self.description,
            'year': self.year
        }