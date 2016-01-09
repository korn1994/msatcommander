## News ##
**06/25/2011**:  Added ability to input `*.fna` files.  Fixed an error with microsat scanning that caused program to hang.  1.0.8 available in [Downloads](http://code.google.com/p/msatcommander/downloads/list)

This is prerelease software - and you should use it carefully.  Please report any bugs to the mailing list or directly to me.  The binary version of msatcommander (available for download) is for OSX 10.6 and greater **only**.  If you are using 10.5 or earlier, you will need to checkout the [source code](http://code.google.com/p/msatcommander/source/checkout) instead.

Now, here's what it looks like:

![http://msatcommander.googlecode.com/svn/wiki/running.png](http://msatcommander.googlecode.com/svn/wiki/running.png)

## Feedback ##
If you have constructive feedback (likes, dislikes, enhancements), please send an email to the [list-serve](mailto:msatcommander-discuss@googlegroups.com).  All suggestions are welcomed and will be considered.

## Purpose ##
msatcommander is a python program written to locate microsatellite (SSR, VNTR, &c) repeats within fasta-formatted sequence or consensus files.  msatcommander will search for all di-, tri-, tetra-, penta-, and hexa-nucleotide repeats (with options to search for fewer repeat types and combinations of repeat types).

msatcommander will also design and tag primers using [primer3](http://primer3.sourceforge.net) as its primer design engine (see [References](References.md) for citations).  Many thanks to the [primer3 team](https://sourceforge.net/project/memberlist.php?group_id=112461), in general, and [Steve Rozen](http://jura.wi.mit.edu/rozen/), in particular.  Additional information regarding primer3 may also be found on the [primer3 wiki](http://jura.wi.mit.edu/primer3/).

## Citation ##

Since primer3 is an integral part of msatcommander, please cite both of the following manuscripts:

  * Faircloth, BC.  2008.  MSATCOMMANDER:  detection of microsatellite repeat arrays and automated, locus-specific primer design.  Molecular Ecology Resources 8:92-94.  doi:[10.1111/j.1471-8286.2007.01884.x](http://dx.doi.org/10.1111/j.1471-8286.2007.01884.x).

  * Rozen S, Skaletsky HJ. 2000.  Primer3 on the WWW for general users and for biologist programmers. In: Bioinformatics Methods and Protocols: Methods in Molecular Biology (eds Krawetz S, Misener S). Humana Press, Totowa, NJ.

I would be more than happy to provide you with a pdf of the primary manuscripts, if needed.

## Supported OSs (msatcommander >= 1.0.0) ##

**NOTE 1:  msatcommander 1.0.0 or greater will not work on OS X < 10.6**
**NOTE 2:  I am working on compiling a Windows binary for XP and potentially Windows 7**

| Apple OS X 10.6+|Binary | [Notes/README](OSXNotes_new.md) |
|:----------------|:------|:--------------------------------|
|Unix-like OSs    | SVN Checkout or tarball | [Notes/README](UnicesNotes_new.md) |


## Supported OSs (msatcommander < 0.8.x) ##

**NOTE:  msatcommander will not work on OS X < 10.4.x**

| Apple OS X 10.4+|Binary | [Notes/README](OSXNotes.md) |
|:----------------|:------|:----------------------------|
| Windows XP (SP2) | Binary | [Notes/README](WinXPNotes.md) |
|Unix-like OSs    | SVN Checkout or tarball | [Notes/README](UnicesNotes.md) |

## Differences from other programs ##
  * searches for all mono-,di-,tri-,tetra-,penta-, and hexanucleotide repeats
  * repeats may be combined across user-specified distances (bp)
  * designs primers for located repeats
  * tags and tests primers with m13R, CAG, or custom tag.  The 'best' primer is reported to the user
  * adds GTTT pigtails to the un-tagged, 'best' primer reported to the user
  * offers a convenient GUI for a majority of users
  * outputs results in csv format, for easy importation to spreadsheet software

## Input ##
msatcommander will read FASTA-formatted files of single or multiple sequences.  These files may end in '.fsa', '.fasta', or '.txt'.

## Output ##
For array searching, the user may select and name a specific output file.  When searching, designing, and/or tagging primers, the user must select or create and select a directory to contain the output.  In this case, the output consists of the following:
  * microsatSearchOutput.csv (contains microsatellite search results)
  * primerCombined.csv  (optional; contains combined microsatellite search results)
  * a primer3 directory
    * formatted text files for each designed primer
    * primerNoTag.csv (contains untagged primer sequences)
    * primerTag.csv (optional; contains tagged primers)

## Reporting Bugs ##
Please report bugs via the [issues](http://code.google.com/p/msatcommander/issues/list) tab.  If you have a question about something that **may** be a bug, please send an email to the [list-serve](mailto:msatcommander-discuss@googlegroups.com).

## About ##
msatcommander is written in [python](http://python.org) and makes use of the [biopython](http://biopython.org) and [wxPython](http://www.wxpython.org/) modules.  msatcommander uses [primer3](http://primer3.sourceforge.net) as its primer design engine.  Primer3 source is C and Perl.  Primer3 was written by Steve Rozen and Helen Skaletsky.  primer3\_core binaries (provided within the msatcommander binaries) are built specifically for each architecture (OSX or WindowsXP).  The primer3 OSX binary is [universal](http://www.apple.com/universal/).
