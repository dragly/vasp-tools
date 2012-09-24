import os
from sys import argv
import shutil
import subprocess

rootdir = argv[1]


#open different folders: sc_runs->0000->
for x in os.listdir(rootdir):
  poscar = []
  f = open(rootdir + "/" + x + "/POSCAR")
  for line in f:
      poscar.append(line)
  f.close()
  
  output = subprocess.check_output(["toten", "OUTCAR"], cwd=rootdir + "/" + x)
  lines = output.split("\n") 
  value = float(lines[1].split("\t")[1])
  
  plot(float(poscar[1]),value)
  
#Read the energy
  
#Plot energies vs a


