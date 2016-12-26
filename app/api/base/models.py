from app import db


class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

    def serialize(self):
        return {
            'id': self.id,
            'date_created': self.date_created,
            'date_modified': self.date_modified
        }