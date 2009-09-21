from slithy.library import *
from slithy.util import *
import math
from macros import *
from fonts import fonts, images
import common
import p2
import pointy

flyfont = fonts['bold']

s = 'meaningless animation'
#s = 'this is a test'
space = text( 0,0, '_', flyfont, nodraw=1 )['width'] * 0.5
nopos = 0
contentpos = [0]
for c in s:
    if c is ' ':
        c = '-'
    d = text( contentpos[-1],0, c, flyfont, anchor = 'fw', nodraw = 1 )['right'] + space * 0.3
    contentpos.append( d )

def flying_text( x = (SCALAR, 0, 1) ):
    set_camera( Rect( -3, -3, contentpos[-1]+3, 5 ) )

    for letter, pos, frac in zip(s, contentpos, split_sequence_smooth( len(s), x, 0.9 ) ):
        frac = 1.0 - frac
        x = 3 * frac * math.cos( frac * 3 * math.pi )
        y = 3 * frac * math.sin( frac * 3 * math.pi )
        color( white, 1.0-frac )
        text( pos+x,y, letter, flyfont, anchor = 'fw' )


    
    

def powerpoint():
    r = get_camera().top( 0.2 ).bottom( 0.85 ).inset( 0.05 )
    title = Text( r, text = 'Our goal', font = fonts['title'], size = 30, justify = 0.0,
                  color = yellow )
    r = get_camera().bottom( 0.85 ).inset( 0.05 )
    bl = BulletedList( r, font = fonts['roman'], color = white,
                       bullet = [fonts['dingbats'], 'w'],
                       size = 22 )
    d = Drawable( get_camera().inset( 0.0 ).move_down( 0.15 ), flying_text )
    im = Image( get_camera().bottom( 0.4 ).inset( 0.05 ).move_up( 0.2 ), image = images['proj'], _alpha = 0 )
    pt = Interactive( get_camera(), controller = pointy.Pointy )


    start_animation( common.bg, title, bl, pt )

    pause()
    bl.add_item( 0, 'make better presentations' )
    
    pause()
    bl.add_item( 0, 'take advantage of electronic projection' )
    enter( im )
    set( im._alpha, 1 )
    #fade_in( 0.5, im )

    pause()
    #fade_out( 0.5, im )
    set( im._alpha, 0 )
    exit( im )
    enter( d )
    linear( 5.0, d.x, 1.0 )
    
#     pause()
#     exit( d )

#     enter( d3a )
#     enter( d3b )
#     enter( d3c )
#     enter( d3d )

#     pause()

#     exit( d3a )
#     exit( d3b )
#     exit( d3c )
#     exit( d3d )

#     enter( d2 )
#     set( d2.textlabel, 1 )
#     set( d2.subdivide, 0.8 )
#     set( d2.linealpha, 1 )
#     set( d2.lineextend, 1 )

#     pause()
#     set( d2.slidea, 1 )
#     pause()
#     set( d2.slidea, 2 )
#     pause()
#     set( d2.slidea, 3 )
    
#     pause()
#     exit( d2 )
#     pause()
#     set( d2._alpha, 0.0 )
#     set( d2.slidea, 0 )
#     enter( d2 )
#     fade_in( 0.5, d2 )

#     smooth( 1.0, d2.slidea, 1 )
#     smooth( 1.0, d2.slidea, 2 )
#     smooth( 1.0, d2.slidea, 3 )
#     smooth( 0.6, d2.slideb, 1 )
#     smooth( 0.6, d2.slideb, 2 )
#     smooth( 0.6, d2.slideb, 3 )

#     pause()
    
#     fade_out( 0.5, d2, title, bl )

    return end_animation()
powerpoint = powerpoint()

def pythagorases():
    r = get_camera().inset( 0.03 ).restrict_aspect( 2 ).left( 0.25 ).top( 0.5 )

    ds = []
    for i in range(8):
        x = i % 4
        y = i / 4
        d = Drawable( r.move_right( x ).move_down( y ), p2.pythagoras,
                      textlabel=1, subdivide=0.8, linealpha=1, lineextend=1 )
        ds.append( d )

    start_animation( *([common.bg] + ds) )

    set( ds[0].subdivide, 0 )
    set( ds[2].slidea, 1 )
    set( ds[3].slidea, 2 )
    set( ds[4].slidea, 3 )
    set( ds[5].slidea, 3 )
    set( ds[6].slidea, 3 )
    set( ds[7].slidea, 3 )
    set( ds[5].slideb, 1 )
    set( ds[6].slideb, 2 )
    set( ds[7].slideb, 3 )

    pause()

    exit( *ds )
    d = Drawable( get_camera().inset( 0.03 ).restrict_aspect( 1 ),
                  p2.pythagoras, textlabel=1, subdivide=0, linealpha=1, lineextend=1 )
    enter( d )

    pause()
    set( d.subdivide, 0.8 )
    pause()
    set( d.slidea, 1 )
    pause()
    set( d.slidea, 2 )
    pause()
    set( d.slidea, 3 )
    pause()
    set( d.slideb, 1 )
    pause()
    set( d.slideb, 2 )
    pause()
    set( d.slideb, 3 )

    pause()
    set( d._alpha, 0 )
    set( d.subdivide, 0.0 )
    set( d.slidea, 0 )
    set( d.slideb, 0 )
    pause()

    exit( d )
    i = Interactive( get_camera().inset( 0.03 ).restrict_aspect( 1 ),
                     controller = p2.PythagorasDemo, _alpha = 0.0 )
    enter( i )

    fade_in( 0.5, i )
    
    pause()

    fade_out( 0.5, i )
    

    return end_animation()
pythagorases = pythagorases()
        
def title():
    title = Text( get_camera().top(0.6).inset( 0.2 ), text = 'On Creating Animated Presentations',
                  color = yellow, size = 34, font = fonts['bold'], _alpha = 1,
                  justify = 0.5, vjustify = 0.5 )
    authors = Text( get_camera().bottom(0.5).left(0.5).inset( 0.2 ).move_left( 10, abs = 1 ), text = 'Doug Zongker\nDavid Salesin',
                  color = white, size = 18, font = fonts['roman'], _alpha = 1,
                  justify = 0.5, vjustify = 0.5 )
    affil = Text( get_camera().bottom(0.5).right(0.85).inset( 0.2 ).move_right(40, abs = 1), text = 'University of Washington\nMicrosoft Research',
                  color = white, size = 18, font = fonts['roman'], _alpha = 1,
                  justify = 0.5, vjustify = 0.5 )

    start_animation( common.bg, title, authors, affil )
 
    return end_animation()
title = title()
    

test_objects( title, powerpoint, pythagorases, flying_text, clear_color = black )
