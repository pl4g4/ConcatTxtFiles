#!/usr/bin/python
# Concat txt files inside a folder
import glob, os, sys, argparse

parser = argparse.ArgumentParser(prog='ConcatTxtFiles')
parser.add_argument("folderpath", help="The path where the txt files are located", type=str)
parser.add_argument("--outputfolder", help="The path where the txt file will be saved", type=str, default=os.getcwd(), metavar=os.getcwd())
args = parser.parse_args()

def main(args):
	
	if (len(sys.argv) < 2) | (len(sys.argv) > 4):
		print "You are missing args, use -h for help"
		sys.exit()
		
	if os.path.exists(args.folderpath):		
		listFiles = getFilesList(args.folderpath)					
		if concatFilesIntoOne(listFiles, args.outputfolder, args.folderpath):			
			print "You can find you new list @ " + args.outputfolder
		else:
			print "File was not created"
				
	else:
		print "folder with txt files not Found"
		sys.exit()
	

def getFilesList(filesPath):
	prevDir = os.getcwd()
	os.chdir(filesPath)
	fileNames = []
	for file in glob.glob("*.txt"):
		fileNames.append(file)
	
	os.chdir(prevDir)
	return fileNames

def concatFilesIntoOne(listFiles, outputfolder, filesPath):
	prevDir = os.getcwd()
		
	if os.path.exists(outputfolder):		
		print "Putting all files together\n This may take a while."		
		with open(outputfolder+'/newList.txt', 'w') as outfile:			
			os.chdir(filesPath)
			for txt in listFiles:
				print "Working with file " + txt
				with open(txt) as infile:
					for line in infile:
						outfile.write(line)
					
	else:
		print "Output folder not Found"
		sys.exit()
	             
	os.chdir(prevDir)
	if os.path.isfile(outputfolder+'/newList.txt'):
		return True
	else:
		return False
	

main(args)
sys.exit()
