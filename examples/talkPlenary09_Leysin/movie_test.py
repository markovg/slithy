from slithy.library import *

import slithy.movie as movie

#from fonts import fonts
#from images import images

import slithy.slidereader as slidereader
images = slidereader.image_library['default']
fonts = slidereader.font_library['default']


import common




cameras = (
  Rect(0,0,1,1),
  Rect(-0.6,0,2.35,1),
  )


def parameterized_title( x = (SCALAR, 0, 1), cursor=(SCALAR,0,1) ):

    str = u"Computational Paradigms\nCollaborative Effort Kick-off"

    disp_str = str[0:int(len(str)*x)]

    if cursor<0.5 or len(disp_str)<len(str):
        cursor_str = '_'
    else:
        cursor_str = ' '
    

    #set_camera(Rect(0,0,10,10))

    r = Rect( -1,-0.5,1,0.8 )

    set_camera( r )

    thickness( 0.01 )

    color(blue,0.2)

    rectangle(r.bottom(0.5).top(0.9))

    color(red,0.9)
    
    if disp_str:
        d = text( -0.9, 0.0, disp_str+cursor_str, font = fonts['mono'], size = 0.10, anchor = 'nw', justify = 0.0 )

    #frame( d['left'], d['bottom'], d['right'], d['top'] ) 
    



def title1_anim():

    d = movie.Movie( get_camera().inset(0.1), './movies/something.mpg')

    cap = Text( get_camera().inset(0.05),
                color = white, font = fonts['times'], size = 30, _alpha = 0.0,
                justify = 0.5 )

    #im = Image( get_camera().bottom( 0.6 ).inset( 0.05 ).move_up( 0.2 ), image = images['neo'], _alpha = 0 )
    im = Image( get_camera().bottom( 0.7 ).inset( 0.05 ), image = images['neo'], _alpha = 0 )

    
    start_animation( common.bg,d,cap,im)


    set( cap.text, 'And now for something\ncompletely\ndifferent ...' )
    
    #fade_in( 2.0, d )

    wait(37.0)

    #fade_out(1.5,d)
    wait(-1.0)
    fade_in(2.0,cap)
    
    wait(1.0)

    fade_in(5.0,im)



    #pause()


    return end_animation() 

title1_anim = title1_anim()



def brainon_anim():

    d = movie.Movie( get_camera().inset(0.1), './movies/brainon.mpg')

    cap = Text( get_camera().inset(0.05),
                color = white, font = fonts['times'], size = 30, _alpha = 0.0,
                justify = 0.5 )

    #im = Image( get_camera().bottom( 0.6 ).inset( 0.05 ).move_up( 0.2 ), image = images['neo'], _alpha = 0 )
    im = Image( get_camera().bottom( 0.7 ).inset( 0.05 ), image = images['neo'], _alpha = 0 )

    start_animation(common.bg,d)

    #pause()


    return end_animation() 

brainon_anim = brainon_anim()



test_objects( parameterized_title, title1_anim )
