from slithy.library import *

import facets

import slithy.slidereader as slidereader
images = slidereader.image_library['default']
fonts = slidereader.font_library['default']


import common


def star(c = ('scalar',0.0,1.0)):

    set_camera(Rect(0,0,1,1))

    color(yellow.interp(red,c))

    polygon(0.1,0, 0.5,0.3, 0.8,0, 0.7,0.5, 1.0,0.75, 0.6,0.7, 0.5,1, 0.4,0.69, 0,0.8, 0.2,0.5) 

    


def awesome_diag(x = ('scalar',0.0,1.0), y = ('scalar',0.0,1.0), z = ('scalar',0.0,1.0),c = ('scalar',0.0,1.0), v = ('scalar',0.0,1.0)):

    set_camera(Rect(0,0,1,1))
    r = Rect(0.1,0.7,0.25,360.0*z,1.0)
    r1 = Rect(0.7,0.1,0.1,360.0*(1.0-v),1.0)
    embed_object(r,star, {'c':x})
    embed_object(r1,star, {'c':1.0-x})

    color(yellow)
    text( 0.5, 0.70, 'One big FAD would be', font = fonts['title'], size = 0.1, anchor = 'c', justify = 0.5 )

    color(yellow.interp(red,c))
    text( 0.5, 0.40, 'AWESOME!', font = fonts['title'], size = 0.1+y*0.1, anchor = 'c', justify = 0.5 )



# interaction which spins the drawable 
class spin(Controller):
    def create_objects( self ):
        self.d = Drawable( None, awesome_diag, _alpha = 0.0 )
        return self.d

    def start( self ):
        fade_in( 0.5, self.d )
        wait(-0.5)
        Undulation(style='sin')(self.d.x,min=0.0,max=1.0,period=3.0)
        Undulation(style='sawup')(self.d.c,min=0.0,max=1.0,period=0.25)
        Undulation(style='sin')(self.d.y,min=0.0,max=1.0,period=0.8)
        Undulation(style='sin')(self.d.z,min=0.0,max=1.0,period=2.0)
        Undulation(style='sawup')(self.d.v,min=0.0,max=1.0,period=1.0)



def awesome_anim():

    d = Interactive( get_camera(),
                      controller = spin)

    #d1 = Drawable( get_camera().bottom(0.5), awesome_diag, _alpha = 0.0 )

    start_animation( common.bg,d)

    fade_in(0.5,d)
    #fade_in(1.0,d1)

    wait(3.0)
  
    #pause()
    
    return end_animation() 

awesome_anim = awesome_anim()
