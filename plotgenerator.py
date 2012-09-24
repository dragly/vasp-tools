# -*- coding: utf-8 -*-
import os
from sys import argv
from pylab import *
import shutil
import subprocess

rootdir = argv[1]
a=[]
E=[]
#open different folders: sc_runs->0000->
#for i in range(runs):
i = 0
for x in os.listdir(rootdir):
    if not os.path.isdir(rootdir + "/" + x):
        continue
    poscar = []
    f = open(rootdir + "/" + x + "/POSCAR")
    for line in f:
        poscar.append(line)
    f.close()

    subprocess.check_call("toten OUTCAR > energies.dat", shell=True, cwd=rootdir + "/" + x)
    f = open(rootdir + "/" + x + "/energies.dat")
    output = f.read()
    f.close()
    lines = output.split("\n") 
    value = float(lines[1].split("\t")[1])

    a.append(float(poscar[1]))
    E.append(value)
    i += 1
    
plot(a, E,'-*')
title(rootdir.replace("_runs","").replace(".","").replace("/",""))
ylabel("Energy [eV]")
xlabel(u"a[Å]")
savefig(rootdir + "/output.pdf")



