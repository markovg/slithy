from slithy.library import *
from math import *

thearrow = Path().moveto( 0,0 ).lineto( 4,3 ).lineto( 3.5,1 ).lineto( 10,2 ).lineto( 11,-2 ).lineto( 3.5,-1 ).lineto( 4,-3 ).closepath()

def arrow_diagram( x = (SCALAR, 0, 100, 0),
                   y = (SCALAR, 0, 100, 0),
                   fade = (SCALAR, 0, 1, 0),
                   angle = (SCALAR, 0, 360, 0),
           ):
    set_camera( Rect(0,0,100,100) )
    
    x, y = unproject( x, y )
    
    translate( x, y )
    rotate( angle )
    color( red, fade )
    fill( thearrow )

class Pointy(Controller):
    def get_arrow( self, x, y, angle ):
        if self.free:
            d = self.free.pop()
            set( d.x, x )
            set( d.y, y )
            set( d.angle, angle )
            set( d.fade, 1 )
        else:
            d = Drawable( None, arrow_diagram, x = x, y = y, angle = angle, fade = 1 )
        return d
    
    def start( self ):
        self.arrows = []
        self.free = []
        self.state = None
    
    def mousedown( self, x, y, m ):
        self.state = x, y

    def mouseup( self, x, y, m ):
        self.state = None

    def mousemove( self, x, y, m ):
        if self.state:
            sx, sy = self.state
            if (x-sx)*(x-sx) + (y-sy)*(y-sy) > 100:
                angle = atan2( y-sy, x-sx ) * 180.0 / pi
                d = self.get_arrow( x, y, angle )
                self.arrows.append( d )
                enter( d )
                self.state = None

    def key( self, k, x, y, m ):
        if k == 'a':
            parallel()
            for i in self.arrows:
                linear( 0.5, i.fade, 0.0 )
            end()
            exit( *self.arrows )
            
            self.free.extend( self.arrows )
            self.arrows = []
            
                
                
        

test_objects( Pointy, arrow_diagram )

    
