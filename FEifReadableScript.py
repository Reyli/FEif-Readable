#! /usr/bin/python
import sys
import re

inputfile = input("Enter input file name: ")
while inputfile == "":
	inputfile = "input.txt" 

textfile1 = open(inputfile, encoding="utf8")
outputfile = input("Enter output file name. Otherwise it will appear as \"output.txt\": ")
if outputfile == "":
	outputfile = "output.txt"

Theoutputtextfile = open(outputfile, 'w', encoding="utf8")
removeitems = [r'\$Wa\$', r'\$E.*,', r'\d\$w0', r'VOICE', r'\$W[sm]',
r'\$Wd\$w0', r'\$b..', r'\$w0', r'PID', r'STRM', r'\$Sbs.*', r'EVT',
r'\$Wc']
#Notes: $k$p = Same person, scroll to new "two line dialogue set".
# $k\n = New person talking. Label right after it.
# $k = dialogue end.
# $k = Scroll button?
MUname = input("Enter MU name, otherwise it will appear as the Japanese \"Kamui\": ")
if MUname == "":
	MUname = "カムイ"

linenumber = 1

for lines in textfile1:
	if linenumber > 6:
		lines = lines.replace("$Nu", MUname)
		lines = lines.replace("username", MUname)
		lines = lines.replace("$k\\n", "$k\\n|")
		lines = lines.replace("$k$p", "$k\\n$p")
		delimiters = "|", ":", "\\n"
		regexPattern = '|'.join(map(re.escape, delimiters))
		splitline = re.split(regexPattern, lines)
		firstitem = True
		seconditem = True
		skipflag = False
		printnameflag = False
		commandfound = False
		currentname = "Test"
		
		for items in splitline:
			nameprinted = False
			commandsearch = re.search(r'\$W.',items) #looks if the line has a command
			if commandsearch == None and firstitem == False:
				printnameflag = True
			else:
				commandfound = True
			#Theoutputtextfile.write("Printnameflag: " + str(printnameflag)+ '\n')
			#Theoutputtextfile.write("Commandfound: " + str(commandfound)+ '\n\n')	
			commandsearch = None
			namesearch = re.search(r'\$W[sm]',items)
			if namesearch:
				currentname = items.replace("$Ws","")
				currentname = currentname.replace("$Wm","")
			namesearch = None
			if firstitem is True:
				Theoutputtextfile.write(items + ":\n") #prints the text ID
				firstitem = False
				commandfound = False
			else:
				items = items.replace("$p","")
				items = items.replace("$k","▼\n")
				if seconditem is True:
					items = items.replace(" ", "")
					seconditem = False
				for stuff in removeitems:
					pattern = stuff
					match = re.search(pattern,items)
					if match:
						skipflag = True
					if items == "":
						skipflag = True
				if (skipflag != True):
					if (printnameflag == True) and (commandfound == True):
						Theoutputtextfile.write(currentname + ":\n")
						printnameflag = False;
						commandfound = False;
					filter = items.replace("$Wa", "")
					Theoutputtextfile.write(filter + "\n")
				previousitem = items
				skipflag = False
				match = None	
		Theoutputtextfile.write('\n')
	else:
		Theoutputtextfile.write(lines)
	linenumber = linenumber + 1
	

print(outputfile + "file successfully generated.\n")

textfile1.close
Theoutputtextfile.close







