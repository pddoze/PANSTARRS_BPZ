# -*- coding: utf-8 -*-
"""
Created on Tue May 23 18:35:27 2017

@author: Peter
"""

#   HOW    TO    USE    THIS    CODE
#You need to put in the catalogs manually (for the time being) that you want to
#be matched together into Table read. You also need to put in the column names
#of the ra and dec positions and their errors. table A (sdss) should be the 
#smaller catalog, by row, or equal
#The difference from catMatchProc.py is that this program works when only one
#catalogue has errors.

#This code takes two cataloges matches positions and using the position errors
#checks if the separation between the matches is larger than the error. If it
#is, it is not a true match and the row is removed from catalogs. Then it 
#puts the respective index in each catalog so that you can get a list of values
#that correspond in order, so if 4 & 2 matches with 3 and 4, you get 
#[4  2]sdss  [3  4]panstar ; then take the appropriate cataloge run it through
#bpz and should get photoZ's which should be in right order. Take the needed


from astropy.coordinates import SkyCoord
from astropy import units as u
from astropy.table import Table
from astropy.io.ascii import write
from astropy.io.votable import from_table
from astropy.io.votable import writeto
import numpy as np

#the below Tabl.read is reading in the two catalogs
#I don't know if it will work it i give the file path to the file
#for now it works when the file is in the same folder as the .py program
A = Table.read('PANSTARRSssv.txt', format='ascii') #the smaller catalogue
B = Table.read('SDSSssv18Col.txt', format='ascii') 



#setting variables coor_sdss etc. to the values of an array or specifically
#the column with name 'ra'...'DEC' of the files its reading, the array is a 
#pair though, of the ra and dec so (ra,dec) is one entry in the array
coor_B = SkyCoord(B['ra']*u.deg, B['dec']*u.deg)
coor_A = SkyCoord(A['ramean']*u.deg, A['decmean']*u.deg) #u.deg is giving the units

#took this from internet it allows you to put in a matrix, in this case a table
#didnt think id work but it did, and you give column indicie and it gives you
#the whole column as a vector, in this case I gave it the column name and it 
#worked
def column(matrix, i):
    return [row[i] for row in matrix]

BErrRa = column(B, 'ra_err')
BErrDec = column(B, 'dec_err')


#find indicies in sdss that match with panstarrs
idx_B, d2d_B, d3d_B = coor_A.match_to_catalog_sky(coor_B)


#find indices in panstarrs that match with sdss
#So for example if the result was [4 2 1] this means the 4th element of panstar
#matches with the 0th element of sdss
idx_A, d2d_A, d3d_A = coor_B.match_to_catalog_sky(coor_A)
index = list(range(0, len(idx_A))) #when the program removes bad matches 
                                #need a index or normal order indicie counts
                                #so the two vectors match up i.e
                                #[4, 2, 1] 4 entry of ps matches with 0 sdss
                                #[0, 1, 2]  but with a bad match remove the 
                                #entry from both idx and index i.e
                                # [2, 1] in final leg prog pulls out 2nd of ps
                                # [1, 2] and corresponding to 1st of sdss

rec = [] #initialize a list so that I can keep track of which i fail sep test
v = list(range(0, len(idx_A)))
for i in v:
    a = idx_A[i] #gets the panstarrs indicie that matches with sdss indicie i
    b = 0.0000
    pone = SkyCoord(coor_A[a]) #panstarrs point
    ptwo = SkyCoord(coor_B[i])   #matching sdss point
    
    poneSDSSerr = SkyCoord(b*u.deg, b*u.deg)
    ptwoSDSSerr = SkyCoord(BErrRa[a]*u.deg, BErrDec[a]*u.deg )
    #print(i)
       
    sep = pone.separation(ptwo) #separation between two matching points
    #treating the errors as points so I can get a sep involving ra,dec error
    sepSDSSerr = poneSDSSerr.separation(ptwoSDSSerr)
    Err = sepSDSSerr.deg       #for determining if two points truly match
        
    
    if sep.deg > Err:    #separation is > error its not a real match remove iT
        rec.append(i)    #keeps track of indicies that have bad mathes
    
    

idx_Alist = idx_A.tolist() #have to turn into array to del
 
for i in sorted(rec, reverse=True): #deletes indicies with bad matches
    del idx_Alist[i]
    del index[i]


A2 = A[idx_Alist] #rewrites panstarrs in the order determined by idx
B2 = B[index]            #rewrites sdss in the order determined by index

write(B2, 'SDSSssvSort.txt')
write(A2, 'PANSTARRSssvSort.txt')

#This next part is because ds9 doenst look at ascii catalog, if you wanted to
#use ds9 to check comparisons
#A2vot = from_table(A2)  #turns table into a vottable file
#writeto(A2vot, 'SDSSssvSortvot.xml') #outputs votable file to actual table



