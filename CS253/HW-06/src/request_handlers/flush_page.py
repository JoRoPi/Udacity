# -*- coding: utf-8 -*-

from google.appengine.api import memcache
from handler import Handler
import const_and_params
   

class FlushPage(Handler):
    def get(self):
        memcache.Client().flush_all()
        self.redirect(const_and_params.get_page_home())
