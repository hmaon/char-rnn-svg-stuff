#!/usr/bin/env python3

import sys
import os
import subprocess
import time
from unstupifyxml import unstupifyxml


f = open(sys.argv[1])
start = 0
if len(sys.argv) > 2:
    start = int(sys.argv[2])

# read input and split it
t = f.read()
f.close()
svgs = t.split("\n")

print(len(svgs))

def name(i):
    return "sample" + str(i) + ".svg"

# don't overwrite files
i = start + 1
while os.path.isfile(name(i)): i += 1

for svg in svgs[start:-1]:
    #print(svg+"</svg>\n")
    print(i)
    sname = name(i)
    f = open(sname, "w")
    unstupifyxml(svg, f.write)
    f.write("\n")
    f.close()
    #if not os.fork():
    subprocess.call(["inkscape.exe", sname, "-e", sname+".png", "-d", "480"])
    #    os._exit(0)
    i+=1
    #time.sleep(0.4)
