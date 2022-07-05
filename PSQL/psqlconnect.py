import psycopg2 as pg

import pandas as pds

from sqlalchemy import create_engine

# Create an engine instance

alchemyEngine = create_engine('postgresql://dbreaduser@3.7.81.85/beneficiaries_db');

# Connect to PostgreSQL server

dbConnection = alchemyEngine.connect();

# Read data from PostgreSQL database table and load into a DataFrame instance

dataFrame = pds.read_sql("select * from beneficiaries", dbConnection);

pds.set_option('display.expand_frame_repr', False);

# Print the DataFrame

print(dataFrame);

# Close the database connection

dbConnection.close();

