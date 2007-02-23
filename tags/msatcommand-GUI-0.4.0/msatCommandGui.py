#!/usr/bin/env python

#-----------------------------------------------------------------------------------------------|
# MicrosatFinder - command line version for Python:  an update to N. Dean Pentcheff's           |
# Ephemeris 1.0 for Perl                                                                        |
# available from http://www.uga.edu/srel/DNA_Lab/ephemeris%201.0.bin.                           |
#                                                                                               |
# Copyright (C) 2005-2006 Brant C. Faircloth.  Modifications/recoding conducted solely by       |
# Brant C. Faircloth in March, 2005 porting program to Python (www.python.org) and recoding     |
# some parts.                                                                                   |                                                                                    
#                                                                                               |                                                                             
# This program is free software; you can redistribute it and/or modify it under the terms of the|
# GNU General Public License as published by the Free Software Foundation; either version 2 of  | 
# the License, or (at your option) any later version.                                           |
#                                                                                               |
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;     |
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.     |
# See the GNU General Public License for more details.                                          |
#                                                                                               |
# You should have received a copy of the GNU General Public License along with this program; if |
# not, write to the Free Software Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA     |
# 02111-1307, USA.                                                                              |
#-----------------------------------------------------------------------------------------------|

import string, re, wx
 
idAbout = wx.NewId()
idOpen  = wx.NewId()
idExit  = wx.NewId()
idListBox = wx.NewId()

try:
    from Bio import Fasta
except:
    print "This program requires BioPython (http://biopython.org/) to be installed."
       


class mods: 
    
    """Class representing DNA as a string sequence.""" 

    def complement(self, s):
            
            """return complementary dna sequence"""
            
            tab = string.maketrans('AGCTagct','TCGAtcga')
            output = string.translate(s, tab)
            return output
    
class search:
    
    def __init__(self):
         
        """Create DNA instance initialized to string s."""
        
        self.repeatUnits = {"mononucleotide":1, "dinucleotide":2, "trinucleotide":3, "tetranucleotide":4, "pentanucleotide":5, "hexanucleotide":6}
        self.minSize={"mononucleotide":'{9,}',"dinucleotide":'{6,}',"trinucleotide":'{4,}',"tetranucleotide":'{3,}', "pentanucleotide":'{3,}', "hexanucleotide":'{3,}'} #defines minimum size for repeat unit
        #defines repeat units (lowest alphabetical, unique, non-complementary) for which we are searching
        self.mononucleotide=['(A)','(C)'] 
        
        self.dinucleotide=['(AC)','(AG)',
                            '(AT)','(CG)'] 
        
        self.trinucleotide=['(AAC)','(AAG)','(AAT)',
                            '(ACC)','(ACG)','(ACT)',
                            '(AGC)','(AGG)','(ATC)',
                            '(CCG)']
                            
        self.tetranucleotide=['(AAAC)','(AAAG)','(AAAT)','(AACC)',
                            '(AACG)','(AACT)','(AAGC)','(AAGG)',
                            '(AAGT)','(ACAG)','(ACAT)','(ACCC)',
                            '(ACCG)','(ACCT)','(ACGC)','(ACGT)',
                            '(ACTC)','(ACTG)','(AGAT)','(AATC)',
                            '(AATG)','(AATT)','(ACGG)','(AGCC)',
                            '(AGCG)','(AGGC)','(AGGG)','(ATCC)',
                            '(ATCG)','(ATGC)','(CCCG)','(CCGG)']
        
        self.pentanucleotide=['(AAAAC)', '(AAAAG)', '(AAAAT)', '(AAACC)', '(AAACG)', 
                            '(AAACT)', '(AAAGC)', '(AAAGG)', '(AAAGT)', '(AAATC)', 
                            '(AAATG)', '(AAATT)', '(AACAC)', '(AACAG)', '(AACAT)', 
                            '(AACCC)', '(AACCG)', '(AACCT)', '(AACGC)', '(AACGG)',
                            '(AACGT)', '(AACTC)', '(AACTG)', '(AACTT)', '(AAGAC)',
                            '(AAGAG)', '(AAGAT)', '(AAGCC)', '(AAGCG)', '(AAGCT)',
                            '(AAGGC)', '(AAGGG)', '(AAGGT)', '(AAGTC)', '(AAGTG)', 
                            '(AATAC)', '(AATAG)', '(AATAT)', '(AATCC)', '(AATCG)', 
                            '(AATCT)', '(AATGC)', '(AATGG)', '(AATGT)', '(AATTC)', 
                            '(ACACC)', '(ACACG)', '(ACACT)', '(ACAGC)', '(ACAGG)', 
                            '(ACAGT)', '(ACATC)', '(ACATG)', '(ACCAG)', '(ACCAT)', 
                            '(ACCCC)', '(ACCCG)', '(ACCCT)', '(ACCGC)', '(ACCGG)', 
                            '(ACCGT)', '(ACCTC)', '(ACCTG)', '(ACGAG)', '(ACGAT)', 
                            '(ACGCC)', '(ACGCG)', '(ACGCT)', '(ACGGC)', '(ACGGG)', 
                            '(ACGTC)', '(ACTAG)', '(ACTAT)', '(ACTCC)', '(ACTCG)', 
                            '(ACTCT)', '(ACTGC)', '(ACTGG)', '(AGAGC)', '(AGAGG)', 
                            '(AGATC)', '(AGATG)', '(AGCAT)', '(AGCCC)', '(AGCCG)', 
                            '(AGCCT)', '(AGCGC)', '(AGCGG)', '(AGCTC)', '(AGGAT)', 
                            '(AGGCC)', '(AGGCG)', '(AGGGC)', '(AGGGG)', '(ATATC)', 
                            '(ATCCC)', '(ATCCG)', '(ATCGC)', '(ATGCC)', '(CCCCG)', 
                            '(CCCGG)', '(CCGCG)']
                            
        self.hexanucleotide=['(AAAAAC)', '(AAAAAG)', '(AAAAAT)', '(AAAACC)', '(AAAACG)', '(AAAACT)', 
                            '(AAAAGC)', '(AAAAGG)', '(AAAAGT)', '(AAAATC)', '(AAAATG)', '(AAAATT)',
                            '(AAACAC)', '(AAACAG)', '(AAACAT)', '(AAACCC)', '(AAACCG)', '(AAACCT)',
                            '(AAACGC)', '(AAACGG)', '(AAACGT)', '(AAACTC)', '(AAACTG)', '(AAACTT)', 
                            '(AAAGAC)', '(AAAGAG)', '(AAAGAT)', '(AAAGCC)', '(AAAGCG)', '(AAAGCT)', 
                            '(AAAGGC)', '(AAAGGG)', '(AAAGGT)', '(AAAGTC)', '(AAAGTG)', '(AAAGTT)', 
                            '(AAATAC)', '(AAATAG)', '(AAATAT)', '(AAATCC)', '(AAATCG)', '(AAATCT)', 
                            '(AAATGC)', '(AAATGG)', '(AAATGT)', '(AAATTC)', '(AAATTG)', '(AAATTT)', 
                            '(AACAAG)', '(AACAAT)', '(AACACC)', '(AACACG)', '(AACACT)', '(AACAGC)', 
                            '(AACAGG)', '(AACAGT)', '(AACATC)', '(AACATG)', '(AACATT)', '(AACCAC)', 
                            '(AACCAG)', '(AACCAT)', '(AACCCC)', '(AACCCG)', '(AACCCT)', '(AACCGC)', 
                            '(AACCGG)', '(AACCGT)', '(AACCTC)', '(AACCTG)', '(AACCTT)', '(AACGAC)', 
                            '(AACGAG)', '(AACGAT)', '(AACGCC)', '(AACGCG)', '(AACGCT)', '(AACGGC)', 
                            '(AACGGG)', '(AACGGT)', '(AACGTC)', '(AACGTG)', '(AACGTT)', '(AACTAC)', 
                            '(AACTAG)', '(AACTAT)', '(AACTCC)', '(AACTCG)', '(AACTCT)', '(AACTGC)', 
                            '(AACTGG)', '(AACTGT)', '(AACTTC)', '(AACTTG)', '(AAGAAT)', '(AAGACC)', 
                            '(AAGACG)', '(AAGACT)', '(AAGAGC)', '(AAGAGG)', '(AAGAGT)', '(AAGATC)', 
                            '(AAGATG)', '(AAGATT)', '(AAGCAC)', '(AAGCAG)', '(AAGCAT)', '(AAGCCC)', 
                            '(AAGCCG)', '(AAGCCT)', '(AAGCGC)', '(AAGCGG)', '(AAGCGT)', '(AAGCTC)', 
                            '(AAGCTG)', '(AAGCTT)', '(AAGGAC)', '(AAGGAG)', '(AAGGAT)', '(AAGGCC)', 
                            '(AAGGCG)', '(AAGGCT)', '(AAGGGC)', '(AAGGGG)', '(AAGGGT)', '(AAGGTC)', 
                            '(AAGGTG)', '(AAGTAC)', '(AAGTAG)', '(AAGTAT)', '(AAGTCC)', '(AAGTCG)', 
                            '(AAGTCT)', '(AAGTGC)', '(AAGTGG)', '(AAGTGT)', '(AATACC)', '(AATACG)', 
                            '(AATACT)', '(AATAGC)', '(AATAGG)', '(AATAGT)', '(AATATC)', '(AATATG)', 
                            '(AATATT)', '(AATCAC)', '(AATCAG)', '(AATCAT)', '(AATCCC)', '(AATCCG)', 
                            '(AATCCT)', '(AATCGC)', '(AATCGG)', '(AATCGT)', '(AATCTC)', '(AATCTG)', 
                            '(AATGAC)', '(AATGAG)', '(AATGAT)', '(AATGCC)', '(AATGCG)', '(AATGCT)', 
                            '(AATGGC)', '(AATGGG)', '(AATGGT)', '(AATGTC)', '(AATGTG)', '(AATTAC)', 
                            '(AATTAG)', '(AATTAT)', '(AATTCC)', '(AATTCG)', '(AATTGC)', '(ACACAG)', 
                            '(ACACAT)', '(ACACCC)', '(ACACCG)', '(ACACCT)', '(ACACGC)', '(ACACGG)', 
                            '(ACACGT)', '(ACACTC)', '(ACACTG)', '(ACAGAG)', '(ACAGAT)', '(ACAGCC)', 
                            '(ACAGCG)', '(ACAGCT)', '(ACAGGC)', '(ACAGGG)', '(ACAGGT)', '(ACAGTC)', 
                            '(ACAGTG)', '(ACATAG)', '(ACATAT)', '(ACATCC)', '(ACATCG)', '(ACATCT)', 
                            '(ACATGC)', '(ACATGG)', '(ACATGT)', '(ACCACG)', '(ACCACT)', '(ACCAGC)', 
                            '(ACCAGG)', '(ACCAGT)', '(ACCATC)', '(ACCATG)', '(ACCCAG)', '(ACCCAT)', 
                            '(ACCCCC)', '(ACCCCG)', '(ACCCCT)', '(ACCCGC)', '(ACCCGG)', '(ACCCGT)', 
                            '(ACCCTC)', '(ACCCTG)', '(ACCGAG)', '(ACCGAT)', '(ACCGCC)', '(ACCGCG)', 
                            '(ACCGCT)', '(ACCGGC)', '(ACCGGG)', '(ACCGGT)', '(ACCGTC)', '(ACCGTG)', 
                            '(ACCTAG)', '(ACCTAT)', '(ACCTCC)', '(ACCTCG)', '(ACCTCT)', '(ACCTGC)', 
                            '(ACCTGG)', '(ACGACT)', '(ACGAGC)', '(ACGAGG)', '(ACGAGT)', '(ACGATC)', 
                            '(ACGATG)', '(ACGCAG)', '(ACGCAT)', '(ACGCCC)', '(ACGCCG)', '(ACGCCT)', 
                            '(ACGCGC)', '(ACGCGG)', '(ACGCGT)', '(ACGCTC)', '(ACGCTG)', '(ACGGAG)', 
                            '(ACGGAT)', '(ACGGCC)', '(ACGGCG)', '(ACGGCT)', '(ACGGGC)', '(ACGGGG)', 
                            '(ACGTAG)', '(ACGTAT)', '(ACGTCC)', '(ACGTCG)', '(ACGTGC)', '(ACTAGC)', 
                            '(ACTAGG)', '(ACTAGT)', '(ACTATC)', '(ACTATG)', '(ACTCAG)', '(ACTCAT)', 
                            '(ACTCCC)', '(ACTCCG)', '(ACTCCT)', '(ACTCGC)', '(ACTCGG)', '(ACTCTC)', 
                            '(ACTCTG)', '(ACTGAG)', '(ACTGAT)', '(ACTGCC)', '(ACTGCG)', '(ACTGCT)', 
                            '(ACTGGC)', '(ACTGGG)', '(AGAGAT)', '(AGAGCC)', '(AGAGCG)', '(AGAGCT)', 
                            '(AGAGGC)', '(AGAGGG)', '(AGATAT)', '(AGATCC)', '(AGATCG)', '(AGATCT)', 
                            '(AGATGC)', '(AGATGG)', '(AGCAGG)', '(AGCATC)', '(AGCATG)', '(AGCCAT)', 
                            '(AGCCCC)', '(AGCCCG)', '(AGCCCT)', '(AGCCGC)', '(AGCCGG)', '(AGCCTC)', 
                            '(AGCCTG)', '(AGCGAT)', '(AGCGCC)', '(AGCGCG)', '(AGCGCT)', '(AGCGGC)', 
                            '(AGCGGG)', '(AGCTAT)', '(AGCTCC)', '(AGCTCG)', '(AGCTGC)', '(AGGATC)', 
                            '(AGGATG)', '(AGGCAT)', '(AGGCCC)', '(AGGCCG)', '(AGGCCT)', '(AGGCGC)', 
                            '(AGGCGG)', '(AGGGAT)', '(AGGGCC)', '(AGGGCG)', '(AGGGGC)', '(AGGGGG)', 
                            '(ATATCC)', '(ATATCG)', '(ATATGC)', '(ATCATG)', '(ATCCCC)', '(ATCCCG)', 
                            '(ATCCGC)', '(ATCCGG)', '(ATCGCC)', '(ATCGCG)', '(ATCGGC)', '(ATGCCC)', 
                            '(ATGCGC)', '(ATGGCC)', '(CCCCCG)', '(CCCCGG)', '(CCCGCG)', '(CCCGGG)', 
                            '(CCGCGG)', '(CCGGCG)']        

    def genericMethod(self, i, repeat):
        
        """generic method for finding various microsatellite repeats"""
        
        #print (("Finding repeats of size %s....\n") % (repeat))
        wildcard='[N]*' + i + '+'                                               # build wildcard string for N bases
        searchString = i + self.minSize[repeat] + wildcard                      # concatenates mononuc[i] and minimum size for repeat type
        compiledRegEx = re.compile(searchString, re.IGNORECASE)                 # compiles regex for concatenated values
        iterator = compiledRegEx.finditer(self.seq)                             # sets up iterative repeat finder
        compIterator = compiledRegEx.finditer(mods().complement(self.seq))
        for match in iterator:
            bases = match.span()                                                # give start/end bases of repeat
            length = (bases[1] - bases[0]) / self.repeatUnits[repeat]           # determine number of repeats for given msat type
            self.msatResults[bases[0]+1] = ('%s repeat %s^%s found between bases %s and %s.') % (repeat, i, length, bases[0]+1, bases[1]+1)
        for match in compIterator:                                              # do the same on the reverse complement of the sequence
            bases = match.span()
            length = (bases[1] - bases[0]) / self.repeatUnits[repeat]
            seq = match.group()
            self.msatResults[bases[0]+1] = ('Reverse complement of %s repeat %s, %s^%s found between bases %s and %s.') % (repeat, i, mods().complement(i), length, bases[0]+1, bases[1]+1)

    def ephemeris(self, s, type):
        
        """Searches for microsatellite sequences (mononucleotide, dinucleotide, trinucleotide, tetranucleotide) in DNA string"""        
        
        self.seq = s
        self.msatResults={}                                 # we will store output for each repeat in dictionary keyed on start base #
        
        for searchClass in type:
            if str(searchClass) == 'Mononucleotide':
                for i in self.mononucleotide:
                    self.genericMethod(i,"mononucleotide")        
            elif str(searchClass) == 'Dinucleotide':
                for i in self.dinucleotide:
                    self.genericMethod(i,"dinucleotide")              
            elif str(searchClass) == 'Trinucleotide':
                for i in self.trinucleotide:
                    self.genericMethod(i,"trinucleotide") 
            elif str(searchClass) == 'Tetranucleotide':             
                for i in self.tetranucleotide:
                    self.genericMethod(i, "tetranucleotide")
            elif str(searchClass) == 'Pentanucleotide':               
                for i in self.pentanucleotide:
                    self.genericMethod(i, "pentanucleotide")
            elif str(searchClass) == 'Hexanucleotide':
                for i in self.hexanucleotide:
                    self.genericMethod(i, "hexanucleotide")
            elif str(searchClass) == 'All (slow!)':
                for i in self.mononucleotide:
                    self.genericMethod(i,"mononucleotide")        
                for i in self.dinucleotide:
                    self.genericMethod(i,"dinucleotide")              
                for i in self.trinucleotide:
                    self.genericMethod(i,"trinucleotide")              
                for i in self.tetranucleotide:
                    self.genericMethod(i, "tetranucleotide")               
                for i in self.pentanucleotide:
                    self.genericMethod(i, "pentanucleotide")
                for i in self.hexanucleotide:
                    self.genericMethod(i, "hexanucleotide")     

        return self.msatResults
    
def readInfo(inFile, repeatChoice, outFile):    
    file=open(outFile,'w')                                   # opens file for output - append only to keep from overwriting
    file.write('Microsatellite repeats found in the following sequences: \n\n')
    parser = Fasta.RecordParser()
    infile = open(inFile)
    iterator = Fasta.Iterator(infile, parser)
    i = 0
    while 1:
        record = iterator.next()
        if not record:
            break
            infile.close()
            file.close()
        dataOut=search().ephemeris(record.sequence, repeatChoice) 
        dictKeys=dataOut.keys()
        dictKeys.sort()                                     # sorts keys so bp locations will be in order
        if dictKeys:
            #file.write(('%s>>%s %s') % ('\n', record.title, '\n'))
            for k in dictKeys:                                  # writes dict values for sorted keys to output file
                dataList = dataOut[k].split()
                file.write(('%s\t%s\t%s\t%s\n') % (record.title, ' '.join(dataList[:-7]), dataList[-7], ' '.join(dataList[-6:])))
            file.write(('---------------------------------------%s') % ('\n'))
        #i += interval
        #prog(i)

#-----------------------------------
# this used to be the main loop code
#-----------------------------------
#if __name__ == '__main__':
#    userInput,userOutput,userRepeatChoice = getUserFiles()
#    readInfo(userInput, userOutput, userRepeatChoice)
#    print '\n'

#---------------------------------
# Main class for wxPython interface
#---------------------------------
class msatCommand(wx.App):
    def OnInit(self):
        frame = msatCommandFrame(None)
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

class DemoPanel(wx.Panel):
    """This Panel hold two simple buttons, but doesn't really do anything."""
    def __init__(self, Parent, *args, **kwargs):
        """Create the DemoPanel."""
        wx.Panel.__init__(self, Parent, *args, **kwargs)

        self.Parent = Parent  # Sometimes one can use inline Comments

        wx.StaticText(Parent, -1, pos=(5,5), label='Choose Repeat Class(es):')
        
        fileSelect = wx.Button(Parent, label="Select file to scan...", size=(200, 20), pos=(220,40))
        fileSelect.Bind(wx.EVT_BUTTON, self.OnOpen )
        
        fileSave =  wx.Button(Parent, label="Select file for output...", size=(200, 20), pos=(220,90))
        fileSave.Bind(wx.EVT_BUTTON, self.SaveFile )
        
        runProgram =  wx.Button(Parent, label="Search file", size=(200, 20), pos=(220,140))
        runProgram.Bind(wx.EVT_BUTTON, self.RunSearch )

        # Create a checklistbox on an existing panel widget
        self.checklist = wx.CheckListBox(Parent, pos=(5, 25), size=(200,150))
        list = ['Mononucleotide','Dinucleotide','Trinucleotide','Tetranucleotide','Pentanucleotide', 'Hexanucleotide', 'All (slow)']
        self.checklist.InsertItems(items=list, pos=0)
        # Bind checklist to event
        self.checklist.Bind(wx.EVT_CHECKLISTBOX, self.OnSelection)    

    #def panelText():
    #    text = "Choose repeat class(es)"
    #    return text
    
    def OnSelection(self,event):
        #id = event.GetSelection()
        #name = self.checklist.GetString(id)
        #print name
        checked = []
        for i in range(self.checklist.GetCount()):
            if self.checklist.IsChecked(i):
                checked.append(self.checklist.GetString(i))       
        self.selection = checked
    
    def OnOpen(self,event):
        dlg = wx.FileDialog(self, 'Choose a File for Searching')
        dlg.SetStyle(wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.infile = dlg.GetPath()                                                       
            #self.userChoice()
            dlg.Destroy()  
        else:
            messageText = 'You must specify an input file!'
            windowTitle = 'Error'
            error = wx.MessageDialog(self, messageText, windowTitle, wx.OK | wx.ICON_INFORMATION)
            error.ShowModal()
            error.Destroy()        
            dlg.Destroy()
            #self.OnOpen(event=None)  
    
    def SaveFile(self, event):
        messageText = 'Choose a Location to Save the Output File'
        dlg = wx.FileDialog(self, messageText)
        dlg.SetStyle(wx.SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            self.outfile = dlg.GetPath()
            #self.runConversion()
            #replace the above with something
            #self.runSearch()
            dlg.Destroy()
        else:
            messageText = 'You must specify an output file!'
            windowTitle = 'Error'
            error = wx.MessageDialog(self, messageText, windowTitle, wx.OK | wx.ICON_INFORMATION)
            error.ShowModal()
            error.Destroy()            
            dlg.Destroy()  
            #self.SaveFile(event=None)
        
    def RunSearch(self, event):
        print "infile:", self.infile
        print "outfile:", self.outfile
        print "selection:", self.selection
        readInfo(self.infile,self.selection,self.outfile)
        
class msatCommandFrame(wx.Frame):
    """Main wxPython frame for msatCommand"""
    title = "msatCommand"
    def __init__(self, parent):
        wx.Frame.__init__(self,parent,-1,self.title,size=(450,225), style=wx.DEFAULT_FRAME_STYLE)
        #wx.Frame.__init__(self, parent, ID, title, wx.DefaultPosition, wx.Size(350, 250)) #old init subclass
        color=(255,255,255)
        self.SetBackgroundColour(color)
#        wx.StaticText(self, -1, self.frameText())
        self.CreateStatusBar()
        self.SetStatusText("")
        
        #create the file menu
#        menu1 = wx.Menu()
#        menu1.Append(idOpen, "&Convert...\tCtrl-C","Open a file for searching")
        
        #and the help menu
        menu2 = wx.Menu()
        menu2.Append(idAbout, "&About\tCtrl-H", "Display Help")
        
        #add menu items to menubar
        menuBar = wx.MenuBar()
#        menuBar.Append(menu1, "&File");
        menuBar.Append(menu2, "&Help") 
        self.SetMenuBar(menuBar)
        
        #create a panel
        self.Panel = DemoPanel(self)
        
        #setup events
        self.Bind(wx.EVT_MENU, self.OnAbout, id=idAbout)
#        self.Bind(wx.EVT_MENU, self.OnOpen, id=idOpen)
        self.Bind(wx.EVT_MENU, self.OnExit, id=idExit)
         
#    def frameText(self):
#        version = 'Choose repeat class(es):'
#        return text
        
    
    def OnAbout(self, event):
        messageText = 'This program searches Fasta files for microsatellite repeats'
        windowTitle = 'msatCommand'
        dlg = wx.MessageDialog(self, messageText, windowTitle, wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

#    def runSearch(self):
#        print "infile:", self.infile
#        print "outfile:", self.outfile
#        print "selection:", self.selection
#        readInfo(self.infile,self.selection,self.outfile)
        
#    def saveFile(self):
#        messageText = 'Choose a Location to Save the Output File'
#        dlg = wx.FileDialog(self, messageText)
#        dlg.SetStyle(wx.SAVE)
#        if dlg.ShowModal() == wx.ID_OK:
#            self.outfile = dlg.GetPath()
#            #self.runConversion()
#           #replace the above with something
#            #self.runSearch()
#            dlg.Destroy()
#        else:
#            messageText = 'You must specify an output file!'
#            windowTitle = 'Error'
#           error = wx.MessageDialog(self, messageText, windowTitle, wx.OK | wx.ICON_INFORMATION)
#            error.ShowModal()
#            error.Destroy()            
#            dlg.Destroy()  
#            self.saveFile()

#    def userChoice(self):
#        choices = [ 'tetranucleotide', 'pentanucleotide', 'di','tri','tetra','mono']
#        n = len(choices)
#        messageText = 'Repeat Classes to Search:'
#        windowTitle = 'Search Class'
#        style = (wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.OK | wx.CENTRE)                       
#        # Create the dialog
        #dlg = wx.SingleChoiceDialog (None, messageText, windowTitle, choices, style)
#        dlg = wx.MultiChoiceDialog ( None, 'Pick repeat class(es) to search....', 'Dialog Title', choices )
        # Show the dialog
        #dlg.ShowModal()
#        selections = []
#        if dlg.ShowModal() == wx.ID_OK:
#            #self.selection = dlg.GetStringSelection() #get user response
#            for item in dlg.GetSelections():
#                selections.append(choices[item])
#            self.selection = selections
#            #print "selections", self.selection
#            self.saveFile()
#        # Destroy the dialog
#        dlg.Destroy()

    def OnOpen(self,event):
        dlg = wx.FileDialog(self, 'Choose a File for Searching')
        dlg.SetStyle(wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.infile = dlg.GetPath()                                                       
            self.userChoice()
            dlg.Destroy()  
        else:
            messageText = 'You must specify an input file!'
            windowTitle = 'Error'
            error = wx.MessageDialog(self, messageText, windowTitle, wx.OK | wx.ICON_INFORMATION)
            error.ShowModal()
            error.Destroy()        
            dlg.Destroy()
        
       
    def OnExit(self, event):
        self.Close()
        #self.Close(true)
 
if __name__ == '__main__':
    app = msatCommand(redirect=True)
    app.MainLoop()