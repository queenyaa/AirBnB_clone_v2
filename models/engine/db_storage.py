#!/usr/bin/python3

"""
DBStorage module for HBNB project
"""

from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base


class DBStorage:
    """
    DBStorage
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize the DBStorage instance """
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        connection_str = "mysql+mysqldb://{}:{}@{}/{}"
        self.__engine = create_engine(connection_str.
                        format(user, password, host, db), pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))

        self.__session = Session()

    def all(self, cls=None):
        """
        Qery all objects depending on the class name
        """
        
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        d_dict = {}

        if cls != "":
            if isinstance(cls, str) is True:
                q_result = self.__session.query(classes[cls]).all()
            else:
                q_result = self.__session.query(cls).all()
            for q_res in q_result:
                ky = "{}.{}".format(q_res.__class__.__name__, q_res.id)
                d_dict[ky] = q_res
            return (d_dict)
        else:
            for k, v in models.classes.items():
                if k != "BaseModel":
                    q_result = self.__session.query(v).all()
                    if len(q_result) > 0:
                        for q_res in q_result:
                            key = "{}.{}".format(q_res.__class__.__name__,
                                                    q_res.id)
                            d_dict[ky] = q_res
            return (d_dict)

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete obj from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables and create the current database session
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                             expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """ Close the current session """
        self.__session.close()
