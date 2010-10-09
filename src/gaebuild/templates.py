production_settings = '''
DEBUG = False
SITE_TITLE = 'Site title'
TEMPLATE_PATH = 'templates'
  
# url, callschuduler
INSTALLED_APPS = [
    #('/', 'app'),
    #('/other/', 'app'),
]
'''

development_settings = '''
DEBUG = True
SITE_TITLE = 'Site title'
TEMPLATE_PATH = 'templates'
  
# url, callschuduler
INSTALLED_APPS = [
    #('/', 'app'),
    #('/other/', 'app'),
]
'''

configs = {
    'turboengine': {
        'app_py': '''
#########################################################
# Extending python path, file generated not edit
#########################################################
  
def update_path():
    import os
    import sys
     
    base_dir = os.path.abspath(os.path.dirname(__file__))
     
    local_dir = os.path.join(base_dir,'%(local)s/')
    external_dir = os.path.join(base_dir,'%(external)s/')

    lib_dir = os.path.join(base_dir,'%(lib)s/')
         
    if lib_dir not in sys.path:
        sys.path.insert(0, lib_dir)
        import site
        site.addsitedir(lib_dir)

         
    if local_dir not in sys.path:
        sys.path.insert(0, local_dir)
        
    if external_dir not in sys.path:
        sys.path.insert(0, external_dir)
     
update_path()
  
#########################################################
# End extending python path, file generated not edit
#########################################################
  
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
  
from turboengine import urls
from turboengine.conf import settings
  
application = webapp.WSGIApplication(urls.generate_urls(settings.INSTALLED_APPS), debug=settings.DEBUG)
  
def main():   
    run_wsgi_app(application)
  
if __name__ == "__main__":
    main()
        ''',
        'webservices_py':'''
#########################################################
# Extending python path, file generated
#########################################################
  
def update_path():
    import os
    import sys
     
    base_dir = os.path.abspath(os.path.dirname(__file__))
     
    local_dir = os.path.join(base_dir,'%(local)s/')
    external_dir = os.path.join(base_dir,'%(external)s/')
    lib_dir = os.path.join(base_dir,'%(lib)s/')
         
    if lib_dir not in sys.path:
        sys.path.insert(0, lib_dir)
        import site
        site.addsitedir(lib_dir)
         
    if local_dir not in sys.path:
        sys.path.insert(0, local_dir)
        
    if external_dir not in sys.path:
        sys.path.insert(0, external_dir)
     
update_path()

from turboengine.webservices.application import SOAPAplication
from turboengine.webservices.application import WSGIAplication

from EchoServer_server import * # this class is generated by 'python wsdl2py SimpleEcho.wsdl' see http://carlitos-kyo.blogspot.com/2009/12/web-services-python-google-app-engine.html

# Implementing services

class wsEchoServer(EchoServer):
    # Make WSDL available for HTTP GET
    wsdl = "".join(open('SimpleEcho.wsdl').readlines())
    disco = "".join(open('SimpleEcho.disco').readlines())

    def soap_Echo(self, ps, **kw):
        request, response = EchoServer.soap_Echo(self, ps, **kw)
        return request, request 

def main():
    application = WSGIApplication()
    application['EchoServer.asmx'] = SOAPAplication(wsEchoServer())
    #application['OtherServer.asmx'] = SOAPAplication(wsOtherServer()) # could have many webservices
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
        '''
    },
    
    'gae':{
        'app_py': '''        
#########################################################
# Extending python path, file generated
#########################################################
  
def update_path():
    import os
    import sys
     
    base_dir = os.path.abspath(os.path.dirname(__file__))
     
    local_dir = os.path.join(base_dir,'%(local)s/')
    external_dir = os.path.join(base_dir,'%(external)s/')
    lib_dir = os.path.join(base_dir,'%(lib)s/')
         
    if lib_dir not in sys.path:
        sys.path.insert(0, lib_dir)
         
    if local_dir not in sys.path:
        sys.path.insert(0, local_dir)
        
    if external_dir not in sys.path:
        sys.path.insert(0, external_dir)
     
update_path()

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!')

application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
        ''',
    },
    
    'common':{
        'app_yaml': '''
application: YOUR_APP_NAME
version: 0
runtime: python
api_version: 1
  
handlers:
# Statics files
- url: /favicon.ico
  static_files: static/favicon.ico
  upload: static/favicon.ico
   
- url: /static
  static_dir: static
   
- url: /.*
  script: app.py

# decomment this if you will use webservices 
#- url: /webservices/.*
#  script: app.py
   
skip_files:
- ^(.*/)?app\.yaml
- ^(.*/)?app\.yml
- ^(.*/)?index\.yaml
- ^(.*/)?index\.yml
- ^(.*/)?#.*#
- ^(.*/)?.*~
- ^(.*/)?.*\.py[co]
- ^(.*/)?.*/RCS/.*
- ^(.*/)?\..*
- ^(.*/)?.old\.*
- ^(.*/)?.docs\.*        
        ''',
        'index_yaml': '''
#indexes:

#- kind: Cat
#  ancestor: no
#  properties:
#  - name: name
#  - name: age
#    direction: desc        
        ''',
        'cron_yaml': '''
#cron:
#- description: daily summary job
#  url: /tasks/summary
#  schedule: every 24 hours
#- description: monday morning mailout
#  url: /mail/weekly
#  schedule: every monday 09:00
#  timezone: Australia/NSW
        ''',
        'queue_yaml': '''
#queue:
#- name: default
#  rate: 1/s
#- name: mail-queue
#  rate: 2000/d
#  bucket_size: 10
#- name: background-processing
#  rate: 5/s       
        ''',
        'dos_yaml': '''
#blacklist:
#- subnet: 1.2.3.4
#  description: a single IP address
#- subnet: 1.2.3.4/24
#  description: an IPv4 subnet
#- subnet: abcd::123:4567
#  description: an IPv6 address
#- subnet: abcd::123:4567/48
#  description: an IPv6 subnet
        ''',
    }    
}