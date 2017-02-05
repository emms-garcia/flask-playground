from playground.models import db


class Todos(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, nullable=False)
    description = db.Column(db.Unicode, nullable=True)
    complete = db.Column(db.Boolean, nullable=False, default=False)
    user_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False,
    )

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
