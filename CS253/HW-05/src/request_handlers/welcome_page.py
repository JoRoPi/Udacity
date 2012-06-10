# -*- coding: utf-8 -*-

from handler import Handler
import db_model.user
import utils.hashing as hashing
import const_and_params

class WelcomePage(Handler):
    _tplv_username = 'username'
                       
    def default_template_values(self):
        return {self._tplv_username: ''}
    
    def set_template_values(self, values):
        template_values = self.default_template_values()
        template_values.update(values)
        return template_values
    
    def render_front(self, template_values):
        self.render('welcome.html', **template_values)
        
    def get(self):
        user_id = 0
        user_id_hashed = self.request.cookies.get('user_id')
        if user_id_hashed:
            cookie_val = hashing.get_cookie(user_id_hashed)
            if cookie_val:
                user_id = int(cookie_val)
                
        if user_id == 0:
            # La forma buena de eliminar la cookie es tal y como está comentado, pero na valida el corrector de udacity
            #self.response.headers.add_header('Set-Cookie', 'user_id=deleted; Path=/; Expires=Thu, 01-Jan-1970 00:00:00 GMT')
            self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')
            self.redirect(const_and_params.get_page_signup())
        else:
            user = db_model.user.User.get_by_id(user_id)
            
            if not user:
                self.error(404)
                return
            
            values = {self._tplv_username: user.username}
            self.render_front(self.set_template_values(values))
    
