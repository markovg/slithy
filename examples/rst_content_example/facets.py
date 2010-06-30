from OpenGL.GL import *
from OpenGL.GLU import *

import math
import numpy

#import polyhedron

## class OpenGLDiagram:

##     def __init__(self):

##         self.parameters = []
##         self.draw = []

##     def add_scalar_parameter(self,name,def,min,max):
##         self.parameters.append((name,"scalar",def,min,max))

##     def add_color_parameter(*args,**kwargs):
##         pass

##     def add_string_parameter(*args,**kwargs):
##         pass
    
##     def add_integer_parameter(*args,**kwargs):
##         pass
    
##     def add_boolean_parameter(*args,**kwargs):
##         pass

##     def add_object_parameter(*args,**kwargs):
##         pass

##     def mark_projection(*args,**kwargs):
##         pass



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



def draw_cube(params,aspect,alpha):

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
    opengl_clear(GL_TRUE)

    # now you can set up your normal OpenGL projection, just as with
    # any other OpenGL drawing.  note that you do NOT do a
    # glLoadIdentity first.
    #
    # you should not push or pop the projection matrix stack.  many
    # OpenGL implementations have only 2 entries on this stack, and
    # Slithy uses both of them.
    gluPerspective( 25.0, aspect, 0.1, 30.0 )
    
    # Slithy will initialize the model-view matrix to the identity
    # before calling your function.  you are free to push and pop
    # this matrix stack normally.
    glMatrixMode( GL_MODELVIEW )
    glTranslated( 0.0, 0.0, -12.0 )

    # note that to use depth testing, you have to explicitly turn it
    # on.  
    glEnable( GL_DEPTH_TEST )
    
    # use the get_*() functions to retrieve parameter
    # values from the dictionary.
    x = params["x"]
    theta = params["theta"]

    #
    # now we will draw a rotated cube with open faces.
    #

    glRotated( theta, 0.7, 0.4, -0.1 )
    
    glPushMatrix()
    glColor3d( 1.0, 0.0, 0.0 )
    draw_face( x )
    glColor3d( 0.0, 1.0, 1.0 )
    glRotated( 180.0, 1.0, 0.0, 0.0 )
    draw_face( x )
    glPopMatrix()
    
    glPushMatrix()
    glColor3d( 0.0, 1.0, 0.0 )
    glRotated( 90.0, 0.0, 1.0, 0.0 )
    draw_face( x )
    glColor3d( 1.0, 0.0, 1.0 )
    glRotated( 180.0, 1.0, 0.0, 0.0 )
    draw_face( x )
    glPopMatrix()
    
    glPushMatrix()
    glColor3d( 0.0, 0.0, 1.0 )
    glRotated( 90.0, 1.0, 0.0, 0.0 )
    draw_face( x )
    glColor3d( 1.0, 1.0, 0.0 )
    glRotated( 180.0, 0.0, 1.0, 0.0 )
    draw_face( x )
    glPopMatrix()

    #
    # end of the drawing code.
    #

    return None



def draw_face( x ):
    glBegin( GL_TRIANGLE_STRIP )
    glVertex3d( 1.0, 1.0, 1.0 )
    glVertex3d( x, x, 1.0 )
    glVertex3d( -1.0, 1.0, 1.0 )
    glVertex3d( -x, x, 1.0 )
    glVertex3d( -1.0, -1.0, 1.0 )
    glVertex3d( -x, -x, 1.0 )
    glVertex3d( 1.0, -1.0, 1.0 )
    glVertex3d( x, -x, 1.0 )
    glVertex3d( 1.0, 1.0, 1.0 )
    glVertex3d( x, x, 1.0 )
    glEnd()


def do_facets(inner_radius,sep,width):
    cos = math.cos
    sin = math.sin
    
    r0 = inner_radius
    da = 2.0*math.pi / 12

    #sep1 = sep*1.2
    sep1 = sep
    
    #glShadeModel(GL_SMOOTH)

    red = (0.8, 0.1, 0.0, 1.0)
    green = (0.0, 0.8, 0.2, 1.0)
    blue = (0.2, 0.2, 1.0, 1.0)
    grey = (0.1,0.1,0.1,1.0)
    gold = (0.8, 0.8, 0.1, 1.0)

    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, grey)

    
    glNormal3f(0.0, 0.0, 1.0)
    
    # draw front face facet 1
    glBegin(GL_POLYGON)
    for i in range(6 ):
         angle = i * 2.0*math.pi / 6
         glVertex3f(r0*cos(angle), r0*sin(angle), width*0.5)
    glEnd()


    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, gold)
    
    glNormal3f(0.0, 0.0, 1.0)
    
    # draw front face facet 1
    glBegin(GL_QUAD_STRIP)
    for i in range(6+1 ):
         angle = i * 2.0*math.pi / 6
         glVertex3f(r0*cos(angle), r0*sin(angle), width*0.5)
         glVertex3f((r0+sep1)*cos(angle), (r0+sep1)*sin(angle), width*0.5)
    glEnd()


    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, grey)

    glNormal3f(0.0, 0.0, -1.0)
    
    # draw back face facet 1
    glBegin(GL_POLYGON)
    for i in range(5,-1,-1):
         angle = i * 2.0*math.pi / 6
         glVertex3f(r0*cos(angle), r0*sin(angle), -width*0.5)
    glEnd()


    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, gold)
    
    
    # draw front face facet 1
    glBegin(GL_QUAD_STRIP)
    for i in range(6,-1,-1):
         angle = i * 2.0*math.pi / 6
         glVertex3f(r0*cos(angle), r0*sin(angle),-width*0.5)
         glVertex3f((r0+sep1)*cos(angle), (r0+sep1)*sin(angle), -width*0.5)
    glEnd()

    dx = 0
    dy = 0

    glBegin(GL_QUAD_STRIP)
    for i in range(6+1):
         angle = i * 2.0*math.pi / 6
         glNormal3f(cos(angle+da), sin(angle+da), 0.0)
         glVertex3f((r0+sep1)*cos(angle)+dx, (r0+sep1)*sin(angle)+dy,width*0.5)
         glVertex3f((r0+sep1)*cos(angle)+dx, (r0+sep1)*sin(angle)+dy, -width*0.5)

    glEnd()


    r1 = r0*cos(2.0*math.pi / 12)
    
    angle = 2.0*math.pi / 12
    dx = (2.0*r1+sep)*cos(angle) 
    dy = (2.0*r1+sep)*sin(angle)

    glNormal3f(0.0, 0.0, 1.0)

    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, red)

    # draw front face facet 1
    glBegin(GL_POLYGON)
    for i in range(6):
         angle = i * 2.0*math.pi / 6
         glVertex3f(r0*cos(angle)+dx, r0*sin(angle)+dy, width*0.5)
    glEnd()

    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, gold)
    
    glNormal3f(0.0, 0.0, 1.0)
    
    # draw front face facet 1
    glBegin(GL_QUAD_STRIP)
    for i in range(6+1 ):
         angle = i * 2.0*math.pi / 6
         glVertex3f(r0*cos(angle)+dx, r0*sin(angle)+dy, width*0.5)
         glVertex3f((r0+sep1)*cos(angle)+dx, (r0+sep1)*sin(angle)+dy, width*0.5)
    glEnd()


    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, red)


    glNormal3f(0.0, 0.0, -1.0)
    
    # draw back face facet 1
    glBegin(GL_POLYGON)
    for i in range(5,-1,-1):
         angle = i * 2.0*math.pi / 6
         glVertex3f(r0*cos(angle)+dx, r0*sin(angle)+dy, -width*0.5)
    glEnd()

    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, gold)

    # draw front face facet 1
    glBegin(GL_QUAD_STRIP)
    for i in range(6,-1,-1):
         angle = i * 2.0*math.pi / 6
         glVertex3f(r0*cos(angle)+dx, r0*sin(angle)+dy,-width*0.5)
         glVertex3f((r0+sep1)*cos(angle)+dx, (r0+sep1)*sin(angle)+dy, -width*0.5)
    glEnd()


    glBegin(GL_QUAD_STRIP)
    for i in range(6+1):
         angle = i * 2.0*math.pi / 6
         glNormal3f(cos(angle+da), sin(angle+da), 0.0)
         glVertex3f((r0+sep1)*cos(angle)+dx, (r0+sep1)*sin(angle)+dy,width*0.5)
         glVertex3f((r0+sep1)*cos(angle)+dx, (r0+sep1)*sin(angle)+dy, -width*0.5)

    glEnd()


    




    angle = - 2.0*math.pi / 12
    dx = (2.0*r1+sep)*cos(angle) 
    dy = (2.0*r1+sep)*sin(angle) 

    glNormal3f(0.0, 0.0, 1.0)

    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, red)

    # draw front face facet 1
    glBegin(GL_POLYGON)
    for i in range(6):
         angle = i * 2.0*math.pi / 6
         glVertex3f(r0*cos(angle)+dx, r0*sin(angle)+dy, width*0.5)
    glEnd()

    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, gold)
    
    glNormal3f(0.0, 0.0, 1.0)
    
    # draw front face facet 1
    glBegin(GL_QUAD_STRIP)
    for i in range(6+1 ):
         angle = i * 2.0*math.pi / 6
         glVertex3f(r0*cos(angle)+dx, r0*sin(angle)+dy, width*0.5)
         glVertex3f((r0+sep1)*cos(angle)+dx, (r0+sep1)*sin(angle)+dy, width*0.5)
    glEnd()



    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, red)


    glNormal3f(0.0, 0.0, -1.0)
    
    # draw back face facet 1
    glBegin(GL_POLYGON)
    for i in range(5,-1,-1):
         angle = i * 2.0*math.pi / 6
         glVertex3f(r0*cos(angle)+dx, r0*sin(angle)+dy, -width*0.5)
    glEnd()

    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, gold)

    # draw front face facet 1
    glBegin(GL_QUAD_STRIP)
    for i in range(6,-1,-1):
         angle = i * 2.0*math.pi / 6
         glVertex3f(r0*cos(angle)+dx, r0*sin(angle)+dy,-width*0.5)
         glVertex3f((r0+sep1)*cos(angle)+dx, (r0+sep1)*sin(angle)+dy, -width*0.5)
    glEnd()

    glBegin(GL_QUAD_STRIP)
    for i in range(6+1):
         angle = i * 2.0*math.pi / 6
         glNormal3f(cos(angle+da), sin(angle+da), 0.0)
         glVertex3f((r0+sep1)*cos(angle)+dx, (r0+sep1)*sin(angle)+dy,width*0.5)
         glVertex3f((r0+sep1)*cos(angle)+dx, (r0+sep1)*sin(angle)+dy, -width*0.5)

    glEnd()



    angle = + 5.0 * 2.0*math.pi / 12
    dx = (2.0*r1+sep)*cos(angle) 
    dy = (2.0*r1+sep)*sin(angle) 

    glNormal3f(0.0, 0.0, 1.0)

    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, red)

    # draw front face facet 1
    glBegin(GL_POLYGON)
    for i in range(6):
         angle = i * 2.0*math.pi / 6
         glVertex3f(r0*cos(angle)+dx, r0*sin(angle)+dy, width*0.5)
    glEnd()

    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, gold)
    
    glNormal3f(0.0, 0.0, 1.0)
    
    # draw front face facet 1
    glBegin(GL_QUAD_STRIP)
    for i in range(6+1 ):
         angle = i * 2.0*math.pi / 6
         glVertex3f(r0*cos(angle)+dx, r0*sin(angle)+dy, width*0.5)
         glVertex3f((r0+sep1)*cos(angle)+dx, (r0+sep1)*sin(angle)+dy, width*0.5)
    glEnd()



    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, red)


    glNormal3f(0.0, 0.0, -1.0)
    
    # draw back face facet 1
    glBegin(GL_POLYGON)
    for i in range(5,-1,-1):
         angle = i * 2.0*math.pi / 6
         glVertex3f(r0*cos(angle)+dx, r0*sin(angle)+dy, -width*0.5)
    glEnd()



    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, gold)

    # draw front face facet 1
    glBegin(GL_QUAD_STRIP)
    for i in range(6,-1,-1):
         angle = i * 2.0*math.pi / 6
         glVertex3f(r0*cos(angle)+dx, r0*sin(angle)+dy,-width*0.5)
         glVertex3f((r0+sep1)*cos(angle)+dx, (r0+sep1)*sin(angle)+dy, -width*0.5)
    glEnd()

    glBegin(GL_QUAD_STRIP)
    for i in range(6+1):
         angle = i * 2.0*math.pi / 6
         glNormal3f(cos(angle+da), sin(angle+da), 0.0)
         glVertex3f((r0+sep1)*cos(angle)+dx, (r0+sep1)*sin(angle)+dy,width*0.5)
         glVertex3f((r0+sep1)*cos(angle)+dx, (r0+sep1)*sin(angle)+dy, -width*0.5)

    glEnd()



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





def draw_facets(params,aspect,alpha):

    # "params" is a dictionary containing the diagram's parameter values.
    # "aspect" is the aspect ratio of the viewport.
    # "alpha" is the alpha value to multiply all of your drawing
    #   colors by, if you want your diagram to respond to Slithy's
    #   normal fade_in() and fade_out() functions.

    info = params.get('info')
    if info:
        info.coords = mark_projection()

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
    gluPerspective( 25.0, aspect, 0.1, 30.0 )
    
    # Slithy will initialize the model-view matrix to the identity
    # before calling your function.  you are free to push and pop
    # this matrix stack normally.
    glMatrixMode( GL_MODELVIEW )
    glTranslated( 0.0, 0.0, -12.0 )

    # note that to use depth testing, you have to explicitly turn it
    # on.  
    glEnable( GL_DEPTH_TEST )
    
    # use trackball if avail

    trackball = params.get('trackball')
    if trackball:
        trackball.install()

    # use spinner if avail

    spinner = params.get('spinner')
    if spinner:
        glRotated( spinner.theta, 0.0 ,1.0, 0.0 )


    # use the get_*() functions to retrieve parameter
    # values from the dictionary.
    theta = params["theta"]

    #
    # now we will draw a rotated cube with open faces.
    #


    glRotated( theta, 0.0, 1.0, 0.0 )
    
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

    do_facets(0.5,0.1,0.2)

    glPopMatrix()    

    #
    # end of the drawing code.
    #

    return None



cube = (draw_cube, [('x', 'scalar', 0.0, 0.0, 1.0), ('theta', 'scalar', 0.0, 0.0, 360.0)], 'cube')


facets = (draw_facets,[('theta', 'scalar', 0.0, 0.0, 360.0), ('trackball','object',None),('spinner','object',None),('info','object',None)], 'facets')
