from logistics import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



# This will also create the database we mentioned above
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    
class Order(db.Model, UserMixin):
    Order_id=db.Column(db.Integer,primary_key=True)
    Order=db.Column(db.String(50),unique=False,nullable=False)
    Quantity=db.Column(db.Integer,unique=False,nullable=False)
    Total_Cost=db.Column(db.Float,unique=False,nullable=False)
    destination=db.Column(db.String(100),unique=False,nullable=False)

    def __repr__(self) -> str:
        return f"{self.Order_id}"