#!/usr/local/bin
"""
setup.py - script for building MyApplication

Usage:
    % python setup.py py2app
"""

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
    # use hdiutil create -srcfolder ../dist msatcommander-0.X.X to create .dmg
    from distutils.core import setup
    import py2app
    setup(
        name='msatcommander-0.8.2',
        version='0.8.2',
        description='python searching of fasta files for microsat repeats',
        author='Brant C. Faircloth',
        author_email='brant@ucla.edu',
        license='GPL',
        app=['msatcommander.py'],
        setup_requires=["py2app"],
        options=dict(py2app=dict(
                excludes=MODULE_EXCLUDES,
                resources=['primer3_core',
                'misprime_lib_weight',
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
        data_files = [("",["mscGui.xrc", "misprime_lib_weight", "primer3_core.exe"])],
        name='msatcommander-0.8.2',
        version='0.8.2',
        description='python searching of fasta files for microsat repeats',
        author='Brant C. Faircloth',
        author_email='brant@ucla.edu',
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
