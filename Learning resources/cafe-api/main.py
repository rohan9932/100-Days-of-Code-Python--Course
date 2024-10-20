from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    results = db.session.execute(db.select(Cafe))
    all_cafe = results.scalars().all()
    random_cafe = random.choice(all_cafe)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all_cafe():
    results = db.session.execute(db.select(Cafe))
    all_cafe = results.scalars().all()
    all_cafe_list = [cafe.to_dict() for cafe in all_cafe] # list comprehension
    return jsonify(cafes=all_cafe_list)


@app.route("/search")
def get_located_cafe():
    query_location = request.args.get("loc")
    results = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    all_cafe_on_location = results.scalars().all()
    if all_cafe_on_location:
        all_cafe_on_location_list = [cafe.to_dict() for cafe in all_cafe_on_location]
        return jsonify(cafes=all_cafe_on_location_list)
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


# HTTP POST - Create Record
@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    new_cafe = Cafe(
        name= request.form.get("name"),
        map_url= request.form.get("map_url"),
        img_url= request.form.get("img_url"),
        location= request.form.get("location"),
        seats= request.form.get("seats"),
        has_toilet= bool(request.form.get("has_toilet")),
        has_wifi= bool(request.form.get("has_wifi")),
        has_sockets= bool(request.form.get("has_sockets")),
        can_take_calls= bool(request.form.get("can_take_calls")),
        coffee_price= request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"Success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def price_update(cafe_id):
    cafe_details = db.session.get(Cafe, cafe_id)
    updated_price = request.args.get("new_price")
    if cafe_details:
        cafe_details.coffee_price = updated_price
        db.session.commit()
        return jsonify(Success="Successfully updated the price."), 200 # return the status code
    else:
        return jsonify(error={"Not Found": "A cafe with that id was not found in the database."}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    input_api_key = request.args.get("api-key")
    api_key = "TopSecretAPIKey"
    cafe = db.session.get(Cafe, cafe_id)

    if input_api_key == api_key:
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(deleted="Successfully deleted the cafe from the database."), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error="Sorry that's not allowed. Make sure you have the correct api_key."), 403



if __name__ == '__main__':
    app.run(debug=True)
