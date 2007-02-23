#!/usr/local/bin
"""
setup.py - script for building MyApplication

Usage:
    % python setup.py py2app
"""
from distutils.core import setup
import os, sys

if os.name == 'posix':
    import py2app
    setup(
        name='msatCommand',
        version='0.10',
        description='python searching of fasta files for microsat repeats',
        author='Brant C. Faircloth',
        author_email='brant@uga.edu',
        license='GPL',
        app=['msatCommandGui.py'],
    )
    
elif os.name == 'nt':
    import py2exe
    setup(
        name='msatCommand',
        version='0.10',
        description='python searching of fasta files for microsat repeats',
        author='Brant C. Faircloth',
        author_email='brant@uga.edu',
        license='GPL',
        windows=[
            {
                'script':'msatCommandGui.py',
                'icon_resources':[(1, 'gmconvert_icon_files2.ico')]
            }
        ],
    )
    
else:
    sys.exit