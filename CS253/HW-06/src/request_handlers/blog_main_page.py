# -*- coding: utf-8 -*-

from handler import Handler
import db_model.blogpost
import const_and_params
import time
   

class BlogMainPage(Handler):
    def render_front(self):
        tm, blogposts = db_model.blogpost.get_blog_list()
        template_values = {'home_page': const_and_params.get_page_home(),
                           'blogposts': blogposts,
                           'top_link_login': const_and_params.get_page_login(),
                           'top_link_signup': const_and_params.get_page_signup(),
                           'seconds_ago': int(round(time.time() - tm))}
        self.render('blogfront.html', **template_values)
        
    def get(self):
        self.render_front()
