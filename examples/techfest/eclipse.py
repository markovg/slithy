from slithy.library import *
from slithy.util import *
from fonts import fonts
from macros import *

cameras = (Rect(-3, -4, 13, 3),
           Rect(0, -4, 14, 3),
           )

sun_radius = 2
earth_radius = 1
moon_radius = 0.3
earth_color = Color( 0.2, 0.7, 0.9 )
moon_color = Color( 0.8 )

def eclipse( which = (SCALAR, 0, 1),
             umbra = (SCALAR, 0, 1),
             penumbra = (SCALAR, 0, 1),
             orbit = (SCALAR, 0, 1, 1),
             c = (SCALAR, 0, 1),
             umbra_label = (SCALAR, 0, 1),
             penumbra_label = (SCALAR, 0, 1),
             shadow_rays = (SCALAR, 0, 1),
             big_label = (SCALAR, 0, 1),
             ):
    #clear( white )

    set_camera( interp_cameralist( c, cameras ) )
    edge = 13
    
    left_pos = interpolate( which, 9, 7 )
    left_radius = interpolate( which, earth_radius, moon_radius )
    
    right_pos = interpolate( which, 11, 9 )
    right_radius = interpolate( which, moon_radius, earth_radius )

    y0 = -sun_radius + (sun_radius + left_radius) / float(left_pos) * right_pos
    y1 = sun_radius - (sun_radius - left_radius) / float(left_pos) * right_pos
    y2 = sun_radius - (sun_radius + left_radius) / float(left_pos) * right_pos
    y3 = -sun_radius + (sun_radius - left_radius) / float(left_pos) * right_pos

    color( black, big_label * abs(0.5 - which) * 2 )
    if which < 0.5:
        t = 'lunar eclipse'
    else:
        t = 'solar eclipse'
    text( 5.5, -sun_radius - 0.5, t, font = fonts['bold'], size = 0.9 )

    if umbra > 0.0:
        color( purple, umbra * 0.8 )
        polygon( left_pos, left_radius, right_pos, y1,
                 right_pos, y3, left_pos, -left_radius )

    if penumbra > 0.0:
        color( purple, penumbra * 0.4 )
        polygon( left_pos, left_radius, right_pos, y0,
                 right_pos, y1 )
        polygon( left_pos, -left_radius, right_pos, y2,
                 right_pos, y3 )

    if umbra_label > 0.0:
        color( purple.interp(black,0.5), umbra_label )
        text( right_pos + 0.5, (y3+y1)/2, 'umbra', font = fonts['bold'], anchor = 'w', size = 0.5 )
    if penumbra_label > 0.0:
        color( purple.interp(black,0.5), penumbra_label )
        text( right_pos + 0.5, (y0+y1)/2, 'penumbra', font = fonts['bold'], anchor = 'w', size = 0.5 )
        text( right_pos + 0.5, (y2+y3)/2, 'penumbra', font = fonts['bold'], anchor = 'w', size = 0.5 )
    
    color( purple, shadow_rays )
    thickness( 0.05 )
    line( 0, -sun_radius, right_pos, y0 )
    line( 0, sun_radius, right_pos, y1 )
    line( 0, sun_radius, right_pos, y2 )
    line( 0, -sun_radius, right_pos, y3 )

    color( yellow )
    dot( sun_radius - 0.025, 0, 0 )

    push()
    translate( right_pos, 0 )
    color( earth_color.interp( moon_color, which ) )
    if which > 0.5:
        rotate( orbit * 90 )
    dot( left_radius, left_pos - right_pos, 0 )
    pop()

    push()
    translate( left_pos, 0 )
    color( moon_color.interp( earth_color, which ) )
    if which < 0.5:
        rotate( orbit * 90 )
    dot( right_radius, right_pos - left_pos, 0 )
    pop()

def blink_on( duration, var ):
    linear( duration/7, var, 1.0 )
    wait( duration/7 )
    linear( duration/7, var, 0.0 )
    linear( duration/7, var, 1.0 )
    wait( duration/7 )
    linear( duration/7, var, 0.0 )
    linear( duration/7, var, 1.0 )

def run_eclipse():
    c = get_camera()
    v = viewport.interp( c, c.top(0.5).inset(0.05) )
    d = Drawable( v, eclipse )
    start_animation( Fill(color=white), d )

    smooth( 1.0, d.shadow_rays, 1.0 )
    pause()
    blink_on( 1.5, d.umbra )
    pause()
    smooth( 1.0, d.c, 1.0 )
    smooth( 0.5, d.umbra_label, 1.0 )
    pause()
    blink_on( 1.5, d.penumbra )
    pause()
    smooth( 0.5, d.penumbra_label, 1.0 )
    pause()
    parallel()
    smooth( 1.0, d.orbit, 0.4 )
    sequence( 0.5 )
    smooth( 0.5, d.big_label, 1.0 )
    end()
    end()
    pause()
    smooth( 1.0, d.orbit, 0.0 )
    pause()

    parallel()
    smooth( 1.0, d.c, 0.0 )
    smooth( 1.0, d.umbra_label, 0.0 )
    smooth( 1.0, d.penumbra_label, 0.0 )
    end()

    pause()

    smooth( 1.0, d.which, 1.0 )
    
    pause()
    parallel()
    smooth( 0.5, d.shadow_rays, 0.0 )
    smooth( 0.5, d.umbra, 0.0 )
    smooth( 0.5, d.penumbra, 0.0 )
    smooth( 0.5, d.big_label, 0.0 )
    end()
    
    smooth( 2.0, d.orbit, 4.0 )
    set( d.orbit, 0.0 )
    pause()
    smooth( 1.0, d.which, 0.0 )
    smooth( 1.0, d.which, 1.0 )

    pause()
    parallel()
    smooth( 0.5, d.which, 0.0 )
    smooth( 0.5, d.shadow_rays, 1.0 )
    smooth( 0.5, d.umbra, 1.0 )
    smooth( 0.5, d.penumbra, 1.0 )
    smooth( 0.5, d.big_label, 1.0 )
    end()
    pause()

    smooth( 1.0, v.x, 1.0 )
    d2 = Drawable( c.bottom(0.5).inset(0.05), eclipse, _alpha = 0.0 )
    enter( d2 )
    set( d2.which, 1.0 )
    set( d2.shadow_rays, 1.0 )
    set( d2.umbra, 1.0 )
    set( d2.penumbra, 1.0 )
    set( d2.orbit, 0.0 )
    set( d2.big_label, 1.0 )
    fade_in( 0.5, d2 )
    
    return end_animation()

run_eclipse = run_eclipse()
eclipse_one = run_eclipse[0].anim    

test_objects( run_eclipse, eclipse )

    
