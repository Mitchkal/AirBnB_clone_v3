#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:

    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

<<<<<<< HEAD
#task 2: Improve storage
    def get(self, cls, id):
        """
        fetches specific object
        :param cls: class of object as string
        :param id: id of object as string
        :return: found object or None
        """
        all_class = self.all(cls)

        for obj in all_class.values():
            if id == str(obj.id):
                return obj

        return None

    def count(self, cls=None):
        """
	count of how many instances of a class
	:param cls: class name
	:return: count of instances of a class
	"""
        return len(self.all(cls))
=======
    def get(self, cls, id):
        """ retrieves one object from db storage"""
        if cls.__name__ in classes and id and type(id) is str:
            try:
                _obj = self.__session.query(cls).filter(cls.id == id)
                return (_obj.first())
            except Exception as e:
                print("Exception found: {}".format(e))
                return (None)

        # for clss in classes:
        # # print(clss)
        # if cls not in classes or cls is None or id is None or \
        # type(id) is not str:
        # print("error on cls, it is {} its id is {}".format(cls, cls.id))
        # return None
        # if cls is classes[clss] or cls is clss and type(id) is str:
        # print("classes clss is {} and cls is {}".
        # format(classes.get(cls), str(cls)))
        # _cls = classes[cls]
        # _obj = self.__session.query(classes[cls]).filter(cls.id == id
        # if _obj is None:
        # return None
        # return (_obj.first())

    def count(self, cls=None):
        """counts number of objects in storage"""
        count = 0

        if cls is not None:
            if cls.__name__ in classes:
                objects = self.__session.query(cls).all()
                count = len(objects)
        else:
            for key, val in classes.items():
                objects = self.__session.query(classes[key]).all()
                count += len(objects)
        return (count)
>>>>>>> development
