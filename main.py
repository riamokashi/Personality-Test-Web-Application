import webapp2
import jinja2
import os
import urllib
from google.appengine.api import urlfetch
import json
from google.appengine.api import users
from google.appengine.ext import ndb

jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class loginPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            email_address = user.nickname()
            logout_url = users.create_logout_url('/')
            logout_button = '<a href="%s" class="logOut">Log Out</a>'  % logout_url
            self.response.write(logout_button)
            main_template = jinja_current_dir.get_template("main.html")
            self.response.write(main_template.render())
        else:
            login_url = users.create_login_url('/')
            login_button = '<a href="%s" class="signIn"><center>Sign In</center></a>'  % login_url
            self.response.write(login_button)
            self.redirect('/survey')

class Survey(webapp2.RequestHandler):
    def get(self):
        survey_template = jinja_current_dir.get_template("survey.html")
        self.response.write(survey_template.render())
    def post(self):
        user = users.get_current_user()
        if user:
            music_user = MusicUser(
                name =self.request.get('name'),
                number=self.request.get('number'),
                color = self.request.get('color'),
                genre = self.request.get('genre'),
                food= self.request.get('food'),
            )
            music_user.put()
            self.redirect('/survey')
            
class Personality1(webapp2.RequestHandler):
   def get(self):
        p1_template = jinja_current_dir.get_template("p1.html")
        self.response.write(p1_template.render())

class Personality2(webapp2.RequestHandler):
   def get(self):
        p2_template = jinja_current_dir.get_template("p2.html")
        self.response.write(p2_template.render())

class Personality3(webapp2.RequestHandler):
   def get(self):
        p3_template = jinja_current_dir.get_template("p3.html")
        self.response.write(p3_template.render())


class Personality4(webapp2.RequestHandler):
   def get(self):
        p4_template = jinja_current_dir.get_template("p4.html")
        self.response.write(p4_template.render())


app = webapp2.WSGIApplication([
    ('/', loginPage),
    ('/survey', Survey),
    ('/p1', Personality1),
    ('/p2', Personality2),
    ('/p3', Personality3),
    ('/p4', Personality4),
], debug=True)
