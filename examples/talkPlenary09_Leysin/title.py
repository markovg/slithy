from slithy.library import *

import facets

import slithy.slidereader as slidereader
images = slidereader.image_library['default']
fonts = slidereader.font_library['default']


import common

# interaction which spins the drawable 
class spin(Controller):
    def create_objects( self ):
        self.d = Drawable( None, facets.facets, _alpha = 0.0 )
        return self.d

    def start( self ):
        fade_in( 0.5, self.d )
        Undulation(style='sawup')(self.d.theta,min=0.0,max=360.0,period=2.0)




cameras = (
  Rect(0,0,1,1),
  Rect(-0.6,0,2.35,1),
  )


def parameterized_title( x = (SCALAR, 0, 1), cursor=(SCALAR,0,1) ):

    str = u"Computational Paradigms\nCollaborative Effort Kick-off"

    disp_str = str[0:int(len(str)*x)]

    if cursor<0.5 or len(disp_str)<len(str):
        cursor_str = '_'
    else:
        cursor_str = ' '
    

    #set_camera(Rect(0,0,10,10))

    r = Rect( -1,-0.5,1,0.8 )

    set_camera( r )

    thickness( 0.01 )

    color(blue,0.2)

    rectangle(r.bottom(0.5).top(0.9))

    color(red,0.9)
    
    if disp_str:
        d = text( -0.9, 0.0, disp_str+cursor_str, font = fonts['mono'], size = 0.10, anchor = 'nw', justify = 0.0 )

    #frame( d['left'], d['bottom'], d['right'], d['top'] ) 
    


class cursor_blink(Controller):
    def create_objects( self ):
        self.d = Drawable( None, parameterized_title,x=0.0,cursor=0.0, _alpha = 0.0 )
        return self.d

    def start( self ):
        fade_in( 1.0, self.d )
        Undulation(style='sawup')(self.d.cursor,min=0.0,max=1.0,period=0.5)
        linear(2.0,self.d.x,1.0)






def title_anim():
    #bg = Fill( style = 'horz', color2 = Color(0.5,0,0) )
    bg = common.bg
    dv = viewport.interp( get_camera().bottom( 0.2 ),
                           get_camera() )

    dv2 = viewport.interp( get_camera().top( 0.2 ),
                           get_camera() )

    cap = Text( dv,
                color = blue, font = fonts['times'], size = 24, _alpha = 0.0,
                justify = 0.5 )

    cap2 = Text( dv2,
                color = blue, font = fonts['times'], size = 16, _alpha = 0.0,
                justify = 0.5 )


    d3 = Interactive( get_camera(),
                      controller = spin)

    start_animation( bg, d3)
    fade_in( 2.0, d3 )
    pause()
    # d3 is interactive, so there is a pause here
    enter(cap)
    set( cap.text, 'Computational Paradigms' )    

    parallel()
    fade_in( 3.0, cap)
    #fade_out(2.0, d3)
    smooth( 2.0, dv.x, 1.0)
    end()
    pause()
    wait(1.0)
    enter(cap2)
    set( cap2.text, 'Kick-off' )
    parallel()
    fade_in( 3.0, cap2)
    #fade_out(2.0, d3)
    smooth( 2.0, dv2.x, 1.0)
    end()
    return end_animation()

title_anim = title_anim()



def title1_anim():
    bg = Fill( style = 'horz', color2 = Color(0.5,0,0) )



    dv = viewport.interp( get_camera(),
                           get_camera().top(0.5) )


    d3 = Interactive( dv,
                      controller = cursor_blink)


    d = Interactive( get_camera(),
                      controller = spin)

    cap = Text( get_camera().bottom(0.5).inset(0.05),
                color = white, font = fonts['times'], size = 20, _alpha = 0.0,
                justify = 0.0 )
    
    bl = BulletedList( get_camera().bottom(0.4).inset(0.05),
                       font = fonts['times'], color = white,
                       bullet = [fonts['dingbats'], 'w'], size = 18 )



    start_animation( common.bg,d,cap,bl)

    #set(common.bg._alpha,0.0)
    set( cap.text, 'Presuppositions:' )
    
    #fade_in( 2.0, d )

    pause()

    enter(d3)
    wait(2.1)
    #fade_in( 2.0, d3 )
    pause()
    # d3 is interactive, so there is a pause here

    #parallel()
    #fade_out(2.0,d)
    #fade_out(2.0,bg)
    #fade_in(2.0,common.bg)

    linear(2.0,dv.x,1.0)
    wait(-1.0)
    
    fade_in(2.0,cap)

    #end()

    pause()
    bl.add_item( 0, 'We are not yet effectively collaborating on Computational paradigms' )
    pause()
    bl.add_item( 0, 'We should start collaborating NOW!')
    
    return end_animation() 

title1_anim = title1_anim()

def title2_anim():

    d = Interactive( get_camera(),
                      controller = spin)


    start_animation( common.bg,d)

  
    #pause()
    
    return end_animation() 

title2_anim = title2_anim()






test_objects( parameterized_title, title1_anim )
