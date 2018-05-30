#!/usr/bin/env python3

import sys
import os
import subprocess
import time


f = open(sys.argv[1])

# read input and split it
t = f.read()
f.close()
svgs = t.split("</svg>")

print(len(svgs))

def name(i):
    return "sample" + str(i) + ".svg"

# don't overwrite files
i = 1
while os.path.isfile(name(i)): i += 1

for svg in svgs[:-1]:
    #print(svg+"</svg>\n")
    print(i)
    sname = name(i)
    f = open(sname, "w")
    f.write(svg + "</svg>\n")
    f.close()
    #if not os.fork():
    subprocess.call(["inkscape.exe", sname, "-e", sname+".png", "-d", "480"])
    #    os._exit(0)
    i+=1
    time.sleep(0.4)
