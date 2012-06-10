# -*- coding: utf-8 -*-

from handler import Handler
import db_model.blogpost
import json


class BlogMainPageJson(Handler):
    def render_front(self):
        blogposts = db_model.blogpost.get_blog_list()
        self.render('blogfront.html',
                    home_page = self.get_home_url(), 
                    blogposts=blogposts)
        
    def get(self):
        posts = db_model.blogpost.get_blog_list()
        
        self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
        
        self.write(json.dumps([post.as_dict() for post in posts], sort_keys=True))
