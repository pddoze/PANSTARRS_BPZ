# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 00:31:39 2017

@author: Peter
"""
import numpy as np
from astropy.table import Table

f = Table.read('SDSSssvSortV1G009.txt', format='ascii', delimiter=' ')
f2 = Table.read('PANSTARRSssvSortV1G009.txt', format='ascii', delimiter=' ')


def column(matrix, i):
    return [row[i] for row in matrix]

#need it to be an array not a list, so that it can be converted to string
ra = np.array(column(f, 'ra')) 
dec = np.array(column(f, 'dec'))
rad = np.array(column(f, 'RadError'))
sep = np.array(column(f, 'Separation'))

ra2 = np.array(column(f2, 'ramean')) 
dec2 = np.array(column(f2, 'decmean'))

    
with open('sloanregV1G009.reg', 'a') as r:
    r.write('# Region file format: DS9 version 4.1\n')
    r.write('global color=green dashlist=8 3 width=1 font="helvetica 10 normal '
            'roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 '
            'include=1 source=1\n')
    r.write('fk5\n')
    for i in list(range(0, len(ra))):
        rastr = '%.5f' % ra[i]
        decstr = '%.5f' % dec[i]
        radstr = '%.5f' % rad[i]
        sepstr = '%.5f' % sep[i]
        r.write('circle('+rastr+','+decstr+','+radstr+') # text={ '
                'separation: '+sepstr+'}\n')
    
with open('psregV1G009.reg', 'a') as r2:
    r2.write('# Region file format: DS9 version 4.1\n')
    r2.write('global color=red dashlist=8 3 width=1 font="helvetica 10 normal '
            'roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 '
            'include=1 source=1\n')
    r2.write('fk5\n')
    for i in list(range(0, len(ra2))):
        rastr2 = '%.5f' % ra2[i]
        decstr2 = '%.5f' % dec2[i]
        r2.write('cross point('+rastr2+','+decstr2+') # text={ '
                'separation: same as sdss}\n')
#print(ra[0], dec[0], rad[0], sep[0])