from app import db

class Status(db.Model):
    __tablename__ = 'status'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    label = db.Column(db.String(64))

    def __repr__(self):
        return f"<Status {self.name}>"