#!/usr/bin/python
# to_pygame_movie.sh movie_name

#sudo apt-get install python-kaa-metadata

import kaa.metadata
import os
import sys


try:
  filename = sys.argv[1]
except IndexError:
  print "usage: to_pygame_movie.py infile"
  sys.exit(1)

info = kaa.metadata.parse(filename)

d = {'f':filename}
d['w'] = info.header['hdrl']['avih']['dwWidth']
d['h'] = info.header['hdrl']['avih']['dwHeight']
d['out_w'] = 640
d['out_h'] = 480

# convert to 30fps
s = "mencoder -really-quiet -lavdopts threads=4 %(f)s -ovc raw -nosound -vf scale,format=i420,harddup  -ofps 30 -of rawvideo -o - | x264 --crf 18 --partitions none --me dia --merange 4 --mvrange 64 --subme 0 --no-chroma-me --aq-mode 0 --threads auto --no-cabac --no-deblock  --fps 30 --output %(f)s_30fps.avi - %(w)dx%(h)d" % d

err = os.system(s)

if err!=0:
  print "Step 0 failed. aborting."

# encode for pygame

s = "mencoder  %(f)s_30fps.avi -vf scale=%(out_w)d:%(out_h)d -of mpeg -mpegopts format=mpeg1:tsaf:muxrate=2000 -o pygame_%(f)s_30fps.avi -srate 44100 -af lavcresample=44100 -oac copy -ovc lavc -lavcopts vcodec=mpeg1video:vbitrate=1152:keyint=15:mbd=2" % d

err = os.system(s)

if err!=0:
  print "Step 0 failed. aborting."
else:
  print "Success -> pygame_%s_30fps.avi" % (filename)

