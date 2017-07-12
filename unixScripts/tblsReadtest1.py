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
	tables = x
	f=open(tables, "r")
	lines = f.readlines()
	f.close()
	length = str(len(lines))
	print("There are "+length+" matched fields.")
	#return(lines)

filepath = "../Projects/matches.txt"
TablesRead(filepath)




