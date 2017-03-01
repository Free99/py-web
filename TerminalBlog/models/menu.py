from TerminalBlog.models.blog import Blog
from TerminalBlog.models.database import Database

__author__ = 'Tianshan'


class Menu(object):
    def __init__(self):
        # Check if they've already got an account
        # If not, prompt them to create one
        self.user = input("Please enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Please enter blog title: ")
        description = input("Please enter blog description: ")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input("Do you want to read (R) or write (W) blogs? ")
        if read_or_write == 'R':
            self._list_blogs()
            self._view_blog()
            pass
        elif read_or_write == 'W':
            self.user_blog.new_post()
        else:
            print("Oops, looks like its not a valid command!")

    def _list_blogs(self):
        # list blogs in database
        blogs = Database.find(collection='blogs',
                              query={'author': self.user})
        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blog(self):
        blog_to_see = input("Please enter the ID of the blog you'd like to read: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {}, Title: {}\n\n{}\n\n".format(post['created_date'], post['title'], post['content']))