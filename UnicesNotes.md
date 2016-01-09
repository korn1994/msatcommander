# Getting the source #

You can check out the source from the trunk using subversion

  * `svn checkout http://msatcommander.googlecode.com/svn/trunk/ msatcommander`

You can also check the code out from github (main development area):

  * `git clone git://github.com/brantfaircloth/msatcommander.git`


# Dependencies #

Before running the code, you will likely need to install the following libraries.  The versions I use to build the OSX application are given in {x.y.z}.  Some of these packages may not be necessary depending on your platform.  I've included them because I needed them to build a proper application bundle with Py2app.  YMMV:

  * [The Qt libraries](http://qt.nokia.com/downloads) for your distribution {4.8}
  * [SIP](http://www.riverbankcomputing.co.uk/software/sip/download) {4.12.1}
  * [PyQt](http://www.riverbankcomputing.co.uk/software/pyqt/download) {4.8.2}
  * [biopython](http://biopython.org/wiki/Download) {1.54]
  * [Primer3](http://primer3.sourceforge.net) {2.2.3}

# Primer3 #

To design primers, you need to have a version of primer3 installed (or built) for your architecture.  If you want to design **tagged** primers, the you will need a modified version of primer3.  It is easiest to download and build the modified version here:

  * https://github.com/BadDNA/mod-primer3/

This version generally tracks the primer3 trunk, but I've altered the source (very slightly) to accept longer primer sequences. The particular edit you need to make to patch the source is here:

  * https://github.com/BadDNA/mod-primer3/commit/0e9dbdf4b6f5a40bca5a25d075217e2315ede3e0

# Setting up the config file #

Because the code is setup to build a package, for OSX and Windows, generally, these distributions come prepackaged with a primer3 binary.  On Unix/Linux/etc., you will need to tell msatcommander where your particular primer3 binary is located (see above note regarding primer3 binaries).  In order to do this, you must edit `msatcommander.conf` and add

  * the path to the primer3 binary
  * the path to the primer3\_config folder
  * [optional](optional.md) the path to a custom mispriming library

Generally speaking, this file will look something like the following

```
[paths]
primer3 = "./primer3_long"
primer3_config = "./primer3_config"
mispriming_library = "misprime_lib_weight"
```

Relative paths and userdir (~) expansion **should** work, but if they do not, try using absolute paths.