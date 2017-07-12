import os 
import numpy as np
#THIS CODE MATCHES CATALOGUE FILE NAMES IN TWO DIFFERENT DIRECTORIES
#You need to copy this into ~/ so that it can find the directories, it won't
#find them from the unixScripts directory. You need to set the path for the two
#directories and the output files of matched filed and unmatched files.

colA =[]
colB =[]
NM = []
#The number of files in each directory
list1 =  os.listdir('../Projects/Work/testFiles/')
list2 =  os.listdir('../Projects/Work/testFiles2/')
a = str(len(list1))
b = str(len(list2))

for file in os.listdir('../Projects/Work/testFiles/'):
	filename1 = os.path.basename(file)
	name = filename1.replace("ssv","bat")
	if name in os.listdir('../Projects/Work/testFiles2/'):
		colA.append(filename1)
		colB.append(name)
	else:
		NM.append(filename1)


M = open('../unixScripts/matches.txt', 'a')
MF = open('../unixScripts/nomatches.txt', 'a')
for c1, c2 in zip(colA, colB):
	M.write(c1+' '+c2+'\n')

for c3 in NM:
	MF.write(c3+'\n')

M.close()
MF.close()
print('The number of elements in directory A = '+a)
print('The number of elements in directory B = '+b)
print('The number of matched elements = '+str(len(colA)))
print('The number of unmatched elements = '+str(len(NM)))
