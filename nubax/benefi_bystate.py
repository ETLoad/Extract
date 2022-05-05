import pandas as pd
import psycopg2 as pg
import sqlite3
from sqlalchemy import *
import pymysql
import mysql.connector as connection
from pandas.io import sql


try:
    conn = connection.connect(host="localhost", database = "nb3", user="root", passwd="", )

    df = pd.read_sql(' select count(state),state from beneficiary_address group by state', conn)
    print(df)

except Exception as e:
    print(str(e))