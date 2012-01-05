import sys
import logging
import os
import site

libdir = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)),'../kardboard-venv/lib//python2.6/site-packages')

    )

site.addsitedir(libdir)

print "lib", libdir

from kardboard.app import app
from kardboard import auth, charts, forms, models, tasks, tickethelpers, util, version, views

from werkzeug import run_simple
from werkzeug.contrib.profiler import ProfilerMiddleware, MergeStream
print "* Profiling"
f = open('/localfs/kardboard/profiler.log', 'w')
profiled_app = ProfilerMiddleware(app, MergeStream(sys.stderr, f))

application = profiled_app

