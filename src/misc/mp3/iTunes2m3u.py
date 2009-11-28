#!/usr/bin/env python
"""Convert iTunes playlist in .txt format to m3u (MusicMatch) format."""

import sys
usage = '%s playlist-iTunes' % sys.argv[0]
if len(sys.argv) < 2:
    print usage
    sys.exit(1)
    
playlist_iTunes = sys.argv[1]
playlist_m3u = playlist_iTunes[:-3] + 'm3u' # m3u extension

# note that iTunes .txt files are in unicode format
import codecs
iTunes_file = codecs.open(playlist_iTunes, 'r', 'utf_16')
songs = iTunes_file.readlines()[1:]
iTunes_file.close()
m3u_file = open(playlist_m3u, 'w')
for song in songs:
    songpath = song.split('\t')[-1].strip()
    m3u_file.write(songpath + '\n')
m3u_file.close()
