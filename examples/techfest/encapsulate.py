from slithy.library import *
from slithy.util import *
import math
from fonts import fonts, images
import hinting
import pythagoras
from macros import *

inner_aframe = Rect( 0.0, 0.0, width = 4, height = 3 )
outer_aframe = Rect( 0.0, 0.0, width = 4.5, height = 4.5 ).move_down( 0.5 )
big_inner_aframe = Rect( 0.0, 0.0, width = 5, height = 3 )
big_outer_aframe = Rect( 0.0, 0.0, width = 5.5, height = 4.5 ).move_down( 0.5 )

def interp_cameralist( c, cameras ):
    if c <= 0.0:
        return cameras[0]
    elif c >= len(cameras)-1:
        return cameras[-1]

    i = int(c)
    f = c - i
    return cameras[i].interp( cameras[i+1], f )

                    

def animation_frame( anim = (OBJECT),
                     t = (SCALAR, 0, 1),
                     c = (SCALAR, 0, 1),
                     ):
    clear( white )
    set_camera( inner_aframe.interp( outer_aframe.outset( 0.1 ), c ) )
    
    color( 0.8 )
    rectangle( outer_aframe )
    color( white )
    rectangle( inner_aframe )

    if anim:
        embed_object( inner_aframe, anim, { 't' : t * anim.length } )

    knob( 0, -2.15, t, 'time', 1.0 )


def framed_animation( a ):
    d = Drawable( get_camera(), animation_frame, anim = a )
    start_animation( d )

    parallel()
    linear( 15.0, d.t, 1.0 )
    serial( 4.0 )
    smooth( 3.0, d.c, 1.0 )
    end()
    end()

    pause()

    linear( 1.0, d.t, 0.25 )
    pause()
    linear( 1.0, d.t, 0.75 )
    pause()
    linear( 1.0, d.t, 0.5 )

    return end_animation()
framed_animation = framed_animation( hinting.character_animation[0].anim )
    

    
cameras = (Rect( -0.3, -0.65, width = 4, height = 4 ).outset( 0.3 ),
           Rect( 0.0, -1.3, width = 4, height = 4 ).outset( 0.3 ),
           Rect( 0.0, -1.3, width = 4, height = 4 ).outset( 0.3 ).move_down( 0.5 ),
           )

inner_frame = Rect( 0.0, -1.3, width = 4, height = 4 )
outer_frame = Rect( 0.0, -1.3, width = 4.5, height = 5.5 ).move_down( 0.5 )

def draw_diagram_frame( alpha, pull, showlabel, second ):
    color( 0.8, alpha )
    rectangle( outer_frame )
    color( white, alpha )
    rectangle( inner_frame )

    knob( -1, -3.9, pull, 'pull', alpha )
    
    if second > 0.0:
        knob( 1, -3.9, showlabel, 'showlabels', second * alpha )
        
knobcolor = Color( 0, 0.4, 0.7 )

knobshape = Path()
knobshape.moveto( 0.4, 0.0 ).lineto( 0.25 * math.cos( math.pi / 8 ), 0.25 * math.sin( math.pi / 8 ) )
knobshape.arc( 0, 0, 22.5, -22.5, 0.25 ).closepath()


def knob( x, y, a, label, alpha ):
    push()
    translate( x, y )
    color( black, alpha )
    push()
    thickness( 0.03 )
    for i in range(0,9):
        line( 0.45, 0, 0.55, 0 )
        rotate( 22.5 )
    pop()
    text( 0, -0.3, label, font = fonts['bold'], anchor = 'n', size = 0.3 )
        
    rotate( (1-a) * 180.0 )
    color( knobcolor, alpha )
    fill( knobshape )

    color( black, alpha )
    dot( 0.05 )
    pop()
    
    
    

def pulley_assembly( assemble = (SCALAR, 0, 1, 1),
                     pull = (SCALAR, 0, 1),
                     v1 = (SCALAR, 0, 1),
                     v2 = (SCALAR, 0, 1),
                     v3 = (SCALAR, 0, 1),
                     v4 = (SCALAR, 0, 1),
                     c = (SCALAR, 0, len(cameras)-1),
                     show_frame = (SCALAR, 0, 1),
                     show_labels = (SCALAR, 0, 1),
                     second_knob = (SCALAR, 0, 1),
                     ):
    clear( white )
    set_camera( interp_cameralist( c, cameras ) )

    if show_frame > 0.0:
        draw_diagram_frame( show_frame, pull, show_labels, second_knob )

    a1, a2, a3 = split_sequence( 3, assemble, 0.7 )
    v31, v32, v33 = split_sequence( 3, v3, 0.4 )

    color( 0.6 )
    thickness( 0.035 + v32 * 0.08 )
    push()
    translate( 0.75 * a1, -0.8 * a1 )
    rotate( -90 * a1 )
    line( 0.5, 0, 0.5, -1-pull )
    pop()

    push()
    thickness( 0.035 + v31 * 0.08 )
    translate( 0.05 * a1, 0.05 * a1 )
    line( 0.3, -1-pull, 0.7, -1-pull )
    pop()
    
    push()
    thickness( 0.035 + v33 * 0.08 )
    translate( -1.25 * a1, -1.15 * a1 )
    rotate( 90 * a1 )
    line( -0.5, 0, -0.5, -2+pull )
    pop()
    
    thickness( 0.05 )
    push()
    rotate( -pull / 0.5 * 180.0 / math.pi )
    push()
    translate( 0.5 * a2, 0 )
    color( Color(0.9).interp(orange, 0.2) )
    dot( 0.5 + 0.25 * v1, 0, 0 )
    pop()
    push()
    translate( -0.75 * a2, -0.9 * a2 )
    color( white )
    dot( 0.1, 0, 0 )
    pop()
    color( black )
    push()
    translate( 0.5 * a2, 0 )
    circle( 0.5 + 0.25 * v1, 0, 0 )
    pop()
    push()
    translate( -0.75 * a2, -0.9 * a2 )
    rotate( 225 * v4 )
    scale( 1 + v4 * 3, 1 + v4 * 5 )
    circle( 0.1, 0, 0 )
    pop()

    translate( -1.25 * a2, -1.25 * a2 )
    scale( 1 + v4 * 3, 1 + v4 * 5 )
    rotate( 225 * v4 )
    polygon( 0, 0.45, 0.1, 0.15, -0.1, 0.15 )
    pop()
    
    if show_labels > 0.0:
        color( black, show_labels )
        msg = '%.1f°' % (pull / 0.5 * 180.0 / math.pi,)
        text( 1.6, 0, msg, font = fonts['roman'], anchor = 'e', size = 0.4 )

    color( green.interp( blue, v2 ) )
    push()
    translate( -0.5 * a3, 2.5 * a3 )
    translate( -0.5, -2+pull )
    rectangle( -0.5, -1, 0.5, 0 )
    if show_labels > 0.0:
        color( white, show_labels )
        text( 0, -0.5, '1 kg', font = fonts['roman'], size = 0.4, anchor = 'c' )
    color( black.interp( red, v2 ) )
    frame( -0.5, -1, 0.5, 0 )
    pop()
    
def run_pulley():
    d = Drawable( get_camera(), pulley_assembly )
    
    start_animation( d )

    smooth( 0.5, d.v1, 1.0 )
    pause()
    smooth( 0.5, d.v2, 1.0 )
    pause()
    smooth( 0.5, d.v3, 1.0 )
    pause()
    smooth( 0.5, d.v4, 1.0 )
    pause()
    parallel()
    smooth( 0.5, d.v1, 0.0 )
    smooth( 0.5, d.v2, 0.0 )
    smooth( 0.5, d.v3, 0.0 )
    smooth( 0.5, d.v4, 0.0 )
    end()
    pause()

    parallel()
    smooth( 1.0, d.assemble, 0.0 )
    smooth( 1.0, d.c, 1.0 )
    end()
    pause()
    parallel()
    smooth( 1.0, d.c, 2.0 )
    smooth( 1.0, d.show_frame, 1.0 )
    end()
    pause()

    smooth( 2.0, d.pull, 1.0 )
    wait( 0.25 )
    smooth( 1.0, d.pull, 0.25 )
    wait( 0.25 )
    linear( 0.5, d.pull, 0.5 )
    pause()



    return end_animation()
run_pulley = run_pulley()

def pythagoras_frame( a = (SCALAR, 0, 1, 1.565/5.0),
                      b = (SCALAR, 0, 1, 3.080/5.0),
                      subdiv = (SCALAR, 0, 1),
                      slide = (SCALAR, 0, 1),
                      ):
    set_camera( big_outer_aframe.outset( 0.1 ) )
    
    color( 0.8 )
    rectangle( big_outer_aframe )
    color( white )
    rectangle( big_inner_aframe )

    slidea, slideb = split_sequence( 2, slide )
                      
    embed_object( big_inner_aframe, pythagoras.pythagoras_d,
                  { 'a' : a * 5 + 1,
                    'b' : b * 5 + 1,
                    'slidea' : slidea * 3,
                    'slideb' : slideb * 3,
                    'linealpha' : 1.0,
                    'lineextend' : 1.0,
                    'subdivide' : subdiv * 0.8,
                    'textlabel' : 1.0,
                    'cam' : 0 } )
    
    knob( -2, -2.15, a, 'a', 1.0 )
    knob( -2/3., -2.15, b, 'b', 1.0 )
    knob( 2/3., -2.15, subdiv, 'subdiv', 1.0 )
    knob( 2, -2.15, slide, 'slide', 1.0 )

def show_pythagoras_frame():
    d = Drawable( get_camera(), pythagoras_frame, a = 0.75, b = 0.2 )

    start_animation( d )
    smooth( 1.0, d.a, 1.565 / 5.0 )
    smooth( 1.0, d.b, 3.080 / 5.0 )
    smooth( 1.0, d.subdiv, 1.0 )
    smooth( 1.0, d.slide, 1.0 )
    pause()
    parallel()
    serial()
    smooth( 0.5, d.a, 0.7 )
    smooth( 1.0, d.a, 0.2 )
    smooth( 0.5, d.a, 0.5 )
    end()
    serial()
    smooth( 0.8, d.b, 0.4 )
    wait( 0.4 )
    smooth( 0.8, d.b, 0.7 )
    end()
    serial()
    smooth( 0.4, d.subdiv, 0.2 )
    smooth( 0.6, d.subdiv, 0.7 )
    smooth( 1.0, d.subdiv, 0.5 )
    end()
    serial()
    smooth( 0.5, d.slide, 0.5 )
    smooth( 1.0, d.slide, 0.2 )
    smooth( 0.5, d.slide, 0.5 )
    end()
    end()

    return end_animation()
show_pythagoras_frame = show_pythagoras_frame()    
    

def framed_pythagoras_animation( a ):
    d = Drawable( get_camera(), animation_frame, anim = a )
    start_animation( d )

    parallel()
    linear( 15.0, d.t, 1.0 )
    serial( 2.0 )
    smooth( 4.0, d.c, 1.0 )
    end()
    end()

    return end_animation()
framed_pythagoras_animation = framed_pythagoras_animation( pythagoras.proof_pair[0].anim )

def container_slide():
    bg = Fill( style = 'horz', color = black, color2 = Color(0.4) )
    colors = { 'title' : yellow, 'body' : white }
    fd = { 'title' : fonts['bold'], 'roman' : fonts['roman'],
           'dingbats' : fonts['dingbats'] }
    set_styles( fonts = fd, colors = colors, fade_interval = 0.5 )

    fade_interval = 0.5

    a = Anim( get_camera().bottom(0.85).inset(0.05).right(0.475),
              anim = pythagoras.pythagoras[0], t = 0.0, _alpha = 0.0 )
    
    camera = start_animation( bg )
    add_title( 'Lorem ipsum' )
    bl = add_bulleted_list()
    bl.add_item( 0, 'Dolor sit amet, consectetaur', fade_interval )
    parallel()
    serial()
    wait( 1.0 )
    bl.add_item( 1, 'adipisicing elit, sed do', fade_interval )
    wait( 1.0 )
    bl.add_item( 1, 'eiusmod tempor incididunt ut labore et dolore magne aliqua', fade_interval )
    wait( 1.0 )
    bl.add_item( 0, 'Ut enim ad minim veniam', fade_interval )
    end()
    serial()
    enter( a )
    fade_in( 0.5, a )
    a.play( pythagoras.pythagoras, pause = 0 )
    end()
    end()
    first = end_animation()

    return first
container_slide = container_slide()

def framed_container_animation( a ):
    d = Drawable( get_camera(), animation_frame, anim = a )
    start_animation( d )

    linear( a.length, d.t, 1.0 )
    pause()
    smooth( 1.0, d.c, 1.0 )
    wait( 0.5 )
    smooth( 2.0, d.t, 0.25 )
    wait( 0.5 )
    smooth( 4.0, d.t, 0.75 )
    
    return end_animation()
framed_container_animation = framed_container_animation( container_slide[0] )


test_objects( show_pythagoras_frame, framed_pythagoras_animation, framed_container_animation )
#test_objects( run_pulley, framed_animation )
# hinting.character_animation[0].anim, pulley_assembly
