#####################
# IMPORT DEPENDENCIES
######################

import numpy as np

# SQL Alchemy (ORM)
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func, desc, Table

# flask (server)
from flask import(
    Flask, 
    render_template, 
    jsonify, 
    request,
    redirect)

#######################
# FLASK SET-UP
#######################
app = Flask(__name__)

#######################
# DATABASE SET-UP
#######################

# dependency
from flask_sqlalchemy import SQLAlchemy

# heroku set-up
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Datasets/cbsa_demographics.sqlite"

db = SQLAlchemy(app)

# create engine
engine = create_engine("sqlite:///Datasets/cbsa_demographics.sqlite")
#engine = db.engine
meta = db.metadata
inspector = inspect(engine)
Base = automap_base()
Base.prepare(engine, reflect = True)

# automap tables

## raw population numbers
population = Table("population", meta, autoload=True, autoload_with=engine)

## population year over year percents
populationYoY = Table("populationYoY", meta, autoload=True, autoload_with=engine)

## raw employment numbers
employment = Table("employment", meta, autoload=True, autoload_with=engine)

## employment year over year percents
employmentYoY = Table("employmentYoY", meta, autoload=True, autoload_with=engine)

# start session
session = Session(engine)

#######################
# FLASK ROUTES
#######################

@app.route("/")
def index():
    return "welcome"

@app.route("/population")
def population():
    results = session.query(population)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug = True)