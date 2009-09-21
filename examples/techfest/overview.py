from slithy.library import *
from fonts import fonts
import codeview


titlecolor = Color(0.0, 0.3, 0.8)

baseblue = Color( 0.2, 0.4, 0.8 )
basered = Color( 0.8, 0.2, 0.1 )

frame = Path()
frame.moveto( -4.5, -4.5 ).lineto( 4.5, -4.5 ).lineto( 4.5, 4.5 ).lineto( -4.5, 4.5 ).closepath()
frame.moveto( -5, -9 ).lineto( 5, -9 ).lineto( 5, 5 ).lineto( -5, 5 ).closepath()

def square( size = (SCALAR,0,1,0),
            redden = (SCALAR,0,1,0),
            rotation = (SCALAR,0,1,0),
            triangle = (SCALAR,0,1,0),
            ):
    set_camera( Rect( (-5.8996295684050333, -9.8879431289309387, 11.83479245392031, 0, 0.75) ) )
    
    color( 0.9 )
    rectangle( -5, -9, 5, 5 )
    color( 1 )
    rectangle( -4.5, -4.5, 4.5, 4.5 )

    c = size * 2 + 1
    push()
    color( baseblue.interp( basered, redden ) )
    rotate( 225 * rotation )
    polygon( c * (1-triangle), c,
             c, -c,
             -c, -c,
             -c * (1-triangle),c )
    pop()

    push()
    translate( 0, -5.4 )
    slider( 'size', size )
    translate( 0, -1 )
    slider( 'redden', redden )
    translate( 0, -1 )
    slider( 'rotation', rotation )
    translate( 0, -1 )
    slider( 'triangle', triangle )
    pop()

pointer = Path()
pointer.moveto( 0,0 ).lineto( -0.2, -0.4 ).lineto( 0.2, -0.4 ).closepath()

def slider( name, val ):
    color( 0 )
    thickness( 0.05 )
    line( -4.5, 0, 4.5, 0 )
    line( -4.5, 0.2, -4.5, -0.2 )
    line( 4.5, 0.2, 4.5, -0.2 )
    
    line( 0, 0.1, 0, -0.1 )
    line( -2.25, 0.1, -2.25, -0.1 )
    line( 2.25, 0.1, 2.25, -0.1 )

    text( -4, 0.2, name, fonts['roman'], size = 0.5, anchor = 'sw' )

    color( 1, 0, 0 )
    push()
    translate( -4.5 + val * 9, 0 )
    fill( pointer )
    pop()

bits = [
"""def square( size = (SCALAR, 0, 1),
            ""","""redden = (SCALAR, 0, 1),
            ""","""rotation = (SCALAR, 0, 1),
            triangle = (SCALAR, 0, 1) ):
    clear( white )

    ""","""color( blue*(1-redden) + red*redden ) )""","""
    rotate( 225 * rotation, (0,0) )

    c = size * 2 + 1
    polygon( (c * (1-triangle),c),
             (c,-c),
             (-c,-c),
             (-c * (1-triangle),c) )""" ]
    
abits = [
"""tx = Text( ..., text = 'Lorem ipsum' )
""","""im = Image( ... )
""","""bl = BulletedList( ... )
""","""d = Diagram( ..., draw = square )

""","""smooth( 2.0, d.size, 1.0 )
""","""linear( 1.0, d.triangle, 0.5 )

""","""parallel()
smooth( 2.0, d.redden, 1.0 )
smooth( 2.0, d.rotation, 1.0 )
end()"""
]

square_code = codeview.CodeViewer( *bits )
squareanim_code = codeview.CodeViewer( *abits )

imagepath.append( 'images' )

slide_bg = [ load_image( imagepath.search( 'sampleslide1.jpg' ) ),
             load_image( imagepath.search( 'sampleslide2.jpg' ) ),
             load_image( imagepath.search( 'sampleslide.jpg' ) ) ]
image_pair = ( (None, slide_bg[0]),
               (slide_bg[0], slide_bg[1]),
               (slide_bg[1], slide_bg[2]),
               (slide_bg[2], None) )

def sample_slide( slidestate = (SCALAR, 0, 3, 0),
                  diagram = (SCALAR, 0, 1),
                  size = (SCALAR,0,1),
                  redden = (SCALAR,0,1),
                  rotation = (SCALAR,0,1),
                  triangle = (SCALAR,0,1),
                  ):
    set_camera( Rect( -0.05, -0.0375, 4.1, 0, 4./3. ) )
    
    bottom, top = image_pair[int(slidestate)]
    if bottom is not None:
        image( 0, 0, bottom, anchor = 'sw', width = 4 )
    if top is not None:
        image( 0, 0, top, anchor = 'sw', width = 4, alpha = slidestate - int(slidestate) )
    color( black )
    thickness( 0.025 )
    line( 0, 0, 4, 0, 4, 3, 0, 3, 0, 0 )

    push()
    translate( 3, 1.2 )
    scale( 0.2 )
    
    c = size * 2 + 1
    push()
    color( baseblue.interp( basered, redden ), diagram )
    rotate( 225 * rotation, 0, 0 )
    polygon( c * (1-triangle), c, c, -c, -c, -c, -c * (1-triangle), c )
    pop()
    pop()
    
def makered( *vars ):
    parallel()
    for i in vars:
        smooth( 0.25, i, red )
    end()

def makeblack( *vars ):
    parallel()
    for i in vars:
        smooth( 0.25, i, black )
    end()


bg = Fill( color = white )
tx = Text( Rect(0, 260, 400, 300), justify = 0.5, _alpha = 0.0, color = titlecolor,
           font = fonts['bold'], size = 20 )

def overview_diagram():
    d1v = viewport.interp( Rect(0,0,400,280), Rect(210,0,400,280) )
    d1 = Drawable( d1v, square, _alpha = 0.0 )
    
    dl = Drawable( Rect(10, 0, 210, 280), square_code, _alpha = 0.0 )
    
    camera = start_animation( bg, tx, d1, dl )
    set( tx.text, 'Parameterized diagram' )

    fade_in( 0.5, d1, tx )

    pause()
    smooth( 1.0, d1.size, 1.0 )
    
    pause()

    # move each slider up in turn
    smooth( 1.0, d1.redden, 1.0 )
    wait( 0.25 )
    smooth( 1.0, d1.rotation, 1.0 )
    wait( 0.25 )
    smooth( 1.0, d1.triangle, 1.0 )
    
    pause()

    # twiddle the sliders together
    parallel()
    serial()
    smooth( 1.0, d1.size, 0.25 )
    smooth( 2.0, d1.size, 0.75 )
    smooth( 1.0, d1.size, 1.0 )
    end()
    serial()
    for i in range(10):
        linear( 0.2, d1.rotation, (9-i)*0.1 )
        wait( 0.2 )
    end()
    serial()
    smooth( 1.33, d1.redden, 0.25 )
    smooth( 1.33, d1.redden, 0.75 )
    smooth( 1.33, d1.redden, 0.0 )
    end()
    serial( 1.0 )
    linear( 2.0, d1.triangle, 0.5 )
    end()
    end()

    pause()

    smooth( 1.0, d1v.x, 1.0 )
    wait( -0.5 )
    fade_in( 0.5, dl )

    pause()
    makered( dl.color1 )
    pause()
    makered( dl.color3 )
    pause()

    linear( 3.0, d1.redden, 1.0 )

    pause()

    fade_out( 0.5, d1, dl, tx )

    return end_animation()
overview_diagram = overview_diagram()

def overview_script():
    dt = Drawable( Rect(0,0,400,140), squareanim_code )
    dp = Drawable( Rect(0,140,400,260), sample_slide, _alpha = 0.0 )
    
    camera = start_animation( bg, tx, dp, dt )
    
    set( tx.text, 'Animation script' )
    set( dt.color0, white )
    set( dt.color1, white )
    set( dt.color2, white )
    set( dt.color3, white )
    set( dt.color4, white )
    set( dt.color5, white )
    set( dt.color6, white )
    
    set( dp._alpha, 1 )
    set( tx._alpha, 1 )

    makered( dt.color0 )
    wait( 0.25 )
    smooth( 0.5, dp.slidestate, 1 )
    pause()
    makeblack( dt.color0 )
    makered( dt.color1 )
    wait( 0.25 )
    smooth( 0.5, dp.slidestate, 2 )
    pause()
    makeblack( dt.color1 )
    makered( dt.color2 )
    wait( 0.25 )
    smooth( 0.5, dp.slidestate, 3 )
    pause()
    makeblack( dt.color2 )

    makered( dt.color3 )
    wait( 0.25 )
    smooth( 0.5, dp.diagram, 1.0 )

    pause()

    makeblack( dt.color3 )
    makered( dt.color4 )
    pause()
    smooth( 2.0, dp.size, 1.0 )
    pause()
    makeblack( dt.color4 )
    makered( dt.color5 )
    linear( 1.0, dp.triangle, 0.5 )
    pause()
    makeblack( dt.color5 )
    makered( dt.color6 )
    pause()
    parallel()
    smooth( 2.0, dp.redden, 1.0 )
    smooth( 2.0, dp.rotation, 1.0 )
    end()
    makeblack( dt.color6 )

    return end_animation()
overview_script = overview_script()
overview_one = overview_script[0].anim

box = Path().moveto(-4,-3).lineto(4,-3).lineto(4,3).lineto(-4,3).closepath()
pointer0 = Path().moveto( 7, 2 ).arcn( 5, 2, 0, 270, 2 )
pointer1 = Path().moveto( 7.5, 0 ).lineto( 5, 0 )
pointer2 = Path().moveto( -5, 0 ).arc( -5, -2, 90, 180, 2 )

titlefillcolor = titlecolor.interp( white, 0.9 )

cameras = {
   'default' : Rect(-15.614556387360389, -5.7934550346055573, 30.803822837813261, 0, 2.7027027027027022),
   'both' : Rect(-9.2227631485141384, -5.7934550346055573, 30.803822837813261, 0, 2.7027027027027022),
   'box1' : Rect(-4, -3, 8, 0, 4.0/3.0),
   'box2' : Rect(8, -3, 8, 0, 4.0/3.0),
}

def block_diagram( box2 = (SCALAR,0,1),
                   fadebox1 = (SCALAR,0,1),
                   fadebox2 = (SCALAR,0,1),
                   box1anim = (OBJECT, overview_diagram[1]),
                   box2anim = (OBJECT, overview_script[1]),
                   fadeframe = (SCALAR, 0, 1, 1),
                   arrow0 = (SCALAR,0,1,0),
                   arrow1 = (SCALAR,0,1,0),
                   arrow2 = (SCALAR,0,1,0),
                   interaction = (BOOLEAN,0),
                   cam = (OBJECT, cameras['default'])
                   ):
    set_camera( cam )
    
    if interaction:
        box2label = 'interactive\ncontroller'
        arrow0label = 'mouse,\nkeyboard,\ntime'
    else:
        box2label = 'animation\nscript'
        arrow0label = 'time'
    
    if fadebox1 < 1.0:
        color( titlefillcolor )
        fill( box )
        color( titlecolor )
        text( 0, 0, 'parameterized\ndiagram', fonts['bold'], justify = 0.5 )
    if fadebox1 > 0.0:
        embed_object( Rect(-4,-3,4,3), box1anim, { 't' : 0.0 }, _alpha = fadebox1 )
    color( black, fadeframe )
    widestroke( box, 0.15 )

    color( black, arrow1 )
    widestroke( pointer1, 0.15 )
    arrow( pointer1, (0,0.8,0.5) )
    text( 6, -0.75, 'parameter\nvalues', fonts['italic'], justify = 0.5, anchor = 'n', size = 0.7 )

    color( black, arrow2 )
    widestroke( pointer2, 0.15 )
    arrow( pointer2, (0,0.8,0.5) )
    text( -7, -3, 'drawing\ncommands', fonts['italic'], justify = 0.5, anchor = 'n', size = 0.7 )
    
    translate( 12, 0 )

    color( black, arrow0 )
    widestroke( pointer0, 0.15 )
    arrow( pointer0, (0,0.8,0.5) )
    text( 7, 2.4, arrow0label, fonts['italic'], justify = 0.5, anchor = 's', size = 0.7 )

    if box2 > 0.0 and fadebox2 < 1.0:
        color( titlefillcolor, box2 )
        fill( box )
        color( titlecolor, box2 )
        text( 0, 0, box2label, fonts['bold'], justify = 0.5 )
    if box2 > 0.0 and fadebox2 > 0.0:
        embed_object( Rect(-4,-3,4,3), box2anim, { 't' : 0.0 }, _alpha = fadebox2 * box2 )
    color( black, box2 * fadeframe )
    widestroke( box, 0.15 )

title = Text( Rect(20,260,380,280), color = titlecolor, font = fonts['bold'],
              _alpha = 0.0, size = 24 )
bl = BulletedList( Rect(20,0,380,240), font = fonts['text'], color = black,
                   size = 18.0, _alpha = 0.0, bullet = [fonts['dingbats'],'w'] )
    
def approach():
    dv = viewport.interp( Rect(0,-20,400,200), Rect(0,0,400,300) )
    d = Drawable( dv, block_diagram, _alpha = 0.0 )
    camera = start_animation( bg, title, bl )

    set( title.text, 'Slithy\'s approach' )
    
    bl.add_item( 0, ['Instead of animating graphical primitives,',
                     RESET, ' animate ', fonts['bolditalic'], titlecolor, 'parameterized diagrams.'] )
    
    fade_in( 0.5, title, bl )

    wait( 0.5 )
    enter( d )
    fade_in( 0.5, d )

    pause()

    smooth( 0.5, d.arrow1, 1.0 )
    pause()
    smooth( 0.5, d.arrow2, 1.0 )
    pause()

    bl.add_item( 0, ['Then, drive those diagrams from an ', fonts['bolditalic'], titlecolor, 'animation script.'] )
    parallel()
    smooth( 1.0, d.cam, cameras['both'] )
    smooth( 1.0, d.box2, 1.0 )
    serial( 0.75 )
    smooth( 0.5, d.arrow0, 1.0 )
    end()
    end()

    pause()

    parallel()
    smooth( 1.0, d.cam, cameras['box1'] )
    smooth( 1.0, dv.x, 1.0 )
    smooth( 1.0, d.fadebox1, 1.0 )
    serial( 0.75 )
    smooth( 0.25, d.fadeframe, 0.0 )
    end()
    end()

    pause()

    set( d.box1anim, overview_diagram[-1] )
    parallel()
    smooth( 1.0, d.cam, cameras['both'] )
    smooth( 1.0, dv.x, 0.0 )
    smooth( 1.0, d.fadebox1, 0.0 )
    smooth( 0.25, d.fadeframe, 1.0 )
    end()

    pause()

    parallel()
    smooth( 1.0, d.cam, cameras['box2'] )
    smooth( 1.0, dv.x, 1.0 )
    smooth( 1.0, d.fadebox2, 1.0 )
    serial( 0.75 )
    smooth( 0.25, d.fadeframe, 0.0 )
    end()
    end()

    pause()

    set( d.box2anim, overview_script[-1] )
    parallel()
    smooth( 1.0, d.cam, cameras['both'] )
    smooth( 1.0, dv.x, 0.0 )
    smooth( 1.0, d.fadebox2, 0.0 )
    smooth( 0.25, d.fadeframe, 1.0 )
    end()

    pause()

    fade_out( 0.5, title, bl, d )

    return end_animation()
approach = approach()

def interaction_approach():
    d = Drawable( Rect(0,-20,400,200), block_diagram, _alpha = 0.0 )
    
    start_animation( bg, title, bl, d )

    set( title.text, 'Interactive controllers' )
    
    bl.add_item( 0, 'Diagrams can be driven by interactive controllers instead of prescripted animations.' )
    
    fade_in( 0.5, title, bl )

    set( d.cam, cameras['both'] )
    set( d.box2, 1.0 )
    set( d.arrow0, 1.0 )
    set( d.arrow1, 1.0 )
    set( d.arrow2, 1.0 )
    fade_in( 0.5, d )

    pause()

    parallel()
    smooth( 0.5, d.box2, 0.0 )
    smooth( 0.5, d.arrow0, 0.0 )
    smooth( 0.5, d.arrow1, 0.0 )
    end()

    set( d.interaction, 1 )

    parallel()
    smooth( 0.5, d.box2, 1.0 )
    smooth( 0.5, d.arrow0, 1.0 )
    smooth( 0.5, d.arrow1, 1.0 )
    end()

    pause()

    fade_out( 0.5, d, title, bl )

    return end_animation()
interaction_approach = interaction_approach()


#test_objects( approach )
test_objects( interaction_approach, approach[:5], overview_diagram[1:-1], approach[5:7], overview_script[1:-1], approach[7:], block_diagram, square, square_code, squareanim_code, sample_slide )




