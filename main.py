#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.api import oauth
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        try:
            # Get the db.User that represents the user on whose behalf the
            # consumer is making this request.
            user = oauth.get_current_user()
            self.response.out.write('Hello %s' % user)

        except oauth.OAuthRequestError, e:
            # The request was not a valid OAuth request.
            # ...
            self.response.out.write('Hello Anonymous')



app = webapp2.WSGIApplication([('/', MainHandler)],
                              debug=True)
