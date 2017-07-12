# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 17:48:28 2017

@author: Peter
"""

from astropy.table import Table
from astropy.table import Column
from astropy.io.ascii import write


A = Table.read('PANSTARRS_Sort_G048.txt', format='ascii', delimiter=' ')

ob = Column(A['objid'], name='id', dtype = object)

gg = Column(A['gmeanpsfmag'], name='g', dtype = object)
ge = Column(A['gmeanpsfmagerr'], name='gerr', dtype = object)

rr = Column(A['rmeanpsfmag'], name='r', dtype = object)
re = Column(A['rmeanpsfmagerr'], name='rerr', dtype = object)

ii = Column(A['imeanpsfmag'], name='i', dtype = object)
ie = Column(A['imeanpsfmagerr'], name='ierr', dtype = object)

zz = Column(A['zmeanpsfmag'], name='z', dtype = object)
ze = Column(A['zmeanpsfmagerr'], name='zerr', dtype = object)

zp = Column(A['Specz'], name='specz', dtype = object) #only for testing bpz plot

PScat = Table([ob, gg, ge, rr, re, ii, ie, zz, ze, zp])


with open('psG048_specz.cat', 'a') as r:
    for i, name in enumerate(PScat.colnames):
        r.write('# '+str(i+1)+' '+name+'\n')
    r.write('#\n')
    PScat.write(r, format='ascii.commented_header')


