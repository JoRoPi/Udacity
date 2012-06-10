import webapp2
import cgi
import urllib
import re

form_rot13="""
<form method="post">
    Enter some text to ROT13:
    <br>
    <textarea name="text" rows="8" cols="100">%(text)s</textarea>
    <br>
    <input type="submit">
</form>
"""

form_signup="""
<!doctype html>
<html>
<head>
    <title>Udacity - CS253 - HW22 signup page</title>
    <link rel="stylesheet" href="/stylesheets/master.css" type="text/css" media="screen">
</head>
<body>
    <header>
        <h1>Signup</h1>
    </header>
    <nav>
        <!-- Navigation -->
    </nav>
    <section id="intro">
        <!-- Introduction -->
    </section>
    <div id="content">
        <div id="mainConten">
            <section>
                <!-- Main content area -->
                <form method="post">
                    <p>
                        <label for="name">Username</label>
                        <input name="username" id="username" type="text" value="%(username)s">
                        <span class="error_msg">%(username_msg)s</span>
                    </p>
                    <p>
                        <label for="password">Password</label>
                        <input name="password" id="password" type="password" value="%(password)s">
                        <span class="error_msg">%(password_msg)s</span>
                    </p>
                    <p>
                        <label for="verify">Verify Password</label>
                        <input name="verify" id="verify" type="password" value="%(verify)s">
                        <span class="error_msg">%(verify_msg)s</span>
                    </p>
                    <p>
                        <label for="email">Email (optional)</label>
                        <input name="email" id="email" type="text" value="%(email)s">
                        <span class="error_msg">%(email_msg)s</span>
                    </p>
                    <p><input type="submit" value="Submit"></p>
                </form>
            </section>
        </div>
        <aside>
            <!-- Sidebar -->
        </aside>
    </div>
    <footer>
        <!-- Footer -->
    </footer>

</body>
</html>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

class HomePage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, Udacity!')
        
class HW11(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, Udacity!')
        
# Rot13
class HW21(webapp2.RequestHandler):
    def write_form(self, text=""):
        self.response.out.write(form_rot13 % {'text' : text})
        
    def get(self):
        self.write_form()
    
    def post(self):
        user_text = self.request.get('text')
        
        text = user_text.encode('rot13')
        
        self.write_form(cgi.escape(text))

# User Signup        
class HW22_signup(webapp2.RequestHandler):
    def write_form(self,
                   username="", password="", verify="", email="", 
                   username_msg="", password_msg="", verify_msg="", email_msg=""):
        self.response.out.write(form_signup % {'username': cgi.escape(username),
                                               'password': cgi.escape(password),
                                               'verify': cgi.escape(verify),
                                               'email' : cgi.escape(email),
                                               'username_msg': username_msg,
                                               'password_msg': password_msg,
                                               'verify_msg': verify_msg,
                                               'email_msg': email_msg})
        
    def get(self):
        self.write_form()
        
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
            self.write_form(user_username, "", "", user_email, username_msg, password_msg, verify_msg, email_msg)
        else:
            self.redirect('/hw22/welcome' + '?' + urllib.urlencode({'username': cgi.escape(user_username)}))

    def valid_username(self, username):
        valid = True
        err_msg = ''
        
        if not(USER_RE.match(username)):
            valid = False
            err_msg = "That's not a valid username."
            
        return valid, err_msg

    def valid_password(self, paswword):
        valid = True
        err_msg = ''
        
        if not(PASSWORD_RE.match(paswword)):
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

    def valid_email(self, email):
        valid = True
        err_msg = ''
        
        if email and not(EMAIL_RE.match(email)):
            valid = False
            err_msg = "That's not a valid email."
            
        return valid, err_msg
        
# User Signup - Welcome        
class HW22_welcome(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('Welcome, %s!' % cgi.escape(self.request.get('username')))
        

app = webapp2.WSGIApplication([('/', HomePage),
                               ('/hw11', HW11),
                               ('/hw21', HW21),
                               ('/hw22/signup', HW22_signup),
                               ('/hw22/welcome', HW22_welcome)],
                              debug=True)

# http://joropi-hello-udacity.appspot.com/hw11
# http://joropi-hello-udacity.appspot.com/hw21
# http://joropi-hello-udacity.appspot.com/hw22/signup
