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
class Population_suburban(Base):
    __tablename__ = "Population_suburban"
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

# raw total population numbers
class Population_total(Base):
    __tablename__ = "Population_total"
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

# raw urban employment numbers
class Employment_urban(Base):
    __tablename__ = "Employment_urban"
    region = Column(String(100), primary_key=True)
    lat = Column(String(10))
    long = Column(String(10))
    cbsa_code = Column(String(10))
    pop_density = Column(String(10))
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

# raw suburban employment numbers
class Employment_suburban(Base):
    __tablename__ = "Employment_suburban"
    region = Column(String(100), primary_key=True)
    lat = Column(String(10))
    long = Column(String(10))
    cbsa_code = Column(String(10))
    pop_density = Column(String(10))
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

# raw total employment numbers
class Employment_total(Base):
    __tablename__ = "Employment_total"
    region = Column(String(100), primary_key=True)
    lat = Column(String(10))
    long = Column(String(10))
    cbsa_code = Column(String(10))
    pop_density = Column(String(10))
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
    
    all_populations = []
    for population_urban in results:
        population_urban_dict = {}
        population_urban_dict["region"] = population_urban.region
        population_urban_dict["lat"] = population_urban.lat
        population_urban_dict["long"] = population_urban.long
        population_urban_dict["cbsa_code"] = population_urban.cbsa_code
        population_urban_dict["pop_density"] = population_urban.pop_density
        population_urban_dict["1970"] = population_urban.Yr_1970
        population_urban_dict["1971"] = population_urban.Yr_1971
        population_urban_dict["1972"] = population_urban.Yr_1972
        population_urban_dict["1973"] = population_urban.Yr_1973
        population_urban_dict["1974"] = population_urban.Yr_1974
        population_urban_dict["1975"] = population_urban.Yr_1975
        population_urban_dict["1976"] = population_urban.Yr_1976
        population_urban_dict["1977"] = population_urban.Yr_1977
        population_urban_dict["1978"] = population_urban.Yr_1978
        population_urban_dict["1979"] = population_urban.Yr_1979
        population_urban_dict["1980"] = population_urban.Yr_1980
        population_urban_dict["1981"] = population_urban.Yr_1981
        population_urban_dict["1982"] = population_urban.Yr_1982
        population_urban_dict["1983"] = population_urban.Yr_1983
        population_urban_dict["1984"] = population_urban.Yr_1984
        population_urban_dict["1985"] = population_urban.Yr_1985
        population_urban_dict["1986"] = population_urban.Yr_1986
        population_urban_dict["1987"] = population_urban.Yr_1987
        population_urban_dict["1988"] = population_urban.Yr_1988
        population_urban_dict["1989"] = population_urban.Yr_1989
        population_urban_dict["1990"] = population_urban.Yr_1990
        population_urban_dict["1991"] = population_urban.Yr_1991
        population_urban_dict["1992"] = population_urban.Yr_1992
        population_urban_dict["1993"] = population_urban.Yr_1993
        population_urban_dict["1994"] = population_urban.Yr_1994
        population_urban_dict["1995"] = population_urban.Yr_1995
        population_urban_dict["1996"] = population_urban.Yr_1996
        population_urban_dict["1997"] = population_urban.Yr_1997
        population_urban_dict["1998"] = population_urban.Yr_1998
        population_urban_dict["1999"] = population_urban.Yr_1999
        population_urban_dict["2000"] = population_urban.Yr_2000
        population_urban_dict["2001"] = population_urban.Yr_2001
        population_urban_dict["2002"] = population_urban.Yr_2002
        population_urban_dict["2003"] = population_urban.Yr_2003
        population_urban_dict["2004"] = population_urban.Yr_2004
        population_urban_dict["2005"] = population_urban.Yr_2005
        population_urban_dict["2006"] = population_urban.Yr_2006
        population_urban_dict["2007"] = population_urban.Yr_2007
        population_urban_dict["2008"] = population_urban.Yr_2008
        population_urban_dict["2009"] = population_urban.Yr_2009
        population_urban_dict["2010"] = population_urban.Yr_2010
        population_urban_dict["2011"] = population_urban.Yr_2011
        population_urban_dict["2012"] = population_urban.Yr_2012
        population_urban_dict["2013"] = population_urban.Yr_2013
        population_urban_dict["2014"] = population_urban.Yr_2014
        population_urban_dict["2015"] = population_urban.Yr_2015
        population_urban_dict["2016"] = population_urban.Yr_2016
        population_urban_dict["2017"] = population_urban.Yr_2017
        
        all_populations.append(population_urban_dict)
  
    return jsonify(all_populations)

@app.route("/population_suburban")
def popSuburbanList():
    results = session.query(Population_suburban).all()

    all_populations = []
    for population_suburban in results:
        population_suburban_dict = {}
        population_suburban_dict["region"] = population_suburban.region
        population_suburban_dict["lat"] = population_suburban.lat
        population_suburban_dict["long"] = population_suburban.long
        population_suburban_dict["cbsa_code"] = population_suburban.cbsa_code
        population_suburban_dict["pop_density"] = population_suburban.pop_density
        population_suburban_dict["1970"] = population_suburban.Yr_1970
        population_suburban_dict["1971"] = population_suburban.Yr_1971
        population_suburban_dict["1972"] = population_suburban.Yr_1972
        population_suburban_dict["1973"] = population_suburban.Yr_1973
        population_suburban_dict["1974"] = population_suburban.Yr_1974
        population_suburban_dict["1975"] = population_suburban.Yr_1975
        population_suburban_dict["1976"] = population_suburban.Yr_1976
        population_suburban_dict["1977"] = population_suburban.Yr_1977
        population_suburban_dict["1978"] = population_suburban.Yr_1978
        population_suburban_dict["1979"] = population_suburban.Yr_1979
        population_suburban_dict["1980"] = population_suburban.Yr_1980
        population_suburban_dict["1981"] = population_suburban.Yr_1981
        population_suburban_dict["1982"] = population_suburban.Yr_1982
        population_suburban_dict["1983"] = population_suburban.Yr_1983
        population_suburban_dict["1984"] = population_suburban.Yr_1984
        population_suburban_dict["1985"] = population_suburban.Yr_1985
        population_suburban_dict["1986"] = population_suburban.Yr_1986
        population_suburban_dict["1987"] = population_suburban.Yr_1987
        population_suburban_dict["1988"] = population_suburban.Yr_1988
        population_suburban_dict["1989"] = population_suburban.Yr_1989
        population_suburban_dict["1990"] = population_suburban.Yr_1990
        population_suburban_dict["1991"] = population_suburban.Yr_1991
        population_suburban_dict["1992"] = population_suburban.Yr_1992
        population_suburban_dict["1993"] = population_suburban.Yr_1993
        population_suburban_dict["1994"] = population_suburban.Yr_1994
        population_suburban_dict["1995"] = population_suburban.Yr_1995
        population_suburban_dict["1996"] = population_suburban.Yr_1996
        population_suburban_dict["1997"] = population_suburban.Yr_1997
        population_suburban_dict["1998"] = population_suburban.Yr_1998
        population_suburban_dict["1999"] = population_suburban.Yr_1999
        population_suburban_dict["2000"] = population_suburban.Yr_2000
        population_suburban_dict["2001"] = population_suburban.Yr_2001
        population_suburban_dict["2002"] = population_suburban.Yr_2002
        population_suburban_dict["2003"] = population_suburban.Yr_2003
        population_suburban_dict["2004"] = population_suburban.Yr_2004
        population_suburban_dict["2005"] = population_suburban.Yr_2005
        population_suburban_dict["2006"] = population_suburban.Yr_2006
        population_suburban_dict["2007"] = population_suburban.Yr_2007
        population_suburban_dict["2008"] = population_suburban.Yr_2008
        population_suburban_dict["2009"] = population_suburban.Yr_2009
        population_suburban_dict["2010"] = population_suburban.Yr_2010
        population_suburban_dict["2011"] = population_suburban.Yr_2011
        population_suburban_dict["2012"] = population_suburban.Yr_2012
        population_suburban_dict["2013"] = population_suburban.Yr_2013
        population_suburban_dict["2014"] = population_suburban.Yr_2014
        population_suburban_dict["2015"] = population_suburban.Yr_2015
        population_suburban_dict["2016"] = population_suburban.Yr_2016
        population_suburban_dict["2017"] = population_suburban.Yr_2017
    
        all_populations.append(population_suburban_dict)
  
        return jsonify(all_populations)
    
@app.route("/population_total")
def popTotalList():
    results = session.query(Population_total).all()

    all_populations = []
    for population_total in results:
        population_total_dict = {}
        population_total_dict["region"] = population_total.region
        population_total_dict["lat"] = population_total
        population_total_dict["long"] = population_total.long
        population_total_dict["cbsa_code"] = population_total.cbsa_code
        population_total_dict["pop_density"] = population_total.pop_density
        population_total_dict["1970"] = population_total.Yr_1970
        population_total_dict["1971"] = population_total.Yr_1971
        population_total_dict["1972"] = population_total.Yr_1972
        population_total_dict["1973"] = population_total.Yr_1973
        population_total_dict["1974"] = population_total.Yr_1974
        population_total_dict["1975"] = population_total.Yr_1975
        population_total_dict["1976"] = population_total.Yr_1976
        population_total_dict["1977"] = population_total.Yr_1977
        population_total_dict["1978"] = population_total.Yr_1978
        population_total_dict["1979"] = population_total.Yr_1979
        population_total_dict["1980"] = population_total.Yr_1980
        population_total_dict["1981"] = population_total.Yr_1981
        population_total_dict["1982"] = population_total.Yr_1982
        population_total_dict["1983"] = population_total.Yr_1983
        population_total_dict["1984"] = population_total.Yr_1984
        population_total_dict["1985"] = population_total.Yr_1985
        population_total_dict["1986"] = population_total.Yr_1986
        population_total_dict["1987"] = population_total.Yr_1987
        population_total_dict["1988"] = population_total.Yr_1988
        population_total_dict["1989"] = population_total.Yr_1989
        population_total_dict["1990"] = population_total.Yr_1990
        population_total_dict["1991"] = population_total.Yr_1991
        population_total_dict["1992"] = population_total.Yr_1992
        population_total_dict["1993"] = population_total.Yr_1993
        population_total_dict["1994"] = population_total.Yr_1994
        population_total_dict["1995"] = population_total.Yr_1995
        population_total_dict["1996"] = population_total.Yr_1996
        population_total_dict["1997"] = population_total.Yr_1997
        population_total_dict["1998"] = population_total.Yr_1998
        population_total_dict["1999"] = population_total.Yr_1999
        population_total_dict["2000"] = population_total.Yr_2000
        population_total_dict["2001"] = population_total.Yr_2001
        population_total_dict["2002"] = population_total.Yr_2002
        population_total_dict["2003"] = population_total.Yr_2003
        population_total_dict["2004"] = population_total.Yr_2004
        population_total_dict["2005"] = population_total.Yr_2005
        population_total_dict["2006"] = population_total.Yr_2006
        population_total_dict["2007"] = population_total.Yr_2007
        population_total_dict["2008"] = population_total.Yr_2008
        population_total_dict["2009"] = population_total.Yr_2009
        population_total_dict["2010"] = population_total.Yr_2010
        population_total_dict["2011"] = population_total.Yr_2011
        population_total_dict["2012"] = population_total.Yr_2012
        population_total_dict["2013"] = population_total.Yr_2013
        population_total_dict["2014"] = population_total.Yr_2014
        population_total_dict["2015"] = population_total.Yr_2015
        population_total_dict["2016"] = population_total.Yr_2016
        population_total_dict["2017"] = population_total.Yr_2017

        all_populations.append(population_total_dict)
  
        return jsonify(all_populations)

@app.route("/employment_urban")
def empUrbanList():
    results = session.query(Employment_urban).all()
    print(len(results))

    all_employment = []
    for employment_urban in results:
        employment_urban_dict = {}
        employment_urban_dict["region"] = employment_urban.region
        employment_urban_dict["lat"] = employment_urban.lat
        employment_urban_dict["long"] = employment_urban.long
        employment_urban_dict["cbsa_code"] = employment_urban.cbsa_code
        employment_urban_dict["pop_density"] = employment_urban.pop_density
        employment_urban_dict["1990"] = employment_urban.Yr_1990
        employment_urban_dict["1991"] = employment_urban.Yr_1991
        employment_urban_dict["1992"] = employment_urban.Yr_1992
        employment_urban_dict["1993"] = employment_urban.Yr_1993
        employment_urban_dict["1994"] = employment_urban.Yr_1994
        employment_urban_dict["1995"] = employment_urban.Yr_1995
        employment_urban_dict["1996"] = employment_urban.Yr_1996
        employment_urban_dict["1997"] = employment_urban.Yr_1997
        employment_urban_dict["1998"] = employment_urban.Yr_1998
        employment_urban_dict["1999"] = employment_urban.Yr_1999
        employment_urban_dict["2000"] = employment_urban.Yr_2000
        employment_urban_dict["2001"] = employment_urban.Yr_2001
        employment_urban_dict["2002"] = employment_urban.Yr_2002
        employment_urban_dict["2003"] = employment_urban.Yr_2003
        employment_urban_dict["2004"] = employment_urban.Yr_2004
        employment_urban_dict["2005"] = employment_urban.Yr_2005
        employment_urban_dict["2006"] = employment_urban.Yr_2006
        employment_urban_dict["2007"] = employment_urban.Yr_2007
        employment_urban_dict["2008"] = employment_urban.Yr_2008
        employment_urban_dict["2009"] = employment_urban.Yr_2009
        employment_urban_dict["2010"] = employment_urban.Yr_2010
        employment_urban_dict["2011"] = employment_urban.Yr_2011
        employment_urban_dict["2012"] = employment_urban.Yr_2012
        employment_urban_dict["2013"] = employment_urban.Yr_2013
        employment_urban_dict["2014"] = employment_urban.Yr_2014
        employment_urban_dict["2015"] = employment_urban.Yr_2015
        employment_urban_dict["2016"] = employment_urban.Yr_2016
        employment_urban_dict["2017"] = employment_urban.Yr_2017
    
        all_employment.append(employment_urban_dict)
  
        return jsonify(all_employment)

@app.route("/employment_suburban")
def empSuburbanList():
    results = session.query(Employment_suburban).all()
    print(len(results))

    all_employment = []
    for employment_suburban in results:
        employment_suburban_dict = {}
        employment_suburban_dict["region"] = employment_suburban.region
        employment_suburban_dict["lat"] = employment_suburban.lat
        employment_suburban_dict["long"] = employment_suburban.long
        employment_suburban_dict["cbsa_code"] = employment_suburban.cbsa_code
        employment_suburban_dict["pop_density"] = employment_suburban.pop_density
        employment_suburban_dict["1990"] = employment_suburban.Yr_1990
        employment_suburban_dict["1991"] = employment_suburban.Yr_1991
        employment_suburban_dict["1992"] = employment_suburban.Yr_1992
        employment_suburban_dict["1993"] = employment_suburban.Yr_1993
        employment_suburban_dict["1994"] = employment_suburban.Yr_1994
        employment_suburban_dict["1995"] = employment_suburban.Yr_1995
        employment_suburban_dict["1996"] = employment_suburban.Yr_1996
        employment_suburban_dict["1997"] = employment_suburban.Yr_1997
        employment_suburban_dict["1998"] = employment_suburban.Yr_1998
        employment_suburban_dict["1999"] = employment_suburban.Yr_1999
        employment_suburban_dict["2000"] = employment_suburban.Yr_2000
        employment_suburban_dict["2001"] = employment_suburban.Yr_2001
        employment_suburban_dict["2002"] = employment_suburban.Yr_2002
        employment_suburban_dict["2003"] = employment_suburban.Yr_2003
        employment_suburban_dict["2004"] = employment_suburban.Yr_2004
        employment_suburban_dict["2005"] = employment_suburban.Yr_2005
        employment_suburban_dict["2006"] = employment_suburban.Yr_2006
        employment_suburban_dict["2007"] = employment_suburban.Yr_2007
        employment_suburban_dict["2008"] = employment_suburban.Yr_2008
        employment_suburban_dict["2009"] = employment_suburban.Yr_2009
        employment_suburban_dict["2010"] = employment_suburban.Yr_2010
        employment_suburban_dict["2011"] = employment_suburban.Yr_2011
        employment_suburban_dict["2012"] = employment_suburban.Yr_2012
        employment_suburban_dict["2013"] = employment_suburban.Yr_2013
        employment_suburban_dict["2014"] = employment_suburban.Yr_2014
        employment_suburban_dict["2015"] = employment_suburban.Yr_2015
        employment_suburban_dict["2016"] = employment_suburban.Yr_2016
        employment_suburban_dict["2017"] = employment_suburban.Yr_2017

        all_employment.append(employment_suburban_dict)
  
        return jsonify(all_employment)

if __name__ == "__main__":
    app.run(debug = True)