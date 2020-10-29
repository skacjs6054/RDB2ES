import pymysql as mysql
import pandas as pd
import numpy as np

def connDB():
    try:
        dbData = pd.read_json('./mysql.json', typ='series').to_dict()
        conn = mysql.connect(user=dbData['user'], passwd=dbData['passwd'], host=dbData['host'], port=dbData['port'],db=dbData['db'], charset='utf8')
        cursor = cursorDB(conn)
        print('Opened database successfully')
        return conn
    except err:
        print('Failed opening database :', err)
        return False

def cursorDB(conn):
    try:
        cursor = conn.cursor(mysql.cursors.DictCursor)
        return cursor
    except err:
        print("Failed cursor :", err)
        return False

def commitDB(conn):
    conn.commit()

def disconnDB(conn):
    conn.close()
