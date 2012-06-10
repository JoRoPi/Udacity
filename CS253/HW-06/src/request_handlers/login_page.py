# -*- coding: utf-8 -*-

from handler import Handler
import db_model.user
import const_and_params
import utils.hashing as hashing

class LoginPage(Handler):
    _tplv_username = 'username'
    _tplv_password = 'password'
    _tplv_login_error_msg = 'login_error_msg'
                       
    def default_template_values(self):
        return {self._tplv_username: '',
                self._tplv_password: '',
                self._tplv_login_error_msg: ''}
    
    def set_template_values(self, values):
        template_values = self.default_template_values()
        template_values.update(values)
        return template_values
    
    def render_front(self, template_values):
        self.render('login.html', **template_values)
        
    def get(self):
        self.render_front(self.default_template_values())
    
    def post(self):
        user_name = self.request.get(self._tplv_username)
        user_password = self.request.get(self._tplv_password)
        
        user = db_model.user.User.get_verified_user(user_name, user_password)

        if user:
            user_id = str(user.key().id())
            self.response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/' % hashing.make_cookie_hash(user_id))
            self.redirect(const_and_params.get_page_welcome())
        else:
            values = {self._tplv_login_error_msg: 'Invalid login'}
            self.render_front(self.set_template_values(values))
        
