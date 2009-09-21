
# export PYTHONPATH=$PYTHONPATH:$HOME/theway/project/slithy

from slithy.presentation import *
#from slithy.library import test_objects

# new slide reader
import slithy.slidereader as slidereader
from slithy.slidereader import load_env, include_slides

# load the image and font environments
load_env('globals.yaml')


# the sections of the talk using old style

import movie_test
import title
import neo
import overview
import end_movie
import awesome


bookmark( 'title' )
play( title.title2_anim )
pause()
bookmark( 'something completely different' )
play( movie_test.title1_anim )

pause()
bookmark( 'overview' )
play( overview.overview_anim )

bookmark( 'neo' )
pause()
play( neo.neo_overview_anim )

bookmark( 'PIN SI' )
pause()
play( neo.pin_overview_anim )

bookmark( 'pause' )
pause()
play( neo.prebrainon_anim )


bookmark( 'Brain on ...' )
pause()
play( movie_test.brainon_anim )

bookmark( 'Mozaik Overview' )
pause()
play( neo.mozaik_overview_anim )


bookmark( 'Mozaik def' )
pause()
play( neo.mozaik_def_anim )

bookmark( 'Unit 1' )
pause()
play( neo.quiz_anim )

pause()
include_slides('thankyou.yaml')

pause()
bookmark( 'mid-overview' )
play( overview.mid_overview_anim )

pause()
include_slides('content.yaml')

bookmark( 'awesome' )
play( awesome.awesome_anim )
pause()


bookmark( 'end' )
#pause()
play( end_movie.end_anim )




#bookmark('pyramid')
#play(pyramid.collab_anim)
#pause()
#bookmark('What next')
#play(pyramid.what_next_anim)
#pause()
#bookmark('example')
#play(example.slide1_anim)
#pause()
#play(example.slide2_anim)

#pause()

#bookmark("let's do it")
#play(plan.plan_anim)
#pause()
#bookmark( 'part1' )
#play( part1.bullets1 )

#pause()
#bookmark('q1')
#play( q1.q1_anim )

# KDE handles full-screen stuff
# (window decorator right click "Configure Window Behaviour")

run_presentation()


