from astropy.coordinates import SkyCoord
from astropy import units as u
from astropy.table import Table
from astropy.io.ascii import write
from astropy.io.votable import from_table
from astropy.io.votable import writeto
import numpy as np
import os

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


