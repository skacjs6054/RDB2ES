from flask import Flask
import json
from elasticsearch import Elasticsearch
import atexit
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
from mymysql import *
from datetime import datetime

app = Flask(__name__)
table_config = pd.read_json('./table_config.json', typ='series').to_dict()
es_config = pd.read_json('./es_config.json', typ='series').to_dict()

conn = connDB()
cursor = cursorDB(conn)

es = Elasticsearch(hosts=es_config['host'], port=es_config['port'])

@app.route('/home')
def index():
    return "Hello World! It's RDB2ES!"

def linkDB():
    try:
        last_date = pd.read_json('./last_date.json', typ='series').to_dict()
    except ValueError:
        last_date = { "date": datetime.now() }
    if not conn :
        print("DB connect failed.")
        return False
    if not cursor :
        print("cursor connect failed")
        return False
    #print(last_date['date'])
    sql = "SELECT "+str(table_config['id'])
    for i in table_config['columns']:
        sql += ","+str(i)
    sql += " from "+str(table_config['table_name'])+" where modification_time > '"+str(last_date['date'])+"';"
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) > 0:
        #print(result)
        for row in result:
            doc = {}
            for key in row.keys():
                if key != table_config['id']:
                    doc[key] = row[key]
            es.index(index=es_config['index'], id=row[table_config['id']], body=doc)
    dayNow = datetime.now()
    last_date['date'] = str(dayNow)
    #print(last_date)
    file = open('./last_date.json', 'w')
    json.dump(last_date, file)
    file.close()


scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(func=linkDB, trigger="interval", seconds=15)
scheduler.start()

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=8080, debug=True)
    finally:
        disconnDB(conn)
        es.close()

atexit.register(lambda: scheduler.shutdown())
