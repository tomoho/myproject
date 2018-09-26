#!/usr/bin/env python
import os
import sys
from distutils.sysconfig import get_python_lib

try:
    from setuptools import find_packages,setup
except ImportError:
    from distutils.core import find_packages,setup

CURRENT_PYTHON=sys.version_info[:2]
REQUIRED_PYTHON = (3,5)

# this check and everything above must remain compatible with Python 2.7
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write('''
==========================
Unsupported Python version
==========================

This version of shippingtracke require Python {}.{},but you're trying to
install it on Python{}.{}.

This may because you are using a version of pip that doesn't understand the
python_requires classifier. Make sure you have pip >=9.0 and setuptools >=
24.2,then try again:
    $ python -m pip install --upgrade pip setuptools
    $ python -m pip install myproject
    
This will install the latest version of shippinttrack which works on your
version of Python. if you can't upgrade your pip(or Python), request an older
version of shippingtrack
    $ python -m pip install "myproject<1" 
'''.format(*(REQUIRED_PYTHON+CURRENT_PYTHON)))
    sys.exit(1)


# Warn if we are installing over top of an existing installation. This can
# cause issues where files that were deleted from a more recent package

overlay_warning =False
if "install" in sys.argv:
    lib_paths=[get_python_lib()]
    if lib_paths[0].startwith("/usr/lib/"):
        # We have to try also with an explicit prefix of /usr/local in order to
        # catch Debian's custom user site-packages directory, for example it is for raspberry pi
        lib_paths.append(get_python_lib(prefix="/usr/local"))
    for lib_path in lib_paths:
        existing_path=os.path.abspath(os.path.join(lib_path,"myproject"))
        if os.path.exists(existing_path):
            # we note the need for the warning here, but present it after the
            # command is run, so it's more likely to be seen.
            overlay_warning=True
            break

EXCLUDE_FRM_PACKAGES=[]
# Dynamically calculate the version based on shippingtrack.VERSION
version =__import__('myproject').get_version()

def read(fname):
    with open(os.path.join(os.path.dirname(__file__),fname)) as f:
        return f.read()
        )

config={
    'name':'myproject',
    'version':version,
    'python_requires'='>={}.{}'.format(*REQUIRED_PYTHON),
    'url':'',
    'download_url':'',
    'author':'tomoho',
    'auther_email':'dongmaopeng@gmail.com'
    'description':'track status and send msg through wechat',
    'long_description':read('README.rst'),
    'license':'',
    'packages':['message','track','itchat','db'],
    'install_requires':['nose'],
    'scripts':[]
    }

setup(**config)

if overlay_warning:
    sys.stderr.write('''
========
WARNING!
========

You have just installed shippingtrack over top of an existing installation,
without removing it first. Because of this,your install may now include
extraneous files from a previous version that have since been removed from
shippingtrack. This is known to cause a variety of problems. You should
manually remove then
%(existing_path)s
directory and re-install shippingtrack.
'''%{"existing_path":existing_path})



