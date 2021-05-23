#!/usr/bin/env python3

from shutil import copyfile
import sys, os

if len(sys.argv)<4 :
    print("Please use: ./gen.py <number of slaves> <max size> <max vector number> (<debug>)")
    exit(1)

debugmode = sys.argv[4] if len(sys.argv)==5 else 0

for fsentry in os.listdir("../") :
    if fsentry.endswith(".c") :
        os.remove(os.path.join("../", fsentry))

for i in range(int(sys.argv[1])) :
    copyfile("slave.c.def", os.path.join("../", f"slave{i+1}.c"))

copyfile("master.c.def", os.path.join("../", "master.c"))
copyfile("common.h.def", os.path.join("../", "common.h"))

f = open(os.path.join("../", "config.h"), "w+")
f.write(f"""#pragma once

#define DEBUG {debugmode}

#define VECTOR_SIZE {sys.argv[2]}
#define MAX_NUMBER {sys.argv[3]}

#define SLAVES_C {int(sys.argv[1])}
unsigned int SLAVES[{int(sys.argv[1])}] = {{{', '.join(f'slave{i+1}' for i in range(int(sys.argv[1])))}}};
""")
f.close()
