# -*- coding: utf-8 -*-

import webapp2
import os
import jinja2
import utils.hashing as hashing
from db_model.user import User


template_dir = os.path.join(os.path.dirname(__file__), '../templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True, trim_blocks=True)


class HandlerBase(webapp2.RequestHandler):
    _cookie_name_user_id = 'user_id'
    
    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        self.user = None
        uid = self.read_secure_cookie(self._cookie_name_user_id)
        self.user = uid and User.by_id(int(uid))
        if not self.user:
            self.del_cookie_user()

    def set_cookie_user(self, uid):
        self.set_secure_cookie(self._cookie_name_user_id, str(uid))

    def del_cookie_user(self):
        self.delete_cookie(self._cookie_name_user_id)

    def read_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        return cookie_val and hashing.get_cookie(cookie_val)
    
    def set_secure_cookie(self, name, val):
        cookie_val = hashing.make_cookie_hash(val)
        self.response.headers.add_header(
             'Set-Cookie',
             '%s=%s; Path=/' % (name, cookie_val))

    def delete_cookie(self, name):
        if self.request.cookies.get(name):
            self.response.headers.add_header(
                 'Set-Cookie',
                 '%s=; Path=/; Expires=Thu, 01-Jan-1970 00:00:00 GMT' % name)
        
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
        
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def set_template_values(self, values):
        template_values = self.default_template_values()
        template_values.update(values)
        return template_values
    
    def render_front(self, page, template_values=None):
        if not template_values:
            template_values = self.default_template_values()
        self.render(page, **template_values)
        
    
