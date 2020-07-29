"""Blogly application."""

from flask import Flask, request, render_template, redirect, session, flash, make_response, jsonify, url_for
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pets
from forms import AddPet, EditPet

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension(app)

@app.route('/')
def root():
    pets=Pets.query.all()
    return render_template("homepage.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    form = AddPet()
    species=[(None, 'Choose ...'), ('cat', 'cat'), ('dog', 'dog'), ('porcupine', 'porcupine')]
    form.species.choices=species

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        pet = Pets(**data)

        db.session.add(pet)
        db.session.commit()

        return redirect("/")
    else:
        return render_template("add.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    pet = Pets.query.get_or_404(pet_id)
    form = EditPet(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()

        return redirect(url_for('root'))
    else:
        return render_template("details.html", form=form, pet=pet)
