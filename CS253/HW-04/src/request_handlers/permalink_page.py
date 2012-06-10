# -*- coding: utf-8 -*-
from handler import Handler
import db_model.blogpost
   

class PermalinkPage(Handler):
    def render_front(self): #, title='', art='', error=''):
        blogposts = db_model.blogpost.get_blog_list()
        self.render('blogfront.html',
                    home_page = self.get_home_url(), 
                    blogposts=blogposts)
        
    def get(self, blog_id):
        post = db_model.blogpost.Blogpost.get_by_id(int(blog_id))
        
        if not post:
            self.error(404)
            return
        
        self.render('blogfront.html',
                    home_page = self.get_home_url(), 
                    blogposts=[post])
