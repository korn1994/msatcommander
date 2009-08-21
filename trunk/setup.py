#!/usr/local/bin
"""
setup.py - script for building MyApplication

Usage:
    % python setup.py py2app
"""
from distutils.core import setup
import os, sys

MODULE_EXCLUDES =[
'doctest',
'pdb',
'unittest',
'inspect',
'optparse',
'pickle',
'email',
'AppKit',
'Foundation',
'bdb',
'difflib',
'tcl',
'Tkinter',
'Tkconstants',
'curses',
'distutils',
'setuptools',
'urllib2',
'BaseHTTPServer',
'_LWPCookieJar',
'_MozillaCookieJar',
'ftplib',
'gopherlib',
'_ssl',
'htmllib',
'httplib',
'mimetools',
'mimetypes',
'rfc822',
'tty',
'webbrowser',
'hashlib',
'base64',
'compiler',
'pydoc']

if os.name == 'posix':
    setup(
        name='msatcommander',
        version='0.8.2',
        description='python searching of fasta files for microsat repeats',
        author='Brant C. Faircloth',
        author_email='brant@uga.edu',
        license='GPL',
        app=['msatcommander.py'],
        setup_requires=["py2app"],
        options=dict(py2app=dict(
                packages=['Bio'],
                resources=['primer3-1.1.1/src/primer3_core',
                'mscGui.xrc', 
                'mscfunc.py',
                'mscprimer.py',
                'mscprimertag.py',
                'repeatClasses.py',
                'primer.py']
            ))
    )
    
elif os.name == 'nt':
    from distutils.core import setup
    import py2exe
    opts= {
        "py2exe":{
            #"packages":"Bio",
            "excludes":MODULE_EXCLUDES,
            "bundle_files":1,
            "compressed":True
            }
        }
    setup(
        options=opts,
        #data_files=[("",["mscGui.xrc","mscfunc.py","mscprimer.py","mscprimertag.py","repeatClasses.py","primer.py",])],
        data_files = [("",["mscGui.xrc"])],
        name='msatcommander',
        version='0.8.2',
        description='python searching of fasta files for microsat repeats',
        author='Brant C. Faircloth',
        author_email='brant@uga.edu',
        license='GPL',
        zipfile=None,
        windows=[
            {
                'script':'msatcommander.py'
            }
        ],
    )
    
else:
    sys.exit
