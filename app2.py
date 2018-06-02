#####################
# IMPORT DEPENDENCIES
######################

import numpy as np

# SQL Alchemy (ORM)
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, scoped_session, sessionmaker, mapper
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, inspect, func, desc, Table, Column, Integer, String


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
#db_session = scoped_session(sessionmaker(autocommit=False,
                                         #autoflush=False,
                                         #bind=engine))
Base = declarative_base()
#Base.query = db_session.query_property()

# declarative tables

## raw urban population numbers
class Population(Base):
    __table__ = "Population_urban"
    region = Column(String(100))
    lat = Column(Integer)
    long_ = Column(Integer)
    cbsa_code = Column(Integer)
    pop_density = Column(Integer)
    Yr_1970 = Column(Integer)
    Yr_1971 = Column(Integer)
    Yr_1972 =Column(Integer)
    Yr_1973 =Column(Integer)
    Yr_1974 =Column(Integer)
    Yr_1975 =Column(Integer)
    Yr_1976 =Column(Integer)
    Yr_1977 =Column(Integer)
    Yr_1978 =Column(Integer)
    Yr_1979 =Column(Integer)
    Yr_1980 =Column(Integer)
    Yr_1981 =Column(Integer)
    Yr_1982 =Column(Integer)
    Yr_1983 =Column(Integer)
    Yr_1984 =Column(Integer)
    Yr_1985 =Column(Integer)
    Yr_1986 =Column(Integer)
    Yr_1987 =Column(Integer)
    Yr_1988 =Column(Integer)
    Yr_1989 =Column(Integer)
    Yr_1990 =Column(Integer)
    Yr_1991 =Column(Integer)
    Yr_1992 =Column(Integer)
    Yr_1993 =Column(Integer)
    Yr_1994 =Column(Integer)
    Yr_1995 =Column(Integer)
    Yr_1996 =Column(Integer)
    Yr_1997 =Column(Integer)
    Yr_1998 =Column(Integer)
    Yr_1999 =Column(Integer)
    Yr_2000 =Column(Integer)
    Yr_2001 =Column(Integer)
    Yr_2002 =Column(Integer)
    Yr_2003 =Column(Integer)
    Yr_2004 =Column(Integer)
    Yr_2005 =Column(Integer)
    Yr_2006 =Column(Integer)
    Yr_2007 =Column(Integer)
    Yr_2008 =Column(Integer)
    Yr_2009 =Column(Integer)
    Yr_2010 =Column(Integer)
    Yr_2011 =Column(Integer)
    Yr_2012 =Column(Integer)
    Yr_2013 =Column(Integer)
    Yr_2014 =Column(Integer)
    Yr_2015 =Column(Integer)
    Yr_2016 =Column(Integer)
    Yr_2017 =Column(Integer)


# ## raw suburban population numbers
# Population_suburban = Table("population_suburban", meta, autoload=True, autoload_with=engine)

# ## raw total population numbers
# Population_total = Table("population_total", meta, autoload=True, autoload_with=engine)

# ## population year over year percents
# PopulationYoY = Table("populationYoY", meta, autoload=True, autoload_with=engine)

# ## raw employment numbers
# Employment = Table("employment", meta, autoload=True, autoload_with=engine)

# ## employment year over year percents
# EmploymentYoY = Table("employmentYoY", meta, autoload=True, autoload_with=engine)

# start session
session = Session(engine)

#######################
# FLASK ROUTES
#######################

@app.route("/")
def index():
    return "welcome"

@app.route("/population_urban")
def population():
    #results = session.query(Population_urban).all()
    population_urban_dict = {}
    population_urban_dict["region"] = Population_urban.Region
    population_urban_dict["cbsa_code"] = Population_urban.cbsa_code
    population_urban_dict["1970"] = Population_urban.yr_1970
    #population_dict["1971"] = population.Yr_1971
    
    return jsonify(population_urban_dict)

if __name__ == "__main__":
    app.run(debug = True)