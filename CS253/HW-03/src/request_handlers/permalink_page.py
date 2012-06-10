# -*- coding: utf-8 -*-
from handler import Handler
import bd_model.blogpost
   

class PermalinkPage(Handler):
    def render_front(self): #, title='', art='', error=''):
        blogposts = bd_model.blogpost.get_blog_list()
        self.render('blogfront.html',
                    home_page = self.get_home_url(), 
                    blogposts=blogposts)
        
    def get(self, blog_id):
        post = bd_model.blogpost.Blogpost.get_by_id(int(blog_id))
        
        if not post:
            self.error(404)
            return
        
        self.render('blogfront.html',
                    home_page = self.get_home_url(), 
                    blogposts=[post])
