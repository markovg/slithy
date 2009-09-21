
# export PYTHONPATH=$PYTHONPATH:$HOME/theway/project/slithy

from slithy.presentation import *
#from slithy.library import test_objects

# new slide reader
import slithy.slidereader as slidereader
from slithy.slidereader import load_env, include_slides

# load the image and font environments
load_env('globals.yaml')


# the sections of the talk using old style

import title


bookmark( 'title' )
play( title.title2_anim )
pause()

include_slides('content.yaml')

#bookmark( 'something completely different' )
#play( movie_test.title1_anim )

#pause()
#bookmark( 'overview' )
#play( overview.overview_anim )


run_presentation()


