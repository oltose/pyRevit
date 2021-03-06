'''
Copyright (c) 2014-2016 Ehsan Iran-Nejad
Python scripts for Autodesk Revit

This file is part of pyRevit repository at https://github.com/eirannejad/pyRevit

pyRevit is a free set of scripts for Autodesk Revit: you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3, as published by
the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

See this link for a copy of the GNU General Public License protecting this package.
https://github.com/eirannejad/pyRevit/blob/master/LICENSE
'''

__window__.Close()

import os, subprocess
import os.path as op

# Checks to see if notepad++ program is installed and available.
def NPPExists():
	pfFolder = os.getenv('ProgramFiles(x86)')
	return op.isfile( op.join( pfFolder, 'Notepad++\\Notepad++.EXE' ))

# def getCurrentJournalFile():
	# appdataFolder = os.getenv('localappdata')
	# journalsFolder = op.join( appdataFolder, 'Autodesk\\Revit\\Autodesk Revit {0}\\Journals'.format( __revit__.Application.VersionNumber ))
	# os.chdir(journalsFolder)
	# journalFiles = [x for x in os.listdir( journalsFolder ) if op.splitext(x)[1].lower() == '.txt']
	# currentJournal = max( journalFiles, key=op.getctime )
	# return currentJournal

def getCurrentJournalFile():
	return __revit__.Application.RecordingJournalFilename

currentJournal = getCurrentJournalFile()

if NPPExists():
	os.system('start notepad++ -lvb -n9999999999 "{0}"'.format( currentJournal ))
else:
	os.system('start notepad "{0}"'.format( currentJournal ))