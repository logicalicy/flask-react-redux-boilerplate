from app import db
from ..base.models import Base


class Entry(Base):

    __tablename__ = 'entries'

    title = db.Column(db.String(128),  nullable=False)
    text = db.Column(db.String(128),  nullable=False)

    def __init__(self, title, text):

        self.title = title
        self.text = text

    def __repr__(self):
        return '<User %r %r>' % (self.title, self.text)

    def serialize(self):
        result = super(Entry, self).serialize()
        result.update({
            'title': self.title,
            'text': self.text
        })
        return result
