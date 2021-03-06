# _*_ coding: utf-8 _*_

from pymongo import MongoClient
from web.config import config

mongo_config = config['mongo']


def get_conn(host=mongo_config['host'],
             port=mongo_config['port'],
             database=mongo_config['database'],
             username=mongo_config['username'],
             password=mongo_config['password']):
    if username is None or password is None:
        uri = "mongodb://%s:%d/%s" % (host, port, database)
    else:
        uri = "mongodb://%s:%s@%s:%d/%s" % (username, password, host, port, database)
    client = MongoClient(uri)
    conn = client[database]
    return conn
