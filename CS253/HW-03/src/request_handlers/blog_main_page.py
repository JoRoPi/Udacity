# -*- coding: utf-8 -*-
from handler import Handler
import bd_model.blogpost
   

class BlogMainPage(Handler):
    def render_front(self): #, title='', art='', error=''):
        blogposts = bd_model.blogpost.get_blog_list()
        self.render('blogfront.html',
                    home_page = self.get_home_url(), 
                    blogposts=blogposts)
        
    def get(self):
        self.render_front()
