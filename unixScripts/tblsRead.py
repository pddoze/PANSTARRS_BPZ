#This Code read in the matched file names from a file and
#turns them into two vectors to be read in by for loop
#to a catalogue matching program

def TablesRead(x):
	#x is the path to file of matched fields
	A, B = [], []
	tables = x
	with open(tables, "r") as f:
		lines = f.readlines()
	for line in lines:
		a, b = line.rsplit(None, -1)
		A.append(a), B.append(b)
	return(A, B)

filepath = "../Projects/PS_SDSS_work/matches.txt"
ps, sdss = TablesRead(filepath)

print(ps[0])


