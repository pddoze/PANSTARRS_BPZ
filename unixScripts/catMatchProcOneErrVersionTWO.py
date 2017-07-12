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


#IN VERSION ONE THE ERROR(RADIUS) OF THE POINT IS ESTIMATED TO BE A VERY GOOD
#SEEING OF 10 ARCSECOND

from astropy.coordinates import SkyCoord
from astropy import units as u
from astropy.table import Table
from astropy.table import Column
from astropy.io.ascii import write


#the below Tabl.read is reading in the two catalogs
#I don't know if it will work it i give the file path to the file
#for now it works when the file is in the same folder as the .py program
A = Table.read('PSZ1_G001.00+25.71_PS1_catalogSSV.txt', format='ascii', delimiter=' ') #the smaller catalogue

B = Table.read('PSZ1_G001.00+25.71_SDSS_catalogSSV.txt', format='ascii', delimiter=' ') 



#setting variables coor_sdss etc. to the values of an array or specifically
#the column with name 'ra'...'DEC' of the files its reading, the array is a 
#pair though, of the ra and dec so (ra,dec) is one entry in the array
coor_A = SkyCoord(A['ramean']*u.deg, A['decmean']*u.deg) #u.deg is giving the units
coor_B = SkyCoord(B['ra']*u.deg, B['dec']*u.deg)


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
separation = []
Errors = []
v = list(range(0, len(idx_A)))
for i in v:
    a = idx_A[i] #gets the panstarrs indicie that matches with sdss indicie i
    b = 0.0000
    pone = SkyCoord(coor_A[a]) #panstarrs point
    ptwo = SkyCoord(coor_B[i])   #matching sdss point
    sep = pone.separation(ptwo) #separation between two matching points
    #treating the errors as points so I can get a sep involving ra,dec error
    Err = 10/3600       #for determining if two points truly match
    
            
    if sep.deg > Err:    #separation is > error its not a real match remove iT
        rec.append(i)    #keeps track of indicies that have bad mathes
        separation.append(sep.deg)
        Errors.append(Err)
    else:
        separation.append(sep.deg)
        Errors.append(Err)
    
    
idx_Alist = idx_A.tolist() #have to turn into array to del
 
for i in sorted(rec, reverse=True): #deletes indicies with bad matches
    del idx_Alist[i]
    del index[i]
    del separation[i]
    del Errors[i]
#have to specify object so I can add it on
aa = Column(separation, name='Separation', dtype = object)
bb = Column(Errors, name='RadError', dtype= object)
A2 = A[idx_Alist] #rewrites panstarrs in the order determined by idx
B2 = B[index]            #rewrites sdss in the order determined by index
B2.add_column(aa, index=23)
B2.add_column(bb, index=24)


write(B2, 'SDSSssvSortV2.txt')
write(A2, 'PANSTARRSssvSortV2.txt')





