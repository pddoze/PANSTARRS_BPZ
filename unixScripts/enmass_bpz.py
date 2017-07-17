import os
#from subprocess import call
import subprocess

#Use bpz, a photonometric estimation program, en mass for multiple fields at a
#time


def bpzRun(x):
    for filename in os.listdir(x):
        if filename.endswith(".cat"):
            fhalf, shalf = filename.rsplit('.',1)
            subprocess.Popen(["python3", "/home/doze/bpz_1.99.3_py3/bpz.py", 
                              filename, "-ZMAX", "1.8", 
                              "-VERBOSE", "no", "-INTERP", "2", "-DZ", 
                              "0.01", "-SPECTRA", "CWWSB_Benitez2003.list", 
                              "-PRIOR", "full", "-PROBS_LITE", 
                              fhalf+".probs"])            
        else:
            continue
        
    

dirpath = "../bpz_1.99.3_py3/test/"
bpzRun(dirpath)
