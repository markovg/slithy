from slithy.library import *

import slithy.movie as movie

#from fonts import fonts
#from images import images

import slithy.slidereader as slidereader
images = slidereader.image_library['default']
fonts = slidereader.font_library['default']


import common


def end_anim():

    d = movie.Movie( get_camera().inset(0.1), './movies/fishdance_postgrey.mpg',loop=True)

    cap = Text( get_camera().inset(0.1).move_down(0.05),
                color = white, font = fonts['times'], size = 30, _alpha = 0.0,
                justify = 0.5 )


    cap1 = Text( get_camera(),
                color = white, font = fonts['times'], size = 30,
                justify = 0.5 )


    #im = Image( get_camera().bottom( 0.6 ).inset( 0.05 ).move_up( 0.2 ), image = images['neo'], _alpha = 0 )
    im = Image( get_camera().bottom( 0.7 ).inset( 0.05 ), image = images['neo'], _alpha = 0 )

    
    start_animation( common.bg,d,cap1,cap,im)


    set( cap.text, 'And now for something\ncompletely\ndifferent ...' )

    set( cap1.text, 'Thank you for your interest ...' )
    
    #fade_in( 2.0, d )

    wait(13.0)

    #fade_out(1.5,d)
    wait(-1.0)
    fade_in(2.0,cap)
    wait(-1.5)
    fade_out(1.0,cap1)

    wait(1.0)

    fade_in(5.0,im)



    #pause()


    return end_animation() 

end_anim = end_anim()


test_objects( end_anim )
