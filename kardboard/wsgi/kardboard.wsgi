import sys
import logging
import os
import site

# Kardboard environment, defaults to prod - inferred from path
print "file", __file__
KENV='prod'
if os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)))).find('-test/') != -1:
    KENV='test'
    
print "env", KENV
libdir = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../../kardboard-venv-%s/lib/python2.6/site-packages' % KENV))
print "libdir", libdir

print "libdir", libdir
site.addsitedir(libdir)

import pprint
pprint.pprint(os.environ)

os.environ['KARDBOARD_SETTINGS'] = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../../../kardboard-conf/kardboard-%s.cfg' % KENV)
)

from kardboard.app import app
from kardboard import auth, charts, forms, models, tasks, tickethelpers, util, version, views

from werkzeug import run_simple
from werkzeug.contrib.profiler import ProfilerMiddleware, MergeStream

f = open('/localfs/kardboard/logs/wsgi-profiler.log', 'w')
profiled_app = ProfilerMiddleware(app, MergeStream(sys.stderr, f))

application = profiled_app

