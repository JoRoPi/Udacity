# -*- coding: utf-8 -*-
from handler import Handler
import const_and_params
import db_model.blogpost

class NewpostMainPage(Handler):
    def render_front(self, subject='', content='', error=''):
        self.render('newpost.html', 
                    home_page = const_and_params.get_page_home(),
                    subject = subject,
                    content = content,
                    error = error)
        
    def get(self):
        self.render_front()
    
    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')
        
        if subject and content:
            newpost = db_model.blogpost.Blogpost(subject = subject, content = content)
            newpost.put()
            db_model.blogpost.update_cache()
            
            self.redirect(const_and_params.get_page_home() + '/%d' % newpost.key().id())
        else:
            error = 'subject and content, please!'
            self.render_front(subject, content, error)
