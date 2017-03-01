import uuid

import datetime
from flask import session
from WebBlog.src.common.database import Database
from WebBlog.src.models.blog import Blog

__author__ = 'Tianshan'

class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def register(cls, email, password):
        user = cls.get_user_by_email(email)
        if user is None:
            # User doesn't exist
            new_user = cls(email, password)
            new_user.save_to_mongo()
            session['email'] = email
            return True
        else:
            # Exists
            return False

    def get_blogs(self):
        return Blog.find_by_author_id(self._id)

    def json(self):
        return {
            'email': self.email,
            '_id': self._id,
            'password': self.password
        }

    def save_to_mongo(self):
        Database.insert('users', self.json())

    @classmethod
    def get_user_by_email(cls, email):
        data = Database.find_one('users', {'email': email})
        if data is not None:
            return cls(**data)
        # return None by default

    @classmethod
    def get_user_by_id(cls, _id):
        data = Database.find_one('users', {'_id': _id})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid_check(email, password):
        # Check whether email matches password
        user = User.get_user_by_email(email)
        if user is not None:
            return user.password == password
        return False

    @staticmethod
    def login(user_email):
        # login_valid has already been called
        session['email'] = user_email

    @staticmethod
    def logout():
        # Empty the email from session
        session['email'] = None

    def new_blog(self, title, description):
        # Creat a new blog
        blog = Blog(author=self.email,
                    title=title,
                    description=description,
                    author_id=self._id)
        blog.save_to_mongo()

    @staticmethod
    def new_post(blog_id, title, content, date=datetime.datetime.utcnow()):
        # Write a new post
        blog = Blog.from_mongo(blog_id)
        blog.new_post(title=title,
                      content=content,
                      date=date)