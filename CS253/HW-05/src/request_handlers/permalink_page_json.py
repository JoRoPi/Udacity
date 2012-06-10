# -*- coding: utf-8 -*-
from handler import Handler
import db_model.blogpost
import json
   

class PermalinkPageJson(Handler):
    def get(self, blog_id):
        post = db_model.blogpost.Blogpost.get_by_id(int(blog_id))
        
        if not post:
            self.error(404)
            return
        
        self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
        self.write(json.dumps(post.as_dict(), sort_keys=True))
