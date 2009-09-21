from slithy.library import *
from slithy.util import *
from fonts import fonts
import math
import common

knobcolor = Color( 0, 0.6, 0.9 )

knobshape = Path()
knobshape.moveto( 0.4, 0.0 ).lineto( 0.25 * math.cos( math.pi / 8 ), 0.25 * math.sin( math.pi / 8 ) )
knobshape.arc( 0, 0, 22.5, -22.5, 0.25 ).closepath()

whitebg = Fill( color = white )

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


def simple_pythagoras( a = (SCALAR, 1, 5),
                       b = (SCALAR, 1, 5),
                       tri = (SCALAR, 0, 1),
                       ):
    set_camera( Rect( -6, -6, 9, 9 ) )

    color( yellow, tri )
    polygon( 0, 0, 0, a, b, 0 )

    color( blue )
    rectangle( 0, 0, -a, a )

    color( red )
    rectangle( 0, 0, b, -b )

    c = math.sqrt( a*a + b*b )
    
    translate( 0, a )
    rotate( -math.atan2( a, b ) * 180 / math.pi )
    color( green )
    rectangle( 0, 0, c, c )


dtext = """
def sample( a = (SCALAR, 1, 5),
            b = (SCALAR, 1, 5),
            tri = (SCALAR, 0, 1),
            ):
    set_camera( Rect( -6, -6, 9, 9 ) )

    color( yellow, tri )
    polygon( 0, 0, 0, a, b, 0 )

    color( blue )
    rectangle( 0, 0, -a, a )

    color( red )
    rectangle( 0, 0, b, -b )

    c = sqrt( a*a + b*b )
    translate( 0, a )
    rotate( -atan2( a, b ) )
    color( green )
    rectangle( 0, 0, c, c )
""".strip()

cameras = (
  Rect(0,0,1,1).outset( 0.1 ),
  Rect(-0.6,0,2.35,1).outset( 0.1 ),
  )

segment = Path().moveto( -0.25, 0.5 ).lineto( -0.2, 0.5 )

def parameterized_diagram( cam = (SCALAR, 0, 1),
                           a = (SCALAR, 0, 1),
                           b = (SCALAR, 0, 1),
                           tri = (SCALAR, 0, 1),
                           show_stuff = (SCALAR, 0, 1),
                           label = (SCALAR, 0, 1),
                           ):
    clear( white )
    set_camera( interp_cameralist( cam, cameras ) )

    color( 0.85 )
    rectangle( 0, 0, 1, 1 )

    if label < 1.0:
        push()
        scale( 0.85, 1 )
        color( black, 1-label )
        text( 0.025, .975, dtext, font = fonts['mono'], size = 0.0475, anchor = 'nw' )
        pop()
    if label > 0.0:
        color( 0.8, 0, 0, label )
        text( 0.5, 0.5, 'parameterized\ndiagram', font = fonts['bold'], size = 0.14, anchor = 'c', justify = 0.5 )

    push()
    translate( -0.5, 0.15 )
    scale( 0.25 )
    knob( 0, 0, tri, 'tri', show_stuff )
    pop()

    push()
    translate( -0.5, 0.5 )
    scale( 0.25 )
    knob( 0, 0, b, 'b', show_stuff )
    pop()

    push()
    translate( -0.5, 0.85 )
    scale( 0.25 )
    knob( 0, 0, a, 'a', show_stuff )
    pop()

    color( black, show_stuff )
    widestroke( segment, 0.075 )
    arrow( segment, (0,0.2,0.1) )

    push()
    translate( 1.35, 0 )
    widestroke( segment, 0.075 )
    arrow( segment, (0,0.2,0.1) )
    pop()

    thickness( 0.01 )
    frame( 1.35, 0, 2.35, 1 )
    embed_object( Rect(1.35,0,2.35,1), simple_pythagoras, { 'a' : a * 4 + 1, 'b' : b * 4 + 1, 'tri' : tri }, _alpha = show_stuff )

def show_parameterized_diagram():
    d = Drawable( get_camera(), parameterized_diagram, _alpha = 0.0 )

    start_animation( common.bg, d )

    fade_in( 0.5, d )
    exit( common.bg )

    pause()

    parallel()
    smooth( 2.0, d.cam, 1 )
    serial( 1.0 )
    smooth( 1.0, d.show_stuff, 1 )
    end()
    end()

    pause()

    smooth( 0.5, d.b, 0.8 )
    wait( 0.25 )
    smooth( 0.5, d.b, 0.2 )
    wait( 0.25 )
    smooth( 0.5, d.b, 0.7 )

    wait( -0.75 )

    smooth( 0.5, d.a, 1.0 )
    wait( 0.25 )
    smooth( 0.5, d.a, 0.0 )
    wait( 0.25 )
    smooth( 0.5, d.a, 0.5 )

    wait( -0.75 )

    smooth( 0.5, d.tri, 1.0 )
    wait( 0.25 )
    smooth( 0.5, d.tri, 0.0 )
    wait( 0.25 )
    smooth( 0.5, d.tri, 1.0 )

    pause()

    smooth( 1.0, d.label, 1.0 )

    pause()
    smooth( 0.5, d.show_stuff, 0.0 )

    return end_animation()
show_parameterized_diagram = show_parameterized_diagram()

def little_animation():
    c = Rect( 0, 0, 1, 1 )
    bg = Fill( style = 'horz', color = black, color2 = Color(0.5) )
    d = Drawable( c, simple_pythagoras )
    tx = Text( c, text = 'hello,\nworld!', font = fonts['fancy'], justify = 0.5, vjustify = 0.15, color = white, size = 0.1 )

    start_animation( bg, d, tx ).view( c )

    parallel()

    serial()
    set( d.a, 5 )
    wait( 0.3 )
    smooth( 0.4, d.a, 1 )
    end()

    serial()
    set( d.b, 1 )
    wait( 0.2 )
    linear( 0.05, d.b, 5 )
    wait( 0.5 )
    linear( 0.05, d.b, 3 )
    end()

    serial()
    set( d.tri, 0 )
    wait( 0.3 )
    linear( 0.5, d.tri, 1 )
    end()

    serial()
    wait( 0.4 )
    linear( 0.1, tx.size, 0.2 )
    linear( 0.1, tx.size, 0.1 )
    wait( 0.3 )
    linear( 0.1, tx.size, 0.2 )
    end()

    linear( 1.0, bg.color2, black )

    end()

    return end_animation()
little_animation = little_animation()

acameras = (
  Rect(-0.6,0,2.35,1).outset( 0.1 ),
  #Rect(-1.4, -2.15, 1.05, 1.05).outset( 0.1 ),
  Rect( -2.45, -2.15, 2.7, 1.05 ).outset( 0.05 ),
  )

seg = Path().moveto( 0, 0 ).lineto( 0.1, 0 )

a1 = Path().moveto( -0.475, 0.5 ).lineto( -0.325, 0.5 )
a2 = Path().moveto( -0.475, 1.55 ).qcurveto( 0.5, 1.55, 0.5, 1.325 )

def animation( cam = (SCALAR, 0, 1),
               t = (SCALAR, 0, 1),
               show_knob = (SCALAR, 0, 1),
               show_sample = (SCALAR, 0, 1),
               show_marrows = (SCALAR, 0, 1),
               show_earrows = (SCALAR, 0, 1),
               show_output = (SCALAR, 0, 1),
               show_bigrect = (SCALAR, 0, 1),
               show_otherboxes = (SCALAR, 0, 1),
               show_timelines = (SCALAR, 0, 1),
               label = (SCALAR, 0, 1),
               ):
    clear( white )
    set_camera( interp_cameralist( cam, acameras ) )

    b2, b3 = split_sequence_smooth( 2, show_otherboxes, 0.5 )
    t1, t2, t3 = split_sequence_smooth( 3, show_timelines, 0.5 )

    thickness( 0.02 )

    if show_bigrect > 0.0:
        color( 0.8, show_bigrect )
        rectangle( 1.1, 1.1, -1.45, -2.2 )

    push()

    color( 0.85 )
    rectangle( 0, 0, 1, 1 )

    color( 0.8, 0, 0 )
    text( 0.5, 0.5, 'parameterized\ndiagram', font = fonts['bold'], size = 0.14, anchor = 'c', justify = 0.5 )

    if show_marrows:
        push()
        color( black, show_marrows )
        translate( -0.275, 0.5 )
        widestroke( seg, 0.08 )
        arrow( seg, (0,0.2,0.1) )
        pop()

    push()
    translate( -1.35, 0 )
    draw_timeline1( t1 )
    if show_sample:
        color( red, show_sample )
        line( t, 0, t, 1 )
    pop()

    translate( 0, -1.05 )

    if b2> 0.0:
        color( 0.85, b2 )
        rectangle( 0, 0, 1, 1 )

        color( 0.8, 0, 0, b2 )
        text( 0.5, 0.5, 'background\nfill', font = fonts['bold'], size = 0.14, anchor = 'c', justify = 0.5 )

    if show_marrows:
        push()
        color( black, show_marrows )
        translate( -0.275, 0.5 )
        widestroke( seg, 0.08 )
        arrow( seg, (0,0.2,0.1) )
        pop()

    push()
    translate( -1.35, 0 )
    draw_timeline2( t2 )
    if show_sample:
        color( red, show_sample )
        line( t, 0, t, 1 )
    pop()

    translate( 0, -1.05 )

    if b3 > 0.0:
        color( 0.85, b3 )
        rectangle( 0, 0, 1, 1 )
        
        color( 0.8, 0, 0, b3 )
        text( 0.5, 0.5, 'text\nbox', font = fonts['bold'], size = 0.14, anchor = 'c', justify = 0.5 )

    if show_marrows:
        push()
        color( black, show_marrows )
        translate( -0.275, 0.5 )
        widestroke( seg, 0.08 )
        arrow( seg, (0,0.2,0.1) )
        pop()

    push()
    translate( -1.35, 0 )
    draw_timeline3( t3 )
    if show_sample:
        color( red, show_sample )
        line( t, 0, t, 1 )
    pop()

    pop()

    push()
    translate( -2.25, -.55 )
    scale( 0.5 )
    if show_knob > 0.0:
        knob( 0, 0, t, 'time', show_knob )

        color( black, show_knob )
        translate( 0.8, 0 )
        scale( 2, 1 )
        widestroke( seg, 0.24 )
        arrow( seg, (0,0.6,0.2) )
    pop()
    
    push()
    thickness( 0.01 )
    translate( 1.7, -1.05 )
    if show_output > 0.0:
        color( black, show_output )
        frame( 0, 0, 1, 1 )
        embed_object( Rect(0,0,1,1), little_animation[0], { 't' : t }, _alpha = show_output )

    if show_earrows or label:
        color( black, max(show_earrows, label) )
        widestroke( a1, 0.12 )
        arrow( a1, (0,0.3,0.2) )
        color( black, show_earrows )
        widestroke( a2, 0.08 )
        arrow( a2, (0,0.3,0.2) )
        scale( 1, -1, 0.5, 0.5 )           
        widestroke( a2, 0.08 )
        arrow( a2, (0,0.3,0.2) )
    
    pop()

    if label > 0.0:
        color( 0.9, label )
        rectangle( 1.1, 1.1, -1.45, -2.2 )

        color( 0.8, 0, 0, label )
        text( -.175, -.55, 'animation\nobject', font = fonts['bold'], size = 0.3, anchor = 'c', justify = 0.5 )

t11 = Path().moveto( 0, 0.95 ).lineto( 0.3, 0.95 ).curveto( 0.5, 0.95, 0.5, 0.7, 0.7, 0.7 ).lineto( 1.0, 0.7 )
t12 = Path().moveto( 0, 0.35 ).lineto( 0.2, 0.35 ).lineto( 0.25, 0.65 ).lineto( 0.75, 0.65 ).lineto( 0.8, 0.5 ).lineto( 1, 0.5 )
t13 = Path().moveto( 0, 0.05 ).lineto( 0.3, 0.05 ).lineto( 0.8, 0.3 ).lineto( 1.0, 0.3 )

def draw_timeline1( a ):
    color( white, a )
    rectangle( 0, 0, 1, 1 )

    color( 0.0, 0.3, 0.8, a )
    widestroke( t11, 0.02 )
    widestroke( t12, 0.02 )
    widestroke( t13, 0.02 )

t21 = Path().moveto( 0, 0.65 ).lineto( 1, 0.35 )
    
def draw_timeline2( a ):
    color( white, a )
    rectangle( 0, 0, 1, 1 )

    color( 0.0, 0.3, 0.8, a )
    widestroke( t21, 0.02 )
    
t31 = Path().moveto( 0, 0.35 ).lineto( 0.4, 0.35 ).lineto( 0.5, 0.65 ).lineto( 0.6, 0.35 ).lineto( 0.9, 0.35 ).lineto( 1.0, 0.65 )
    
def draw_timeline3( a ):
    color( white, a )
    rectangle( 0, 0, 1, 1 )

    color( 0.0, 0.3, 0.8, a )
    widestroke( t31, 0.02 )


def show_animation():
    d = Drawable( get_camera(), animation )

    start_animation( d )

    parallel()
    smooth( 2.0, d.cam, 1.0 )
    smooth( 2.0, d.show_bigrect, 1.0 )
    end()

    smooth( 1.0, d.show_otherboxes, 1.0 )

    pause()

    smooth( 1.0, d.show_timelines, 1.0 )

    set( d.t, 0.3 )
    
    pause()
    smooth( 0.5, d.show_knob, 1.0 )
    pause()
    smooth( 0.5, d.show_sample, 1.0 )
    pause()
    smooth( 0.5, d.show_marrows, 1.0 )
    pause()
    
    parallel()
    smooth( 0.5, d.show_earrows, 1.0 )
    serial(0.25)
    smooth( 0.5, d.show_output, 1.0 )
    end()
    end()

    pause()

    linear( 4.0, d.t, 1.0 )
#     wait( 1.0 )
#     smooth( 1.0, d.t, 0.0 )
#     wait( 1.0 )
#     linear( 5.0, d.t, 1.0 )

    pause()

    parallel()
    smooth( 0.5, d.label, 1.0 )
    smooth( 0.5, d.show_earrows, 0.0 )
    end()

    pause()

    enter( whitebg )
    lower( whitebg )
    fade_out( 0.5, d )
    wait( 0.5 )

    return end_animation()
show_animation = show_animation()

sampletimes = [None] * 42
for i in range(0,21):
    sampletimes[i*2] = i * 0.05



def draw_itimeline1(  info, t, h ):
    color( white )
    rectangle( 0, 0, 1, 1 )
    if h > 0:
        color( yellow, h )
        rectangle( 0.3, 0, 1, 1 )
    color( 0.0, 0.3, 0.8 )
    thickness( 0.02 )

    pts = [None] * 22
    for i in range(0,11):
        pts[i*2] = i * 0.1
        pts[i*2+1] = info.b_t.eval( (i*0.1)+t-0.3 ) * 0.7 + 0.1
    line( *pts )
    
    for i in range(0,11):
        pts[i*2] = i * 0.1
        pts[i*2+1] = info.a_t.eval( (i*0.1)+t-0.3 ) * 0.7 + 0.1
    line( *pts )
    

    line( 0, 0.9, 1, 0.9 )

def draw_itimeline2( info, t, h ):
    color( white )
    rectangle( 0, 0, 1, 1 )

    color( 0.0, 0.3, 0.8 )
    thickness( 0.02 )

    pts = [None] * 22
    for i in range(0,11):
        pts[i*2] = i * 0.1
        pts[i*2+1] = info.bg_t.eval( (i*0.1)+t-0.3 ) * 0.6 + 0.2
    line( *pts )
    
def draw_itimeline3( info, t, h ):
    color( white )
    rectangle( 0, 0, 1, 1 )
    if h > 0:
        color( yellow, h )
        rectangle( 0.3, 0, 1, 1 )
    color( 0.0, 0.3, 0.8 )
    thickness( 0.02 )

    pts = [None] * 42
    for i in range(0,21):
        pts[i*2] = i * 0.05
        pts[i*2+1] = info.tx_t.eval( (i*0.05)+t-0.3 ) * 0.6 + 0.2
    line( *pts )
    

icameras = (
  Rect( -2.45, -2.15, 2.7, 1.05 ).outset( 0.05 ).move_right( 0.1 ),
  Rect( -2.45, -2.65, 2.7, 1.05 ).outset( 0.05 ).move_right( 0.1 ),
  )


darkblue = Color( 0, 0, 0.6 )

def interaction( cam = (SCALAR, 0, 1),
                 show_arrows = (SCALAR, 0, 1),
                 grow_bigrect = (SCALAR, 0, 1),
                 info = (OBJECT, None),
                 a = (SCALAR, 0, 1),
                 b = (SCALAR, 0, 1),
                 tx = (SCALAR, 0, 1),
                 bg = (SCALAR, 0, 1),
                 draw_time = (SCALAR, 0, 1),
                 h1 = (SCALAR, 0, 1),
                 h3 = (SCALAR, 0, 1),
                 show_evhandle = (SCALAR, 0, 1),
                 ):
    clear( white )
    set_camera( interp_cameralist( cam, icameras ) )

    a = info.a_t.eval( draw_time )
    b = info.b_t.eval( draw_time )
    tx = info.tx_t.eval( draw_time )
    bg = info.bg_t.eval( draw_time )

    thickness( 0.02 )

    color( 0.8 )
    rectangle( 1.1, 1.1, -1.45, -2.2 - 0.5 * grow_bigrect )

    if show_evhandle > 0.0:
        color( 0.95, show_evhandle )
        rectangle( 1, -2.2, -1.35, -2.6 )
        color( darkblue.interp( yellow, max(h1,h3) ), show_evhandle )
        text( -.175, -2.4, 'event handlers', font = fonts['bold'], size = 0.18, anchor = 'c', justify = 0.5 )

    push()

    color( 0.85 )
    rectangle( 0, 0, 1, 1 )

    color( 0.8, 0, 0 )
    text( 0.5, 0.5, 'parameterized\ndiagram', font = fonts['bold'], size = 0.14, anchor = 'c', justify = 0.5 )

    if show_arrows:
        push()
        color( black, show_arrows )
        translate( -0.275, 0.5 )
        widestroke( seg, 0.08 )
        arrow( seg, (0,0.2,0.1) )
        pop()

    push()
    translate( -1.35, 0 )
    draw_itimeline1( info, draw_time, h1 )
    color( red )
    line( 0.3, 0, 0.3, 1 )
    pop()

    translate( 0, -1.05 )

    color( 0.85 )
    rectangle( 0, 0, 1, 1 )

    color( 0.8, 0, 0 )
    text( 0.5, 0.5, 'background\nfill', font = fonts['bold'], size = 0.14, anchor = 'c', justify = 0.5 )

    if show_arrows:
        push()
        color( black, show_arrows )
        translate( -0.275, 0.5 )
        widestroke( seg, 0.08 )
        arrow( seg, (0,0.2,0.1) )
        pop()

    push()
    translate( -1.35, 0 )
    draw_itimeline2( info, draw_time, 0 )
    color( red )
    line( 0.3, 0, 0.3, 1 )
    pop()

    translate( 0, -1.05 )

    color( 0.85 )
    rectangle( 0, 0, 1, 1 )
        
    color( 0.8, 0, 0 )
    text( 0.5, 0.5, 'text\nbox', font = fonts['bold'], size = 0.14, anchor = 'c', justify = 0.5 )

    if show_arrows:
        push()
        color( black, show_arrows )
        translate( -0.275, 0.5 )
        widestroke( seg, 0.08 )
        arrow( seg, (0,0.2,0.1) )
        pop()

    push()
    translate( -1.35, 0 )
    draw_itimeline3( info, draw_time, h3 )
    color( red )
    line( 0.3, 0, 0.3, 1 )
    pop()

    pop()

    push()
    thickness( 0.01 )
    translate( 1.7, -1.05 - 0.25 * grow_bigrect )

    color( black )
    frame( 0, 0, 1, 1 )
    color( 0 )
    other = black.interp( purple, bg )
    rectangle( 0, 0, 1, 1, sw = other, se = other )
    embed_object( Rect(0,0,1,1), simple_pythagoras, { 'tri' : 1, 'a' : a*4+1, 'b' : b*4+1 } )
    color( white )
    text( 0.5, 0.2, 'hello', font = fonts['title'], size = 0.2 + 0.4 * tx )

    if show_arrows:
        color( black, show_arrows )
        widestroke( a1, 0.12 )
        arrow( a1, (0,0.3,0.2) )
        #color( black, show_earrows )
        #widestroke( a2, 0.08 )
        #arrow( a2, (0,0.3,0.2) )
        #scale( 1, -1, 0.5, 0.5 )           
        #widestroke( a2, 0.08 )
        #arrow( a2, (0,0.3,0.2) )
    
    pop()

    if info:
        info.last_drawn = mark()

def icoverbox():
    set_camera( icameras[1] )
    color( 0.9 )
    rectangle( 1.1, 1.1, -1.45, -2.7 )

    color( 0.8, 0, 0 )
    text( -.175, -.8, 'interactive\ncontroller', font = fonts['bold'], size = 0.3, anchor = 'c', justify = 0.5 )
    
    


class InteractiveInteractive(Controller):
    def create_objects( self ):
        self.d = Drawable( None, interaction, a = 0, b = 1, tx = 0,
                           show_arrows = 1, grow_bigrect = 1,
                           show_evhandle = 1, cam = 1 )
        return self.d

    def start( self ):
        self.a_t = self.d.a
        self.b_t = self.d.b
        self.tx_t = self.d.tx
        self.bg_t = self.d.bg
        set( self.d.info, self )
        wait( -0.3 )
        #set( self.d.a, 0.0 )
        #set( self.d.b, 1.0 )
        #set( self.d.tx, 0.0 )
        wave( self.d.bg, period = 2.0, min = 0, max = 1 )
        wait( 0.3 )
        self.toggle = 0
        self.accum = 0

        linear( 10000.0, self.d.draw_time, 10000.0 )
        wait( -10000.0 )

    def key( self, k, x, y, m ):
        if k == 'a':
            parallel()
            linear ( 0.2, self.d.h1, 1.0, 0.0 )
            if self.toggle:
                smooth( 1.0, self.d.a, 0.0 )
                smooth( 1.0, self.d.b, 1.0 )
                self.toggle = 0
            else:
                smooth( 1.0, self.d.a, 1.0 )
                smooth( 1.0, self.d.b, 0.0 )
                self.toggle = 1
            end()
        elif k == 'o' or k == 's':
            linear ( 0.2, self.d.h3, 1.0, 0.0 )
            smooth( 0.25, self.d.tx, 1.0 )
            smooth( 0.25, self.d.tx, 0.0 )

class Blank:
    pass
                    
def interactive_animation():
    info = Blank()
    
    d = Drawable( get_camera(), interaction, info = info, show_arrows = 1, _alpha = 0 )
    d2 = Drawable( get_camera(), icoverbox, _alpha = 0 )
    i = Interactive( get_camera(), controller = InteractiveInteractive )

    start_animation( whitebg, d )
    info.a_t = d.a
    info.b_t = d.b
    info.bg_t = d.bg
    info.tx_t = d.tx
    
    wait( -0.3 )
    set( d.b, 1 )
    wave( d.bg, period = 2.0, min = 0, max = 1 )
    wait( 0.3 )

    fade_in( 0.5, d )
    exit( whitebg )
    
    pause()

    parallel()
    smooth( 0.75, d.grow_bigrect, 1.0 )
    smooth( 0.75, d.cam, 1 )
    end()
    smooth( 0.75, d.show_evhandle, 1.0 )

    pause()
    exit( d )
    enter( i )
    pause()

    enter( d2 )
    fade_in( 0.5, d2 )

    pause()

    enter( common.bg )
    lower( common.bg )
    fade_out( 0.5, i, d2 )
    return end_animation()
interactive_animation = interactive_animation()    
            
            
                

slithy_objects = show_parameterized_diagram + show_animation

test_objects( interactive_animation, InteractiveInteractive, interaction, show_animation )
#test_objects( show_parameterized_diagram, show_animation )
#test_objects( little_animation, animation, show_parameterized_diagram, simple_pythagoras )

    
