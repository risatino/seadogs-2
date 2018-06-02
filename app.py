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

## raw urban population numbers
Population_urban = Table("population_urban", meta, autoload=True, autoload_with=engine)

## raw suburban population numbers
Population_suburban = Table("population_suburban", meta, autoload=True, autoload_with=engine)

## raw total population numbers
Population_total = Table("population_total", meta, autoload=True, autoload_with=engine)

## population year over year percents
PopulationYoY = Table("populationYoY", meta, autoload=True, autoload_with=engine)

## raw employment numbers
Employment = Table("employment", meta, autoload=True, autoload_with=engine)

## employment year over year percents
EmploymentYoY = Table("employmentYoY", meta, autoload=True, autoload_with=engine)

# start session
session = Session(engine)

#######################
# FLASK ROUTES
#######################

# @app.route("/")
# def index():
#     return "welcome"

# @app.route("/population_urban")
# def population():
#     results = session.query(Population_urban).all()
    
#     population_urban = []
#     for result in results:
#         population_urban_dict = {}
#         population_urban_dict["region"] = population.Region
#         population_urban_dict["cbsa_code"] = population.CBSA_Code
#         population_dict["1970"] = population.Yr_1970
#         population_dict["1971"] = population.Yr_1971
#         population_urban.append(population_urban_dict)

#     return jsonify(population_urban)

# if __name__ == "__main__":
#     app.run(debug = True)pop