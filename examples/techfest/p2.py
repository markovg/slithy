from slithy.library import *
from slithy.util import *
from fonts import fonts
import math

def sheared_rectangle( b, h, shear, shift ):
    if shear == 0.0 or shift == 0.0:
        rectangle( 0, 0, b, h )
    else:
        push()
        if shear < 0.0:
            scale( -1, 1, b/2.0, 0 )
            shear = -shear
            
        
        paths = []
        sections = int(math.ceil((b + shear) / float(b)))

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

        shifts = (0,) + split_sequence_smooth( sections-1, 1-shift, 0.3 )
        i = 0
        for p,s in zip(paths,shifts):
            push()
            translate( -s * (i*b), 0 )
            fill( p )
            pop()

            i += 1

        pop()

def pythagoras( a = (SCALAR,1,5,2),
                slidea = (SCALAR, 0, 3),
                slideb = (SCALAR, 0, 3),
                linealpha = (SCALAR,0,1),
                lineextend = (SCALAR,0,1),
                subdivide = (SCALAR,0,1),
                textlabel = (SCALAR,0,1),
                info = (OBJECT),
                ):
    b = 6-a

    id( -1 )
    clear( white )
    set_camera( Rect( 0, 0, a+a+b, a+b+b ).outset( 0.1 ) )
    
    c = math.sqrt( a*a + b*b )
    af = (a*a) / (c*c)
    bf = 1.0 - af
    theta = math.atan2( a, b ) * 180.0 / math.pi
    
    color( 0, 0, 0.5 )
    rectangle( 0, b, a, a+b )

    color( 0.8, 0, 0 )
    rectangle( a, 0, a+b, b )

    color( 0, 0.7, 0 )
    push()
    translate( a, a+b )
    rotate( -theta )
    rectangle( 0, 0, c, c )
    pop()

    push()
    color( 1.0, 0.8, 0.0, subdivide )
    if slidea < 1.0:
        translate( a, a+b )
        rotate( 90-theta )
        translate( 0, -af * c )
        sheared_rectangle( c, af * c, -b*a/c, slidea )
    elif slidea < 2.0:
        translate( a, a+b )
        rotate( -90 * (slidea-1.0) )
        polygon( 0, 0, 0, -a, a, b-a, a, b )
    else:
        translate( 0, b )
        sheared_rectangle( a, a, b, 3.0-slidea )
    pop()

    push()
    color( 0.5, 0.0, 0.7, subdivide )
    if slideb < 1.0:
        translate( a, a+b )
        rotate( -90-theta )
        translate( -c, af*c )
        sheared_rectangle( c, bf * c, b*a/c, slideb )
    elif slideb < 2.0:
        translate( a+b, b )
        rotate( 90 * (slideb-1.0) )
        polygon( 0, 0, -b, 0, a-b, b, a, b )
    else:
        translate( a, b )
        rotate( -90 )
        sheared_rectangle( b, b, -a, 3.0-slideb )
    pop()
    
    if linealpha > 0.0:
        thickness( 0.06 )
        color( 0, 0, 0, linealpha )
        line( a,b, a+a*lineextend+af*b, a+b*lineextend+b-af*a )
        line( a+(af+0.05)*b,a+b-(af+0.05)*a,
              a*0.95+(af+0.05)*b,a+b*0.95-(af+0.05)*a,
              a*0.95+af*b,a+b*0.95-af*a )

    if textlabel > 0.0:
        color( 1, textlabel )
        text( a/2.0,b+a/2.0, 'a', fonts['text'], size = 1.0, anchor = 'e' )
        text( a/2.0+0.05,b+a/2.0+0.05, '2', fonts['text'], size = 0.6, anchor = 'sw' )
        
        text( a+b/2.0,b/2.0, 'b', fonts['text'], size = 1.0, anchor = 'e' )
        text( a+b/2.0+0.05,b/2.0+0.05, '2', fonts['text'], size = 0.6, anchor = 'sw' )
    
        text( a+(a+b)/2.0, b+(a+b)/2.0, 'c', fonts['text'], size = 1.0, anchor = 'e' )
        text( a+(a+b)/2.0+0.05, b+(a+b)/2.0+0.05, '2', fonts['text'], size = 0.6, anchor = 'sw' )

    id( 1 )
    color( invisible )
    dot( 0.5, a, b )

    if info:
        info.last_drawn = mark()
        
class PythagorasDemo(Controller):
    limit = 1.5
    
    def create_objects( self ):
        self.d = Drawable( None, pythagoras, textlabel=1, subdivide=0, linealpha=1, lineextend=1,
                           info = self )
        return self.d

    def start( self ):
        self.toggle = 1
        self.last_drawn = None
        
        d = self.d
        smooth( 1.0, d.subdivide, 0.8 )
        smooth( 1.0, d.slidea, 1 )
        smooth( 1.0, d.slidea, 2 )
        smooth( 1.0, d.slidea, 3 )
        smooth( 1.0, d.slideb, 1 )
        smooth( 1.0, d.slideb, 2 )
        smooth( 1.0, d.slideb, 3 )

    def key( self, k, x, y, m ):
        if k == 'a':
            if self.toggle:
                smooth( 0.5, self.d.subdivide, 0.0 )
                set( self.d.slidea, 0.0 )
                set( self.d.slideb, 0.0 )
                self.toggle = 0
            else:
                smooth( 1.0, self.d.subdivide, 0.8 )
                smooth( 1.0, self.d.slidea, 1 )
                smooth( 1.0, self.d.slidea, 2 )
                smooth( 1.0, self.d.slidea, 3 )
                smooth( 1.0, self.d.slideb, 1 )
                smooth( 1.0, self.d.slideb, 2 )
                smooth( 1.0, self.d.slideb, 3 )
                self.toggle = 1

    def mousedown( self, x, y, m ):
        if not self.last_drawn: return
        what, = query_id( x, y )

        if what:
            self.drag = 1
            x, y = unproject( x, y, self.last_drawn )
            a = x
            if self.limit > a:
                a = self.limit
            elif 6-self.limit < a:
                a = 6-self.limit
            print x, y, a, get(self.d.a)
            set( self.d.a, a )

    def mousemove( self, x, y, m ):
        if self.drag:
            x, y = unproject( x, y, self.last_drawn )
            a = x
            if self.limit > a:
                a = self.limit
            elif 6-self.limit < a:
                a = 6-self.limit
            set( self.d.a, a )
        
    def mouseup( self, x, y, m ):
        self.drag = 0
                
                
        
    

test_objects( PythagorasDemo, pythagoras )
