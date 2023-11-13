from app import db
from datetime import datetime

class StatusHistory(db.Model):
    __tablename__ = 'status_history'

    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)
    update_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    property = db.relationship('Property', back_populates='status_history')
    status = db.relationship('Status')

    def __repr__(self):
        return f"<StatusHistory property_id={self.property_id}, status_id={self.status_id}, update_date={self.update_date}>"