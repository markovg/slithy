#!/usr/bin/python
# to_pygame_movie.sh movie_name

#sudo apt-get install python-kaa-metadata

import os
import sys
import getopt



def to_pygame_movie(filename, outname=None, w=None,h=None,crop=None,startpos=None,endpos=None,sound=True):
  """
  converts movie media to format suitable for playback with pygame.
  uses mencoder.

  filename - source file to convert
  outname - target file to convert [default: pygame_$filename_30fps.avi]
  w,h - width,height of output [default: 640,480]
  crop - dictionary with keys w,h,x,y:
       -> width,height, x,y of top-left corner.  

  startpos - start pos in seconds
  endpos - end pos in seconds

  """

  # get metadata from file
  import kaa.metadata
  info = kaa.metadata.parse(filename)

  if w==None:
    w=640
  if h==None:
    w=480

  # get frames per second
  fps = info['video'][0]['fps']

  d = {'f':filename}
  d['w'] = info.header['hdrl']['avih']['dwWidth']
  d['h'] = info.header['hdrl']['avih']['dwHeight']
  d['out_w'] = 640
  d['out_h'] = 480
  d['crop'] = ''

  if startpos:
    d['startpos'] = '-ss %s' % startpos
    
  if endpos:
    d['endpos'] = '-endpos %s' % endpos

  if not outname:
    outname = "pygame_%s_30fps.avi" % filename
  d['outname'] = outname

  if type(crop)==dict:
    d['crop'] = ',crop=%(w)d:%(h)d:%(x)d:%(y)d' % crop
  elif type(crop)==str:
    d['crop'] = ',crop=%s' % crop

  if sound:
    d['snd'] = "-audiofile %(f)s.mp3 -oac copy" % d
    #d['snd'] = "-oac twolame -twolameopts br=160"
    s = "mencoder %(startpos)s %(endpos)s %(f)s -of rawaudio -ovc copy -oac twolame -twolameopts br=160 -o %(f)s.mp3" % d

    print s
    err = os.system(s)

    if err!=0:
      print "Step 0 failed. aborting."

  else:
    d['snd'] = "-nosound"

  



  # convert to 30fps
  s = "mencoder -really-quiet %(startpos)s %(endpos)s -lavdopts threads=4 %(f)s -ovc raw  -vf scale,format=i420,harddup  -ofps 30 -nosound -of rawvideo -o - | x264 --crf 18 --partitions none --me dia --merange 4 --mvrange 64 --subme 0 --no-chroma-me --aq-mode 0 --threads auto --no-cabac --no-deblock  --fps 30 --output %(f)s_30fps.avi - %(w)dx%(h)d" % d

  print s
  err = os.system(s)
  

  if err!=0:
    print "Step 0 failed. aborting."

  # encode for pygame

  s = "mencoder  %(f)s_30fps.avi -vf scale=%(out_w)d:%(out_h)d%(crop)s -of mpeg -mpegopts format=mpeg1:tsaf:muxrate=2000 -o %(outname)s -srate 44100 -af lavcresample=44100 %(snd)s -ovc lavc -lavcopts vcodec=mpeg1video:vbitrate=1152:keyint=15:mbd=2" % d

  print s
  err = os.system(s)

  if err!=0:
    print "Step 0 failed. aborting."
  else:
    print "Success -> pygame_%s_30fps.avi" % (filename)



options = 'o:w:h:s:e:'
long_options = 'crop='


if __name__=='__main__':

  try:
    filename = sys.argv[1]
    opts,args = getopt.gnu_getopt(sys.argv[2:],options,long_options)
    o = dict(opts)
    print o
    
  except IndexError:
    print "usage: to_pygame_movie.py infile [-o oufile -w width -h height -crop=w:h:x:y]"
    sys.exit(1)


  to_pygame_movie(filename,o.get('-o'),o.get('-w'),o.get('-h'),o.get('--crop'),o.get('-s'),o.get('-e'))
