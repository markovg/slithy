from slithy.library import *
import math
import common
from fonts import fonts

def ptor( r, theta ):
    return r * math.cos( theta * math.pi / 180.0 ), r * math.sin( theta * math.pi / 180.0 )

def make_arc( start, end ):
    rad = 1.761
    return Path().moveto( *ptor( rad, start ) ).arc( 0, 0, start, end, rad )
    

def iteration_cycle( text1 = (SCALAR, 0, 1),
                     text2 = (SCALAR, 0, 1),
                     text3 = (SCALAR, 0, 1),
                     a1 = (SCALAR, 0, 1),
                     a2 = (SCALAR, 0, 1),
                     a3 = (SCALAR, 0, 1),
                     af1 = (SCALAR, 0, 1, 0),
                     af2 = (SCALAR, 0, 1, 0),
                     af3 = (SCALAR, 0, 1, 0),
                     fade1 = (SCALAR, 0, 1, 0),
                     fade2 = (SCALAR, 0, 1, 0),
                     fade3 = (SCALAR, 0, 1, 0),
                     ):
    fadedcolor = Color( 0.4 )
    
    set_camera( Rect( -4, -3, 4, 3 ) )

    if a1 > 0.0:
        if a1 < 0.1:
            color( yellow, a1 * 10 )
        else:
            color( yellow.interp( fadedcolor, af1 ) )
        arrow1 = make_arc( 195.1, 195.1 + a1 * (260.3-195.1) )
        widestroke( arrow1, 0.1 )
        arrow( arrow1, (0,0.3,0.3) )

    if a2 > 0.0:
        if a2 < 0.1:
            color( yellow, a2 * 10 )
        else:
            color( yellow.interp( fadedcolor, af2 ) )
        arrow2 = make_arc( 317.2, 317.2 + a2 * (387.4 - 317.2) )
        widestroke( arrow2, 0.1 )
        arrow( arrow2, (0,0.3,0.3) )

    if a3 > 0.0:
        if a3 < 0.1:
            color( yellow, a3 * 10 )
        else:
            color( yellow.interp( fadedcolor, af3 ) )
        arrow3 = make_arc( 91.1, 91.1 + a3 * (154.8-91.1) )
        widestroke( arrow3, 0.1 )
        arrow( arrow3, (0,0.3,0.3) )

    color( yellow.interp( fadedcolor, fade1 ), text1 )
    text( -2, 0, 'create\ntalk(s)', font = fonts['bold'], size = 0.4,
          anchor = 'c', justify = 0.5 )

    color( yellow.interp( fadedcolor, fade2 ), text2 )
    x, y = ptor( 2, -60 )
    text( x, y, 'extract\nprinciples', font = fonts['bold'], size = 0.4,
          anchor = 'c', justify = 0.5 )

    color( yellow.interp( fadedcolor, fade3 ), text3 )
    x, y = ptor( 2, 60 )
    text( x, y, 'improve\nauthoring\nsystem', font = fonts['bold'], size = 0.4,
          anchor = 'c', justify = 0.5 )

def make_line( fx, fy, tx, ty, u ):
    r = (math.sqrt( (fx-tx)*(fx-tx) + (fy-ty)*(fy-ty) ) - 0.3) * u
    th = math.atan2( ty - fy, tx - fx )
    return Path().moveto( fx, fy ).lineto( fx + r*math.cos(th), fy + r*math.sin(th) )


def iteration_vee( text1 = (SCALAR, 0, 1),
                   text2 = (SCALAR, 0, 1),
                   text3 = (SCALAR, 0, 1),
                   slidetext = (SCALAR, 0, 1),
                   slidearrow = (SCALAR, 0, 1),
                   a1 = (SCALAR, 0, 1),
                   a2 = (SCALAR, 0, 1),
                   a3 = (SCALAR, 0, 1),
                   a4 = (SCALAR, 0, 1),
                   af1 = (SCALAR, 0, 1, 0),
                   af2 = (SCALAR, 0, 1, 0),
                   af3 = (SCALAR, 0, 1, 0),
                   af4 = (SCALAR, 0, 1, 0),
                   fade1 = (SCALAR, 0, 1, 0),
                   fade2 = (SCALAR, 0, 1, 0),
                   fade3 = (SCALAR, 0, 1, 0),
                   ):
    fadedcolor = Color( 0.4 )
    
    set_camera( Rect( -4, -3, 4, 3 ) )
    translate( 0, -0.1 )

    sep = 0.2

    if a1 > 0.0:
        if a1 < 0.1:
            color( yellow, a1 * 10 )
        else:
            color( yellow.interp( fadedcolor, af1 ) )
        arrow1 = make_line( slidearrow * sep - 0.3 * slidetext, 0.74, slidearrow * sep - 1.3 * slidetext, -.65, a1 )
        widestroke( arrow1, 0.1 )
        arrow( arrow1, (0,0.3,0.3) )

    if a2 > 0.0:
        if a2 < 0.1:
            color( yellow, a2 * 10 )
        else:
            color( yellow.interp( fadedcolor, af2 ) )
        arrow2 = make_line( -sep  - 1.3 * slidetext, -.65, -sep - 0.3 * slidetext, .74, a2 )
        widestroke( arrow2, 0.1 )
        arrow( arrow2, (0,0.3,0.3) )

    if a3 > 0.0:
        if a3 < 0.1:
            color( yellow, a3 * 10 )
        else:
            color( yellow.interp( fadedcolor, af3 ) )
        arrow3 = make_line( slidearrow * sep + 0.3, 0.74, slidearrow * sep + 1.3, -.65, a3 )
        widestroke( arrow3, 0.1 )
        arrow( arrow3, (0,0.3,0.3) )

    if a4 > 0.0:
        if a4 < 0.1:
            color( yellow, a4 * 10 )
        else:
            color( yellow.interp( fadedcolor, af4 ) )
        arrow4 = make_line( -sep + 1.3 * slidetext, -.65, -sep + 0.3 * slidetext, .74, a4 )
        widestroke( arrow4, 0.1 )
        arrow( arrow4, (0,0.3,0.3) )


    color( yellow.interp( fadedcolor, fade1 ), text1 )
    text( 0, 1.4, 'create\nanimated\ntalk(s)', font = fonts['bold'], size = 0.4,
          anchor = 'c', justify = 0.5 )

    color( yellow.interp( fadedcolor, fade2 ), text2 )
    x, y = ptor( 2, -60 )
    text( -1.5 * slidetext, -1.2, 'authoring\nprinciples', font = fonts['bold'], size = 0.4,
          anchor = 'c', justify = 0.5 )

    color( yellow.interp( fadedcolor, fade3 ), text3 )
    x, y = ptor( 2, 60 )
    text( 1.5, -1.2, 'animation\nprinciples', font = fonts['bold'], size = 0.4,
          anchor = 'c', justify = 0.5 )


def iteration1():
    d = Drawable( get_camera(), iteration_vee )

    start_animation( common.bg, d )

    smooth( 0.4, d.text1, 1.0 )

    pause()

    parallel()
    smooth( 1.2, d.a1, 1.0 )
    serial( 0.8 )
    smooth( 0.4, d.text2, 1.0  )
    end()
    end()

    pause()

    parallel()
    smooth( 1.0, d.slidearrow, 1.0 )
    serial( 0.5 )
    smooth( 1.2, d.a2, 1.0 )
    end()
    end()

    pause()

    parallel()
    smooth( 0.5, d.af1, 1.0 )
    smooth( 0.5, d.af2, 1.0 )
    smooth( 0.5, d.fade1, 1.0 )
    end()

    pause()
    fade_out( 0.5, d )

    return end_animation()
iteration1 = iteration1()

def iteration2():
    d = Drawable( get_camera(), iteration_vee,
                  text1 = 1, text2 = 1, slidearrow = 1, a1 = 1, a2 = 1, _alpha = 0 )

    start_animation( common.bg, d )

    fade_in( 0.5, d )
    pause()

    parallel()
    smooth( 1.2, d.slidetext, 1.0 )
    smooth( 1.2, d.a3, 1.0 )
    serial( 0.8 )
    smooth( 0.4, d.text3, 1.0  )
    end()
    end()

    pause()

    smooth( 1.2, d.a4, 1.0 )

    pause()

    parallel()
    smooth( 0.5, d.af1, 1.0 )
    smooth( 0.5, d.af2, 1.0 )
    smooth( 0.5, d.af4, 1.0 )
    smooth( 0.5, d.af3, 1.0 )
    smooth( 0.5, d.fade1, 1.0 )
    smooth( 0.5, d.fade2, 1.0 )
    end()

    pause()

    fade_out( 0.5, d )

    return end_animation()
iteration2 = iteration2()



def iteration():
    d = Drawable( get_camera(), iteration_cycle )

    start_animation( common.bg, d )

    smooth( 0.4, d.text1, 1.0 )
    
    pause()
    
    parallel()
    smooth( 1.2, d.a1, 1.0 )
    serial( 0.8 )
    smooth( 0.4, d.text2, 1.0  )
    end()
    end()

    pause()
    
    parallel()
    smooth( 1.2, d.a2, 1.0 )
    serial( 0.8 )
    smooth( 0.4, d.text3, 1.0  )
    end()
    end()

    pause()
    
    smooth( 1.2, d.a3, 1.0 )

    pause()

    parallel()
    smooth( 0.5, d.af1, 1.0 )
    smooth( 0.5, d.af2, 1.0 )
    smooth( 0.5, d.af3, 1.0 )
    smooth( 0.5, d.fade1, 1.0 )
    smooth( 0.5, d.fade3, 1.0 )
    end()

    pause()
    
    fade_out( 0.5, d )

    return end_animation()
iteration = iteration()

# def iteration2():
#     d = Drawable( get_camera(), iteration_cycle, text1 = 1, text2 = 1, text3 = 1,
#                   a1 = 1, a2 = 1, a3 = 1, af1 = 1, af2 = 1, af3 = 1, fade1 = 1, fade2 = 0, fade3 = 1,
#                   _alpha = 0.0 )

#     start_animation( common.bg, d )

#     fade_in( 0.5, d )
#     pause()
#     parallel()
#     smooth( 0.5, d.fade2, 1 )
#     smooth( 0.5, d.fade3, 0 )
#     serial()
#     linear( 0.25, d.af2, 0 )
#     linear( 0.25, d.af2, 1 )
#     end()
#     end()
#     pause()
#     fade_out( 0.5, d )

#     return end_animation()
# iteration2 = iteration2()
    
    


test_objects( iteration1, iteration2, iteration_vee, clear_color = black )

