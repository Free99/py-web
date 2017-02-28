from menu import Menu
from models.blog import Blog
from models.post import Post
from database import Database

__author__ = 'Tianshan'


Database.initialize()

menu = Menu()

menu.run_menu()
