from slithy.library import *
from slithy.util import *

import slithy.movie as movie

#from fonts import fonts
#from images import images

import slithy.slidereader as slidereader
images = slidereader.image_library['default']
fonts = slidereader.font_library['default']


import common

def fullmonty_diag(full_alpha = ('scalar',0.0,1.0),monty_alpha = ('scalar',0.0,1.0),x=('scalar',0.0,1.0)):

    #set_camera(Rect(0,0,1024.0,768.0))

    cam = Rect(0.0,0.0,1.0,0.0,get_camera().aspect())
    set_camera(cam)
    #im = Image( dv, image = images['fullin'],_alpha=0, fit=STRETCH)
    #im1 = Image( dv, image = images['montypython'],_alpha=1, fit=STRETCH)

    #cam = get_camera()
    width = cam.width()
    height = cam.height()
    #image(cam[0],cam[1],images['montypython'],width=width,height=height,anchor='sw',alpha=monty_alpha)
    #image(cam[0],cam[1],images['fullin'],width=width,height=height,anchor='sw',alpha=full_alpha)

    image(cam[0],cam[1]+height*(1.0-x),images['montypython'],width=width,height=height*x,anchor='sw',alpha=monty_alpha,stretch=True)
    image(cam[0],cam[1]+height*(1.0-x),images['fullin'],width=width,height=height*x,anchor='sw',alpha=full_alpha,stretch=True)
    
    

    #image(0.0,1.0-x,images['montypython'],width=1.0,height=x,anchor='sw',alpha=monty_alpha,stretch=1)
    #image(0.0,1.0-x,images['fullin'],width=1.0,height=x,anchor='sw',alpha=full_alpha,stretch=1)

def overview_anim():

    #r = get_camera()
    
    #set_camera(r)

    #dv = viewport.interp(get_camera(),get_camera().top(0.5))

    #m = movie.Movie( get_camera().top(0.5), './movies/fullmonty.mpg',loop=True)

    #im = Image( dv, image = images['fullin'],_alpha=0, fit=STRETCH)
    #im1 = Image( dv, image = images['montypython'],_alpha=1, fit=STRETCH)

    im = Drawable(get_camera(), fullmonty_diag, full_alpha=0.0,monty_alpha=1.0,_alpha = 1.0,x=1.0)


    m2 = movie.Movie( get_camera().bottom(0.5), './movies/stomp.mpg', loop=True)
    #im2 = Image( get_camera().bottom(0.5), image = images['fullin'])

    start_animation(m2,im)
    #set(dv.x,0.0)

    #fade_in( 1.0, im )
    linear(1.0,im.monty_alpha,1.0)

    pause()

    #fade_in( 1.5, im )
    linear(1.0,im.full_alpha,1.0)

    pause()

    #smooth(1.5,dv.x,1.0)
    smooth(1.5,im.x,0.5)

    wait(-1.5)
    fade_in( 1.5, m2 )


    #get_camera_object().view(get_camera(),1.0)

    #pause()


    return end_animation() 

overview_anim = overview_anim()


def mid_overview_anim():

    #r = get_camera()
    
    #set_camera(r)

    #dv = viewport.interp(get_camera(),get_camera().top(0.5))

    #m = movie.Movie( get_camera().top(0.5), './movies/fullmonty.mpg',loop=True)

    #im = Image( dv, image = images['fullin'],_alpha=0, fit=STRETCH)
    #im1 = Image( dv, image = images['montypython'],_alpha=1, fit=STRETCH)

    im = Drawable(get_camera(), fullmonty_diag, full_alpha=1.0,monty_alpha=1.0,_alpha = 1.0,x=0.5)


    m2 = movie.Movie( get_camera().bottom(0.5), './movies/stomp.mpg', loop=True)
    #im2 = Image( get_camera().bottom(0.5), image = images['fullin'])

    start_animation(m2,im)


    return end_animation() 

mid_overview_anim = mid_overview_anim()





test_objects( overview_anim )
