
# export PYTHONPATH=$PYTHONPATH:$HOME/theway/project/slithy

from slithy.presentation import *
#from slithy.library import test_objects

import title
import part1
import pyramid
import plan

import example

import q1


bookmark( 'title' )
play( title.title1_anim )
pause()
bookmark('pyramid')
play(pyramid.collab_anim)
pause()
bookmark('What next')
play(pyramid.what_next_anim)
pause()
bookmark('example')
play(example.slide1_anim)
pause()
play(example.slide2_anim)

pause()

bookmark("let's do it")
play(plan.plan_anim)
pause()
#bookmark( 'part1' )
#play( part1.bullets1 )

pause()
bookmark('q1')
play( q1.q1_anim )

# KDE handles full-screen stuff
# (window decorator right click "Configure Window Behaviour")

run_presentation()


