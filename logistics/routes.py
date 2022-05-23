# Imports
from logistics import app, db, bcrypt
from flask import Flask, redirect, render_template, url_for, flash, request
from logistics.forms import RegistrationForm, LoginForm
from logistics.models import Item, User
from flask_login import login_user, current_user, logout_user, login_required

# Routes for different pages
@app.route('/')
def home():
    return redirect(url_for('dashboard'))


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            return redirect(url_for('booking'))
        else:
            flash("Login Unsuccessful. Please check email and password")
    return render_template('login.html', form = form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('booking'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form =form)


@app.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out")
    return redirect(url_for("login"))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/booking')
@login_required
def booking():
    return render_template('booking.html')

@app.route('/track')
def track():
    # Order_id=Order_id(Order="Nintendo",destination="Patna")
    # db.session.add(Order)
    # db.session.commit()


    return render_template('track.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/kart', methods=['GET', 'POST'])
def kart():
    item = Item()
    if request.method == "POST":
        item_id = request.table.get("product_id")
        print(item_id)
    # if request.method == "POST":
    #     button_id = int(request.table['name'])
    #     print(button_id)
        # item = Item.query(id = button_id).first()
        # current_user.items.append(item)
        # db.session.commit()
        # return render_template("kart.html", item = item)
        return render_template('kart.html', item = item)
    return render_template('kart.html', item = item)


if __name__ == '__main__':
    app.run(debug=True)