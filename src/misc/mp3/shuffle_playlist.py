#!/usr/bin/env python
import sys, random
f = open(sys.argv[1], 'r'); lines = f.readlines(); f.close()
random.shuffle(lines) # in-place shuffle
f = open(sys.argv[2], 'w'); f.writelines(lines); f.close()
