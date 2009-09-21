#ifdef _DEBUG
#undef _DEBUG
#include <Python.h>
#define _DEBUG
#else
#include <Python.h>
#endif

#ifdef WIN32
#include <windows.h>
#endif

#include <GL/gl.h>
#include <GL/glu.h>

#include "slithygl.h"

static PyObject* cube_draw( PyObject* self, PyObject* args );
static void draw_face( double x );

// each OpenGL diagram needs one function in the methods array.
static PyMethodDef SkeletonMethods[] = {
    { "cube", cube_draw, METH_VARARGS },     
    { NULL, NULL } };

void 
#ifdef WIN32
__declspec( dllexport )
#endif
initskeleton( void )
{
    PyObject* m;
    PyObject* p;

    m = Py_InitModule( "skeleton", SkeletonMethods );

    // for each diagram:
    //    1. call make_opengl_diagram
    //    2. call the add_*_parameter() functions to define the parameters
    //    3. do PY_XDECREF() on the return value from step 1

    // here we define the "cube" diagram with a two scalar
    // parameters called "x" and "theta". 
    
    p = make_opengl_diagram( m, "cube" );
    add_scalar_parameter( p, "x", 0.0, 1.0, 0.0 );
    add_scalar_parameter( p, "theta", 0.0, 360.0, 0.0 );
    Py_XDECREF( p );
}

static PyObject* cube_draw( PyObject* self, PyObject* args )
{
    PyObject* dict;
    double aspect, alpha;
    double x, theta;

    if ( !PyArg_ParseTuple( args, "Odd", &dict, &aspect, &alpha ) )
	return NULL;

    // "dict" is a dictionary containing the diagram's parameter values.
    // "aspect" is the aspect ratio of the viewport.
    // "alpha" is the alpha value to multiply all of your drawing
    //   colors by, if you want your diagram to respond to Slithy's
    //   normal fade_in() and fade_out() functions. 


    // if you want to use mark_projection() to save the coordinate
    // system for later use with unproject(), do that here. 


    // now we'll get started setting up our projection.  When this
    // function is called, the corners of the viewport will be at
    // (-aspect,-1) and (aspect,1).
    glMatrixMode( GL_PROJECTION );
    // we'll stretch things out so that the viewport corners are at
    // (-1,-1) and (1,1).  this corresponds to the normal OpenGL
    // default projection.  Do this if you want to use the normal
    // projection setup functions like gluPerspective() or
    // glFrustum().
    glScaled( aspect, 1.0, 1.0 );

    // if you want to use depth testing, you MUST call either
    // opengl_clear_blank() or opengl_clear_color() at this point in
    // order to initialize the depth buffer.
    //
    // opengl_clear_color() will clear the viewport to the current
    // OpenGL color; opengl_clear_blank() will have not alter the
    // color buffer.
    glColor4d( 0.2, 0.2, 0.3, alpha );
    opengl_clear_color();

    // now you can set up your normal OpenGL projection, just as with
    // any other OpenGL drawing.  note that you do NOT do a
    // glLoadIdentity first.
    //
    // you should not push or pop the projection matrix stack.  many
    // OpenGL implementations have only 2 entries on this stack, and
    // Slithy uses both of them.
    gluPerspective( 25.0, aspect, 0.1, 30.0 );

    // Slithy will initialize the model-view matrix to the identity
    // before calling your function.  you are free to push and pop
    // this matrix stack normally.
    glMatrixMode( GL_MODELVIEW );
    glTranslated( 0.0, 0.0, -12.0 );

    // note that to use depth testing, you have to explicitly turn it
    // on.  
    glEnable( GL_DEPTH_TEST );
    
    // use the get_*() functions to retrieve parameter
    // values from the dictionary.
    x = get_scalar( dict, "x" );
    theta = get_scalar( dict, "theta" );

    //
    // now we will draw a rotated cube with open faces.
    //

    glRotated( theta, 0.7, 0.4, -0.1 );
    
    glPushMatrix();
    glColor3d( 1.0, 0.0, 0.0 );
    draw_face( x );
    glColor3d( 0.0, 1.0, 1.0 );
    glRotated( 180.0, 1.0, 0.0, 0.0 );
    draw_face( x );
    glPopMatrix();
    
    glPushMatrix();
    glColor3d( 0.0, 1.0, 0.0 );
    glRotated( 90.0, 0.0, 1.0, 0.0 );
    draw_face( x );
    glColor3d( 1.0, 0.0, 1.0 );
    glRotated( 180.0, 1.0, 0.0, 0.0 );
    draw_face( x );
    glPopMatrix();
    
    glPushMatrix();
    glColor3d( 0.0, 0.0, 1.0 );
    glRotated( 90.0, 1.0, 0.0, 0.0 );
    draw_face( x );
    glColor3d( 1.0, 1.0, 0.0 );
    glRotated( 180.0, 0.0, 1.0, 0.0 );
    draw_face( x );
    glPopMatrix();

    //
    // end of the drawing code.
    //


    // the return value is discarded, but we have to return something,
    // so return the "None" object.
    // to raise an exception, use PyErr_SetString() and return NULL.
    Py_INCREF( Py_None );
    return Py_None;
}

static void draw_face( double x )
{
    glBegin( GL_TRIANGLE_STRIP );
    glVertex3d( 1.0, 1.0, 1.0 );
    glVertex3d( x, x, 1.0 );
    glVertex3d( -1.0, 1.0, 1.0 );
    glVertex3d( -x, x, 1.0 );
    glVertex3d( -1.0, -1.0, 1.0 );
    glVertex3d( -x, -x, 1.0 );
    glVertex3d( 1.0, -1.0, 1.0 );
    glVertex3d( x, -x, 1.0 );
    glVertex3d( 1.0, 1.0, 1.0 );
    glVertex3d( x, x, 1.0 );
    glEnd();
}
