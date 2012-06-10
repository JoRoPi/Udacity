# -*- coding: utf-8 -*-

from handler import Handler
import db_model.user
import const_and_params
import utils.hashing as hashing

class SignupPage(Handler):
    _tplv_username = 'username'
    _tplv_password = 'password'
    _tplv_verify = 'verify'
    _tplv_email = 'email'
    _tplv_username_msg = 'username_msg'
    _tplv_password_msg = 'password_msg'
    _tplv_verify_msg = 'verify_msg'
    _tplv_email_msg = 'email_msg'
                       
    def default_template_values(self):
        return {self._tplv_username: '', self._tplv_username_msg: '',
                self._tplv_password: '', self._tplv_password_msg: '',
                self._tplv_verify: '', self._tplv_verify_msg: '',
                self._tplv_email : '', self._tplv_email_msg:''}
    
    def set_template_values(self, values):
        template_values = self.default_template_values()
        template_values.update(values)
        return template_values
    
    def render_front(self, template_values):
        self.render('signup.html', **template_values)
        
    def get(self):
        self.render_front(self.default_template_values())
    
    def post(self):
        user_name = self.request.get(self._tplv_username)
        user_password = self.request.get(self._tplv_password)
        user_verify = self.request.get(self._tplv_verify)
        user_email = self.request.get(self._tplv_email)
        
        newuser, val_errors = db_model.user.User.create_user(user_name, user_password, user_verify, user_email)
        
        if not newuser:
            values = {self._tplv_username: user_name, self._tplv_email: user_email}
            self.set_error_msgs(val_errors, values)
            self.render_front(self.set_template_values(values))
        else:
            newuser.put()
            user_id = str(newuser.key().id())

            self.response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/' % hashing.make_cookie_hash(user_id))
            self.redirect(const_and_params.get_page_welcome())
        
    def set_error_msgs(self, val_errors, values):
        if db_model.user.User.VAL_ERROR_INVALID_USERNAME in val_errors:
            values[self._tplv_username_msg] = "That's not a valid username."
            
        if db_model.user.User.VAL_ERROR_USER_EXIST in val_errors:
            values[self._tplv_username_msg] = "That user already exits."
             
        if db_model.user.User.VAL_ERROR_INVALID_PASSWORD in val_errors:
            values[self._tplv_password_msg] = "That wasn't a valid password."
             
        if db_model.user.User.VAL_ERROR_PASSWORDS_MISMATCH in val_errors:
            values[self._tplv_verify_msg] = "Your passwords didn't match."
             
        if db_model.user.User.VAL_ERROR_INVALID_EMAIL in val_errors:
            values[self._tplv_email_msg] = "That's not a valid email."
