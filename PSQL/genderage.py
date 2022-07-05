import pandas as pd
import psycopg2 as pg
import sqlite3
from sqlalchemy import *
import pymysql
import mysql.connector as connection
from pandas.io import sql


try:
    conn = connection.connect(host="localhost", database = "nb3", user="root", passwd="", )

    df = pd.read_sql(' select count(id),age,gender from beneficiary_family group by age,gender limit 10', conn)
    print(df)

except Exception as e:
    print(str(e))