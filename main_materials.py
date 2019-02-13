#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import webapp2
import jinja2
from string import letters
from google.appengine.api import mail

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

USER_RE = re.compile(u"^[а-яА-ЯёЁa-zA-Z0-9]+$")
def valid_username(username):
    return username and USER_RE.match(username)

PHONE_RE = re.compile(r"^((8|\+38)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,9}$")
def valid_phone(phone):
    return phone and PHONE_RE.match(phone)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        return render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class Comfort(Handler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.render("materials.html")

    def post(self):
        username = self.request.get(u'username')
        phone = self.request.get(u'phone')
        have_error = False
        params = dict(username = username[0], phone = phone)
        if not valid_username(username):
            params['error'] = "This is an error"
            have_error = True
        if not valid_phone(phone):
            params['error'] = "This is an error"
            have_error = True
        if have_error == True:
            params['switch'] = True
            self.render('materials.html', **params)
        else:
            self.redirect('/')
        message = mail.EmailMessage(sender="alekseev1980artem@gmail.com",subject="Calling",to="artem_alexeev@rambler.ru")
        message.body = username + "  " + phone
        message.send()
        




app = webapp2.WSGIApplication([
    ('/materials.html', Comfort)],
     debug=True)
