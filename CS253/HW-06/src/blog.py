# -*- coding: utf-8 -*-
import webapp2

from request_handlers.blog_main_page import BlogMainPage
from request_handlers.newpost_main_page import NewpostMainPage
from request_handlers.permalink_page import PermalinkPage
from request_handlers.signup_page import SignupPage
from request_handlers.welcome_page import WelcomePage
from request_handlers.login_page import LoginPage
from request_handlers.logout_page import LogoutPage
from request_handlers.permalink_page_json import PermalinkPageJson
from request_handlers.blog_main_page_json import BlogMainPageJson
from request_handlers.flush_page import FlushPage


import const_and_params


app = webapp2.WSGIApplication([(const_and_params.get_page_home(), BlogMainPage),
                               (const_and_params.get_page_home_json(), BlogMainPageJson),
                               (const_and_params.get_page_new_post(), NewpostMainPage),
                               (const_and_params.get_filter_post_permalink_json(), PermalinkPageJson),
                               (const_and_params.get_filter_post_permalink(), PermalinkPage),
                               (const_and_params.get_page_signup(), SignupPage),
                               (const_and_params.get_page_welcome(), WelcomePage),
                               (const_and_params.get_page_login(), LoginPage),
                               (const_and_params.get_page_logout(), LogoutPage),
                               (const_and_params.get_page_flush_cache(), FlushPage)], debug=True)


# http://joropi-hello-udacity.appspot.com/blog
# http://joropi-hello-udacity.appspot.com/blog/signup
# http://udacity-cs253.appspot.com/blog
