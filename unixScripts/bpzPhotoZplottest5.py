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
import os
from astropy.table import Column

#This code reads all the panstars bpz results, collects all the photoz's and 
#maximum likiehood and organizes it to be plotted

def BPZPhotoZPlot(xx):
    photoz = [] #append to this list and plot all acceptable points at once
    ml = []
    specz = []
    for filename in os.listdir(xx):
        if filename.endswith('.bpz'):
            pZ = Table.read(xx + filename, format='ascii')
            
            def column(matrix, i):
                return [row[i] for row in matrix]
            
            zb = column(pZ, 'zb') #1 python counting 
            zlb = column(pZ, 'zml')#6
            zs = column(pZ, 'zspec')#9
    
            for i, value in enumerate(zs):
                if value == -99.0:
                    continue
                else:
                    photoz.append(zb[i])
                    ml.append(zlb[i])
                    specz.append(zs[i])
        else:
            continue
    
    plotzb = Column(photoz, name='Photoz', dtype = object)
    plotzml = Column(ml, name='ML', dtype = object)
    plotzspec = Column(specz, name='Zspec', dtype = object)
    Plotlist = Table([plotzb, plotzml, plotzspec])    
    with open('../Projects/PS_SDSS_work/bpzplot.txt', 'a') as r:
        Plotlist.write(r, format='ascii.commented_header')

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


bpzpath = "../bpz_1.99.3_py3/test/"
BPZPhotoZPlot(bpzpath)