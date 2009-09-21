from slithy.library import *

from fonts import fonts

import common

def bullets1():
    r = get_camera().top( 0.2 ).bottom( 0.85 ).inset( 0.05 )
    title = Text( r, text = 'Our goal', font = fonts['title'], size = 30, justify = 0.0,
                  color = yellow )
    r = get_camera().bottom( 0.85 ).inset( 0.05 )
    bl = BulletedList( r, font = fonts['roman'], color = white,
                       bullet = [fonts['dingbats'], 'w'],
                       size = 22 )
    #d = Drawable( get_camera().inset( 0.0 ).move_down( 0.15 ), flying_text )
    #im = Image( get_camera().bottom( 0.4 ).inset( 0.05 ).move_up( 0.2 ), image = images['proj'], _alpha = 0 )
    #pt = Interactive( get_camera(), controller = pointy.Pointy )


    start_animation( common.bg, title, bl)

    pause()
    bl.add_item( 0, 'make better presentations' )
    
    pause()
    bl.add_item( 0, 'take advantage of electronic projection' )

    pause()

    r = get_camera().outset(0.5).bottom(0.2).left(0.2)

    get_camera_object().view(r,1.0)

    


    return end_animation()


bullets1 = bullets1()
