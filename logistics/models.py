from email.policy import default
from logistics import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



# This will also create the database we mentioned above
user_items = db.Table('user_items',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('item_id', db.Integer, db.ForeignKey('item.id'))
)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    items = db.relationship('Item', secondary = user_items, backref = 'things')

    def __repr__(self) -> str:
        return f"{self.username}"
    
class Item(db.Model, UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    item_name =db.Column(db.String(50),unique=False,nullable=False)
    quantity=db.Column(db.Integer,unique=False,nullable=False, default = 1)
    price = db.Column(db.Integer, unique = False, nullable = False)

    def __repr__(self) -> str:
        return f"{self.item_name}"