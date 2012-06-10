# -*- coding: utf-8 -*-
from google.appengine.ext import db
from google.appengine.api import memcache
import time

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


_key_blog_list = 'blog_list'
     
def _get_blog_list(max_list_length=10):
    return db.GqlQuery('SELECT * FROM Blogpost '
                       'ORDER BY created DESC '
                       'LIMIT %s' % max_list_length)
    
def get_blog_list(max_list_length=10, update_cache=False):
    client = memcache.Client()
    blog_list = client.get(_key_blog_list)
    
    if update_cache: # Update with CAS
        if blog_list:
            while True:
                blog_list = client.gets(_key_blog_list)
                new_blog_list = (time.time(), _get_blog_list(max_list_length))
                if client.cas(_key_blog_list, new_blog_list):
                    break
    else: # Only get or compute-and-set
        if blog_list:
            return blog_list
        else:
            blog_list = (time.time(), _get_blog_list(max_list_length))
            client.set(_key_blog_list, blog_list)
            return blog_list

def get_by_id(blog_id):
    """ blog_id: as str """
    client = memcache.Client()
    key = _key_blog_list + ': %s' % blog_id
    blog_post = client.get(key)
    if blog_post:
        return blog_post
    else:
        post = Blogpost.get_by_id(int(blog_id))
        blog_post = (time.time(), post)
        client.set(key, blog_post)
        return blog_post
 
def update_cache():
    get_blog_list(update_cache=True)

