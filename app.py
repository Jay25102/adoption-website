"""sample pet adoption page project"""

from flask import Flask, render_template, request, redirect
from models import *
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddNewPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "somekey"
toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route("/")
def homepage_list_pets():
    """the root route which shows a list of all pets"""
    pets = Pet.query.all()
    return render_template("show_all_pets.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def show_add_pet():
    """renders a form to add a new pet and adds to db"""
    form = AddNewPetForm()
    
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    
    else:
        return render_template("pet_add_form.html", form=form)
    
@app.route("/pets/<int:pet_id>")
def show_pet_details(pet_id):
    """shows user a page of all the pet's details"""
    pet = Pet.query.get_or_404(pet_id)
    return render_template("pet_details.html", pet=pet)

@app.route("/<int:pet_id>/", methods=["GET", "POST"])
def edit_pet(pet_id):
    """allows user to edit a current pet"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect(f"/pets/{pet_id}")

    else:
        return render_template("edit_pet_details.html", form=form, pet=pet)
