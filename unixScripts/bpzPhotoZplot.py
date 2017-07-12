# -*- coding: utf-8 -*-
"""
Created on Sun May 21 17:06:35 2017

@author: Peter
"""
# Plotting Photoz of Panstarrs catalogue from bpz versus the spec z of the 
#corresponding SDSS object and field.

from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt
import pylab

pZ = Table.read('psG048_specz_bpz.cat', format='ascii')

sZ = Table.read('SDSS_Sort_G048.txt', format='ascii') 
def column(matrix, i):
    return [row[i] for row in matrix]

zb = column(pZ, 'zb')
zlb = column(pZ, 'zml')
sb = column(sZ, 'Specz')
#sb = [None if i is -99.0 else i for i in sb] #won't plot points with no specz

x = np.arange(0, 2)
y = np.arange(0, 2)

plt.figure(0)
plt.plot(sb, zb, 'g^')
plt.plot(x, y)
plt.ylabel('Photonometic Z (PANSTARRS)')
plt.xlabel('Spectroscopic Z (SDSS) ')
plt.title('SpecZ vs. BPZ G048 bands: g, r, i, z with specz')

plt.figure(1)
plt.plot(sb, zlb, 'r^')
plt.plot(x, y)
plt.ylabel('Max Likelihood Z (PANSTARRS)')
plt.xlabel('Spectroscopic Z (SDSS) ')
plt.title('SpecZ vs. Maximum Likelihood G048: g, r, i, z with specz')
#print('zb is ', zb)
#print('sb is ', sb)

ZS = Table([zb, sb, zlb])

with open('ZSSG048.txt', 'a') as r:
    ZS.write(r, format='ascii.commented_header')



