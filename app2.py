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

# heroku set-up
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Datasets/cbsa_demographics.sqlite"

# create engine
engine = create_engine("sqlite:///Datasets/cbsa_demographics.sqlite")
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()

################################
# DECLARATIVE BASE TABLE SETUP
################################

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

# year over year percent urban population numbers
class PopulationYoY_urban(Base):
    __tablename__ = "PopulationYoY_urban"
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

# year over year percent suburban population numbers
class PopulationYoY_suburban(Base):
    __tablename__ = "PopulationYoY_suburban"
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

# year over year percent total population numbers
class PopulationYoY_total(Base):
    __tablename__ = "PopulationYoY_total"
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

# year over year percent urban employment numbers
class EmploymentYoY_urban(Base):
    __tablename__ = "EmploymentYoY_urban"
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

# year over year percent suburban employment numbers
class EmploymentYoY_suburban(Base):
    __tablename__ = "EmploymentYoY_suburban"
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

# year over year percent total employment numbers
class EmploymentYoY_total(Base):
    __tablename__ = "EmploymentYoY_total"
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

# start session
session = Session(engine)

#######################
# FLASK ROUTES
#######################

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fig1")
def fig1():
    return render_template("fig1.html")

@app.route("/fig2")
def fig2():
    return render_template("fig2.html")
    
@app.route("/fig3")
def fig3():
    return render_template("fig3.html")
    
@app.route("/employment")
def employment_table():
    return render_template("resources_employment.html")
    
@app.route("/population")
def population_table():
    return render_template("resources_population.html")

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
        population_total_dict["lat"] = population_total.lat
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
        print("pie")
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

@app.route("/employment_total")
def empTotalList():
    results = session.query(Employment_total).all()

    all_employment = []
    for employment_total in results:
        employment_total_dict = {}
        employment_total_dict["region"] = employment_total.region
        employment_total_dict["lat"] = employment_total.lat
        employment_total_dict["long"] = employment_total.long
        employment_total_dict["cbsa_code"] = employment_total.cbsa_code
        employment_total_dict["pop_density"] = employment_total.pop_density
        employment_total_dict["1990"] = employment_total.Yr_1990
        employment_total_dict["1991"] = employment_total.Yr_1991
        employment_total_dict["1992"] = employment_total.Yr_1992
        employment_total_dict["1993"] = employment_total.Yr_1993
        employment_total_dict["1994"] = employment_total.Yr_1994            
        employment_total_dict["1995"] = employment_total.Yr_1995
        employment_total_dict["1996"] = employment_total.Yr_1996
        employment_total_dict["1997"] = employment_total.Yr_1997
        employment_total_dict["1998"] = employment_total.Yr_1998
        employment_total_dict["1999"] = employment_total.Yr_1999
        employment_total_dict["2000"] = employment_total.Yr_2000
        employment_total_dict["2001"] = employment_total.Yr_2001
        employment_total_dict["2002"] = employment_total.Yr_2002
        employment_total_dict["2003"] = employment_total.Yr_2003
        employment_total_dict["2004"] = employment_total.Yr_2004
        employment_total_dict["2005"] = employment_total.Yr_2005
        employment_total_dict["2006"] = employment_total.Yr_2006
        employment_total_dict["2007"] = employment_total.Yr_2007
        employment_total_dict["2008"] = employment_total.Yr_2008
        employment_total_dict["2009"] = employment_total.Yr_2009
        employment_total_dict["2010"] = employment_total.Yr_2010
        employment_total_dict["2011"] = employment_total.Yr_2011
        employment_total_dict["2012"] = employment_total.Yr_2012
        employment_total_dict["2013"] = employment_total.Yr_2013
        employment_total_dict["2014"] = employment_total.Yr_2014
        employment_total_dict["2015"] = employment_total.Yr_2015
        employment_total_dict["2016"] = employment_total.Yr_2016
        employment_total_dict["2017"] = employment_total.Yr_2017

        all_employment.append(employment_total_dict)
  
    return jsonify(all_employment)

@app.route("/populationYoY_urban")
def popYoYUrbanList():
    results = session.query(PopulationYoY_urban).all()
    print(len(results))
    
    all_populations = []
    for populationYoY_urban in results:
        populationYoY_urban_dict = {}
        populationYoY_urban_dict["region"] = populationYoY_urban.region
        populationYoY_urban_dict["lat"] = populationYoY_urban.lat
        populationYoY_urban_dict["long"] = populationYoY_urban.long
        populationYoY_urban_dict["cbsa_code"] = populationYoY_urban.cbsa_code
        populationYoY_urban_dict["pop_density"] = populationYoY_urban.pop_density
        populationYoY_urban_dict["1970"] = populationYoY_urban.Yr_1970
        populationYoY_urban_dict["1971"] = populationYoY_urban.Yr_1971
        populationYoY_urban_dict["1972"] = populationYoY_urban.Yr_1972
        populationYoY_urban_dict["1973"] = populationYoY_urban.Yr_1973
        populationYoY_urban_dict["1974"] = populationYoY_urban.Yr_1974
        populationYoY_urban_dict["1975"] = populationYoY_urban.Yr_1975
        populationYoY_urban_dict["1976"] = populationYoY_urban.Yr_1976
        populationYoY_urban_dict["1977"] = populationYoY_urban.Yr_1977
        populationYoY_urban_dict["1978"] = populationYoY_urban.Yr_1978
        populationYoY_urban_dict["1979"] = populationYoY_urban.Yr_1979
        populationYoY_urban_dict["1980"] = populationYoY_urban.Yr_1980
        populationYoY_urban_dict["1981"] = populationYoY_urban.Yr_1981
        populationYoY_urban_dict["1982"] = populationYoY_urban.Yr_1982
        populationYoY_urban_dict["1983"] = populationYoY_urban.Yr_1983
        populationYoY_urban_dict["1984"] = populationYoY_urban.Yr_1984
        populationYoY_urban_dict["1985"] = populationYoY_urban.Yr_1985
        populationYoY_urban_dict["1986"] = populationYoY_urban.Yr_1986
        populationYoY_urban_dict["1987"] = populationYoY_urban.Yr_1987
        populationYoY_urban_dict["1988"] = populationYoY_urban.Yr_1988
        populationYoY_urban_dict["1989"] = populationYoY_urban.Yr_1989
        populationYoY_urban_dict["1990"] = populationYoY_urban.Yr_1990
        populationYoY_urban_dict["1991"] = populationYoY_urban.Yr_1991
        populationYoY_urban_dict["1992"] = populationYoY_urban.Yr_1992
        populationYoY_urban_dict["1993"] = populationYoY_urban.Yr_1993
        populationYoY_urban_dict["1994"] = populationYoY_urban.Yr_1994
        populationYoY_urban_dict["1995"] = populationYoY_urban.Yr_1995
        populationYoY_urban_dict["1996"] = populationYoY_urban.Yr_1996
        populationYoY_urban_dict["1997"] = populationYoY_urban.Yr_1997
        populationYoY_urban_dict["1998"] = populationYoY_urban.Yr_1998
        populationYoY_urban_dict["1999"] = populationYoY_urban.Yr_1999
        populationYoY_urban_dict["2000"] = populationYoY_urban.Yr_2000
        populationYoY_urban_dict["2001"] = populationYoY_urban.Yr_2001
        populationYoY_urban_dict["2002"] = populationYoY_urban.Yr_2002
        populationYoY_urban_dict["2003"] = populationYoY_urban.Yr_2003
        populationYoY_urban_dict["2004"] = populationYoY_urban.Yr_2004
        populationYoY_urban_dict["2005"] = populationYoY_urban.Yr_2005
        populationYoY_urban_dict["2006"] = populationYoY_urban.Yr_2006
        populationYoY_urban_dict["2007"] = populationYoY_urban.Yr_2007
        populationYoY_urban_dict["2008"] = populationYoY_urban.Yr_2008
        populationYoY_urban_dict["2009"] = populationYoY_urban.Yr_2009
        populationYoY_urban_dict["2010"] = populationYoY_urban.Yr_2010
        populationYoY_urban_dict["2011"] = populationYoY_urban.Yr_2011
        populationYoY_urban_dict["2012"] = populationYoY_urban.Yr_2012
        populationYoY_urban_dict["2013"] = populationYoY_urban.Yr_2013
        populationYoY_urban_dict["2014"] = populationYoY_urban.Yr_2014
        populationYoY_urban_dict["2015"] = populationYoY_urban.Yr_2015
        populationYoY_urban_dict["2016"] = populationYoY_urban.Yr_2016
        populationYoY_urban_dict["2017"] = populationYoY_urban.Yr_2017
        
        all_populations.append(populationYoY_urban_dict)

@app.route("/populationYoY_suburban")
def popYoYsuburbanList():
    results = session.query(PopulationYoY_suburban).all()
    
    all_populations = []
    for populationYoY_suburban in results:
        populationYoY_suburban_dict = {}
        populationYoY_suburban_dict["region"] = populationYoY_suburban.region
        populationYoY_suburban_dict["lat"] = populationYoY_suburban.lat
        populationYoY_suburban_dict["long"] = populationYoY_suburban.long
        populationYoY_suburban_dict["cbsa_code"] = populationYoY_suburban.cbsa_code
        populationYoY_suburban_dict["pop_density"] = populationYoY_suburban.pop_density
        populationYoY_suburban_dict["1970"] = populationYoY_suburban.Yr_1970
        populationYoY_suburban_dict["1971"] = populationYoY_suburban.Yr_1971
        populationYoY_suburban_dict["1972"] = populationYoY_suburban.Yr_1972
        populationYoY_suburban_dict["1973"] = populationYoY_suburban.Yr_1973
        populationYoY_suburban_dict["1974"] = populationYoY_suburban.Yr_1974
        populationYoY_suburban_dict["1975"] = populationYoY_suburban.Yr_1975
        populationYoY_suburban_dict["1976"] = populationYoY_suburban.Yr_1976
        populationYoY_suburban_dict["1977"] = populationYoY_suburban.Yr_1977
        populationYoY_suburban_dict["1978"] = populationYoY_suburban.Yr_1978
        populationYoY_suburban_dict["1979"] = populationYoY_suburban.Yr_1979
        populationYoY_suburban_dict["1980"] = populationYoY_suburban.Yr_1980
        populationYoY_suburban_dict["1981"] = populationYoY_suburban.Yr_1981
        populationYoY_suburban_dict["1982"] = populationYoY_suburban.Yr_1982
        populationYoY_suburban_dict["1983"] = populationYoY_suburban.Yr_1983
        populationYoY_suburban_dict["1984"] = populationYoY_suburban.Yr_1984
        populationYoY_suburban_dict["1985"] = populationYoY_suburban.Yr_1985
        populationYoY_suburban_dict["1986"] = populationYoY_suburban.Yr_1986
        populationYoY_suburban_dict["1987"] = populationYoY_suburban.Yr_1987
        populationYoY_suburban_dict["1988"] = populationYoY_suburban.Yr_1988
        populationYoY_suburban_dict["1989"] = populationYoY_suburban.Yr_1989
        populationYoY_suburban_dict["1990"] = populationYoY_suburban.Yr_1990
        populationYoY_suburban_dict["1991"] = populationYoY_suburban.Yr_1991
        populationYoY_suburban_dict["1992"] = populationYoY_suburban.Yr_1992
        populationYoY_suburban_dict["1993"] = populationYoY_suburban.Yr_1993
        populationYoY_suburban_dict["1994"] = populationYoY_suburban.Yr_1994
        populationYoY_suburban_dict["1995"] = populationYoY_suburban.Yr_1995
        populationYoY_suburban_dict["1996"] = populationYoY_suburban.Yr_1996
        populationYoY_suburban_dict["1997"] = populationYoY_suburban.Yr_1997
        populationYoY_suburban_dict["1998"] = populationYoY_suburban.Yr_1998
        populationYoY_suburban_dict["1999"] = populationYoY_suburban.Yr_1999
        populationYoY_suburban_dict["2000"] = populationYoY_suburban.Yr_2000
        populationYoY_suburban_dict["2001"] = populationYoY_suburban.Yr_2001
        populationYoY_suburban_dict["2002"] = populationYoY_suburban.Yr_2002
        populationYoY_suburban_dict["2003"] = populationYoY_suburban.Yr_2003
        populationYoY_suburban_dict["2004"] = populationYoY_suburban.Yr_2004
        populationYoY_suburban_dict["2005"] = populationYoY_suburban.Yr_2005
        populationYoY_suburban_dict["2006"] = populationYoY_suburban.Yr_2006
        populationYoY_suburban_dict["2007"] = populationYoY_suburban.Yr_2007
        populationYoY_suburban_dict["2008"] = populationYoY_suburban.Yr_2008
        populationYoY_suburban_dict["2009"] = populationYoY_suburban.Yr_2009
        populationYoY_suburban_dict["2010"] = populationYoY_suburban.Yr_2010
        populationYoY_suburban_dict["2011"] = populationYoY_suburban.Yr_2011
        populationYoY_suburban_dict["2012"] = populationYoY_suburban.Yr_2012
        populationYoY_suburban_dict["2013"] = populationYoY_suburban.Yr_2013
        populationYoY_suburban_dict["2014"] = populationYoY_suburban.Yr_2014
        populationYoY_suburban_dict["2015"] = populationYoY_suburban.Yr_2015
        populationYoY_suburban_dict["2016"] = populationYoY_suburban.Yr_2016
        populationYoY_suburban_dict["2017"] = populationYoY_suburban.Yr_2017
        
        all_populations.append(populationYoY_suburban_dict)
  
    return jsonify(all_populations)

@app.route("/populationYoY_total")
def popYoYtotalList():
    results = session.query(PopulationYoY_total).all()
    
    all_populations = []
    for populationYoY_total in results:
        populationYoY_total_dict = {}
        populationYoY_total_dict["region"] = populationYoY_total.region
        populationYoY_total_dict["lat"] = populationYoY_total.lat
        populationYoY_total_dict["long"] = populationYoY_total.long
        populationYoY_total_dict["cbsa_code"] = populationYoY_total.cbsa_code
        populationYoY_total_dict["pop_density"] = populationYoY_total.pop_density
        populationYoY_total_dict["1970"] = populationYoY_total.Yr_1970
        populationYoY_total_dict["1971"] = populationYoY_total.Yr_1971
        populationYoY_total_dict["1972"] = populationYoY_total.Yr_1972
        populationYoY_total_dict["1973"] = populationYoY_total.Yr_1973
        populationYoY_total_dict["1974"] = populationYoY_total.Yr_1974
        populationYoY_total_dict["1975"] = populationYoY_total.Yr_1975
        populationYoY_total_dict["1976"] = populationYoY_total.Yr_1976
        populationYoY_total_dict["1977"] = populationYoY_total.Yr_1977
        populationYoY_total_dict["1978"] = populationYoY_total.Yr_1978
        populationYoY_total_dict["1979"] = populationYoY_total.Yr_1979
        populationYoY_total_dict["1980"] = populationYoY_total.Yr_1980
        populationYoY_total_dict["1981"] = populationYoY_total.Yr_1981
        populationYoY_total_dict["1982"] = populationYoY_total.Yr_1982
        populationYoY_total_dict["1983"] = populationYoY_total.Yr_1983
        populationYoY_total_dict["1984"] = populationYoY_total.Yr_1984
        populationYoY_total_dict["1985"] = populationYoY_total.Yr_1985
        populationYoY_total_dict["1986"] = populationYoY_total.Yr_1986
        populationYoY_total_dict["1987"] = populationYoY_total.Yr_1987
        populationYoY_total_dict["1988"] = populationYoY_total.Yr_1988
        populationYoY_total_dict["1989"] = populationYoY_total.Yr_1989
        populationYoY_total_dict["1990"] = populationYoY_total.Yr_1990
        populationYoY_total_dict["1991"] = populationYoY_total.Yr_1991
        populationYoY_total_dict["1992"] = populationYoY_total.Yr_1992
        populationYoY_total_dict["1993"] = populationYoY_total.Yr_1993
        populationYoY_total_dict["1994"] = populationYoY_total.Yr_1994
        populationYoY_total_dict["1995"] = populationYoY_total.Yr_1995
        populationYoY_total_dict["1996"] = populationYoY_total.Yr_1996
        populationYoY_total_dict["1997"] = populationYoY_total.Yr_1997
        populationYoY_total_dict["1998"] = populationYoY_total.Yr_1998
        populationYoY_total_dict["1999"] = populationYoY_total.Yr_1999
        populationYoY_total_dict["2000"] = populationYoY_total.Yr_2000
        populationYoY_total_dict["2001"] = populationYoY_total.Yr_2001
        populationYoY_total_dict["2002"] = populationYoY_total.Yr_2002
        populationYoY_total_dict["2003"] = populationYoY_total.Yr_2003
        populationYoY_total_dict["2004"] = populationYoY_total.Yr_2004
        populationYoY_total_dict["2005"] = populationYoY_total.Yr_2005
        populationYoY_total_dict["2006"] = populationYoY_total.Yr_2006
        populationYoY_total_dict["2007"] = populationYoY_total.Yr_2007
        populationYoY_total_dict["2008"] = populationYoY_total.Yr_2008
        populationYoY_total_dict["2009"] = populationYoY_total.Yr_2009
        populationYoY_total_dict["2010"] = populationYoY_total.Yr_2010
        populationYoY_total_dict["2011"] = populationYoY_total.Yr_2011
        populationYoY_total_dict["2012"] = populationYoY_total.Yr_2012
        populationYoY_total_dict["2013"] = populationYoY_total.Yr_2013
        populationYoY_total_dict["2014"] = populationYoY_total.Yr_2014
        populationYoY_total_dict["2015"] = populationYoY_total.Yr_2015
        populationYoY_total_dict["2016"] = populationYoY_total.Yr_2016
        populationYoY_total_dict["2017"] = populationYoY_total.Yr_2017
        
        all_populations.append(populationYoY_total_dict)
  
    return jsonify(all_populations)

@app.route("/employmentYoY_urban")
def empYoYUrbanList():
    results = session.query(EmploymentYoY_urban).all()
    print(len(results))

    all_employment = []
    for employmentYoY_urban in results:
        employmentYoY_urban_dict = {}
        employmentYoY_urban_dict["region"] = employmentYoY_urban.region
        employmentYoY_urban_dict["lat"] = employmentYoY_urban.lat
        employmentYoY_urban_dict["long"] = employmentYoY_urban.long
        employmentYoY_urban_dict["cbsa_code"] = employmentYoY_urban.cbsa_code
        employmentYoY_urban_dict["pop_density"] = employmentYoY_urban.pop_density
        employmentYoY_urban_dict["1990"] = employmentYoY_urban.Yr_1990
        employmentYoY_urban_dict["1991"] = employmentYoY_urban.Yr_1991
        employmentYoY_urban_dict["1992"] = employmentYoY_urban.Yr_1992
        employmentYoY_urban_dict["1993"] = employmentYoY_urban.Yr_1993
        employmentYoY_urban_dict["1994"] = employmentYoY_urban.Yr_1994
        employmentYoY_urban_dict["1995"] = employmentYoY_urban.Yr_1995
        employmentYoY_urban_dict["1996"] = employmentYoY_urban.Yr_1996
        employmentYoY_urban_dict["1997"] = employmentYoY_urban.Yr_1997
        employmentYoY_urban_dict["1998"] = employmentYoY_urban.Yr_1998
        employmentYoY_urban_dict["1999"] = employmentYoY_urban.Yr_1999
        employmentYoY_urban_dict["2000"] = employmentYoY_urban.Yr_2000
        employmentYoY_urban_dict["2001"] = employmentYoY_urban.Yr_2001
        employmentYoY_urban_dict["2002"] = employmentYoY_urban.Yr_2002
        employmentYoY_urban_dict["2003"] = employmentYoY_urban.Yr_2003
        employmentYoY_urban_dict["2004"] = employmentYoY_urban.Yr_2004
        employmentYoY_urban_dict["2005"] = employmentYoY_urban.Yr_2005
        employmentYoY_urban_dict["2006"] = employmentYoY_urban.Yr_2006
        employmentYoY_urban_dict["2007"] = employmentYoY_urban.Yr_2007
        employmentYoY_urban_dict["2008"] = employmentYoY_urban.Yr_2008
        employmentYoY_urban_dict["2009"] = employmentYoY_urban.Yr_2009
        employmentYoY_urban_dict["2010"] = employmentYoY_urban.Yr_2010
        employmentYoY_urban_dict["2011"] = employmentYoY_urban.Yr_2011
        employmentYoY_urban_dict["2012"] = employmentYoY_urban.Yr_2012
        employmentYoY_urban_dict["2013"] = employmentYoY_urban.Yr_2013
        employmentYoY_urban_dict["2014"] = employmentYoY_urban.Yr_2014
        employmentYoY_urban_dict["2015"] = employmentYoY_urban.Yr_2015
        employmentYoY_urban_dict["2016"] = employmentYoY_urban.Yr_2016
        employmentYoY_urban_dict["2017"] = employmentYoY_urban.Yr_2017
    
        all_employment.append(employmentYoY_urban_dict)
  
    return jsonify(all_employment)

@app.route("/employmentYoY_suburban")
def empYoYSuburbanList():
    results = session.query(EmploymentYoY_suburban).all()

    all_employment = []
    for employmentYoY_suburban in results:
        employmentYoY_suburban_dict = {}
        employmentYoY_suburban_dict["region"] = employmentYoY_suburban.region
        employmentYoY_suburban_dict["lat"] = employmentYoY_suburban.lat
        employmentYoY_suburban_dict["long"] = employmentYoY_suburban.long
        employmentYoY_suburban_dict["cbsa_code"] = employmentYoY_suburban.cbsa_code
        employmentYoY_suburban_dict["pop_density"] = employmentYoY_suburban.pop_density
        employmentYoY_suburban_dict["1990"] = employmentYoY_suburban.Yr_1990
        employmentYoY_suburban_dict["1991"] = employmentYoY_suburban.Yr_1991
        employmentYoY_suburban_dict["1992"] = employmentYoY_suburban.Yr_1992
        employmentYoY_suburban_dict["1993"] = employmentYoY_suburban.Yr_1993
        employmentYoY_suburban_dict["1994"] = employmentYoY_suburban.Yr_1994
        employmentYoY_suburban_dict["1995"] = employmentYoY_suburban.Yr_1995
        employmentYoY_suburban_dict["1996"] = employmentYoY_suburban.Yr_1996
        employmentYoY_suburban_dict["1997"] = employmentYoY_suburban.Yr_1997
        employmentYoY_suburban_dict["1998"] = employmentYoY_suburban.Yr_1998
        employmentYoY_suburban_dict["1999"] = employmentYoY_suburban.Yr_1999
        employmentYoY_suburban_dict["2000"] = employmentYoY_suburban.Yr_2000
        employmentYoY_suburban_dict["2001"] = employmentYoY_suburban.Yr_2001
        employmentYoY_suburban_dict["2002"] = employmentYoY_suburban.Yr_2002
        employmentYoY_suburban_dict["2003"] = employmentYoY_suburban.Yr_2003
        employmentYoY_suburban_dict["2004"] = employmentYoY_suburban.Yr_2004
        employmentYoY_suburban_dict["2005"] = employmentYoY_suburban.Yr_2005
        employmentYoY_suburban_dict["2006"] = employmentYoY_suburban.Yr_2006
        employmentYoY_suburban_dict["2007"] = employmentYoY_suburban.Yr_2007
        employmentYoY_suburban_dict["2008"] = employmentYoY_suburban.Yr_2008
        employmentYoY_suburban_dict["2009"] = employmentYoY_suburban.Yr_2009
        employmentYoY_suburban_dict["2010"] = employmentYoY_suburban.Yr_2010
        employmentYoY_suburban_dict["2011"] = employmentYoY_suburban.Yr_2011
        employmentYoY_suburban_dict["2012"] = employmentYoY_suburban.Yr_2012
        employmentYoY_suburban_dict["2013"] = employmentYoY_suburban.Yr_2013
        employmentYoY_suburban_dict["2014"] = employmentYoY_suburban.Yr_2014
        employmentYoY_suburban_dict["2015"] = employmentYoY_suburban.Yr_2015
        employmentYoY_suburban_dict["2016"] = employmentYoY_suburban.Yr_2016
        employmentYoY_suburban_dict["2017"] = employmentYoY_suburban.Yr_2017
    
        all_employment.append(employmentYoY_suburban_dict)
  
    return jsonify(all_employment)

@app.route("/employmentYoY_total")
def empYoYTotalList():
    results = session.query(EmploymentYoY_total).all()

    all_employment = []
    for employmentYoY_total in results:
        employmentYoY_total_dict = {}
        employmentYoY_total_dict["region"] = employmentYoY_total.region
        employmentYoY_total_dict["lat"] = employmentYoY_total.lat
        employmentYoY_total_dict["long"] = employmentYoY_total.long
        employmentYoY_total_dict["cbsa_code"] = employmentYoY_total.cbsa_code
        employmentYoY_total_dict["pop_density"] = employmentYoY_total.pop_density
        employmentYoY_total_dict["1990"] = employmentYoY_total.Yr_1990
        employmentYoY_total_dict["1991"] = employmentYoY_total.Yr_1991
        employmentYoY_total_dict["1992"] = employmentYoY_total.Yr_1992
        employmentYoY_total_dict["1993"] = employmentYoY_total.Yr_1993
        employmentYoY_total_dict["1994"] = employmentYoY_total.Yr_1994
        employmentYoY_total_dict["1995"] = employmentYoY_total.Yr_1995
        employmentYoY_total_dict["1996"] = employmentYoY_total.Yr_1996
        employmentYoY_total_dict["1997"] = employmentYoY_total.Yr_1997
        employmentYoY_total_dict["1998"] = employmentYoY_total.Yr_1998
        employmentYoY_total_dict["1999"] = employmentYoY_total.Yr_1999
        employmentYoY_total_dict["2000"] = employmentYoY_total.Yr_2000
        employmentYoY_total_dict["2001"] = employmentYoY_total.Yr_2001
        employmentYoY_total_dict["2002"] = employmentYoY_total.Yr_2002
        employmentYoY_total_dict["2003"] = employmentYoY_total.Yr_2003
        employmentYoY_total_dict["2004"] = employmentYoY_total.Yr_2004
        employmentYoY_total_dict["2005"] = employmentYoY_total.Yr_2005
        employmentYoY_total_dict["2006"] = employmentYoY_total.Yr_2006
        employmentYoY_total_dict["2007"] = employmentYoY_total.Yr_2007
        employmentYoY_total_dict["2008"] = employmentYoY_total.Yr_2008
        employmentYoY_total_dict["2009"] = employmentYoY_total.Yr_2009
        employmentYoY_total_dict["2010"] = employmentYoY_total.Yr_2010
        employmentYoY_total_dict["2011"] = employmentYoY_total.Yr_2011
        employmentYoY_total_dict["2012"] = employmentYoY_total.Yr_2012
        employmentYoY_total_dict["2013"] = employmentYoY_total.Yr_2013
        employmentYoY_total_dict["2014"] = employmentYoY_total.Yr_2014
        employmentYoY_total_dict["2015"] = employmentYoY_total.Yr_2015
        employmentYoY_total_dict["2016"] = employmentYoY_total.Yr_2016
        employmentYoY_total_dict["2017"] = employmentYoY_total.Yr_2017
    
        all_employment.append(employmentYoY_total_dict)
  
    return jsonify(all_employment)

if __name__ == "__main__":
    app.run(debug = True)