# SQL Alchemy (ORM)
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func, desc

# flask (server)
from flask import(
    Flask, 
    render_template, 
    jsonify, 
    request,
    redirect)

# flask setup
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config ["SQLAlCHEMY_DATABASE_URI"] = "sqlite:///Datasets/cbsa_demographics.sqlite"

db = SQLAlchemy(app)

engine = create_engine("sqlite:///Datasets/cbsa_demographics.sqlite")
inspector = inspect(engine)
Base = automap_base()
base.prepare(engine, reflect = True)

population = Base.classes.population

session = Session(engine)

@app.route("/")
def index():
    return "welcome"

@app.route("/population")
    def population():
        regionNames =[]
        for field in inspector.get_columns(table_name = "population"):
            regionNames.append(field["region"])
        return jsonify(regionNames)

if __name__ == "__main__":
    app.run(debug = True)