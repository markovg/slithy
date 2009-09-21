from slithy.library import *
from fonts import fonts, images
import math

imagepath.append( 'images' )


def sliding_square( stretch = (SCALAR, -1, 1, 0),
                    c = (COLOR, red),
                    x = (SCALAR, 0, 1, 0),
                    hi = (SCALAR, 0, 1, 0),
                    label = (SCALAR, 0, 1, 0),
                    ):
    color( c )
    set_camera( Rect(0, 0, 5, 1).outset( 0.75, abs = 1 ) )
    translate( x * 4, 0 )

    push()
    translate( 0.5, 0.5 )
    scale( 2 ** stretch, 2 ** -stretch )
    translate( -0.5, -0.5 )
    
    rectangle( 0, 0, 1, 1 )

    if hi > 0.0:
        color( black, hi )
        thickness( 0.1 )
        circle( 0.9, 0.5, 0.5 )
    pop()

    if label > 0.0:
        color( black, label )
        text( 0.5, 0.5, 'staging', fonts['bold'], size = 0.4, anchor = 'c' )

def simple_motion():
    bg = Fill( color = Color(0.9) )
    start_animation( bg, camera = Rect(0, 0, 150, 100) )
    dt = Drawable( get_camera().top(0.5), sliding_square )
    db = Drawable( get_camera().bottom(0.5), sliding_square, c = blue )
    enter( dt, db )

    parallel()
    smooth( 0.45, dt.x, -0.2 )
    smooth( 0.45, dt.stretch, -0.8 )
    end()
    wait( 0.15 )
    parallel()
    linear( 0.2, dt.x, 1.1 )
    sequence()
    smooth( 0.125, dt.stretch, 0.5 )
    wait( 0.0625 )
    smooth( 0.0625, dt.stretch, -0.5 )
    end()
    end()

    parallel()
    sequence()
    smooth( 0.1, dt.x, 0.9 )
    smooth( 0.1, dt.x, 1.05 )
    smooth( 0.1, dt.x, 0.95 )
    smooth( 0.1, dt.x, 1.025 )
    smooth( 0.1, dt.x, 0.975 )
    smooth( 0.1, dt.x, 1.0125 )
    smooth( 0.1, dt.x, 1 )
    end()
    sequence()
    smooth( 0.15, dt.stretch, 0.1 )
    smooth( 0.15, dt.stretch, 0.0 )
    end()
    end()
    

    pause()

    # slide the blue square over
    smooth( 1.55, db.x, 1.0 )
    pause()

    # reset diagram
    fade_out( 0.3, db, dt )
    set( db.x, 0.0 )
    set( dt.x, 0.0 )
    fade_in( 0.3, db, dt )
    pause()
    
    parallel()
    smooth( 0.45, dt.x, -0.2 )
    smooth( 0.45, dt.stretch, -0.8 )
    end()

    pause()
    smooth( 0.5, dt.label, 1.0 )
    pause()
    smooth( 0.5, dt.label, 0.0 )
    wait( 0.25 )

    parallel()
    linear( 0.2, dt.x, 1.1 )
    sequence()
    smooth( 0.125, dt.stretch, 0.5 )
    wait( 0.0625 )
    smooth( 0.0625, dt.stretch, -0.5 )
    end()
    end()

    parallel()
    sequence()
    smooth( 0.1, dt.x, 0.9 )
    smooth( 0.1, dt.x, 1.05 )
    smooth( 0.1, dt.x, 0.95 )
    smooth( 0.1, dt.x, 1.025 )
    smooth( 0.1, dt.x, 0.975 )
    smooth( 0.1, dt.x, 1.0125 )
    smooth( 0.1, dt.x, 1 )
    end()
    sequence()
    smooth( 0.15, dt.stretch, 0.1 )
    smooth( 0.15, dt.stretch, 0.0 )
    end()
    end()

    pause()

    smooth( 0.5, db.c, orange )
    pause()

    smooth( 0.5, db.hi, 1.0 )
    pause()

    parallel()
    smooth( 0.5, db.c, blue )
    smooth( 0.5, db.hi, 0.0 )
    end()

    pause()

    smooth( 1.0, db.x, 1.0 )

    return end_animation()
simple_motion = simple_motion()

def square_tiling( x = (SCALAR, 0, 1) ):
    set_camera( Rect(-0.2, -0.2, 5.2, 5.2 ) )

    x /= 2
    tile = Path().moveto(0,0)
    tile.lineto(x,0).lineto(0.5,-x).lineto(1-x,0).lineto(1,0)
    tile.lineto(1,x).lineto(1-x,0.5).lineto(1,1-x).lineto(1,1)
    tile.lineto(1-x,1).lineto(0.5,1+x).lineto(x,1).lineto(0,1)
    tile.lineto(0,1-x).lineto(x,0.5).lineto(0,x).closepath()

    for i in range(-1,7):
        for j in range(-1,7):
            if (i+j) % 2:
                push()
                translate( i, j )
                color( green )
                fill( tile )
                pop()


hyp = [(0, 0, 1),
       (1, 0.1947060, 0.7288162),
       (2, 0.3670319, 0.7704121),
       (3, 0.4977620, 0.6812780),
       (8, 0.3714308, 0.4141071),
       (7, 0.2584504, 0.5655194),
       (6, 0.3684982, 0.6516438),
       (4, 0.4374904, 0.5632814),
       (5, 0.3695786, 0.5641303),
       ]

side = [(0, 0, 0),
        (8, 0.6797345, -0.05849668),
        (7, 0.5486186,  0.06189227),
        (6, 0.3317642,  0.12710295),
        (5, 0.1849051,  0.02268869),
        (1, 0.1872203, -0.16484025),
        (2, 0.4146473, -0.08643309),
        (4, 0.2536657, -0.04692082),
        (3, 0.3331533,  0.01458558),
        ]

def escher( h = (SCALAR, 0, 1, 0),
            s = (SCALAR, 0, 1, 0),
            im = (SCALAR, 0, 1, 0),
            sp = (SCALAR, 0, 1, 0),
            show_hyp = (SCALAR, 0, 1),
            rotate_hyp = (SCALAR, 0, 1),
            show_leg = (SCALAR, 0, 1),
            rotate_leg = (SCALAR, 0, 1),
#              x = (SCALAR, -2, 2, 0),
#              y = (SCALAR, -2, 2, 0),
#              w = (SCALAR, 3, 7, 5)
            ):
    set_camera( Rect( -1.5, -1.6, 2.2, 2.1 ) )

    #if im > 0:
    #    image( 0.428, 0.120, images['escher'], width = 4.168, anchor = 'c' )

    clear( linen, 1.0-im )
    
    tile = Path()
    phyp = Path()
    pleg = Path()

    ##
    ## hypotenuse
    ##
    
    tile.moveto( 0, 1 )

    h *= 8
    all = hyp[1:int(h)+1]
    if h < 8:
        frac = h - int(h)
        i = int(h)
        k = hyp[i+1][0]
        all.append( (k,
                     hyp[i][1] * (1.0-frac) + hyp[i+1][1] * frac,
                     hyp[i][2] * (1.0-frac) + hyp[i+1][2] * frac) )
                     
    all.sort()

    phyp.moveto( 0, 1 )
    for n, x, y in all:
        tile.lineto( x, y )
        phyp.lineto( x, y )
    all.reverse()
    for n, x, y in all:
        tile.lineto( 1-x, 1-y )
        phyp.lineto( 1-x, 1-y )
    tile.lineto( 1, 0 )
    phyp.lineto( 1, 0 )

    ##
    ## sides
    ##

    s *= 8
    all = side[1:int(s)+1]
    if s < 8:
        frac = s - int(s)
        i = int(s)
        k = side[i+1][0]
        all.append( (k,
                     side[i][1] * (1.0-frac) + side[i+1][1] * frac,
                     side[i][2] * (1.0-frac) + side[i+1][2] * frac) )

    
    all.sort()
    all.reverse()
    pleg.moveto( 1, 0 )
    for n, x, y in all:
        tile.lineto( x, y )
        pleg.lineto( x, y )
    tile.lineto( 0, 0 )
    pleg.lineto( 0, 0 )
    all.reverse()
    for n, x, y, in all:
        tile.lineto( -y, x )
        
    tile.closepath()

    tilecolor = Color(0.0, 0.5, 0.2)

    color( tilecolor, 1.0 - im )
    for i in range(-2,3):
        for j in range(-2,3):
            push()
            translate( i, j )
            if i%2:
                if j%2:
                    translate( 0.5, 0.5 )
                    rotate( 180 )
                    translate( -0.5, -0.5 )
                else:
                    translate( 0.5, 0.5 )
                    rotate( -90 )
                    translate( -0.5, -0.5 )
            else:
                if j%2:
                    translate( 0.5, 0.5 )
                    rotate( 90 )
                    translate( -0.5, -0.5 )
                else:
                    pass

            if i == 0 and j == 0 and sp > 0:
                color( tilecolor.interp(red,sp), 1.0 - im )
                
            fill( tile )
            pop()

    if show_hyp > 0.0:
        color( black, show_hyp )
        push()
        rotate( rotate_hyp * 180, 0.5, 0.5 )
        widestroke( phyp, 0.03 )
        pop()

    if show_leg > 0.0:
        color( black, show_leg )
        push()
        rotate( rotate_leg * 90 )
        widestroke( pleg, 0.03 )
        pop()

def smooth_transitions():
    start_animation()
    d = Drawable( get_camera().inset( 0.05 ).restrict_aspect(1), escher )
    enter( Fill(color=white), d )

    pause()
    smooth( 1.0, d.sp, 1.0 )
    pause()
    smooth( 2.0, d.h, .368 )
    pause()
    smooth( 2.0, d.s, 0.25 )
    pause()
    smooth( 2.0, d.h, 1.0 )
    pause()
    smooth( 2.0, d.s, 1.0 )
    pause()
    
    smooth( 0.5, d.show_hyp, 1.0 )
    pause()
    #smooth( 1.0, d.rotate_hyp, 1.0 )

    smooth( 1.0, d.rotate_hyp, 1 )
    
    pause()
    parallel()
    smooth( 0.5, d.show_hyp, 0.0 )
    smooth( 0.5, d.show_leg, 1.0 )
    end()
    pause()
    smooth( 1.0, d.rotate_leg, 1.0 )
    pause()
    smooth( 0.5, d.show_leg, 0.0 )
    
    #pause()
    #smooth( 4.0, d.im, 1.0 )
    
    return end_animation()
smooth_transitions = smooth_transitions()
escher_one = smooth_transitions[0].anim


    
test_objects( smooth_transitions )
#test_objects( structure_transitions, simple_motion, sliding_square )
 
    
    
    
