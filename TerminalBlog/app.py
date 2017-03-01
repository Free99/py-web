from TerminalBlog.models.database import Database
from TerminalBlog.models.menu import Menu

__author__ = 'Tianshan'


Database.initialize()

menu = Menu()

menu.run_menu()
