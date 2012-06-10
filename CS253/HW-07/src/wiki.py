# -*- coding: utf-8 -*-

import os
import webapp2

from reqHandlers.wikiMainPage import WikiMainPage
from reqHandlers.loginPage import LoginPage
from reqHandlers.signupPage import SignupPage
from reqHandlers.logoutPage import LogoutPage
from reqHandlers.wikiEditPage import WikiEditPage
from reqHandlers.historyPage import HistoryPage


DEBUG = os.environ['SERVER_SOFTWARE'].startswith('Development')

PAGE_RE = r'(/(?:[a-zA-Z0-9_-]+/?)*)'

app = webapp2.WSGIApplication([('/signup', SignupPage),
                               ('/login', LoginPage),
                               ('/logout', LogoutPage),
                               ('/_edit' + PAGE_RE, WikiEditPage),
                               ('/_history' + PAGE_RE, HistoryPage),
                               (PAGE_RE, WikiMainPage),
                               ],
                              debug=DEBUG)


# http://joropi-hello-udacity.appspot.com/
# http://udacity-cs253.appspot.com/
