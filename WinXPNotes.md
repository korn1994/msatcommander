There is no installer for the Windows XP Distribution:

  * just unzip the archive somewhere you like.  Make sure to leave all of the files in the unzipped folder.
  * if you are only searching for repeats, ensure you add the '.csv' to the filename in the save-file dialog

# Installation #

  1. Download the windows '.zip' file (currently:  msatcommander-0.8.1-WINXP.zip)
  1. Unzip the file to a location of your choosing
  1. Double-click on the msatcommander application (program icon) to run the program

# Editing Primer Features #

After much investigation, I've not determined an easy way to allow editing of the primer features in primer.py (thanks for Rick Noyes for pointing out the problem).  Although this is possible on OS X by editing the files in the application bundle, it doesn't appear to be possible on the WinXP version, because of the way in which the EXE is built.

Hopefully, I will be able to incorporate most changes into the GUI, when I have a chance.

# Additional Notes #
  * Binary is built using Python 2.5.4
  * wxPython 2.8
  * BioPython 1.51
  * py2exe 0.6.9 was used to build the actual executable
  * source code (used as modules) are included in the tar.gz archive files