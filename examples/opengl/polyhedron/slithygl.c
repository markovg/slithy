#ifndef _MAKEDEPEND

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
#endif

#include "slithygl.h"

static int invert_matrix( const double src[16], double inverse[16] );

double get_scalar( PyObject* obj, char* keyname )
{
    return PyFloat_AsDouble( PyDict_GetItemString( obj, keyname ) );
}

void get_color( PyObject* obj, char* keyname, double color[4] )
{
    PyObject* temp;
    
    temp = PyDict_GetItemString( obj, keyname );
    
    if ( !PyTuple_Check( temp ) || PyTuple_Size( temp ) != 4 )
	return;

    color[0] = PyFloat_AsDouble( PyTuple_GetItem( temp, 0 ) );
    color[1] = PyFloat_AsDouble( PyTuple_GetItem( temp, 1 ) );
    color[2] = PyFloat_AsDouble( PyTuple_GetItem( temp, 2 ) );
    color[3] = PyFloat_AsDouble( PyTuple_GetItem( temp, 3 ) );
}

char* get_string( PyObject* obj, char* keyname )
{
    return PyString_AsString( PyDict_GetItemString( obj, keyname ) );
}

int get_integer( PyObject* obj, char* keyname )
{
    return PyInt_AsLong( PyDict_GetItemString( obj, keyname ) );
}

int get_boolean( PyObject* obj, char* keyname )
{
    return !!PyInt_AsLong( PyDict_GetItemString( obj, keyname ) );
}

PyObject* get_object( PyObject* obj, char* keyname )
{
    return PyDict_GetItemString( obj, keyname );
}



static void opengl_clear( GLboolean color )
{
    glPushAttrib( GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT );
    
    glEnable( GL_DEPTH_TEST );
    glDepthFunc( GL_ALWAYS );
    glDepthMask( GL_TRUE );
    glColorMask( color, color, color, color );
    glBegin( GL_TRIANGLE_STRIP );
    glVertex3d( -1.0, -1.0, 1.0 );
    glVertex3d(  1.0, -1.0, 1.0 );
    glVertex3d( -1.0,  1.0, 1.0 );
    glVertex3d(  1.0,  1.0, 1.0 );
    glEnd();

    glPopAttrib();
}

void opengl_clear_blank( void )
{
    opengl_clear( GL_FALSE );
}

void opengl_clear_color( void )
{
    opengl_clear( GL_TRUE );
}


PyObject* make_opengl_diagram( PyObject* module, char* fnname )
{
    PyObject* fn;
    PyObject* item;
    PyObject* plist;

    fn = PyObject_GetAttrString( module, fnname );
    if ( fn == NULL || !PyCallable_Check( fn ) )
    {
	Py_XDECREF( fn );
	return NULL;
    }

    plist = PyList_New( 0 );
    item = Py_BuildValue( "OOs", fn, plist, fnname );
    PyObject_SetAttrString( module, fnname, item );
    
    Py_DECREF( item );
    Py_DECREF( fn );
    return plist;
}

void add_scalar_parameter( PyObject* plist, char* pname, double min, double max, double def )
{
    PyObject* v = Py_BuildValue( "ssddd", pname, "scalar", def, min, max );
    PyList_Append( plist, v );
    Py_DECREF( v );
}

void add_color_parameter( PyObject* plist, char* pname, double r, double g, double b, double a )
{
    PyObject* v = Py_BuildValue( "ss(dddd)", pname, "color", r, g, b, a );
    PyList_Append( plist, v );
    Py_DECREF( v );
}

void add_string_parameter( PyObject* plist, char* pname, char* def )
{
    PyObject* v = Py_BuildValue( "sss", pname, "string", def );
    PyList_Append( plist, v );
    Py_DECREF( v );
}

void add_integer_parameter( PyObject* plist, char* pname, int min, int max, int def )
{
    PyObject* v = Py_BuildValue( "ssiii", pname, "integer", def, min, max );
    PyList_Append( plist, v );
    Py_DECREF( v );
}

void add_boolean_parameter( PyObject* plist, char* pname, int def )
{
    PyObject* v = Py_BuildValue( "ssi", pname, "boolean", def );
    PyList_Append( plist, v );
    Py_DECREF( v );
}

void add_object_parameter( PyObject* plist, char* pname, PyObject* def )
{
    PyObject* v = Py_BuildValue( "ssO", pname, "object", def );
    PyList_Append( plist, v );
    Py_DECREF( v );
}

    
PyObject* mark_projection( void )
{
    double proj[16];
    double mv[16];
    double PM[16];
    double *IPM;
    int *VP;
    int i, j;
    PyObject* ipm_obj;
    PyObject* vp_obj;
    PyObject* result;
    
    glGetDoublev( GL_MODELVIEW_MATRIX, mv );
    glGetDoublev( GL_PROJECTION_MATRIX, proj );

    for ( i = 0; i < 4; ++i )
	for ( j = 0; j < 4; ++j )
	    PM[i*4+j] =
		proj[j] * mv[i*4] +
		proj[j+4] * mv[i*4+1] +
		proj[j+8] * mv[i*4+2] +
		proj[j+12] * mv[i*4+3];

    IPM = malloc( 16 * sizeof( double ) );
    if ( invert_matrix( PM, IPM ) )
    {
	for ( i = 0; i < 16; ++i )
	    IPM[i] = (i%5==0);
    }
    ipm_obj = PyCObject_FromVoidPtr( (void*)IPM, free );

    VP = malloc( 4 * sizeof( int ) );
    glGetIntegerv( GL_VIEWPORT, VP );
    vp_obj = PyCObject_FromVoidPtr( (void*)VP, free );

    result = Py_BuildValue( "OO", ipm_obj, vp_obj );
    Py_DECREF( ipm_obj );
    Py_DECREF( vp_obj );
    
    return result;
}
    
static int invert_matrix( const double src[16], double inverse[16] )
{
    int i, j, k, swap;
    double t;
    double temp[4][4];
    
    for ( i = 0; i < 4; ++i )
	for ( j = 0; j < 4; ++j )
	    temp[i][j] = src[i*4+j];
    for ( i = 0; i < 16; ++i )
	inverse[i] = ((i%5)==0);
    
    for ( i = 0; i < 4; ++i)
    {
	// look for largest element in column 
	swap = i;
	for ( j = i + 1; j < 4; j++ ) 
	    if ( fabs(temp[j][i]) > fabs(temp[i][i]) )
		swap = j;
	
	if ( swap != i )
	{
	    // swap rows
	    for ( k = 0; k < 4; k++ )
	    {
		t = temp[i][k];
		temp[i][k] = temp[swap][k];
		temp[swap][k] = t;
		
		t = inverse[i * 4 + k];
		inverse[i * 4 + k] = inverse[swap * 4 + k];
		inverse[swap * 4 + k] = t;
	    }
	}
	if ( temp[i][i] == 0 )
	{
	    // No non-zero pivot.  The matrix is singular, which
	    // shouldn't happen.  This means the user gave us a bad
	    // matrix.  Bad, bad user.
	    return -1;
	}
	
	t = temp[i][i];
	for ( k = 0; k < 4; ++k )
	{
	    temp[i][k] /= t;
	    inverse[i * 4 + k] /= t;
	}
	
	for ( j = 0; j < 4; j++ )
	{
	    if (j != i)
	    {
		t = temp[j][i];
		for ( k = 0; k < 4; ++k )
		{
		    temp[j][k] -= temp[i][k] * t;
		    inverse[j * 4 + k] -= inverse[i * 4 + k] * t;
		}
	    }
	}
    }
    return 0;
}
    
	

    
