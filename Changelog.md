# 1.0.8 #
  * fixed an error that caused program to hang when only searching for microsatellites (thanks to Travis Glenn)

# 1.0.7 #
  * added `*`.fna files as allowable input

# 1.0.6 #
  * fixed an issue w/ the combining loci returning too few loci in certain circumstances ([issue #26](https://code.google.com/p/msatcommander/issues/detail?id=#26))
  * fixed an issue (hopefully) with the build not running on some OSX machines

# 1.0.5 #
  * fixed an issue with duplicate primer reporting in certain cases (thanks to Jarek Bryk) ([issue #25](https://code.google.com/p/msatcommander/issues/detail?id=#25))

# 1.0.4 #
  * bumped python to 2.7
  * bumped Qt, PyQT, SIP to current versions
  * fixed an issue designing primers from **large** contigs
  * fixed an issue with the subversion trunk/source on unix-like OSs ([issue #24](https://code.google.com/p/msatcommander/issues/detail?id=#24))
  * fixed an issue with the primer3 binary name by adding config file
  * fixed an issue with foreign keys in sqlite
  * fixed an issue where duplicate primers might be reported for certain loci (added visual indicator for user)
  * rearranged directory structure to be more sensible

# 1.0.3 #
  * bumped primer3\_core to 2.2.3 (stable)
  * fixed an issue with using improper tags for primer3 (doesn't affect primers previously designed)
  * updated underlying p3wrapr/primer.py to take -strict\_tags only (to prevent event above)

# 1.0.2 #
  * fixed issue with combining loci and foreign keys
  * fixed issue with incorrect amplicon size returned for tagged primers (thanks to T. Glenn for reporting)

# 1.0.1 #
  * fixed issue in locus combination code that returned an incorrect terminal position of a combined locus (i,e. it returned the start, instead of end).

# 1.0.0 #
  * replaced wxPython with Qt and PyQt
  * replaced primer3 version 1 with the primer3 version2 which incorporates thermodynamics
  * incorporated sqlite3 as a backend storage engine
  * rewrote microsatellite locating code
  * rewrote primer design code
  * rewrote main GUI code (see first entry above)
  * added ability to alter a number of primer design parameters
  * should be fully functional on OSX 10.6 in 32 and 64 bit modes

# 0.8.2 #
  * fixed issue with occasional improper treatment of overlapping bases btw. primer and tag
  * fixed issue with improper selection of repeat regions as primer binding sites using a custom mispriming file
  * altered primer product size definitions (now just 150-450 bp)
  * added ability to GTTT 'pigtail' the non-tagged primer (see Browstein et al. 1996 in [References](References.md))
  * updated Primer3 to version 1.1.4
  * updated code to work with Python 2.5 on both platforms
  * decreased size of binaries
  * Thanks go to Travis Glenn, Stacey Lance, Ken Jones, and Rick Noyes for pointing out bugs and/or requesting enhancements

# 0.8.1 #
  * changes to the code to support windows build (uses subprocess.Popen)
  * fixed an issue with spaces in directory names
  * fixed an issue with windows failing to delete a temporary file

# 0.8.0 (Unreleased, Test Version) #
  * major changes to the GUI - rebuilt for wxPython 2.8 using xml
  * addition of primer design function using primer3
  * addition of primer tagging function using primer3
  * addition of repeat combination (i,e. deals with interrupted/compound repeats)
  * now allows user-defined repeat unit length via drop-down selection
  * code cleanup and modularization to make my life easier
  * primer features may be changed by the user by editing the primer.py file (should support all primer3 1.1.1 features)

# 0.4.5 #
  * fixed spacing issue on opening output csv file in Excel (WinXP)
  * alert window now indicates when program is finished scanning
  * update of command-line version to 0.4.5
  * windows version
  * code cleanup

# 0.4.4 #
  * allow selection of '.fasta' files in File-Open Dialog (Fixed chromas issue?)
  * addition of option to output clone name and 'No Repeats Found' (T. Glenn enhancement request)
  * summary information added to end of file (T. Glenn enhancement request)
  * issue with duplicate display of repeats (particularly dinucs.) fixed
  * works in OS X 10.3.9 (no guarantees < 10.3.9)

# 0.4.3 #
  * universal binary

# 0.4.2 #
  * slight mod to GUI code
  * slight mod to output files (column-izing output of start and end bp)
  * output files are now CSV

# 0.4.1 #
  * program should work correctly (removes Fasta error)
  * rewrote regex code resulting in 2X speedup
  * can no longer overwrite input file
  * results output similar to ephemeris