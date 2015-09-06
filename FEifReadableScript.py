#! /usr/bin/python
import sys
import re

def promptuserforinput(prompt, default):
	userinput = input(prompt)
	if not userinput:
		userinput = default
	return userinput
	
def replacelistofstuff(list, string, replace):
	for stuff in list:
		string = string.replace(stuff, replace)
	return string

inputfile = promptuserforinput("Enter input file name: ", "input.txt")
outputfile =  promptuserforinput("Enter output file name: ", "output.txt")
outputtextfile = open(outputfile, 'w', encoding="utf8")

removeitems = [r'\$Wa\$', r'\$E.*,', r'\d\$W\w', r'VOICE', r'\$W[sm]',
r'\$Wd\$w0', r'\$b..', r'\$w0', r'PID', r'STRM', r'\$Sbs.*', r'EVT',
r'\$Wc']
beforenamecommands = [r'\d\$Ws', r'\$W[sm]']
#Notes: $k$p = Same person, scroll to new "two line dialogue set".
# $k\n = New person talking. Label right after it.
# $k = dialogue end.
# $k = Scroll button?
MUname = promptuserforinput("Enter MU name, otherwise it will appear as the Japanese \"Kamui\": ", "カムイ")


	

with open(inputfile, encoding="utf8") as inputtextfile:
	for x in range( 6):
		outputtextfile.write(next(inputtextfile))
	for lines in inputtextfile:	
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
		currentname = ""
		
		for items in splitline:
			nameprinted = False
			commandsearch = re.search(r'\$W.',items) #looks if the line has a command
			if commandsearch == None and firstitem == False:
				printnameflag = True
			else:
				commandfound = True
			#outputtextfile.write("Printnameflag: " + str(printnameflag)+ '\n')
			#outputtextfile.write("Commandfound: " + str(commandfound)+ '\n\n')	
			commandsearch = None
			namesearch = re.search(r'\$W[sm]',items)
			if namesearch:
				currentname = items
				for things in beforenamecommands:
					pattern = things
					currentname = re.sub(pattern, "", currentname)
			namesearch = None
			if firstitem == True:
				outputtextfile.write(items + ":\n") #prints the text ID
				firstitem = False
				commandfound = False
			else:
				items = items.replace("$p","")
				items = items.replace("$k","▼\n")
				if seconditem == True:
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
						outputtextfile.write(currentname + ":\n")
						printnameflag = False;
						commandfound = False;
					filter = items.replace("$Wa", "")
					outputtextfile.write(filter + "\n")
				previousitem = items
				skipflag = False
				match = None	
		outputtextfile.write('\n')
inputtextfile.close
outputtextfile.close
	

print(outputfile + " file successfully generated.\n")








