from slithy.library import *
from slithy.util import *

import facets

from fonts import fonts
import common

from images import images


flyfont = fonts['mono']
s = 'Python'
#s = 'this is a test'
space = text( 0,0, '_', flyfont, nodraw=1 )['width'] * 0.5
nopos = 0
contentpos = [0]
for c in s:
    if c is ' ':
        c = '-'
    d = text( contentpos[-1],0, c, flyfont, anchor = 'fw', nodraw = 1 )['right'] + space * 0.3

    contentpos.append( d )


def python_logo():

    set_camera(Rect(0,0,1,1))

    image(0,0, images['python-logo'],width=1.0,anchor='sw')



def flying_text( x = (SCALAR, 0, 1) ):
    set_camera( Rect( -3, -3, contentpos[-1]+3, 5 ).move_up(0.2).inset(0.1) )

    for letter, pos, frac in zip(s, contentpos, split_sequence_smooth( len(s), x, 0.9 ) ):
        frac = 1.0 - frac
        x = 3 * frac * math.cos( frac * 3 * math.pi )
        y = 3 * frac * math.sin( frac * 3 * math.pi )
        color( white, 1.0-frac )
        if letter is 'o':
            color(1.0-frac)
            d = text( pos+x,y, letter, flyfont, anchor = 'fw',nodraw=1)
            embed_object(Rect(d['left'],d['bottom'],d['right'],d['top']), python_logo,{},_alpha = 1.0-frac)
        elif letter is '@':
            text( pos+x,y, 'w', fonts['dingbats'], anchor = 'fw')
        else:
            text( pos+x,y, letter, flyfont, anchor = 'fw' )




def q1_anim():

    

    d = Drawable( get_camera(), flying_text, x= 0.0 )

    start_animation(common.bg, d)

    pause()


    bl = BulletedList( get_camera().inset(0.1),
                       font = fonts['times'], color = white,
                       bullet = [fonts['dingbats'], ' '], size = 18 )

    enter(bl)

    bl.add_item( 0, 'a) Powerpoint 2008 Vista Beta Genuine Open Advantage' )

    pause()

    bl.add_item( 0, 'b) Sub-contracted to a professional' )

    pause()

    bl.add_item( 0, 'c) Quantum leap in presentation complexity' )

    pause()

    linear(2.0,d.x,1.0)


    return end_animation()

q1_anim = q1_anim()


test_objects(q1_anim)
    
    
