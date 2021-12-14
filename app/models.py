from app import db

class Snip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rawCode = db.Column(db.String(5000))
    description = db.Column(db.String(5000))

    def __repr__(self):
        return '<Snip {}>'.format(self.rawCode)
