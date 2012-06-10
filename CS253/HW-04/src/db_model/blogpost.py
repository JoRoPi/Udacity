# -*- coding: utf-8 -*-
from google.appengine.ext import db

class Blogpost(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add= True)
    last_modified = db.DateTimeProperty(auto_now= True)
    
    def content_ajust_render(self):
        return self.content.replace('\n', '<br>')

    
def get_blog_list(max_list_length=10):
    return db.GqlQuery('SELECT * FROM Blogpost '
                       'ORDER BY created DESC '
                       'LIMIT %s' % max_list_length)
