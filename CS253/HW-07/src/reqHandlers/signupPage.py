# -*- coding: utf-8 -*-

from handlerBase import HandlerBase
from db_model.user import User

class SignupPage(HandlerBase):
    def default_template_values(self):
        return {self._tp_username: '', self._tp_username_msg: '',
                self._tp_password: '', self._tp_password_msg: '',
                self._tp_verify: '', self._tp_verify_msg: '',
                self._tp_email : '', self._tp_email_msg:''}
    
    def render_front(self, template_values):
        super(SignupPage, self).render_front('signup.html', template_values)
        
    def get(self):
        self.render_front(self.default_template_values())
    
    def post(self):
        user_name = self.request.get(self._id_username)
        user_password = self.request.get(self._id_password)
        user_verify = self.request.get(self._id_verify)
        user_email = self.request.get(self._id_email)
        
        newuser, val_errors = User.create_user(user_name, user_password, user_verify, user_email)
        
        if not newuser:
            templates_values = {self._tp_username: user_name, self._tp_email: user_email}
            self._set_error_msgs(val_errors, templates_values)
            self.render_front(self.set_template_values(templates_values))
        else:
            self.set_cookie_user(newuser.key().id())
            self.redirect('/')



        
    _tp_username = 'username'
    _tp_password = 'password'
    _tp_verify = 'verify'
    _tp_email = 'email'
    _tp_username_msg = 'username_msg'
    _tp_password_msg = 'password_msg'
    _tp_verify_msg = 'verify_msg'
    _tp_email_msg = 'email_msg'

    _id_username = 'username'
    _id_password = 'password'
    _id_verify = 'verify'
    _id_email = 'email'
                       
    def _set_error_msgs(self, val_errors, values):
        if User.VAL_ERROR_INVALID_USERNAME in val_errors:
            values[self._tp_username_msg] = "That's not a valid username."
            
        if User.VAL_ERROR_USER_EXIST in val_errors:
            values[self._tp_username_msg] = "That user already exits."
             
        if User.VAL_ERROR_INVALID_PASSWORD in val_errors:
            values[self._tp_password_msg] = "That wasn't a valid password."
             
        if User.VAL_ERROR_PASSWORDS_MISMATCH in val_errors:
            values[self._tp_verify_msg] = "Your passwords didn't match."
             
        if User.VAL_ERROR_INVALID_EMAIL in val_errors:
            values[self._tp_email_msg] = "That's not a valid email."
