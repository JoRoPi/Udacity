# -*- coding: utf-8 -*-

from handlerBase import HandlerBase
from db_model.user import User

class LoginPage(HandlerBase):
    def default_template_values(self):
        return {self._tp_username: '',
                self._tp_password: '',
                self._tp_login_error_msg: ''}
    
    def render_front(self, template_values):
        super(LoginPage, self).render_front('login.html', template_values)
        
    def get(self):
        self.render_front(self.default_template_values())
    
    def post(self):
        user_name = self.request.get(self._id_username)
        user_password = self.request.get(self._id_password)
        user = None
        
        if user_name and user_password:
            user = User.get_verified_user(user_name, user_password)

        if user:
            self.set_cookie_user(user.key().id())
            self.redirect('/')
        else:
            template_values = {self._tp_login_error_msg: 'Invalid login'}
            self.render_front(self.set_template_values(template_values))
        



    _tp_username = 'username'
    _tp_password = 'password'
    _tp_login_error_msg = 'login_error_msg'
    
    _id_username = 'username'
    _id_password = 'password'
                       
