from astropy.coordinates import SkyCoord
from astropy import units as u
from astropy.table import Table
from astropy.io.ascii import write
from astropy.io.votable import from_table
from astropy.io.votable import writeto
import numpy as np
import tblsReadM1
import coorErrReadM2

L = tblsReadM1.TablesRead()
coorErrREadM2.CoorErrGet(L) 
