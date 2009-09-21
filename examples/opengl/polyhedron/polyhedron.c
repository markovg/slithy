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
#include "trackball.h"

static PyObject* polyhedron_draw( PyObject* self, PyObject* args );

static PyMethodDef PolyhedronMethods[] = {
    { "draw", polyhedron_draw, METH_VARARGS },
    { NULL, NULL } };

void 
#ifdef WIN32
__declspec( dllexport )
#endif
initpolyhedron( void )
{
    PyObject* m;
    PyObject* p;

    m = Py_InitModule( "polyhedron", PolyhedronMethods );

    p = make_opengl_diagram( m, "draw" );
    add_scalar_parameter( p, "angle", 0.0, 360.0, 0.0 );
    add_color_parameter( p, "tri_color", 1.0, 0.6, 0.0, 1.0 );
    add_color_parameter( p, "pent_color", 0.7, 1.0, 0.2, 1.0 );
    add_object_parameter( p, "trackball", Py_None );
    add_object_parameter( p, "info", Py_None );
    Py_XDECREF( p );
}

double vertices[90] ={
    0, 0, 1.6180339887499,
    0.951056516295154, 0, 1.30901699437496,
    0.425325404176028, 0.850650808352039, 1.30901699437496,
    -0.951056516295154, -0, 1.30901699437496,
    -0.425325404176028, -0.850650808352039, 1.30901699437496,
    1.53884176858763, 0, 0.500000000000007,
    1.11351636441162, -0.850650808352039, 0.809016994374952,
    -0.262865556059563, 1.37638192047118, 0.809016994374952,
    0.688190960235591, 1.37638192047118, 0.500000000000007,
    -1.53884176858763, -0, 0.500000000000007,
    -1.11351636441162, 0.850650808352039, 0.809016994374952,
    0.262865556059563, -1.37638192047118, 0.809016994374952,
    -0.688190960235591, -1.37638192047118, 0.500000000000007,
    1.53884176858763, 0, -0.500000000000007,
    1.37638192047118, 0.850650808352039, 0,
    0.850650808352039, -1.37638192047118, 0,
    -0.850650808352039, 1.37638192047118, 0,
    0.688190960235591, 1.37638192047118, -0.500000000000007,
    -1.53884176858763, -0, -0.500000000000007,
    -1.37638192047118, -0.850650808352039, 0,
    -0.688190960235591, -1.37638192047118, -0.500000000000007,
    0.951056516295154, 0, -1.30901699437496,
    1.11351636441162, -0.850650808352039, -0.809016994374952,
    0.262865556059563, -1.37638192047118, -0.809016994374952,
    -1.11351636441162, 0.850650808352039, -0.809016994374952,
    -0.262865556059563, 1.37638192047118, -0.809016994374952,
    0.425325404176028, 0.850650808352039, -1.30901699437494,
    -0.951056516295154, -0, -1.30901699437494,
    -0.425325404176028, -0.850650808352039, -1.30901699437494,
    -0, 0, -1.61803398874989
};

int faces[] = {
    3, 2, 1, 0,
    5, 3, 10, 7, 2, 0,
    3, 4, 3, 0,
    5, 1, 6, 11, 4, 0,
    3, 5, 6, 1,
    5, 2, 8, 14, 5, 1,
    3, 7, 8, 2,
    3, 9, 10, 3,
    5, 4, 12, 19, 9, 3,
    3, 11, 12, 4,
    5, 13, 22, 15, 6, 5,
    3, 14, 13, 5,
    3, 15, 11, 6,
    5, 16, 25, 17, 8, 7,
    3, 10, 16, 7,
    3, 17, 14, 8,
    5, 18, 24, 16, 10, 9,
    3, 19, 18, 9,
    5, 15, 23, 20, 12, 11,
    3, 20, 19, 12,
    3, 21, 22, 13,
    5, 14, 17, 26, 21, 13,
    3, 22, 23, 15,
    3, 24, 25, 16,
    3, 25, 26, 17,
    3, 27, 24, 18,
    5, 19, 20, 28, 27, 18,
    3, 23, 28, 20,
    5, 29, 28, 23, 22, 21,
    3, 26, 29, 21,
    5, 27, 29, 26, 25, 24,
    3, 28, 29, 27,
    0 };

static PyObject* polyhedron_draw( PyObject* self, PyObject* args )
{
    int *f;
    int i;
    GLfloat f_specular[] = { 1.0f, 1.0f, 1.0f, 1.0f };
    GLfloat f_shininess[] = { 100.0f };
    GLfloat ambient_light[] = { 0.3f, 0.3f, 0.3f, 1.0f };
    GLfloat diffuse_light[] = { 1.0f, 1.0f, 1.0f, 1.0f };
    GLfloat light_position[] = { 10.0f, 10.0f, 10.0f, 0.0f };
    double angle;
    PyObject* dict;
    double aspect, alpha;
    static GLfloat triangle_color[4] = { 1.0f, 0.6f, 0.0f, 1.0f };
    static GLfloat pentagon_color[4] = { 0.7f, 1.0f, 0.2f, 1.0f };
    double rgba[4];
    PyObject* proj;
    PyObject* info;

    if ( !PyArg_ParseTuple( args, "Odd", &dict, &aspect, &alpha ) )
	return NULL;

#if 0
    PyObject_Print( dict, stdout, 0 );
    printf( "\n" );
#endif
    
    angle = get_scalar( dict, "angle" );

    get_color( dict, "tri_color", rgba );
    triangle_color[0] = (GLfloat)rgba[0];
    triangle_color[1] = (GLfloat)rgba[1];
    triangle_color[2] = (GLfloat)rgba[2];
    triangle_color[3] = (GLfloat)(rgba[3] * alpha);

    get_color( dict, "pent_color", rgba );
    pentagon_color[0] = (GLfloat)rgba[0];
    pentagon_color[1] = (GLfloat)rgba[1];
    pentagon_color[2] = (GLfloat)rgba[2];
    pentagon_color[3] = (GLfloat)(rgba[3] * alpha);
    
    f_specular[3] = (GLfloat)alpha;

    // if we were passed an object through the "info" parameter, save
    // the coordinate system in that object's "coords" attribute.
    info = get_object( dict, "info" );
    if ( info && info != Py_None )
    {
	proj = mark_projection();
	PyObject_SetAttrString( info, "coords", proj );
	Py_DECREF( proj );
    }
    
    glMatrixMode( GL_PROJECTION );
    glScaled( aspect, 1.0, 1.0 );
    opengl_clear_blank();
    gluPerspective( 25.0, aspect, 0.1, 30.0 );

    glMatrixMode( GL_MODELVIEW );
    glTranslated( 0.0, 0.0, -12.0 );
    
    glLightfv( GL_LIGHT0, GL_POSITION, light_position );

    INSTALL_TRACKBALL( get_object( dict, "trackball" ) );
    glRotated( angle, 0.7, 0.4, -0.1 );

    glEnable( GL_DEPTH_TEST );
    glEnable( GL_LIGHTING );
    glEnable( GL_LIGHT0 );
    glLightModeli( GL_LIGHT_MODEL_TWO_SIDE, GL_FALSE );
    glLightModelfv( GL_LIGHT_MODEL_AMBIENT, ambient_light );
    glLightfv( GL_LIGHT0, GL_DIFFUSE, diffuse_light );
    glMaterialfv( GL_FRONT, GL_SPECULAR, f_specular );
    glMaterialfv( GL_FRONT, GL_SHININESS, f_shininess );

    // draw colored triangles and pentagons.  compute normal of each
    // face so that they are lit correctly.   

    f = faces;
    while ( *f )
    {
	double ax, ay, az, bx, by, bz, cx, cy, cz;
	double nx, ny, nz, nlen;

	ax = vertices[f[1]*3+0];
	ay = vertices[f[1]*3+1];
	az = vertices[f[1]*3+2];
	
	bx = vertices[f[2]*3+0] - ax;
	by = vertices[f[2]*3+1] - ay;
	bz = vertices[f[2]*3+2] - az;
	
	cx = vertices[f[3]*3+0] - ax;
	cy = vertices[f[3]*3+1] - ay;
	cz = vertices[f[3]*3+2] - az;

	nx = by * cz - bz * cy;
	ny = bz * cx - bx * cz;
	nz = bx * cy - by * cx;
	nlen = -sqrt( nx*nx + ny*ny + nz*nz );

	//
	// "Every functioning graphics program has an even number of sign errors."
	//                                                   -- Jim Blinn
	//
	    
	glNormal3d( nx / nlen, ny / nlen, nz / nlen );
	
	if ( *f == 3 )
	    glMaterialfv( GL_FRONT, GL_AMBIENT_AND_DIFFUSE, triangle_color );
	else
	    glMaterialfv( GL_FRONT, GL_AMBIENT_AND_DIFFUSE, pentagon_color );

	glBegin( GL_POLYGON );
	for ( i = 0; i < *f; ++i )
	    glVertex3dv( vertices + f[i+1]*3 );
	glEnd();

	f += *f + 1;
    }

    // now outline the faces with black lines

    glEnable( GL_BLEND );
    glBlendFunc( GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA );
    glEnable( GL_LINE_SMOOTH );
    glDisable( GL_LIGHTING );
    f = faces;
    glColor4d( 0.0, 0.0, 0.0, alpha );
    glLineWidth( 2.0 );
    while ( *f )
    {
	glBegin( GL_LINE_LOOP );
	for ( i = 0; i < *f; ++i )
	    glVertex3dv( vertices + f[i+1]*3 );
	glEnd();
	
	f += *f + 1;
    }

    Py_INCREF( Py_None );
    return Py_None;
}

/** Local Variables: **/
/** dsp-name:"polyhedron" **/
/** End: **/

