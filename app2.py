#####################
# IMPORT DEPENDENCIES
######################

import numpy as np

# SQL Alchemy (ORM)
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, scoped_session, sessionmaker, mapper
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, inspect, func, desc, Table, Column, Integer, Float, String


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
#from flask_sqlalchemy import SQLAlchemy

# heroku set-up
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Datasets/cbsa_demographics.sqlite"

#db = SQLAlchemy(app)

# create engine
engine = create_engine("sqlite:///Datasets/cbsa_demographics.sqlite")
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
#Base.query = db_session.query_property()

# declarative tables

# raw urban population numbers
class Population_urban(Base):
    __tablename__ = "Population_urban"
    region = Column(String(100), primary_key=True)
    lat = Column(String(10))
    long = Column(String(10))
    cbsa_code = Column(String(10))
    pop_density = Column(String(10))
    Yr_1970 = Column(String(10))
    Yr_1971 = Column(String(10))
    Yr_1972 = Column(String(10))
    Yr_1973 = Column(String(10))
    Yr_1974 = Column(String(10))
    Yr_1975 = Column(String(10))
    Yr_1976 = Column(String(10))
    Yr_1977 = Column(String(10))
    Yr_1978 = Column(String(10))
    Yr_1979 = Column(String(10))
    Yr_1980 = Column(String(10))
    Yr_1981 = Column(String(10))
    Yr_1982 = Column(String(10))
    Yr_1983 = Column(String(10))
    Yr_1984 = Column(String(10))
    Yr_1985 = Column(String(10))
    Yr_1986 = Column(String(10))
    Yr_1987 = Column(String(10))
    Yr_1988 = Column(String(10))
    Yr_1989 = Column(String(10))
    Yr_1990 = Column(String(10))
    Yr_1991 = Column(String(10))
    Yr_1992 = Column(String(10))
    Yr_1993 = Column(String(10))
    Yr_1994 = Column(String(10))
    Yr_1995 = Column(String(10))
    Yr_1996 = Column(String(10))
    Yr_1997 = Column(String(10))
    Yr_1998 = Column(String(10))
    Yr_1999 = Column(String(10))
    Yr_2000 = Column(String(10))
    Yr_2001 = Column(String(10))
    Yr_2002 = Column(String(10))
    Yr_2003 = Column(String(10))
    Yr_2004 = Column(String(10))
    Yr_2005 = Column(String(10))
    Yr_2006 = Column(String(10))
    Yr_2007 = Column(String(10))
    Yr_2008 = Column(String(10))
    Yr_2009 = Column(String(10))
    Yr_2010 = Column(String(10))
    Yr_2011 = Column(String(10))
    Yr_2012 = Column(String(10))
    Yr_2013 = Column(String(10))
    Yr_2014 = Column(String(10))
    Yr_2015 = Column(String(10))
    Yr_2016 = Column(String(10))
    Yr_2017 = Column(String(10))

# # raw suburban population numbers
# class Population_suburban(db.Model):
#     __tablename__ = "Population_suburban"
#     region = Column(String(100), primary_key=True)
#     lat = Column(Float)
#     long = Column(Float)
#     cbsa_code = Column(Integer)
#     pop_density = Column(Float)
#     Yr_1970 = Column(Integer)
#     Yr_1971 = Column(Integer)
#     Yr_1972 = Column(Integer)
#     Yr_1973 = Column(Integer)
#     Yr_1974 = Column(Integer)
#     Yr_1975 = Column(Integer)
#     Yr_1976 = Column(Integer)
#     Yr_1977 = Column(Integer)
#     Yr_1978 = Column(Integer)
#     Yr_1979 = Column(Integer)
#     Yr_1980 = Column(Integer)
#     Yr_1981 = Column(Integer)
#     Yr_1982 = Column(Integer)
#     Yr_1983 = Column(Integer)
#     Yr_1984 = Column(Integer)
#     Yr_1985 = Column(Integer)
#     Yr_1986 = Column(Integer)
#     Yr_1987 = Column(Integer)
#     Yr_1988 = Column(Integer)
#     Yr_1989 = Column(Integer)
#     Yr_1990 = Column(Integer)
#     Yr_1991 = Column(Integer)
#     Yr_1992 = Column(Integer)
#     Yr_1993 = Column(Integer)
#     Yr_1994 = Column(Integer)
#     Yr_1995 = Column(Integer)
#     Yr_1996 = Column(Integer)
#     Yr_1997 = Column(Integer)
#     Yr_1998 = Column(Integer)
#     Yr_1999 = Column(Integer)
#     Yr_2000 = Column(Integer)
#     Yr_2001 = Column(Integer)
#     Yr_2002 = Column(Integer)
#     Yr_2003 = Column(Integer)
#     Yr_2004 = Column(Integer)
#     Yr_2005 = Column(Integer)
#     Yr_2006 = Column(Integer)
#     Yr_2007 = Column(Integer)
#     Yr_2008 = Column(Integer)
#     Yr_2009 = Column(Integer)
#     Yr_2010 = Column(Integer)
#     Yr_2011 = Column(Integer)
#     Yr_2012 = Column(Integer)
#     Yr_2013 = Column(Integer)
#     Yr_2014 = Column(Integer)
#     Yr_2015 = Column(Integer)
#     Yr_2016 = Column(Integer)
#     Yr_2017 = Column(Integer)

# # raw total population numbers
# class Population_total(db.Model):
#     __tablename__ = "Population_total"
#     region = Column(String(100), primary_key=True)
#     lat = Column(Float)
#     long = Column(Float)
#     cbsa_code = Column(Integer)
#     pop_density = Column(Float)
#     Yr_1970 = Column(Integer)
#     Yr_1971 = Column(Integer)
#     Yr_1972 = Column(Integer)
#     Yr_1973 = Column(Integer)
#     Yr_1974 = Column(Integer)
#     Yr_1975 = Column(Integer)
#     Yr_1976 = Column(Integer)
#     Yr_1977 = Column(Integer)
#     Yr_1978 = Column(Integer)
#     Yr_1979 = Column(Integer)
#     Yr_1980 = Column(Integer)
#     Yr_1981 = Column(Integer)
#     Yr_1982 = Column(Integer)
#     Yr_1983 = Column(Integer)
#     Yr_1984 = Column(Integer)
#     Yr_1985 = Column(Integer)
#     Yr_1986 = Column(Integer)
#     Yr_1987 = Column(Integer)
#     Yr_1988 = Column(Integer)
#     Yr_1989 = Column(Integer)
#     Yr_1990 = Column(Integer)
#     Yr_1991 = Column(Integer)
#     Yr_1992 = Column(Integer)
#     Yr_1993 = Column(Integer)
#     Yr_1994 = Column(Integer)
#     Yr_1995 = Column(Integer)
#     Yr_1996 = Column(Integer)
#     Yr_1997 = Column(Integer)
#     Yr_1998 = Column(Integer)
#     Yr_1999 = Column(Integer)
#     Yr_2000 = Column(Integer)
#     Yr_2001 = Column(Integer)
#     Yr_2002 = Column(Integer)
#     Yr_2003 = Column(Integer)
#     Yr_2004 = Column(Integer)
#     Yr_2005 = Column(Integer)
#     Yr_2006 = Column(Integer)
#     Yr_2007 = Column(Integer)
#     Yr_2008 = Column(Integer)
#     Yr_2009 = Column(Integer)
#     Yr_2010 = Column(Integer)
#     Yr_2011 = Column(Integer)
#     Yr_2012 = Column(Integer)
#     Yr_2013 = Column(Integer)
#     Yr_2014 = Column(Integer)
#     Yr_2015 = Column(Integer)
#     Yr_2016 = Column(Integer)
#     Yr_2017 = Column(Integer)

# # raw urban employment numbers
# class Employment_urban(db.Model):
#     __tablename__ = "Employment_urban"
#     region = Column(String(100), primary_key=True)
#     lat = Column(Float)
#     long = Column(Float)
#     cbsa_code = Column(Integer)
#     pop_density = Column(Float)
#     Yr_1990 = Column(Integer)
#     Yr_1991 = Column(Integer)
#     Yr_1992 = Column(Integer)
#     Yr_1993 = Column(Integer)
#     Yr_1994 = Column(Integer)
#     Yr_1995 = Column(Integer)
#     Yr_1996 = Column(Integer)
#     Yr_1997 = Column(Integer)
#     Yr_1998 = Column(Integer)
#     Yr_1999 = Column(Integer)
#     Yr_2000 = Column(Integer)
#     Yr_2001 = Column(Integer)
#     Yr_2002 = Column(Integer)
#     Yr_2003 = Column(Integer)
#     Yr_2004 = Column(Integer)
#     Yr_2005 = Column(Integer)
#     Yr_2006 = Column(Integer)
#     Yr_2007 = Column(Integer)
#     Yr_2008 = Column(Integer)
#     Yr_2009 = Column(Integer)
#     Yr_2010 = Column(Integer)
#     Yr_2011 = Column(Integer)
#     Yr_2012 = Column(Integer)
#     Yr_2013 = Column(Integer)
#     Yr_2014 = Column(Integer)
#     Yr_2015 = Column(Integer)
#     Yr_2016 = Column(Integer)
#     Yr_2017 = Column(Integer)

# # raw suburban employment numbers
# class Employment_suburban(db.Model):
#     __tablename__ = "Employment_suburban"
#     region = Column(String(100), primary_key=True)
#     lat = Column(Float)
#     long = Column(Float)
#     cbsa_code = Column(Integer)
#     pop_density = Column(Float)
#     Yr_1990 = Column(Integer)
#     Yr_1991 = Column(Integer)
#     Yr_1992 = Column(Integer)
#     Yr_1993 = Column(Integer)
#     Yr_1994 = Column(Integer)
#     Yr_1995 = Column(Integer)
#     Yr_1996 = Column(Integer)
#     Yr_1997 = Column(Integer)
#     Yr_1998 = Column(Integer)
#     Yr_1999 = Column(Integer)
#     Yr_2000 = Column(Integer)
#     Yr_2001 = Column(Integer)
#     Yr_2002 = Column(Integer)
#     Yr_2003 = Column(Integer)
#     Yr_2004 = Column(Integer)
#     Yr_2005 = Column(Integer)
#     Yr_2006 = Column(Integer)
#     Yr_2007 = Column(Integer)
#     Yr_2008 = Column(Integer)
#     Yr_2009 = Column(Integer)
#     Yr_2010 = Column(Integer)
#     Yr_2011 = Column(Integer)
#     Yr_2012 = Column(Integer)
#     Yr_2013 = Column(Integer)
#     Yr_2014 = Column(Integer)
#     Yr_2015 = Column(Integer)
#     Yr_2016 = Column(Integer)
#     Yr_2017 = Column(Integer)

# # raw total employment numbers
# class Employment_total(db.Model):
#   # __tablename__ = "Employment_total"
    # region = Column(String(100), primary_key=True)
    # lat = Column(Float)
    # long = Column(Float)
    # cbsa_code = Column(Integer)
    # pop_density = Column(Float)
    # Yr_1990 = Column(Integer)
    # Yr_1991 = Column(Integer)
    # Yr_1992 = Column(Integer)
    # Yr_1993 = Column(Integer)
    # Yr_1994 = Column(Integer)
    # Yr_1995 = Column(Integer)
    # Yr_1996 = Column(Integer)
    # Yr_1997 = Column(Integer)
    # Yr_1998 = Column(Integer)
    # Yr_1999 = Column(Integer)
    # Yr_2000 = Column(Integer)
    # Yr_2001 = Column(Integer)
    # Yr_2002 = Column(Integer)
    # Yr_2003 = Column(Integer)
    # Yr_2004 = Column(Integer)
    # Yr_2005 = Column(Integer)
    # Yr_2006 = Column(Integer)
    # Yr_2007 = Column(Integer)
    # Yr_2008 = Column(Integer)
    # Yr_2009 = Column(Integer)
    # Yr_2010 = Column(Integer)
    # Yr_2011 = Column(Integer)
    # Yr_2012 = Column(Integer)
    # Yr_2013 = Column(Integer)
    # Yr_2014 = Column(Integer)
    # Yr_2015 = Column(Integer)
    # Yr_2016 = Column(Integer)
    # Yr_2017 = Column(Integer)


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
    results = session.query(Population_urban).all()
    print(len(results))
    print(results[0].region)
    
    all_populations = []
    for population_urban in results:
        population_urban_dict = {}
        population_urban_dict["region"] = population_urban.region
        population_urban_dict["lat"] = population_urban.lat
        population_urban_dict["long"] = population_urban.long
        population_urban_dict["cbsa_code"] = population_urban.cbsa_code
        population_urban_dict["pop_density"] = population_urban.pop_density
        population_urban_dict["1970"] = population_urban.Yr_1970
        all_populations.append(population_urban_dict)
    #population_dict["1971"] = population.Yr_1971
    
    #result_dict = [u.__dict__ for u in ]
    return jsonify(all_populations)

# @app.route("/population_urban")
# def popUrbanList():
#     results = session.query(Population_urban).all()
#     pop_urban_list = list(np.ravel(results))
#     print("---")
#     print(type(pop_urban_list))
#     print("----")
#     print(type(results[0].Yr_1970))
#     print("------")
#     print(pop_urban_list)
#     #result_dict = [dict(x) for x in pop_urban_list]
#     #result_dict = [dict(x) for x in results]
#     #result_dict = [x.to_dict() for x in pop_urban_list]
#     result_dict = dict(results)
#     return jsonify(result_dict)

@app.route("/population_suburban")
def popSuburbanList():
    results = session.query(Population_suburban).all()
    pop_suburban_list = list(np.ravel(results))
    return jsonify(str(pop_suburban_list))

if __name__ == "__main__":
    app.run(debug = True)