from astropy.coordinates import SkyCoord
from astropy import units as u
from astropy.table import Table
from astropy.io.ascii import write
from astropy.io.votable import from_table
from astropy.io.votable import writeto
import numpy as np
import os

#tables = input("Write path to file:")

def TablesRead():
	tables = input("Write path to file:")
	f=open(tables, "r")
	lines = f.readlines()
	f.close()
	length = str(len(lines))
	print("There are "+length+" matched fields.")
	return(lines)



#TablesRead()
