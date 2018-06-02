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
Population = Table("Population", meta, autoload=True, autoload_with=engine)

## population year over year percents
PopulationYoY = Table("PopulationYoY", meta, autoload=True, autoload_with=engine)

## raw employment numbers
Employment = Table("Employment", meta, autoload=True, autoload_with=engine)

## employment year over year percents
EmploymentYoY = Table("EmploymentYoY", meta, autoload=True, autoload_with=engine)

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
    results = session.query(Population).all()
    
    all_populations = []
    for result in results:
        population_dict = {}
        population_dict["Region"] = population.region
        population_dict["1970"] = population.year
        population_dict["1971"] = population.year
        all_populations.append(population_dict)

    return jsonify(all_populations)

if __name__ == "__main__":
    app.run(debug = True)