__author__ = 'Tianshan'

import pymongo

url = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(url)
database = client['fullstack']
collection = database['students']

student_list = [student for student in collection.find({})]