from slithy.library import *
from slithy.util import *
from fonts import fonts
import math

p_cameralist = (
   Rect(-1.6902989943596083, -0.74708253316098538, 11.876188565032392, 0, 1),  # default
   Rect(-0.50129427884517952, -1.7898585820799475, 12.640660989814032, 0, 1),  # bigblue
   Rect(-1.4493438530812313, -1.2210288375383163, 12.640660989814032, 0, 1),     # equal
   )

def pythagoras_d( a = (SCALAR,1,6,2.565), b = (SCALAR,1,6,4.080),
                  slidea=(SCALAR,0,3), slideb=(SCALAR,0,3),
                  linealpha = (SCALAR,0,1),
                  lineextend = (SCALAR,0,1),
                  subdivide = (SCALAR,0,1),
                  textlabel = (SCALAR,0,1),
                  cam = (SCALAR, 0, 2),
                  ):
    clear( white )
    set_camera( interp_cameralist( cam, p_cameralist ) )

    shear1a, rotatea, shear2a = split_sequence( 3, slidea/3.0 )
    shear1b, rotateb, shear2b = split_sequence( 3, slideb/3.0 )
    
    c = math.sqrt( a*a + b*b )
    afrac = (a*a) / float(c*c)
    bfrac = 1-afrac

    #clear( 1, 1, 1 )
    thickness( 0.06 )
    
    color( 0, 0.0, 0.5 )
    polygon( 0,b, a,b, a,b+a, 0,b+a )

    color( 0.8, 0, 0 )
    polygon( a,0, a+b,0, a+b,b, a,b )

    color( 0, 0.7, 0 )
    polygon( a+b,b, a+a+b,b+b, a+a,a+b+b, a,a+b )

    color( 0.5, 0, 0.7, subdivide )
    push()
    rotate( rotateb * 90, a+b, b )
    polygon( a+b,b,
             a+b - (bfrac+afrac*shear1b)*b, b + (bfrac*(1-shear1b))*a,
             a+a+b - (bfrac+afrac*shear1b)*b - a*shear2b, b+b + (bfrac*(1-shear1b))*a,
             a+a+b - a*shear2b, b+b )
    pop()

    color( 1, 0.8, 0, subdivide )
    push()
    rotate( rotatea * -90, a, a+b )
    polygon( a,a+b,
             a+(afrac*(1-shear1a))*b, a+b-(afrac+bfrac*shear1a)*a,
             a+a+(afrac*(1-shear1a))*b, a+b+b-(afrac+bfrac*shear1a)*a - shear2a*b,
             a+a,a+b+b - shear2a*b )
    pop()

    if linealpha > 0.0:
        color( 0, 0, 0, linealpha )
        line( a,b, a+a*lineextend+afrac*b, a+b*lineextend+b-afrac*a )
        line( a+(afrac+0.05)*b,a+b-(afrac+0.05)*a,
              a*0.95+(afrac+0.05)*b,a+b*0.95-(afrac+0.05)*a,
              a*0.95+afrac*b,a+b*0.95-afrac*a )

    if textlabel > 0.0:
        color( 1, textlabel )
        text( a/2.0,b+a/2.0, 'a', fonts['text'], size = 1.0, anchor = 'e' )
        text( a/2.0+0.05,b+a/2.0+0.05, '2', fonts['text'], size = 0.6, anchor = 'sw' )
        
        text( a+b/2.0,b/2.0, 'b', fonts['text'], size = 1.0, anchor = 'e' )
        text( a+b/2.0+0.05,b/2.0+0.05, '2', fonts['text'], size = 0.6, anchor = 'sw' )
    
        text( a+(a+b)/2.0, b+(a+b)/2.0, 'c', fonts['text'], size = 1.0, anchor = 'e' )
        text( a+(a+b)/2.0+0.05, b+(a+b)/2.0+0.05, '2', fonts['text'], size = 0.6, anchor = 'sw' )

rectangle_color = Color(0.8,1.0)
dissection_color2 = Color(0.3, 0.4, 0.9, 0.5)
dissection_color1 = Color(0.8, 0.0, 0.0, 0.5)

s_cameras = (
    Rect(-2.7484788674869685, -2.4877421969747844, 11.670606681171915, 0, 1.2966666666666666), # default
    Rect(-0.61407966731115682, -3.1694518700460206, 13.97752964115587, 0, 1.3333333333333333), # slideleft
    Rect(-0.99846173244294312, -2.0163056746506607, 13.97752964115587, 0, 1.3333333333333333), # tallrectangle
    Rect(-5.7333498983844944, -2.0163056746506607, 13.97752964115587, 0, 1.3333333333333333), # centertall
)


def shear_dissection_d( b=(SCALAR,0,10,6), h=(SCALAR,0,10,4),
                        shear=(SCALAR,-30,30,0),
                        shearline=(SCALAR,0,1),
                        dissection=(SCALAR,0,1),
                        shift=(SCALAR,0,1),
                        cam=(SCALAR, 0, 3),
                        ):
    set_camera( interp_cameralist( cam, s_cameras ) )
    
    clear( 1, 1, 1 )
    thickness( 0.03 )
    
    b = float(b)
    h = float(h)
    shear = float(shear)

    color( rectangle_color )
    rectangle( 0, 0, b, h )

    if dissection == 0.0:
        color( dissection_color1 )
        polygon( shear, 0, shear+b, 0, b, h, 0, h )
    else:
        paths = []
        sections = int(math.ceil((b + shear) / b))

        # first section
        p = Path()
        if sections > 2:
            p.moveto( 0,h ).lineto( b,h ).lineto( b,h*(shear-b)/shear ).closepath()
        else:
            p.moveto( 0,h ).lineto( b,h ).lineto( b,0 ).lineto( shear,0 )
        paths.append( p )

        # middle sections
        for i in range(1,sections-1):
            x1 = i * b
            x2 = (i+1) * b
            p = Path()
            p.moveto( x1, h * (shear+b - x1) / shear ).lineto( x2, h * (shear+b - x2) / shear )
            if i == sections-2:
                p.lineto( x2, 0 ).lineto( shear, 0 )
            else:
                p.lineto( x2, h * (shear - x2) / shear )
            p.lineto( x1, h * (shear - x1) / shear )
            p.closepath()
            paths.append( p )

        # last section
        p = Path()
        x = (sections-1) * b
        p.moveto( x,0 ).lineto( b+shear,0 ).lineto( x, (h*(shear+b-x)) / shear ).closepath()
        paths.append( p )

        shifts = (0,) + split_sequence_smooth( sections-1, shift, 0.8 )
        #shifts = (0,) + (shift,) * (sections-1)
        i = 0
        for p,s in zip(paths,shifts):
            if i % 2 == 0:
                color( dissection_color1 )
            else:
                color( dissection_color1.interp( dissection_color2, dissection ) )

            push()
            translate( -s * (i*b), 0 )
            fill( p )
            pop()

            i += 1

    if shearline > 0.0:
        color( 0, shearline )
        line( -100, 0, 100, 0 )

# sa_cameras = (
#     Rect(2.9402, 2.0388, width=5.7358, height=5.7358), # default
#     Rect(9.5455, 2.0388, width=9.5797, height=9.5797), # zoomout
# )

# def shear_algebra( b=(SCALAR,0,10,6), h=(SCALAR,0,10,4),
#                    shear=(SCALAR,-30,30,0),
#                    shearline=(SCALAR,0,1),
#                    labels = (SCALAR,0,1),
#                    cam = (SCALAR, 0, 1),
#                    ):
#     set_camera( interp_cameralist( cam, sa_cameras ) )
#     clear( 1, 1, 1 )

#     b = float(b)
#     h = float(h)
#     shear = float(shear)

#     color( rectangle_color )
#     rectangle( 0, 0, b, h )

#     color( dissection_color1 )
#     polygon( shear, 0, shear+b, 0, b, h, 0, h )

#     if shearline > 0.0:
#         color( 0, shearline )
#         thickness( 0.03 )
#         line( -100, 0, 100, 0 )

#     if labels > 0.0:
#         color( 0, labels )
#         thickness( 0.05 )

#         text( -1.0, h/2.0, 'h', fonts['text'] )
#         line( -1.3, h, -0.7, h )
#         line( -1.0, h, -1.0, h/2 + 0.7 )
#         line( -1.0, 0, -1.0, h/2 - 0.7 )
#         line( -1.3, 0, -0.7, 0 )

#         push()
#         translate( shear, 0 )
#         text( b/2.0, -1.0, 'b', fonts['text'] )
#         line( 0, -1.3, 0, -0.7 )
#         line( b, -1.3, b, -0.7 )
#         line( 0, -1.0, b/2-0.7, -1.0 )
#         line( b, -1.0, b/2+0.7, -1.0 )
#         pop()

#         text( b/2.0, h+1.5, 'area = bh', fonts['text'] )

t_cameras = (
    Rect(1.2408820154740305, 2.2038921242810408, 5.8158900692812407, 0, 1), # default
    Rect(-1.6902989943596083, -0.74708253316098538, 11.876188565032392, 0, 1), # expand
)
                      
def triangle_to_area( a = (SCALAR,1,6,2.565),
                      b = (SCALAR,1,6,4.080),
                      a_show = (SCALAR,0,1),
                      b_show = (SCALAR,0,1),
                      c_show = (SCALAR,0,1),
                      a_label = (SCALAR,0,1),
                      b_label = (SCALAR,0,1),
                      c_label = (SCALAR,0,1),
                      a2_label = (SCALAR,0,1),
                      b2_label = (SCALAR,0,1),
                      c2_label = (SCALAR,0,1),
                      cam = (SCALAR, 0, 1),
                      label_offset = (SCALAR,0,1),
                      ):

    set_camera( interp_cameralist( cam, t_cameras ) )
    clear( 1, 1, 1 )

    thickness( 0.03 )

    color( 0 )
    line( a,b+0.2, a+0.2,b+0.2, a+0.2,b )
    
    if a_show < 1.0:
        color( 0, 0.0, 0.5 )
        line( a,b, a,b+a )

    if b_show < 1.0:
        color( 0.8, 0, 0 )
        line( a,b, a+b,b )

    if c_show < 1.0:
        color( 0, 0.7, 0 )
        line( a,b+a, a+b,b )

    color( 0, 0.0, 0.5 )
    a_rotation, a_drag = split_sequence( 2, a_show )
    if a_rotation <= 1.0:
        push()
        translate( a, b )
        rotate( 90 * a_rotation )
        line( 0,0, 0,a )
        pop()
    if a_drag > 0.0:
        polygon( 0,b, a,b, a,b+a*a_drag, 0,b+a*a_drag )

    color( 0.8, 0, 0 )
    b_rotation, b_drag = split_sequence( 2, b_show )
    if b_rotation <= 1.0:
        push()
        translate( a, b )
        rotate( -90 * b_rotation )
        line( b,0, 0,0 )
        pop()
    if b_drag > 0.0:
        polygon( a,0, a,b, a+b*b_drag,b, a+b*b_drag,0 )

    color( 0, 0.7, 0 )
    c_rotation, c_drag = split_sequence( 2, c_show )
    if c_rotation <= 1.0:
        push()
        translate( a+b, b )
        rotate( -90 * c_rotation )
        line( -b,a, 0,0 )
        pop()
    if c_drag > 0.0:
        polygon( a+b,b, a+b+a,b+b, a+b+a-b*c_drag, b+b+a*c_drag, a+b+-b*c_drag, b+a*c_drag )

    translate( label_offset * b * 3, label_offset * a * 2 )

    if a2_label > 0.0:
        color( 1, a2_label )
        text( a/2.0,b+a/2.0, 'a', fonts['text'], size = 1.0, anchor = 'e' )
        text( a/2.0+0.05,b+a/2.0+0.05, '2', fonts['text'], size = 0.6, anchor = 'sw' )
        
    if a_label > 0.0:
        color( 0, 0, 0.5, a_label )
        text( a - 0.5,b+a/2.0, 'a', fonts['text'], size = 1.0, anchor = 'e' )
        
    if b2_label > 0.0:
        color( 1, b2_label )
        text( a+b/2.0,b/2.0, 'b', fonts['text'], size = 1.0, anchor = 'e' )
        text( a+b/2.0+0.05,b/2.0+0.05, '2', fonts['text'], size = 0.6, anchor = 'sw' )
    
    if b_label > 0.0:
        color( 0.8, 0, 0, b_label )
        text( a+b/2.0,b - 0.5, 'b', fonts['text'], size = 1.0, anchor = 'n' )
    
    if c2_label > 0.0:
        color( 1, c2_label )
        text( a+(a+b)/2.0, b+(a+b)/2.0, 'c', fonts['text'], size = 1.0, anchor = 'e' )
        text( a+(a+b)/2.0+0.05, b+(a+b)/2.0+0.05, '2', fonts['text'], size = 0.6, anchor = 'sw' )
        
    if c_label > 0.0:
        color( 0, 0.7, 0, c_label )
        text( a+b/2.0+0.3, b+a/2.0+0.3, 'c', fonts['text'], size = 1.0, anchor = 'sw' )


def standard_triangle( a, b, a_label, b_label, c_label, angle, alpha ):
    #color( 0 )
    #line( a,b+0.2, a+0.2,b+0.2, a+0.2,b )

    color( 0, 0.0, 0.5, alpha )
    line( a,b, a,b+a )

    color( 0.8, 0, 0, alpha )
    line( a,b, a+b,b )
        
    color( 0, 0.7, 0, alpha )
    line( a,b+a, a+b,b )

    if a_label > 0.0:
        push()
        translate( a - 0.5, b+a/2.0 )
        rotate( -angle )
        color( 0, 0, 0.5, a_label )
        text( 0, 0, 'a', fonts['text'], size = 1.0, anchor = 'e' )
        pop()
        
    if b_label > 0.0:
        push()
        translate( a+b/2.0, b - 0.5 )
        rotate( -angle )
        color( 0.8, 0, 0, b_label )
        text( 0, 0, 'b', fonts['text'], size = 1.0, anchor = 'n' )
        pop()
    
    if c_label > 0.0:
        push()
        translate( a+b/2.0+0.3, b+a/2.0+0.3 )
        rotate( -angle )
        color( 0, 0.7, 0, c_label )
        text( 0, 0, 'c', fonts['text'], size = 1.0, anchor = 'sw' )
        pop()
        

sd_cameralist = [
   Rect(-1.6902989943596083, -0.74708253316098538, 11.876188565032392, 0, 1),  # default
   None,
   ]
   


def square_dissection( a = (SCALAR,1,6,2.565),
                       b = (SCALAR,1,6,4.080),
                       copies = (SCALAR,0,1),
                       a_label = (SCALAR,0,1),
                       b_label = (SCALAR,0,1),
                       c_label = (SCALAR,0,1),
                       show_c2 = (SCALAR,0,1),
                       cam = (SCALAR,0,1),
                       compress = (SCALAR,0,1),
                       compress2 = (SCALAR,0,1),
                       show_ab = (SCALAR,0,1),
                       hide_tri = (SCALAR,0,1),
                       ):

    sd_cameralist[1] = Rect( a+(a+b)/2.0, b+(a+b)/2.0, width = a+b, height = a+b ).outset( 0.3 ) 

    set_camera( interp_cameralist( cam, sd_cameralist ) )
    thickness( 0.05 )

    standard_triangle( a, b, a_label, b_label, c_label, 0, 1.0 - hide_tri )

    a_label = b_label = c_label = 0

    if copies > 0:
        if copies > 1.0/3.0:
            push()
            rotate( 90, a+(a+b)/2,b+(a+b)/2 )
            if compress2 < a/(a+b):
                translate( compress2 * (a+b), 0 )
            else:
                translate( a, (compress2 - (a/(a+b))) * (a+b) )
                
            standard_triangle( a, b, a_label, b_label, c_label, 90, 1.0 - hide_tri )
            pop()
        if copies > 2.0/3.0:
            push()
            rotate( 180, a+(a+b)/2,b+(a+b)/2 )
            translate( compress * a, compress * b )
            standard_triangle( a, b, a_label, b_label, c_label, 180, 1.0 - hide_tri )
            pop()
        
        push()
        rotate( 270 * copies, a+(a+b)/2,b+(a+b)/2 )
        standard_triangle( a, b, a_label, b_label, c_label, 270 * copies, 1.0 - hide_tri )
        pop()


    if show_c2 > 0.0:
        f, t = split_sequence_smooth( 2, show_c2 )
        color( 0, 0.7, 0, f )
        polygon( a+b, b,
                 a+b+a, b+b,
                 a+a, b+b+a,
                 a, a+b )
        color( white, t )
        text( a+(a+b)/2.0, b+(a+b)/2.0, 'c', fonts['text'], size = 1.0, anchor = 'e' )
        text( a+(a+b)/2.0+0.05, b+(a+b)/2.0+0.05, '2', fonts['text'], size = 0.6, anchor = 'sw' )

    if show_ab > 0.0:
        af, at, bf, bt = split_sequence_smooth( 4, show_ab )
        
        color( 0, 0.0, 0.5, af )
        rectangle( a+b, b, a+b+a, b+a )
        color( white, at )
        text( a+b+a/2.0, b+a/2.0, 'a', fonts['text'], size = 1.0, anchor = 'e' )
        text( a+b+a/2.0+0.05, b+a/2.0+0.05, '2', fonts['text'], size = 0.6, anchor = 'sw' )
        
        color( 0.8, 0.0, 0.0, bf )
        rectangle( a+a, b+a, a+b+a, b+a+b )
        color( white, at )
        text( a+a+b/2.0, b+a+b/2.0, 'b', fonts['text'], size = 1.0, anchor = 'e' )
        text( a+a+b/2.0+0.05, b+a+b/2.0+0.05, '2', fonts['text'], size = 0.6, anchor = 'sw' )

        
#  square_dissection.cameras = {
#      'default' : (3.9424, 4.9469, 2.639),
#      'full' : (5.9319, 7.3374, 4.7239),
#      }




###
### animations
###


def square():
    c = get_camera()
    v1 = viewport.interp( c, c.right(0.5) )
    v2 = viewport.interp( c, c.left(0.5) )
    
    d1 = Drawable( v1, square_dissection, a_label = 1, b_label = 1, c_label = 1, cam = 1 )
    d2 = Drawable( v2, square_dissection, a_label = 1, b_label = 1, c_label = 1, cam = 1, copies = 1 )
    eq = Text( get_camera(), text = '=', size = 40, justify = 0.5, vjustify = 0.475, font = fonts['text'], _alpha = 0.0 )

    start_animation( d1 )

    #smooth( 1.0, d1.cam, 1.0 )
    #pause()
    smooth( 3.0, d1.copies, 1.0 )
    pause()

    enter( d2 )
    parallel()
    smooth( 1.0, v1.x, 1.0 )
    smooth( 1.0, v2.x, 1.0 )
    end()
    enter( eq )
    fade_in( 0.5, eq )

    pause()
    smooth( 1.0, d1.show_c2, 1.0 )
    pause()
    
    smooth( 1.0, d2.compress, 1.0 )
    smooth( 1.0, d2.compress2, 1.0 )
    smooth( 2.0, d2.show_ab, 1.0 )
    pause()

    parallel()
    smooth( 1.0, d1.hide_tri, 1.0 )
    smooth( 1.0, d2.hide_tri, 1.0 )
    smooth( 1.0, d1.a_label, 0.0 )
    smooth( 1.0, d1.b_label, 0.0 )
    smooth( 1.0, d1.c_label, 0.0 )
    smooth( 1.0, d2.a_label, 0.0 )
    smooth( 1.0, d2.b_label, 0.0 )
    smooth( 1.0, d2.c_label, 0.0 )
    end()

    return end_animation()
square = square()

    
    


def unfold( show, label1, label2 ):
    sequence()
    smooth( 0.5, show, 0.5 )
    parallel()
    smooth( 0.5, show, 1.0 )
    sequence()
    wait( 0.3 )
    set( label1, 0.0 )
    smooth( 0.25, label2, 1.0 )
    end()
    end()
    end()
    
def expand_triangle():
    d = Drawable( get_camera(), triangle_to_area, a_label = 1, b_label = 1, c_label = 1, cam = 1, label_offset = 1 )

    start_animation( d )

    pause()
    smooth( 2.0, d.label_offset, 0.0 )
    pause()

#     parallel()
#     smooth( 0.5, d.a_label, 1.0 )
#     smooth( 0.5, d.b_label, 1.0 )
#     smooth( 0.5, d.c_label, 1.0 )
#     end()
#     pause()

    parallel()
    unfold( d.a_show, d.a_label, d.a2_label )
    sequence( 0.5 )
    unfold( d.b_show, d.b_label, d.b2_label )
    end()
    sequence( 1.0 )
    unfold( d.c_show, d.c_label, d.c2_label )
    end()
    end()
 
    return end_animation()
expand_triangle = expand_triangle()    
    
def shear_dissection():
    d = Drawable( get_camera(), shear_dissection_d, _alpha = 0.0 )

    start_animation( d )

    fade_in( 0.5, d )
    pause()

    smooth( 0.5, d.shearline, 1.0 )
    wait( 0.5 )
    smooth( 0.5, d.shear, 1.0 )
    smooth( 1.0, d.shear, -2.0 )
    smooth( 1.0, d.shear, 2.76 )
    pause()

    smooth( 0.5, d.dissection, 1.0 )
    pause()

    linear( 1.0, d.shift, 1.0 )
    pause()

    linear( 0.5, d.shift, 0.0 )
    smooth( 0.5, d.dissection, 0.0 )

    smooth( 1.0, d.cam, 1.0 )
    
    smooth( 1.0, d.shear, 5.34 )
    pause()

    smooth( 0.5, d.dissection, 1.0 )
    linear( 0.5, d.shift, 1.0 )
    pause()

    linear( 0.25, d.shift, 0.0 )
    smooth( 0.25, d.dissection, 0.0 )
    smooth( 0.5, d.shear, 7.0 )
    pause()

    smooth( 0.5, d.shear, 0.0 )
    parallel()
    smooth( 1.0, d.cam, 2 )
    smooth( 1.0, d.b, 2.25 )
    smooth( 1.0, d.h, 6.6 )
    end()
    pause()

    smooth( 1.0, d.shear, 10.02 )
    pause()

    smooth( 1.0, d.dissection, 1.0 )
    pause()

    linear( 3.0, d.shift, 1.0 )
    pause()

    smooth( 1.0, d.shear, 3.9 )
    linear( 1.0, d.shift, 0.0 )
    smooth( 1.0, d.dissection, 0.0 )
    smooth( 1.0, d.shear, 0.0 )
    pause()

    smooth( 1.0, d.cam, 3 )
    smooth( 0.5, d.shear, 3.3 )
    smooth( 1.0, d.shear, -3.3 )
    smooth( 1.0, d.shear, 3.3 )
    pause()
    fade_out( 0.5, d )

    return end_animation()
shear_dissection = shear_dissection()    
    

def pythagoras():
    d = Drawable( get_camera(), pythagoras_d, textlabel = 1.0 )
    bg = Fill( color = white )

    start_animation( bg, d )

    #smooth( 0.5, d.textlabel, 0.0 )
    smooth( 0.5, d.linealpha, 1.0 )
    pause()

    smooth( 1.0, d.lineextend, 1.0 )
    pause()

    smooth( 1.0, d.subdivide, 0.8 )
    pause()

    smooth( 1.0, d.slidea, 1 )
    wait( 0.25 )
    smooth( 1.0, d.slidea, 2 )
    wait( 0.25 )
    smooth( 1.0, d.slidea, 3 )
    #pause()

    smooth( 2.0, d.slideb, 3 )

##     pause()

##     smooth( 1.0, d.subdivide, 0 )
##     pause()

##     parallel()
##     smooth( 2.0, d.a, 4.930 )
##     smooth( 2.0, d.b, 1.940 )
##     smooth( 2.0, d.cam, 1.0 )
##     end()
##     pause()

##     set( d.slidea, 0 )
##     set( d.slideb, 0 )
    
##     smooth( 1.0, d.subdivide, 0.8 )
##     smooth( 3.0, d.slidea, 3 )
##     smooth( 3.0, d.slideb, 3 )
##     smooth( 0.5, d.subdivide, 0 )
##     pause()

##     parallel()
##     smooth( 2.0, d.a, 3.34 )
##     smooth( 2.0, d.b, 3.485 )
##     smooth( 2.0, d.cam, 2.0 )
##     end()
##     pause()

##     set( d.slidea, 0 )
##     set( d.slideb, 0 )
    
##     smooth( 0.5, d.subdivide, 0.8 )
##     parallel()
##     smooth( 2.0, d.slidea, 3 )
##     sequence()
##     wait( 1.0 )
##     smooth( 2.0, d.slideb, 3 )
##     end()
##     end()
##     smooth( 0.5, d.subdivide, 0 )
##     pause()

##     fade_out( 0.5, d )

    return end_animation()
pythagoras = pythagoras()    

def proof_pair():
    c = get_camera()
    v1 = viewport.interp( c, c.move_right(1.0), c.right(0.5) )
    v2 = viewport.interp( c.move_left(1.0), c, c.left(0.5) )

    a1 = Anim( v1 )
    a2 = Anim( v2, anim = square[0] )

    start_animation( a1 )
    a1.play( expand_triangle )
    a1.play( pythagoras )
    pause()
    enter( a2 )
    parallel()
    smooth( 1.0, v1.x, 1.0 )
    smooth( 1.0, v2.x, 1.0 )
    end()
    exit( a1 )
    pause()
    a2.play( square )
    pause()
    enter( a1 )
    parallel()
    smooth( 1.0, v1.x, 2.0 )
    smooth( 1.0, v2.x, 2.0 )
    end()
    
    

    return end_animation()
proof_pair = proof_pair()
    
pythagoras_one = pythagoras[0].anim

#test_objects( triangle_to_area )            
#test_objects( square, square_dissection, expand_triangle, pythagoras )
#test_objects( proof_pair )
test_objects( pythagoras_one, pythagoras_d )


