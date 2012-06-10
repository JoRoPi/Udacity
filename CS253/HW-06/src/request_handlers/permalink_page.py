# -*- coding: utf-8 -*-
from handler import Handler
import db_model.blogpost
import const_and_params
import time
   

class PermalinkPage(Handler):
    def render_front(self): #, title='', art='', error=''):
        blogposts = db_model.blogpost.get_blog_list()
        self.render('blogfront.html',
                    home_page = const_and_params.get_page_home(), 
                    blogposts=blogposts)
        
    def get(self, blog_id):
        tm, post = db_model.blogpost.get_by_id(blog_id)
        
        if not post:
            self.error(404)
            return

        template_values = {'home_page': const_and_params.get_page_home(),
                           'blogposts': [post],
                           'top_link_login': const_and_params.get_page_login(),
                           'top_link_signup': const_and_params.get_page_signup(),
                           'seconds_ago': int(round(time.time() - tm))}
        self.render('blogfront.html', **template_values)
        
