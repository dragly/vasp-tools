import os
from sys import argv
import shutil
import subprocess

rootdir = argv[1]



#open different folders: sc_runs->0000->
for x in os.listdir(rootdir):
  print rootdir + "/" + x
  output = subprocess.check_output(["toten", "OUTCAR"], cwd=rootdir + "/" + x)
  lines = output.split("\n") 
  value = lines[1].split("\t")[1]
  print value
  
#Read the energy
  
#Plot energies vs a

