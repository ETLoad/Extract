import pandas as pd
import psycopg2 as pg
import sqlite3
from sqlalchemy import *
import pymysql
import mysql.connector as connection
from pandas.io import sql


try:
    conn = connection.connect(host="localhost", database = "nb3", user="root", passwd="", )
#engine = pg.connect("dbname='beneficiary_db' user='dbreaduser' host='3.7.81.85' port='5432' password='DBPROD@read$#$'")
#df = pd.read_sql('select * from beneficiaries ', con=engine)
    df = pd.read_sql(' select count(id) from df ', conn)
    print(df)

#engine=create_engine("mysql+pymysql://" + "root" + ":" + "" + "@" + "127.0.0.1" + "/" + "nb3")
#df.to_sql('df', engine, if_exists='replace', index = False)
except Exception as e:
    print(str(e))