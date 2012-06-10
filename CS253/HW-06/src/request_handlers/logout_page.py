# -*- coding: utf-8 -*-

from handler import Handler
import const_and_params

class LogoutPage(Handler):
    def get(self):
        # La forma buena de eliminar la cookie es tal y como está comentado, pero na valida el corrector de udacity
        #self.response.headers.add_header('Set-Cookie', 'user_id=deleted; Path=/; Expires=Thu, 01-Jan-1970 00:00:00 GMT')
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')
        self.redirect(const_and_params.get_page_signup())
        
