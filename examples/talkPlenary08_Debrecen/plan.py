from slithy.library import *

import facets

from fonts import fonts
import common

from images import images




def plan_anim():

    cap = Text( get_camera().top(0.2).inset(0.1),
                color = yellow, font = fonts['times'], size = 22, _alpha = 1.0,
                justify = 0.5, text="Let's do it!" )


    start_animation( common.bg,cap)


    pause()

    bl = BulletedList( get_camera().bottom(0.8).inset(0.1),
                       font = fonts['times'], color = white,
                       bullet = [fonts['dingbats'], 'w'], size = 18 )

    enter(bl)
    bl.add_item( 0, 'Setup a central code repository for the common FACETS model -> http://neuralensemble.org' )

    pause()

    bl.add_item( 0, 'Collect (unit) tests & low-level benchmarks, which are run weekly/for-each-commit' )


    bl.add_item( 0, '...' )



    

    return end_animation()

plan_anim = plan_anim()


test_objects(plan_anim)
