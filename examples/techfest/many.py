from slithy.library import *
import common
from fonts import fonts, images
from chart import chart_one
from escher import escher_one
from pythagoras import pythagoras_one
from simple import slideshow_one
from linechart import linechart_one
from overview import overview_one
from bullet import infinite_one, sort_one
from eclipse import eclipse_one
#from morehint import hinting_one

an1 = scale_length( pythagoras_one, 16.0 )
an2 = scale_length( chart_one, 14.0 )
an3 = scale_length( escher_one, 12.0 )
an4 = scale_length( slideshow_one, 10.0 )

tt1 = scale_length( pythagoras_one, 12.0 )
tt2 = scale_length( chart_one, 12.0 )
tt3 = scale_length( escher_one, 12.0 )
tt4 = scale_length( slideshow_one, 12.0 )
tt5 = scale_length( linechart_one, 12.0 )
tt6 = scale_length( overview_one, 12.0 )
tt7 = scale_length( infinite_one, 12.0 )
tt8 = scale_length( sort_one, 12.0 )
tt9 = scale_length( eclipse_one, 12.0 )
#an10 = scale_length( hinting_one, 10.0 )


def two_by_two():
    a1 = Anim( get_camera().left( 0.5 ).top( 0.5 ).inset( 0.05 ).move_right( 0.03 ).move_down( 0.03 ) )
    a2 = Anim( get_camera().right( 0.5 ).top( 0.5 ).inset( 0.05 ).move_left( 0.03 ).move_down( 0.03 ) )
    a4 = Anim( get_camera().left( 0.5 ).bottom( 0.5 ).inset( 0.05 ).move_right( 0.03 ).move_up( 0.03 ) )
    a3 = Anim( get_camera().right( 0.5 ).bottom( 0.5 ).inset( 0.05 ).move_left( 0.03 ).move_up( 0.03 ) )

    start_animation( common.bg, a1, a2, a3, a4 )

    parallel()

    serial()
    a1.fade_in_start( an1, 0.5 )
    a1.play( an1 )
    end()
    
    serial( 2.0 )
    a2.fade_in_start( an2, 0.5 )
    a2.play( an2 )
    end()
    
    serial( 4.0 )
    a3.fade_in_start( an3, 0.5 )
    a3.play( an3 )
    end()

    serial( 6.0 )
    a4.fade_in_start( an4, 0.5 )
    a4.play( an4 )
    end()

    end()

    pause()

    fade_out( 0.5, a1, a2, a3, a4 )

    return end_animation()
two_by_two = two_by_two()

def three_by_three():
    r = get_camera().left( 0.29 ).top( 0.29 )
    w = get_camera().width()
    h = get_camera().height()

    a = []
    for i in range(0,9):
        x = (i%3) * 0.305 + 0.05
        y = (i/3) * 0.305 + 0.05

        a.append( Anim( r.move_right( w * x, abs = 1 ).move_down( h * y, abs = 1 ) ) )

    start_animation( *([Fill(color=black), common.bg] + a) )

    set( common.bg._alpha, 0.0 )
    pause()

    fade_in( 0.5, common.bg )

    parallel()

    for d, n, i in zip( a, [tt1, tt2, tt4, tt5, tt6, tt8, tt7, tt9, tt3], range(9) ):
        serial( 2 * i )
        d.fade_in_start( n, 0.5 )
        d.play( n )
        end()

    end()

    pause()

    fade_out( *([0.5] + a) )

    tx = Text( get_camera().inset( 0.2 ), text = 'the end',
               color = yellow, size = 40, font = fonts['bold'], _alpha = 0,
               justify = 0.5, vjustify = 0.5 )
    enter( tx )
    fade_in( 0.5, tx )
    pause()
    fade_out( 0.5, common.bg, tx )

    return end_animation()
three_by_three = three_by_three()
    

test_objects( three_by_three )


#test_objects( an10, an9, an8, an7, an6, an5, an1, an2, an3, an4 )
