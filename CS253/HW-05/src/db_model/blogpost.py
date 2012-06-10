# -*- coding: utf-8 -*-
from google.appengine.ext import db

class Blogpost(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add= True)
    last_modified = db.DateTimeProperty(auto_now= True)
    
    def content_ajust_render(self):
        return self.content.replace('\n', '<br>')
    
    def as_dict(self):
        d = {}
        d['subject'] = self.subject
        d['content'] = self.content
#        d['created'] = self.created.strftime('%a %B %d %H:%M:%S %Y')
#        d['last_modified'] = self.last_modified.strftime('%a %B %d %H:%M:%S %Y')
        d['created'] = self.created.strftime('%c')
        d['last_modified'] = self.last_modified.strftime('%c')
        return d

    
def get_blog_list(max_list_length=10):
    return db.GqlQuery('SELECT * FROM Blogpost '
                       'ORDER BY created DESC '
                       'LIMIT %s' % max_list_length)

 
