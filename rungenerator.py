import os
from sys import argv
import shutil
import subprocess
rootdir = argv[1]
a = float(argv[2])
astep = float(argv[3])
runs= float(argv[4])
runsdir = rootdir + "_runs"

if not os.path.exists(runsdir):
    os.makedirs(runsdir)

poscar = []

f = open(rootdir + "/POSCAR")
for line in f:
    poscar.append(line)
f.close()
#a = float(poscar[1])

for i in range(runs):
    rundir = runsdir + "/" + ("%04d" % i)
    if not os.path.exists(rundir):
        os.makedirs(rundir)
    for x in os.listdir(rootdir):
        sourcename = rootdir + "/" + x
        targetname = rundir + "/" + x
        if not os.path.exists(targetname) or os.path.getmtime(sourcename) > os.path.getmtime(targetname):
            shutil.copyfile(sourcename, targetname)
        
    f = open(rundir + "/POSCAR", "w")
    linenum = 0
    for line in poscar:
        if linenum == 1:
            f.write(str(a) + "\n")
        else:
            f.write(line)
        linenum += 1
    f.close()
            
    a += astep
    
    subprocess.call(["makekpoints", rundir + "/"])
    subprocess.call(["sbatch", "jobfile"], cwd=rundir)
