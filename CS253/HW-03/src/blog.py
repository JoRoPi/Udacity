# -*- coding: utf-8 -*-
import webapp2

from request_handlers.blog_main_page import BlogMainPage
from request_handlers.newpost_main_page import NewpostMainPage
from request_handlers.permalink_page import PermalinkPage

import const_and_params


app = webapp2.WSGIApplication([(const_and_params.get_home_page(), BlogMainPage),
                               (const_and_params.get_new_post_page(), NewpostMainPage),
                               (const_and_params.get_post_permalink_filter(), PermalinkPage)], debug=True)

# http://joropi-hello-udacity.appspot.com/blog
# http://udacity-cs253.appspot.com/blog
