from slithy.library import *
from slithy.util import *
import random
import math
from fonts import fonts

i_cameras = (
    Rect(-2.6166666666666671, -2.0333333333333337, 10, 0, 1),
    Rect(-2.9333333333333345, -3.5333333333333341, 10, 0, 1),
    Rect(3.4623819824800712, -4.0332262131584855, 7.1451564169086206, 32.903102400913447, 1.3333333333333333),
    Rect(-3.3923839067116344, -0.200395339092998, 6.3950941288350958, 0, 1.3333333333333333),
)

def infinite_canvas( grid = (SCALAR, 0, 1),
                     expand = (SCALAR, 0, 1),
                     cam = (SCALAR, 0, 3),
                     ):
    set_camera( interp_cameralist( cam, i_cameras ) )
    #clear( white )
    
    if grid:
        thickness( 0.03 )
        color( 0.9, grid )
        for i in range(-5,11):
            line( i,-5, i,10 )
            line( -5,i, 10,i )
        thickness( 0.05 )
        line( 0,-5, 0,10 )
        line( -5,0, 10,0 )

    push()
    color( red, 0.2 )
    for i in range(5):
        rectangle( 1,0, 3,4 )
        translate( expand * 0.17, expand * 0.25 )
    pop()

    push()
    color( green, 0.2 )
    for i in range(5):
        dot( 1, -1.5, 2.5 )
        scale( 1 - 0.1 * expand, 1 - 0.15 * expand )
    pop()

    push()
    color( blue, 0.2 )
    translate( 6, -1 )
    for i in range(5):
        polygon( -1,-0.5, 1,-0.5, 0,3 )
        rotate( expand * -15 )
    pop()
        

        
            
    


test_objects( infinite_canvas )

    
    
                
        
