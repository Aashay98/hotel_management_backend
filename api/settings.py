FL_DEBUG = True
TZ='UTC'

#
# JWT
#
JWT_SECRET = 'replace this secret'

#
# MongoEngine
#

ME_CONNECT_OPTS = {
    'db': 'database',
}
#if connecting to mongo atlas add below
"""'username':'user',
    'password':'12345',
    'host': 'mongodb://admin:qwerty@localhost/production',
"""

CORS_ALLOWED = []
CORS_HEADERS = ['Public-Session', 'CSRF-Token', 'Content-Disposition']

