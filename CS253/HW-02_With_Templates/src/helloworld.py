import cgi
import jinja2
import os
import re
import urllib
import webapp2

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))


class HomePage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, Udacity!')

# Hello, Udacity!        
class HW11(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        template = jinja_environment.get_template('hw11.html')
        self.response.out.write(template.render())
        
# Rot13
class HW21(webapp2.RequestHandler):
    def write_form(self, text=""):
        template_values = {'text' : text}
        template = jinja_environment.get_template('hw21-rot13.html')
        self.response.out.write(template.render(template_values))
        
    def get(self):
        self.write_form()
    
    def post(self):
        user_text = self.request.get('text')
        text = user_text.encode('rot13')
        self.write_form(text)

# User Signup        
class HW22_signup(webapp2.RequestHandler):
    def default_template_values(self):
        template_values = {'username': '',
                           'password': '',
                           'verify': '',
                           'email' : '',
                           'username_msg': '',
                           'password_msg': '',
                           'verify_msg': '',
                           'email_msg': ''}
        return template_values
    
    def set_template_values(self, values):
        return self.default_template_values().update(values)
                
        
    def write_form(self, template_values):
        template = jinja_environment.get_template('hw22-signup.html')
        self.response.out.write(template.render(template_values))
        
    def get(self):
        self.write_form(self.default_template_values())
        
    def post(self):
        user_username = self.request.get('username')
        user_password = self.request.get('password')
        user_verify = self.request.get('verify')
        user_email = self.request.get('email')
        
        valid_username, username_msg = self.valid_username(user_username)
        valid_password, password_msg = self.valid_password(user_password)
        valid_verify, verify_msg = self.valid_verify(user_password, user_verify)
        valid_email, email_msg = self.valid_email(user_email)
        
        if not (valid_username and valid_password and valid_verify and valid_email):
            template_values = {'username': user_username,
                               'email' : user_email,
                               'username_msg': username_msg,
                               'password_msg': password_msg,
                               'verify_msg': verify_msg,
                               'email_msg': email_msg}
            self.write_form(template_values)
        else:
            self.redirect('/hw22/welcome' + '?' + urllib.urlencode({'username': cgi.escape(user_username)}))

    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    def valid_username(self, username):
        valid = True
        err_msg = ''
        
        if not(self.USER_RE.match(username)):
            valid = False
            err_msg = "That's not a valid username."
            
        return valid, err_msg

    PASSWORD_RE = re.compile(r"^.{3,20}$")
    def valid_password(self, paswword):
        valid = True
        err_msg = ''
        
        if not(self.PASSWORD_RE.match(paswword)):
            valid = False
            err_msg = "That wasn't a valid password."
            
        return valid, err_msg

    def valid_verify(self, password, verify):
        valid = True
        err_msg = ''
        
        if password != verify:
            valid = False
            err_msg = "Your passwords didn't match."
            
        return valid, err_msg

    EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
    def valid_email(self, email):
        valid = True
        err_msg = ''
        
        if email and not(self.EMAIL_RE.match(email)):
            valid = False
            err_msg = "That's not a valid email."
            
        return valid, err_msg
        
# User Signup - Welcome        
class HW22_welcome(webapp2.RequestHandler):
    def get(self):
        template_values = {'username' : self.request.get('username')}
        template = jinja_environment.get_template('hw22-welcome.html')
        self.response.out.write(template.render(template_values))
        

app = webapp2.WSGIApplication([('/', HomePage),
                               ('/hw11', HW11),
                               ('/hw21', HW21),
                               ('/hw22/signup', HW22_signup),
                               ('/hw22/welcome', HW22_welcome)],
                              debug=True)

# http://joropi-hello-udacity.appspot.com/hw11
# http://joropi-hello-udacity.appspot.com/hw21
# http://joropi-hello-udacity.appspot.com/hw22/signup
