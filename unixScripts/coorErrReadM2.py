from astropy.coordinates import SkyCoord
from astropy import units as u
from astropy.table import Table
from astropy.io.ascii import write
from astropy.io.votable import from_table
from astropy.io.votable import writeto
import numpy as np

def CoorErrGet(X):
	pathA = input("Write path (../) to directory with catalogue A:")
	pathB = input("Write path (../) to directory with catalogue B:")
	
	rcA = input("Type the header for the RA column of catalogue A:")
	dcA = input("Type the header for the DEC column of catalogue A:")
	rcB = input("Type the header for the RA column of catalogue B:")
	dcB = input("Type the header for the DEC column of catalogue B:")
	
	catA = X[0].rsplit(' ', 1)[0]
	catB = X[0].rsplit(' ', 1)[1]
	
	A = Table.read(pathA+catA, format='ascii', delimiter=' ')
	B = Table.read(pathB+catB, format='ascii', delimiter=' ')
	coor_A = SkyCoord(A[rcA]*u.deg, A[dcA]*u.deg)
	coor_B = SkyCoord(B[rcB]*u.deg, B[dcB]*u.deg)
	print(coor_A)
	print(coor_B)
	
