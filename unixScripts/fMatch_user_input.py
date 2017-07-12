import os 
import numpy as np
#THIS CODE MATCHES CATALOGUE FILE NAMES IN TWO DIFFERENT DIRECTORIES
#You need to copy this into ~/ so that it can find the directories, it won't
#find them from the unixScripts directory. <-- Don't need to do this with ../ 
#You need to set the path for the two directories and the output files 
#of matched filed and unmatched files.

print("This code matches catalogue file names in two different directories")
relpathA = input("Write the relative path (../) for directory A:")
relpathB = input("Write the relative path (../) for directory B:")
relpathC = input("Write the relative path (../) to create matches file:")
relpathD = input("Write the relative path (../) to create no-matches file:")
Aport = input("Input the portion of the filename to be replaced:")
Bport = input("Input what it is to be replaced with:")
colA =[]
colB =[]
NM = []
#The number of files in each directory
list1 =  os.listdir(relpathA)
list2 =  os.listdir(relpathB)
a = str(len(list1))
b = str(len(list2))

for file in os.listdir(relpathA):
	filename1 = os.path.basename(file)
	name = filename1.replace(Aport,Bport)
	if name in os.listdir(relpathB):
		colA.append(filename1)
		colB.append(name)
	else:
		NM.append(filename1)


M = open(relpathC, 'a')
MF = open(relpathD, 'a')
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
