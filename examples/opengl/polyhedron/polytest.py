from slithy.library import *

import polyhedron
import trackball

thefont = load_font( 'minion.slf' )

def my_diagram( theta = (SCALAR, 0, 360),
                spin = (SCALAR, 0, 360),
                ):
    set_camera( Rect( -1.5, -1.5, 1.5, 1.5 ) )

    rotate( theta )
    color( white )
    rectangle( -1, -1, 1, 1 )
    embed_object( Rect(-1,-1,1,1), polyhedron.draw, { 'angle' : spin,
                                                      'tri_color' : blue,
                                                      'pent_color' : yellow } )
    thickness( 0.1 )
    id( 5 )
    color( Color(0,0.7,0) )
    frame( -1, -1, 1, 1 )
    
class my_interaction(Controller):
    def create_objects( self ):
        self.colorscheme = 0
        self.rot = trackball.new()
        self.d = Drawable( None, polyhedron.draw, tri_color = red, pent_color = white,
                           trackball = self.rot, _alpha = 0.0, info = self )
        return self.d

    def start( self ):
        fade_in( 0.5, self.d )

    def key( self, k, x, y, m ):
        if k == 'a':
            self.colorscheme = (self.colorscheme + 1) % 3
            parallel()
            smooth( 0.5, self.d.tri_color, (red,yellow,Color(0,0,0.6))[self.colorscheme] )
            smooth( 0.5, self.d.pent_color, (white,green,Color(0,0.7,0.6))[self.colorscheme] )
            end()

        elif k == 'x':
            self.rot.reset()

    def mousedown( self, x, y, m ):
        x, y = unproject( x, y, self.coords )
        if 'control' in m:
            self.rot.spin_start( x, y )
        else:
            self.rot.rotate_start( x, y )

    def mousemove( self, x, y, m ):
        x, y = unproject( x, y, self.coords )
        self.rot.move( x, y )

    def mouseup( self, x, y, m ):
        x, y = unproject( x, y, self.coords )
        self.rot.end( x, y )
        
            
def my_animation():
    bg = Fill( style = 'horz', color2 = Color(0.5,0,0) )
    cap = Text( get_camera().bottom( 0.2 ).inset( 0.05 ),
                color = white, font = thefont, size = 16, _alpha = 0.0,
                justify = 0.5 )
    dv = viewport.interp( get_camera(),
                          get_camera().inset( 0.1 ).right( 0.5 ) )
    d = Drawable( dv, polyhedron.draw )
    d2v = viewport.interp( get_camera().inset( 0.1 ).left( 0.5 ),
                           get_camera().inset( 0.1 ).left( 0.5 ).top( 0.5 ) )
    d2 = Drawable( d2v, my_diagram, _alpha = 0.0 )

    d3 = Interactive( get_camera().inset( 0.1 ).left( 0.5 ).bottom( 0.5 ),
                      controller = my_interaction )

    start_animation( bg, d, cap )
    set( cap.text, 'Here is an OpenGL diagram embedded within an animation.' )
    fade_in( 0.5, cap )
    smooth( 6.0, d.angle, 360 )
    wait( -5.0 )
    smooth( 5.0, dv.x, 1.0 )
    wait( -0.5 )
    fade_out( 0.5, cap )
    set( cap.text, 'Here the OpenGL diagram is embedded within an ordinary parameterized diagram, which is then placed in the animation.' )
    enter( d2 )
    lift( cap )
    fade_in( 0.5, d2, cap )

    parallel()
    smooth( 6.0, d.angle, 0 )
    smooth( 6.0, d2.spin, 360 )
    smooth( 6.0, d2.theta, 45 )
    end()
    wait( -3 )
    smooth( 3, d2v.x, 1 )

    wait( -0.5 )
    fade_out( 0.5, cap )
    set( cap.text, "The third OpenGL diagram is run by an interactive controller.  You can spin it with the mouse, and use the 'a' key to change colors." )
    enter( d3 )
    lift( cap )
    fade_in( 0.5, cap )

    pause()

    fade_out( 0.5, cap )
    set( cap.text, "You can continue manipulating the interactive part as the animation runs." )
    fade_in( 0.5, cap )
    
    parallel()
    smooth( 6.0, d.angle, 720 )
    smooth( 6.0, d2.spin, 450 )
    smooth( 6.0, d2.theta, -60 )
    end()

    pause()

    exit( d3 )
    fade_out( 0.5, d, d2, cap )
    
    return end_animation()
my_animation = my_animation()

    
    
test_objects( my_diagram, my_interaction, polyhedron.draw, my_animation, clear_color = black )
