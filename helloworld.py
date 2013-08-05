#!/usr/bin/env python

import StringIO
import zipfile

import webapp2

class Test_GAE_Handler(webapp2.RequestHandler):
    def get(self):
        buf = StringIO.StringIO()
        with zipfile.ZipFile(buf, 'w',
                compression=zipfile.ZIP_DEFLATED) as myzip:
            for c in 'abc':
                fn = '%s.txt' % c
                myzip.writestr(fn, c*20)
        self.response.headers['Content-Type'] = 'application/zip'
        self.response.headers['Content-Disposition'] = 'inline; filename="project.zip"'
        self.response.write(buf.getvalue())

app = webapp2.WSGIApplication([
    ('/', Test_GAE_Handler)
], debug=True)
