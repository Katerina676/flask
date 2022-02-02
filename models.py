from app import db
from datetime import datetime


class Advertisement(db.Model):
    __tablename__ = 'advertisement'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    owner = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return '<id %r>' % self.id


db.create_all()
