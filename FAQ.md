## Why? ##
> Because designing and tagging primers is a **very** time-consuming process, if done by hand.  Primer design can be automated, but there was previously not an easy way to tag primers.  msatcommander attempts to do both, easily.

## Does msatcommander work in OS X 10.3? ##
> As of version 0.8.0, msatcommander requires OSX 10.4.x

## What are these 'tags' and where do they come from? ##
> The primary reference re: tagging primers is Boutin-Ganache et al. 2001 (see [References](References.md)).  Since that article, there have been several others using tags to fluorescently label primers (e.g. Schable et al. 2002).  Travis Glenn provides addtional information re: tagging primers [here](http://www.uga.edu/srel/DNA_Lab/Universal_Fluorescent_PrimerTags4.pdf).  Additionally, you may design and attach your own tagged sequences.

## What are the tag sequences? ##
> These may be found in the source code (mscprimertag.py), as well.  Remember that common bases (between the 3' end of the tag and 5' end of the primer sequence) will be removed:

> `CAG    = 'CAGTCGGGCGTCATCA'`

> `M13R  = 'GGAAACAGCTATGACCAT'`

## Which tag is 'better'? ##
> In my experience, the CAG tag has more desirable properties than the M13R tag.  Generally, M13R causes problems with self-, end-, and pair-complementarity or it introduces hairpins to the primer that is tagged.

> You will notice that, in large part, if you choose to tag primers with either CAG or M13R, the software 'chooses' CAG-tagged primers more often.  This is for the reasons given above (largely based on measures of complementarity).

## Can I use tagged primers for large studies? ##
> Yes, you can.  We are currently using tagged primers to genotype roughly 2000 individuals @ 16 loci.  The nice thing about tags is that they allow a modular approach to fluorescent genotyping.  If you want/need to change dye 'colors' (due to overlap problems, for instance), it's easy enough - just purchase the tag you need with a new dye attached.

> Similarly, you can quickly, easily, and inexpensively change entire dye sets, just by purchasing the tags you need in the 'colors' you want.  For example, you can choose to move from DS-30 to DS-33 (see [here](http://www.uri.edu/research/gsc/docs/ABI%20Dye%20Set%20card.pdf) if you are using an Applied Biosytems machine).

> With every benefit, there is some cost.  In this case, PCR setup _can_ be a little more complicated.  That said, if you premix your tagged primer, your untagged primer, and the labelled tag, things are easy enough.  Then you just need to add an appropriate amount of this mix to your PCR reaction.

> You should also remember that results acquired from tagged primers are not equivalent to those acquired from directly-labelled primers.  Theoretically, the tagged fragments will be equivalent in length to the untagged (directly labelled) fragments + the length of the tag.  In practice, things are not always so easy.  So, it is generally easier to make the choice prior to beginning a study and stick with that method.

## How does msatcommander deal with hairpins? ##
> This is sort of a loaded question.  msatcommander uses primer3 for primer design.  primer3 takes a non-thermodynamic approach to evaluating self-, pair-, and end-complementarity.  As such, hairpins are evaluated without respect to thermodynamic properties.

> There are packages (free and commercial) that will evaluate hairpins in a sequence ([UNAFold](http://www.bioinfo.rpi.edu/applications/hybrid/quikfold.php)).  However, secondary structure prediction is not an easy task, and one that is affected by many parameters (Salt conc., Mg conc., Temperature, Oligo conc.).  For more information see:  Santalucia and Hicks, 2004.  Annu. Rev. Biophys. Biomol. Struct. 33:415–40 doi: [10.1146/annurev.biophys.32.110601.141800](http://dx.doi.org/10.1146/annurev.biophys.32.110601.141800).  You should also be aware that these programs are meant to provide **predictive results**.

> Therefore, **primers and tagged primers may be designed that have hairpins with high stability as indicated by certain software packages** (i,e. they have high Tms).  It is also likely that results will differ between packages used for these evaluations.  For example, a tagged primer sequence recently tested gave the following results on 3 different packages:

  * OligoAnalyzer (IDTDNA):
    * IDT Structure 1:  delta\_G= - 3.4; Tm = 52.7 C
  * Mfold DINAMelt Server:
    * Mfold Structure 1:  delta\_G = -3.59; Tm = 54.4 C
    * Mfold Structure 2:  delta\_G = -2.72; Tm = 42.3 C
  * Oligo 6.8 (Primer Duplexes Window):
    * Oligo Structure 1:  delta\_G = -3.10; Tm = 64.0 C

> So, how do you deal with this problem?
    1. You could ignore it, order the primers or tagged-primers and test them as you would any others.  This is what we have done with respect to the results presented below.
    1. You could test primers/tagged primers for hairpins and re-design problematic primers

## Why do my primers for certain loci (in some cases) contain repeats from other loci? ##
> In a sense, this is a limitation of primer3.  We can define the max-poly-x flag to keep primers from having a run of identical bases, but primer3 does not have a flag to avoid including various classes of repeat arrays.

> That being said, you can sometimes get around this problem by choosing to **combine repeat arrays**.  In other cases, you will just need to visually scan your primers to ensure they do not contain repeats (this is generally easy, as repeat arrays tend to be easy to see in short lengths of sequence).

> A future addition to msatcommander will scan designed and tagged primers to fix this issue.

## Why is the Windows version so ugly? ##
> Windows is ugly, ergo msatcommander on windows follows that pattern.  Seriously, wxPython applications for windows look slightly different from their OS X counterparts.  There are numerous reasons for this.  Basically, I don't have time to keep 2 GUI codebases up to date so that things are pretty on each OS.

## What is searching performance like? ##

> _Pretty good_.  Here are some examples:

  * Scanning a single ~80,000 bp sequence from _Didelphis virgniana_ for all repeats took roughly 28 seconds on a pentium 4 @ 3 ghz.

  * Scanning chromosome 2L from _Drosophila melanogaster_ (23Mb; GI: NT\_033779.4) for dinucleotide arrays resulted in identification of 1645 arrays in approximately 5.2 minutes on a DP 867 mhz G4 powermac.

  * Scanning 10,000 reptile contigs (approximately 16% of the entire genome) for tetra-nucleotide repeats took roughly 2 hours on a pentium D @ 3.4 ghz.  Six-thousand, one hundred twenty-four sequences contained repeats; 25,434 repeat arrays were identified (Thanks go to Nick Crawford, Savannah River Ecology Lab, for the information.)

  * Scanning 96 contigs for all microsatellite repeats (mean contig length ~ 400bp) took roughly 33 seconds on a DP 867 mhz G4 powermac.

  * Scanning the same 96 contigs for all microsatellite repeats from above on a Core Duo 2 Intel iMac @ 2.16 ghz took roughly 16 seconds.

  * GUI and command-line speeds are roughly the same (+/- 0.2 seconds)

## What is the success rate of designed primers? ##
> Primers designed using the design **and** tagging features of msatcommander have yielded approximately 85% amplification success.  This **does not** mean 85% of your primer will be polymorphic.  It does mean that roughly 85% should amplify some (perhaps monomorphic) product.

> This success rate is largely due to the fact that the primer3 program (the primer design engine) is pretty darn good at what it does.

> _Note_:  **this is dependent on your sequence quality, read-lengths, and organism of interest.  For example, organisms with lots of transposable elements (gymnosperms) are finicky, to say the least.**

> It is **probably a good idea** to design a batch of 10ish primer pairs for your organism of interest using msatcommander.  These can be tested to evaluate your success prior to ordering larger batches (>50 primer pairs).

> If you would like to provide me with information on your success rate (and organism), I would love to have it in hand and possibly to post to this wiki, with your permission.  You may contact me via the [list-serve](mailto:msatcommander-discuss@googlegroups.com) or by adding 'faircloth' to '@gmail.com'.

## Why do you use a vector sequence for the primer tagging? ##
> Good question.  The vector sequence is used to keep things short and fast.  Generally speaking, we only want to know about self-,pair-, and end-complementarity of the tagged primers.  We don't care so much about the sequence in between these.  This also keeps things a bit open in the source code.  If you wanted to use just the tagging module, you could do so by just sending it a list of designed primers (in the correct format) for tagging - you don't need to have the FASTA file of sequence data.

> This becomes handy if you want to tag a bunch of primers that were designed using another program (again, you could do this with the source - you cannot currently do this using msatcommander).

## Will msatCommander work with Chromas files? ##
> In > 0.4.4, Chromas files should work.

## Is msatCommander a universal binary? ##
> Yes.

## Why the Beachball? ##
> You will notice that (at least in the osx version of msatCommander) you get the beachball while the program is running.  This is **normal**.

> At some point (not a priority) I will use python threads to get rid of the beachball.  I will also implement a progress bar.  For now (0.4.5 and above), a popup window indicates completion.

## Why do you use subprocess.Popen versus os.popen? ##
> Because windows does not play nicely with os.popen and the primer3\_core binary.  That being said, there remains an 'issue' with subprocess.Popen and py2exe, and you must call it as follows (if building the windows GUI using py2exe):
```
p=subprocess.Popen(pathToPrimer3,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True).stdout
```
> If you do not set stdin, stdout, and stderr to PIPE, you will get the following error:
```
TypeError: an integer is required
```