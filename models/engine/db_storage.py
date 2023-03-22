#!/usr/bin/python3
'''A new database storage engine for our project'''
import os
import sqlalchemy
from sqlalchemy import create_engine


user = os.getenv('HBNB_MYSQL_USER', default='hbnb_dev')
password = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST', default='localhost')
database = os.getenv('HBNB_MYSQL_DB', defaulf='hbnb_dev_db')


class DBStorage:
    '''our DB storage class'''
    __engine = None
    __session = None

    def __init__(self):
        '''initialize the class'''
        string = 'mysql+mysqldb://{}:{}@{}/{}'.format(
                user, password, host, database)
        self.__engine = create_engine(string, pool_pre_ping=True)
