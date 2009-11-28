#!/usr/bin/env python
def checkfile(arg, dir, files):
    for file in files:
        path = os.path.join(dir, file)
        for pattern in sys.argv[3:]:
            if re.search(pattern, file):
                arg.append(path)
playlist = []
os.path.walk(sys.argv[2], checkfile, playlist)
f = open(sys.argv[1], 'w')
f.writelines(playlist)
f.close()
