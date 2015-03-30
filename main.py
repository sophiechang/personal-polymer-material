#!/usr/bin/env python

import os
import webapp2
import jinja2

env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))
        
class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = env.get_template('main.html')
        self.response.out.write(template.render(template_values))        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
