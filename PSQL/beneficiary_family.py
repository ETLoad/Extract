# Data Migration from Postgresql to MySQL

# 1. Sync psql table to mysql

# Read data from psql table and write it to mysql using pandas dataframe
# Source readonly
# Table : beneficiaries
# DB : beneficiary_db
# psql_server = "3.7.81.85"
# psql_username = "dbreaduser"
# psql_password = "DBPROD@read$#$"
# Destination : setup mysql on localhost and write in beneficiary_db (create new db on localhost through code)


import psycopg2 as pg
import pandas as pd
from sqlalchemy import create_engine

import pymysql
import mysql.connector as connection
from pandas.io import sql



engine = pg.connect("dbname='beneficiary_db' user='dbreaduser' host='3.7.81.85' port='5432' password='DBPROD@read$#$'")
df = pd.read_sql_query('select * from beneficiary_family', con=engine, chunksize=10000)

for data in df:


    url = "mysql+pymysql://root:""@127.0.0.1/nb3"

#engine = create_engine("mysql+pymysql://" + "root" + ":" + "" + "@" + "127.0.0.1" + "/" + "beneficiary_db")

    engine = create_engine(url)
    data.to_sql('beneficiary_family', con = engine, if_exists = 'append')

print("Done")
