#!/usr/bin/python3
'''A new database storage engine for our project'''
import os
from models.base_model import Base
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity


user = os.getenv('HBNB_MYSQL_USER', default='hbnb_dev')
password = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST', default='localhost')
database = os.getenv('HBNB_MYSQL_DB', default='hbnb_dev_db')


class DBStorage:
    '''our DB storage class'''
    __engine = None
    __session = None

    def __init__(self):
        '''initialize the class'''
        string = 'mysql+mysqldb://{}:{}@{}/{}'.format(
                user, password, host, database)
        self.__engine = create_engine(string, pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        '''query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        if cls=None, query all types of objects (User, State, City,
        Amenity, Place and Review)'''

        if cls == None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            classes = {"State": State, "City": City, "User": User, "Place": Place, "Review": Review, "Amenity": Amenity}

            if cls not in classes.keys():
                if cls not in classes.values():
                    return

            if type(cls).__name__ == 'str':
                objs = self__session.query(classes[cls])
            else:
                objs = self.__session.query(cls)

        new_dict = {}
        for obj in objs:
            new_dict["{}.{}".format(type(obj).__name__, obj.id)] = obj
        
        return new_dict

    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)
    
    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()
    
    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        '''close the session'''
        self.__session.close()

