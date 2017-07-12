# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 17:48:28 2017

@author: Peter
"""

from astropy.table import Table
from astropy.table import Column
from astropy.io.ascii import write
import os

#   HOW TO USE THIS CODE
#   When you call the fucntion you have to tell it where the matched panstarrs
#   are located and you have to tell it where to put the .cat and .columns files
#   This code takes matched catalogues and creates .cat and .columns files 
#   that bpz needs to run photoz estimation.

def CatCreator(x, y):
    #Running through the matched catalogues in the given directory
    for filename in os.listdir(x):
    
        A = Table.read(filename, format='ascii', delimiter=' ')
        
        ob = Column(A['objid'], name='id', dtype = object)
        
        gg = Column(A['gmeanpsfmag'], name='g', dtype = object)
        ge = Column(A['gmeanpsfmagerr'], name='gerr', dtype = object)
        
        rr = Column(A['rmeanpsfmag'], name='r', dtype = object)
        re = Column(A['rmeanpsfmagerr'], name='rerr', dtype = object)
        
        ii = Column(A['imeanpsfmag'], name='i', dtype = object)
        ie = Column(A['imeanpsfmagerr'], name='ierr', dtype = object)
        
        zz = Column(A['zmeanpsfmag'], name='z', dtype = object)
        ze = Column(A['zmeanpsfmagerr'], name='zerr', dtype = object)
        #only for testing bpz plot
        zp = Column(A['Specz'], name='specz', dtype = object) 
        
        PScat = Table([ob, gg, ge, rr, re, ii, ie, zz, ze, zp])
        fhalf, shalf = filename.rsplit('.',1)
        #Create the .cat file for bpz
        with open(y + fhalf + '.cat', 'a') as r:
            for i, name in enumerate(PScat.colnames):
                r.write('# '+str(i+1)+' '+name+'\n')
            r.write('#\n')
            PScat.write(r, format='ascii.commented_header')
        #Create the .columns file for bpz
        with open(y + fhalf + '.columns', 'a') as t:
            t.write('# Filter'.ljust(20, ' ') + 'columns'.ljust(9, ' ') + 
                    'AB/Vega'.ljust(9, ' ') + 'zp_error'.ljust(10, ' ') + 
                    'zp_offset'.ljust(9, ' ') + '\n') 
            t.write('PAN-STARRS-PS1.g.res'.ljust(25, ' ') + '2, 3'.ljust(7, ' ') + 
                    'AB'.ljust(10, ' ') + '0.05'.ljust(10, ' ') + 
                    '0.0' + '\n')
            t.write('PAN-STARRS-PS1.r.res'.ljust(25, ' ') + '4, 5'.ljust(7, ' ') + 
                    'AB'.ljust(10, ' ') + '0.05'.ljust(10, ' ') + 
                    '0.0' + '\n')
            t.write('PAN-STARRS-PS1.i.res'.ljust(25, ' ') + '6, 7'.ljust(7, ' ') + 
                    'AB'.ljust(10, ' ') + '0.05'.ljust(10, ' ') + 
                    '0.0' + '\n')
            t.write('PAN-STARRS-PS1.z.res'.ljust(25, ' ') + '8, 9'.ljust(7, ' ') + 
                    'AB'.ljust(10, ' ') + '0.05'.ljust(10, ' ') + 
                    '0.0' + '\n')
            t.write('ID'.ljust(22, ' ') + '1'.ljust(9, ' ') + '\n')
            t.write('Z_S'.ljust(22, ' ') + '10'.ljust(9, ' ') + '\n')
            t.write('M_0'.ljust(22, ' ') + '6'.ljust(9, ' '))
            
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||




dirpath = "../Projects/PS_SDSS_work/PS_Match/"
outpath = "../bpz_1.99.3_py3/test/"

CatCreator(dirpath, outpath)

