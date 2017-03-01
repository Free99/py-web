Terminal Blog
================
Python + MongoDB

Features
---------
* Register
* Read from your blog
* Write a new post

Screnshots
----------
* Register and write a new post  
![register_and_write](https://github.com/Free99/py-web/blob/master/TerminalBlog/screenshots/register_and_write.jpg)

* Registered, so let's read from your blog
![registered_and_read](https://github.com/Free99/py-web/blob/master/TerminalBlog/screenshots/registered_and_read.jpg)

Design
--------
* Database class
  * Initialize() -- *Use pymongo to connect my database*
  * Insert() -- *Insert new data to my collection*
  * Find() -- *Find all with given query*
  * Find_one() -- *Find one with given query*
  
* Post class
  * Constructor() -- *Collect blog_id, title, content, author, date(opt), id(opt)*
  * Save_to_mongo() -- *Save current post to database*
  * json() -- *Return current post data*
  * From_mongo() -- *Use Database.find_one() to find post from database, then return as an object*
  * From_blog() -- *Use Database.find() to get the post cursor, then return as an array of posts*
  
* Blog class
  * Constructor() -- *Collect author, blog_title, description, id(opt)*
  * New_post() -- *Collect basic post info from user, then save the post to database*
  * Get_post() -- *Find a specific post from database*
  * json() -- *Return current blog data*
  * Save_to_mongo() -- *Save current blog to database*
  * From_blog() -- *Get blog from database by id, then return it as an object*
  
* Menu class
  * _user_has_account() -- *Find blog by given author name*
  * _prompt_user_for_account() -- *Register a blog with inputs from user*
  * run_menu() -- *Collect 'Read' or 'Write' operation from user and excute the order
  * _list_blogs() -- *Display all blogs with given author name*
  * _view_blog() -- *Display all posts from the given blog id*
  
  
