# -*- coding: utf-8 -*-
import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.write('Hi!')

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

