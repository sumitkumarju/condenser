import string
from random import choices
from .extensions import db
from datetime import datetime

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url =  db.Column(db.String(3))
    visits = db.Column(db.Integer,default=0)
    date_created=db.Column(db.DateTime,default=datetime.now)

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.short_url=self.generate_short_link()

    def generate_short_link(self):
        characters=string.digits+string.ascii_letters
        shorturl=''.join(choices(characters,k=3))

        link = self.query.filter_by(short_url=shorturl).first()

        if link:
            self.generate_short_link()
        else:
            return shorturl





