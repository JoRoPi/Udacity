# -*- coding: utf-8 -*-

from handlerBase import HandlerBase

class LogoutPage(HandlerBase):
    def get(self):
        self.del_cookie_user()
        self.redirect('/')
        
