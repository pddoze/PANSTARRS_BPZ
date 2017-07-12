from astropy.coordinates import SkyCoord
from astropy import units as u
from astropy.table import Table
from astropy.table import Column
from astropy.io.ascii import write
import math
import numpy as np
import os

#This Code reads in the matched file names from a file and
#turns them into two vectors to be read in by for loop
#to a catalogue matching program

def TablesRead(x):
    #x is the path to file of matched fields
    A, B = [], []
    tables = x
    with open(tables, "r") as f:
        lines = f.readlines()
    for line in lines:
        a, b = line.rsplit(None, -1)
        A.append(a), B.append(b)
    return(A, B)

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||| 

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

def Match(catA, catB, dirA, dirB, filepath):
    A = Table.read(dirA+catA, format='ascii', delimiter=' ') #the smaller catalogue
    B = Table.read(dirB+catB, format='ascii', delimiter=' ') 

    #setting variables coor_sdss etc. to the values of an array or specifically
    #the column with name 'ra'...'DEC' of the files its reading, the array is a 
    #pair though, of the ra and dec so (ra,dec) is one entry in the array
    coor_A = SkyCoord(A['ramean']*u.deg, A['decmean']*u.deg) #u.deg is giving the unit
    coor_B = SkyCoord(B['ra']*u.deg, B['dec']*u.deg)
    #find indices in A that match with B
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
    separation = [] #for the output table
    Errors = []  #for the output table
    v = list(range(0, len(idx_A)))
    for i in v:
        a = idx_A[i] #gets the panstarrs indicie that matches with sdss indicie i
        b = 0.0000
        pone = SkyCoord(coor_A[a]) #panstarrs point
        ptwo = SkyCoord(coor_B[i])   #matching sdss point
        sep = pone.separation(ptwo) #separation between two matching points
        #treating the errors as points so I can get a sep involving ra,dec error
        Err = 1/3600       #for determining if two points truly match
                
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

    def column(matrix, i):
        return [row[i] for row in matrix]
    #Setting up output directory and output file name
    outpathA = os.path.dirname(filepath)+"/PS_Match/"
    outpathB = os.path.dirname(filepath)+"/SDSS_Match/"
    fhalfA, shalfA = catA.rsplit('_', 1)
    fhalfB, shalfB = catB.rsplit('_', 1)

    for index, i in enumerate(A2['objid'][:]):
        A2['objid'][index] = index+1
        B2['objid'][index] = index+1 

    write(B2, outpathB+fhalfB+'_Match.txt')
    sb = column(B2, 'Specz')
    sb2 =np.asarray(sb) #turning list into array so I can do something about 
    #these masked constants
    #got this from online replaces every nan with a number -99.0 in numpy? array
    sb2 = [-99.0 if math.isnan(x) else x for x in sb2] 

    cc = Column(sb2, name='Specz', dtype = object)

    A2.add_column(cc, index=26)

    write(A2, outpathA+fhalfA+'_Match.txt')
    #the delimiter in changing the output filename will probably change depending
    #on the stat the original catalogues are in
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||



filepath = "../Projects/PS_SDSS_work/matches.txt"
dirA = "../Projects/panstarSSV/"
dirB = "../Projects/SDSSssv/"
ps, sdss = TablesRead(filepath)
count = list(range(0, len(ps)))
for i in count[159:]:
    Match(ps[i], sdss[i], dirA, dirB, filepath)     
    #print(ps[i])
    #print(sdss[i])
    #print(type(ps[i]))




