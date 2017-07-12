import os
#from subprocess import call
import subprocess

#Use bpz, a photonometric estimation program, en mass for multiple fields at a
#time
os.environ["HOME"] = "/home/doze"
os.environ["BPZPATH"] = "$HOME/bpz-1.99.3"
os.environ["PYTHONPATH"] = "$PYTHONPATH:$BPZPATH"
#os.environ[alias] bpz="python $BPZPATH/bpz.py"
os.environ["NUMERIX"] = "numpy"

#bpz psG048_specz.cat -ZMAX 1.8 -VERBOSE no -INTERP 2 -DZ 0.01 -SPECTRA CWWSB_Benitez2003.list -PRIOR full -PROBS_LITE psG048_specz.probs

#python $BPZPATH/bpzfinalize.py psG055_specz

#os.system('python $BPZPATH/bpz.py psG108_specz.color -ZMAX 1.8 -VERBOSE no -INTERP 2 -DZ 0.01 -SPECTRA CWWSB_Benitez2003.list -PRIOR full -PROBS_LITE psG108_specz.probs')


subprocess.Popen(["python", "$BPZPATH/bpz.py", "psG048_specz.color", "-ZMAX", "1.8", "-VERBOSE", "no", "-INTERP", "2", "-DZ", "0.01", "-SPECTRA", "CWWSB_Benitez2003.list", "-PRIOR", "full", "-PROBS_LITE", "psG048_specz.probs"])

