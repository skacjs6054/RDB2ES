Relationship DataBase To ElasticSearch
=============

This code is just my private code to use only python that link the RDBMS to Elasticsearch.
I just share my code and I'm never responsible for the problem that is caused by this code.


Requirements
-------
 - Elasticsearch(in this used 7.9)
 - MariaDB (in this used 10.3.22, or MySQL available)
 - Flask (in this used 1.1.x)
 - and other modules that you can install by use pip
 
if you want to use this code, just use by command
```
python app.py
```

File Instruction
-------
app.py - Main code that connect rdbms and elasticsearch, and link these  
mymysql.py - the code to connect rdbms

### Please your configuration in json file.
1. es_config.json
 - host : your elasticsearch's ip address
 - port : your elasticsearch's port
 - index : your elasticsearch's index that you want to link with rdbms

2. mysql.json
 - user : your mysql user id
 - passwd : your mysql user password
 - host : your mysql's ip address
 - port : your mysql's port
 - db : your mysql's database that you want to link with Elasticsearch

3. table_config.json
 - table_name : your mysql's table that you want to link with Elasticsearchc
 - id : please mysql's column name that you want to use as a id in Elasticsearch
 - columns : mysql columns list that you want to link with elasticsearch


#### You must create the table with some fixed columns in RDBMS.
1. id
2. modification_time
3. insertion_time
please refer to [this site](https://www.elastic.co/blog/how-to-keep-elasticsearch-synchronized-with-a-relational-database-using-logstash).

