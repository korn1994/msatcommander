# Summary #
  1. msatcommander searches for user-specified classes (di-, tri-, tetranucleotide, etc.) of microsatellite arrays
  1. msatcommander designs primers using python code, primer3, and [the default primer values](PrimerDefaults.md)
  1. these primers are written to an output file for each contig/sequence/array
  1. msatcommander tags 'good' primers from the previous set using python code and evaluates them using Primer3
  1. msatcommander places the 'best' tag+primer combination (in addition to the untagged forward or reverse primer) in an output file

# Microsatellite Array Searching #

This program uses regular expression pattern matching within each DNA sequence to locate microsatellite arrays within user-selected repeat classes.  Length of located repeat arrays within each class is a user-definable option. Repeat sequences are located using their lowest alphabetical, non-complementary designation, and repeat sequences fitting these designations are written to the summary output file.  To locate all microsatellite repeats fitting these designations, DNA sequences are first scanned in the 5’ – 3’ orientation.  The program then takes a second pass through the complement of the sequence in the 3’ – 5’ orientation.  Unknown bases (N) are allowed within microsatellite arrays of any class.  Users are given a choice of searching for any combination of repeat classes (mononucleotide to hexanucleotide) or all repeat classes at once.  Searches progress from simple to complex classes on a sequence-by-sequence basis.  Users also have the option to combine multiple repeat arrays located within a single sequence provided they occur within a user-defined distance from one another.

# Primer Design #
Given that repeats were located within the source FASTA file, msatcommander will:
  1. (optional) combine multiple arrays within a sequence/contig if within the user-specified distance (default: 50bp)
  1. move through each contig/sequence containing a repeat or combined repeat
  1. generate a temporary input file for Primer3 using the sequence, the located repeat, and [the default primer values](PrimerDefaults.md)
  1. send this Boulder-IO file to Primer3
  1. generate a Primer3 formatted text file for the best 4 primers (if there are 4)
  1. place the absolute best primer (lowest penalty score) in primersNoTag.csv
  1. move to the next contig/sequence

# Primer Tagging #
If the primer tagging option is chosen, msatcommander will:
  1. move through each primer pair in primersNoTag.csv
  1. apply a CAG &/ M13 &/ custom 5'-tail to the forward primer
  1. remove any common bases between the 3' end of the 5'-tail and the 5'-end of the forward primer
  1. 'build' a contig that consists of the tailed, forward primer + Enterobacteria phage lambda sequence (gi:9626243) + the rev. complement of the reverse primer
  1. apply a CAG &/ M13 &/ custom 5'-tail to the reverse primer
  1. remove any common bases between the 3' end of the 5'-tail and the 5'-end of the reverse primer
  1. 'build' a contig that consists of the forward primer + Enterobacteria phage lambda sequence (gi:9626243) + the rev. complement of the tailed, reverse primer
  1. send all of these combinations to Primer3 as Boulder-IO files
  1. keep the data that are returned from Primer3
  1. discard primer sequences that do not return values (i,e. they are "bad")
  1. keep tailed primers returning statistics (primarily self-, end-, and pair-complementarity)
  1. scan these tailed primers, and write the best one (lowest penalty score) to the primerTag.csv file
  1. move to the next primer pair
