#from google.appengine.ext import webapp
#from google.appengine.ext.webapp.util import run_wsgi_app
#
#
#class MainPage(webapp.RequestHandler):
#    
#    
#    def get(self):
#        self.response.headers['Content-Type'] = 'text/plain'
#        self.response.out.write('Hello, webapp World!')
#
#
#application = webapp.WSGIApplication([('/', MainPage)], debug=True)
#
#
#def main():
#    run_wsgi_app(application)
#
#if __name__ == "__main__":
#    main()

import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, Udacity!')

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)

# http://joropi-hello-udacity.appspot.com/