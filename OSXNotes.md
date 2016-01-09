The OS X version has been tested by a number of individuals and is recommended.  It is a [universal binary](http://www.apple.com/universal/).

# Installation #

  1. Download the disk-image file (currently:  msatcommander-0.8.1-OSX.dmg)
  1. Open it (if not opened automatically by your browser)
  1. Drag the program icon to some location (e.g. /Applications)

# Editing Primer Features #

You can make changes to primer features by editing the `primer.py` file.  This is a little complicated on OSX.

  1. Right click on the Application
  1. Choose `Show Package Contents`
  1. Double-click `Contents`
  1. Double-click `Resources`
  1. Edit `primer.py` to your liking
  1. Delete `primer.pyc` (and ONLY primer.pyc)

Primer design should support all primer3 1.1.4 features by making additions/changes in this file.

Feature changes are not currently available for the tagging options.  This is primarily because primer3 is somewhat picky with which values get input to the program. An incorrect addition could render the program useless and/or give you primers that do not work at all.

# Additional Notes #
  * Binary is built with Python 2.5.1
  * wxPython 2.8
  * BioPython 1.50
  * py2app 0.3.6 was used to build the actual executable
  * py2app was used to build the application bundle
  * source code (used as modules) are included in the tar.gz archive files