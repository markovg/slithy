"""

The pygame movie player is used, which is based on SDL/SMPEG.  It is no where near as flexible 
a player as mplayer, for example.  It plays MPEG-1 video, and MPEG-2 audio ... and even then it is rather fussy.

In short, encode mpegs for this module as the following example:

mencoder something_completely.flv -of mpeg -mpegopts format=mpeg1:tsaf:muxrate=2000 \
  -o test.mpg -srate 44100 -af lavcresample=44100 -oac twolame -twolameopts br=160 \
  -ovc lavc -lavcopts vcodec=mpeg1video:vbitrate=1152:keyint=15:mbd=2

For cutting:

-ss 00:00:20 -endpos 00:00:50 

Remove the current audio track:

mencoder -ovc copy -nosound video.avi -o video_nosound.avi

Place a new audio track:


mencoder -ovc copy -audiofile soundtrack.mp3 -oac copy video_nosound.avi -o video_new.avi

Blank time

ffmpeg -loop_input -f image2 -i image.jpeg -t 20 image-movie.mpeg

#mencoder mf://blank.png -mf w=800:h=600:fps=0.2:type=png -ovc lavc \
#    -lavcopts vcodec=mpeg4:mbd=2:trell -oac copy -o output.avi

Join 2:

mencoder fishdance.mpg blank.mpg -of mpeg -mpegopts format=mpeg1:tsaf:muxrate=2000 \
  -o fishdance_postgrey.mpg -nosound -twolameopts br=160 \
  -ovc lavc -lavcopts vcodec=mpeg1video:vbitrate=1152:keyint=15:mbd=2

Cut

mencoder -ovc copy -nosound -o stomp.mpg -ss 37 test.mpg


More information at:

http://www.mplayerhq.hu/DOCS/HTML/en/menc-feat-vcd-dvd.html


"""


from OpenGL.GL import *
from OpenGL.GLU import *

import math
import numpy
import pygame

import lamina
from slithy.library import *

def opengl_clear( color ):

    glPushAttrib( GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT )
    
    glEnable( GL_DEPTH_TEST )
    glDepthFunc( GL_ALWAYS )
    glDepthMask( GL_TRUE )
    glColorMask( color, color, color, color )
    glBegin( GL_TRIANGLE_STRIP )
    glVertex3d( -1.0, -1.0, 1.0 )
    glVertex3d(  1.0, -1.0, 1.0 )
    glVertex3d( -1.0,  1.0, 1.0 )
    glVertex3d(  1.0,  1.0, 1.0 )
    glEnd()

    glPopAttrib()


def mark_projection():

##     double proj[16];
##     double mv[16];
##     double PM[16];
##     double *IPM;
##     int *VP;
##     int i, j;
##     PyObject* ipm_obj;
##     PyObject* vp_obj;
##     PyObject* result;
    
    mv = glGetDoublev( GL_MODELVIEW_MATRIX)
    proj = glGetDoublev( GL_PROJECTION_MATRIX )

    pm = numpy.dot(proj,mv)
    #or
    #pm = dot(mv,proj)

    

##     for ( i = 0; i < 4; ++i )
## 	for ( j = 0; j < 4; ++j )
## 	    PM[i*4+j] =
## 		proj[j] * mv[i*4] +
## 		proj[j+4] * mv[i*4+1] +
## 		proj[j+8] * mv[i*4+2] +
## 		proj[j+12] * mv[i*4+3];


    ipm = numpy.linalg.pinv(pm)

    
##     IPM = malloc( 16 * sizeof( double ) );
##     if ( invert_matrix( PM, IPM ) )
##     {
## 	for ( i = 0; i < 16; ++i )
## 	    IPM[i] = (i%5==0);
##     }
##     ipm_obj = PyCObject_FromVoidPtr( (void*)IPM, free );

    #VP = malloc( 4 * sizeof( int ) );
    #glGetIntegerv( GL_VIEWPORT, VP );
    #vp_obj = PyCObject_FromVoidPtr( (void*)VP, free );

    vp = glGetIntegerv( GL_VIEWPORT)

    #result = Py_BuildValue( "OO", ipm_obj, vp_obj );
    #Py_DECREF( ipm_obj );
    #Py_DECREF( vp_obj );
    
    return (ipm,vp)

def update_movie(movie):
		
    #pygame.event.pump()
    #pygame.display.update()

    event = pygame.event.poll()


    
def draw_movie(params,aspect,alpha):

    # "params" is a dictionary containing the diagram's parameter values.
    # "aspect" is the aspect ratio of the viewport.
    # "alpha" is the alpha value to multiply all of your drawing
    #   colors by, if you want your diagram to respond to Slithy's
    #   normal fade_in() and fade_out() functions.

    # if you want to use mark_projection() to save the coordinate
    # system for later use with unproject(), do that here. 


    # now we'll get started setting up our projection.  When this
    # function is called, the corners of the viewport will be at
    # (-aspect,-1) and (aspect,1).
    glMatrixMode( GL_PROJECTION )
    # we'll stretch things out so that the viewport corners are at
    # (-1,-1) and (1,1).  this corresponds to the normal OpenGL
    # default projection.  Do this if you want to use the normal
    # projection setup functions like gluPerspective() or
    # glFrustum().
    glScaled( aspect, 1.0, 1.0 )

    # if you want to use depth testing, you MUST call either
    # opengl_clear_blank() or opengl_clear_color() at this point in
    # order to initialize the depth buffer.
    #
    # opengl_clear_color() will clear the viewport to the current
    # OpenGL color; opengl_clear_blank() will have not alter the
    # color buffer.
    glColor4d( 0.2, 0.2, 0.3, alpha )
    opengl_clear(GL_FALSE)

    pos = (5.0, 5.0, 10.0, 0.0)

    #glClearColor(1.0, 1.0, 1.0, 1.0)

    #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLightfv(GL_LIGHT0, GL_POSITION, pos)
    glEnable(GL_CULL_FACE)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)


    #glPushAttrib( GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT )
    
    #glEnable( GL_DEPTH_TEST )
    #glDepthFunc( GL_ALWAYS )
    #glDepthMask( GL_TRUE )

    #glPopAttrib()

    # now you can set up your normal OpenGL projection, just as with
    # any other OpenGL drawing.  note that you do NOT do a
    # glLoadIdentity first.
    #
    # you should not push or pop the projection matrix stack.  many
    # OpenGL implementations have only 2 entries on this stack, and
    # Slithy uses both of them.

    #gluPerspective( 25.0, aspect, 0.1, 30.0 )
    
    # Slithy will initialize the model-view matrix to the identity
    # before calling your function.  you are free to push and pop
    # this matrix stack normally.
    glMatrixMode( GL_MODELVIEW )

    #glTranslated( 0.0, 0.0, -4.5 )

    # note that to use depth testing, you have to explicitly turn it
    # on.  
    glEnable( GL_DEPTH_TEST )
    

    theta = params["theta"]
    overlay = params["overlay"]
    movie = params["movie"]
    loop = params["loop"]

    #glRotated( theta, 0.0, 0.0, 1.0 )
    glRotated( 0.0, 0.0, 0.0, 1.0 )
    
    #glPushMatrix()
    #glColor3d( 1.0, 0.0, 0.0 )
    #draw_face( x )
    #glColor3d( 0.0, 1.0, 1.0 )
    #glRotated( 180.0, 1.0, 0.0, 0.0 )
    #draw_face( x )
    #glPopMatrix()

    #glRotated(theta, 0.0, 1.0, 0.0)

    glPushMatrix()
    #glTranslated(0.0, 0.0, 0.0)

    #glCallList(facets_list)


    if not movie.get_busy() and loop:
        movie.rewind()
        movie.play()

    update_movie(movie)

    overlay.alpha = alpha

    #overlay.clear()
    #overlay.testMode(alpha=int(255.0*alpha))

    overlay.regen()
    overlay.refresh()
    overlay.display()

    glPopMatrix()    

    #
    # end of the drawing code.
    #

    return None

    

# A MovieController controls each movie, and contains a lamina pygame surface to be drawn to OpenGL

class MovieController(Controller):
    def create_objects( self ):
        #self.d = Drawable( None, movie.facets, _alpha = 0.0 )

        pygame.mixer.quit()
        movie = pygame.movie.Movie(self.filename)

        overlay = lamina.LaminaPanelSurface(winSize=movie.get_size())
        overlay.clear()

        movie.set_display(overlay._surfTotal)

        #image = pygame.image.load(self.filename)
        #overlay._surfTotal.blit(image,(0,0))
        
        overlay.clear = None

        overlay.regen()
        overlay.refresh()


        movie_descriptor = (draw_movie,[('theta', 'scalar', 0.0, 0.0, 360.0),('overlay','object',overlay),('movie','object',movie),('loop','object',self.loop)], 'movie')
        self.d = Drawable( None, movie_descriptor, _alpha = self.int_alpha )
        self.movie = movie
        self.overlay = overlay
        return self.d

    def start( self ):
        fade_in( 0.5, self.d )
        # start movie here
        self.movie.play()

        # triger texture refresh events
        Undulation(style='sawup')(self.d.theta,min=0.0,max=360.0,period=2.0)


        


# class for Movies
class Movie(Interactive):
    def __init__(self,camera,filename,loop=False,int_alpha=1.0):
        # create movie controller class

        c = type('MovieController',(MovieController,),{'filename':filename,'loop':loop,'int_alpha':int_alpha})

        Interactive.__init__(self,camera,controller = c)


