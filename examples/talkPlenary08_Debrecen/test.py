

from slithy.library import *

from slithy.util import *


def my_square():

    set_camera(Rect(0,0,1,1))

    color(green,0.5)
    rectangle(0,0,1,1)
    

cameras = (
    Rect(0,0,1,1),
    Rect(-0.25,0.25,0.25,0.75),
    Rect(-5,-5,5,5)

    )


def my_diag( cam = (SCALAR,0,2), s1 = (SCALAR,0,1), s2 = (SCALAR,0,1)):

    set_camera( interp_cameralist( cam, cameras ) )

    color(blue,s1)

    rectangle(0,0,1,1)


    color(red,s2)

    rectangle(Rect(-20.0,0.25,20.0,0.75))


    color(green,s2)

    rectangle(get_camera().inset(0.1))
    



def animation():

    c = Rect(0,0,1000,1000)
    bg = Fill( style = 'horz', color = black, color2 = Color(0.5) )
    start_animation( bg )

    


    dv1 = viewport.interp( Rect(50,50,100,100),Rect(0.0,50,50,100),Rect(0.0,0.0,50,50) ) 
    dv = viewport.interp( get_camera().inset(0.1), get_camera().inset(0.2), get_camera().inset(0.3) )


    d = Drawable( dv, my_diag, cam=0.0,s1 = 1.0,s2=1.0,_alpha = 0.0)
    d2 = Drawable( dv1, my_diag, cam=0.0,s1 = 1.0,s2=1.0,_alpha = 0.0)
    #d = Drawable( get_camera().inset(0.1), my_diag, cam=0.0,s1 = 1.0,s2=1.0,_alpha = 0.0)

    d1 = Drawable( get_camera(), my_square, _alpha = 0.0)

    enter(d1)
    enter(d)
    enter(d2)

    fade_in(1.0,d)
    fade_in(1.0,d1)
    fade_in(1.0,d2)
    r = get_camera()
    get_camera_object().view(c,1.0)
    get_camera_object().view(r,1.0)

    pause()

    #smooth(2.0,d._alpha,0.2)
    parallel()
    smooth(2.0,dv.x,1.0)
    smooth(2.0,dv1.x,1.0)
    end()

    pause()

    lift(d1)

    parallel()
    smooth(2.0,dv.x,2.0)
    smooth(2.0,dv1.x,2.0)
    smooth(2.0,d2.cam,2.0)
    smooth(2.0,d.cam,2.0)

    end()

    return end_animation()

animation = animation()


test_objects(animation, my_diag,my_square)
