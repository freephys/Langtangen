#!/usr/bin/env python
"""
Copy files from a playlist in m3u (MusicMatch) format to a memory stick,
preserving the order of the files in the playlist.
"""
import shutil, sys, re, os

usage = "%s playlistfile [-fp from-path -tp to-path] destination-dir" % \
        sys.argv[0]

if '-fp' in sys.argv:
    from_path = sys.argv[sys.argv.index('-fp')+1]
else:
    from_path = None
if '-tp' in sys.argv:
    to_path = sys.argv[sys.argv.index('-tp')+1]
else:
    to_path = None

destdir = sys.argv[-1]
playlistfile = sys.argv[1]

try:
    songpaths = open(playlistfile, 'r')
except IOError:
    print 'no file %s; maybe wrong arguments to the script?' %  playlistfile
    sys.exit(1)
    
track_counter = 0
for songpath in songpaths:
    songpath = songpath.strip()
    if from_path is not None:
        songpath = re.sub(from_path, to_path, songpath)
    if not os.path.isfile(songpath):
        print "****************** song file %s does not exist" % songpath
    track_counter += 1
    # prefix song name by the track counter to preserve the sequence of songs on
    # the destination memory stick:
    songname = os.path.basename(songpath)
    destsong = os.path.join(destdir, "%03d - " % track_counter + songname)
    if not os.path.isfile(destsong):
        print 'copy %s to %s' % (songname, destsong)
        shutil.copy(songpath, destsong)
    else:
        print '%s was already on %s' % (songname, destdir)
    

    

