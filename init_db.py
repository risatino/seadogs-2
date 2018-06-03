#####################
# IMPORT DEPENDENCIES
######################


# SQL Alchemy (ORM)
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func, desc, Table

#######################
# DATABASE SET-UP
#######################

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

# reflect the tables
Base.prepare(engine, reflect=True)
Population_urban = Base.classes.population_urban
# start session
session = Session(engine)
