# coding: utf-8
import sys
from platform import node

# Development and production hosts. Used to connect to necessary settings
DOCKER_HOSTS = ('byor.burningbuttons.com')
DEVELOPMENT_HOSTS = ('127.0.0.1')
# STAGING_HOSTS = ('ip-172-31-35-85',)
# PRODUCTION_HOSTS = ('ip-172-31-9-100',)

if len(sys.argv) > 1 and sys.argv[1] == 'test' and node() in DOCKER_HOSTS:
    from test_docker import *
elif len(sys.argv) > 1 and sys.argv[1] == 'test':
    from test import *
elif node() in DOCKER_HOSTS:
    from docker import *
elif node() in DEVELOPMENT_HOSTS:
    from dev import *
# elif node() in STAGING_HOSTS:
#     from stage import *
# elif node() in PRODUCTION_HOSTS:
#     from prod import *
else:
    raise Exception('Unknown host "%s". You have to explicitly add this host into settings in order to run the application.' % node())
