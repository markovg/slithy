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

#include <math.h>

#ifndef M_PI
# define M_PI		3.14159265358979323846
#endif


#define MODE_OFF     0
#define MODE_SPIN    1
#define MODE_ROTATE  2

typedef struct
{
    PyObject_HEAD

    int mode;
    double spin_stheta;
    double rp0[3];
    GLdouble oldM[16];
    GLdouble M[16];
} TrackballObject;

static PyObject* trackball_getmatrix( TrackballObject* self )
{
    return PyCObject_FromVoidPtr( (void*)self->M, NULL );
}

static void matrix_multiply( GLdouble out[16], GLdouble A[16], GLdouble B[16] )
{
    int i, j;

    for ( i = 0; i < 4; ++i )
	for ( j = 0; j < 4; ++j )
	    out[j*4+i] =
		A[0*4+i] * B[j*4+0] +
		A[1*4+i] * B[j*4+1] +
		A[2*4+i] * B[j*4+2] +
		A[3*4+i] * B[j*4+3];
}

static PyObject* trackball_spinstart( TrackballObject* self, PyObject* args )
{
    double x, y;
    
    if ( !PyArg_ParseTuple( args, "dd", &x, &y ) )
	return NULL;

    memcpy( self->oldM, self->M, 16 * sizeof( GLdouble ) );
    self->mode = MODE_SPIN;
    self->spin_stheta = atan2( y, x );

    Py_INCREF( Py_None );
    return Py_None;
}

static PyObject* trackball_rotatestart( TrackballObject* self, PyObject* args )
{
    double x, y;
    double xangle, yangle;
    
    if ( !PyArg_ParseTuple( args, "dd", &x, &y ) )
	return NULL;

    memcpy( self->oldM, self->M, 16 * sizeof( GLdouble ) );
    self->mode = MODE_ROTATE;

    xangle = sqrt( x*x + 1.0 );
    yangle = sqrt( y*y + 1.0 );
    self->rp0[0] = x / (xangle * yangle);
    self->rp0[1] = y / yangle;
    self->rp0[2] = 1.0 / (xangle * yangle);
    
    Py_INCREF( Py_None );
    return Py_None;
}

static PyObject* trackball_move( TrackballObject* self, PyObject* args )
{
    double x, y;
    GLdouble temp[16];
    double theta;
    double c, s;
    
    if ( !PyArg_ParseTuple( args, "dd", &x, &y ) )
	return NULL;

    if ( self->mode == MODE_SPIN )
    {
	theta = self->spin_stheta - atan2( y, x );
	
	c = cos( theta );
	s = sin( theta );
	
	temp[0] = c;
	temp[1] = -s;
	temp[2] = 0.0;
	temp[3] = 0.0;
	temp[4] = s;
	temp[5] = c;
	temp[6] = 0.0;
	temp[7] = 0.0;
	temp[8] = 0.0;
	temp[9] = 0.0;
	temp[10] = 1.0;
	temp[11] = 0.0;
	temp[12] = 0.0;
	temp[13] = 0.0;
	temp[14] = 0.0;
	temp[15] = 1.0;
	
	matrix_multiply( self->M, temp, self->oldM );
    }
    else if ( self->mode == MODE_ROTATE )
    {
	double xangle, yangle, p1[3], a[3], alpha;

	xangle = sqrt( x*x + 1.0 );
	yangle = sqrt( y*y + 1.0 );
	p1[0] = x / (xangle * yangle);
	p1[1] = y / yangle;
	p1[2] = 1.0 / (xangle * yangle);
	    
	a[0] = self->rp0[1] * p1[2] - self->rp0[2] * p1[1];
	a[1] = self->rp0[2] * p1[0] - self->rp0[0] * p1[2];
	a[2] = self->rp0[0] * p1[1] - self->rp0[1] * p1[0];
	    
	s = sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2]);
	alpha = asin( s );
	if ( self->rp0[0]*p1[0] + self->rp0[1]*p1[1] + self->rp0[2]*p1[2] < 0 )
	    alpha += M_PI / 2.0;
	a[0] /= s;
	a[1] /= s;
	a[2] /= s;
	    
	alpha *= 2.0;

	/* the desired rotation is "alpha" radians, about the
	   axis (a[0],a[1],a[2]). */
	    
	s = sin( alpha );
	c = cos( alpha );
	    
	temp[0] = a[0] * a[0] * ( 1 - c ) + c;
	temp[1] = a[1] * a[0] * ( 1 - c ) + a[2] * s;
	temp[2] = a[0] * a[2] * ( 1 - c ) - a[1] * s;
	temp[3] = 0.0;
	temp[4] = a[0] * a[1] * ( 1 - c ) - a[2] * s;
	temp[5] = a[1] * a[1] * ( 1 - c ) + c;
	temp[6] = a[1] * a[2] * ( 1 - c ) + a[0] * s;
	temp[7] = 0.0;
	temp[8] = a[0] * a[2] * ( 1 - c ) + a[1] * s;
	temp[9] = a[1] * a[2] * ( 1 - c ) - a[0] * s;
	temp[10] = a[2] * a[2] * ( 1 - c ) + c;
	temp[11] = 0.0;
	temp[12] = 0.0;
	temp[13] = 0.0;
	temp[14] = 0.0;
	temp[15] = 1.0;
	
	matrix_multiply( self->M, temp, self->oldM );
    }

    Py_INCREF( Py_None );
    return Py_None;
}

static PyObject* trackball_end( TrackballObject* self, PyObject* args )
{
    PyObject* result;

    switch( self->mode )
    {
      case MODE_SPIN:
      case MODE_ROTATE:
	result = trackball_move( self, args );
	break;

      default:
	Py_INCREF( Py_None );
	result = Py_None;
    }
	
    if ( result )
	self->mode = MODE_OFF;

    return result;
}

static PyObject* trackball_reset( TrackballObject* self, PyObject* args )
{
    int i;
    
    self->mode = MODE_OFF;
    for ( i = 0; i < 16; ++i )
	self->M[i] = ((i%5) == 0);

    Py_INCREF( Py_None );
    return Py_None;
}

static PyMethodDef trackball_methods[] = {
    { "getmatrix", (PyCFunction)trackball_getmatrix, METH_NOARGS },
    { "spin_start", (PyCFunction)trackball_spinstart, METH_VARARGS },
    { "rotate_start", (PyCFunction)trackball_rotatestart, METH_VARARGS },
    { "move", (PyCFunction)trackball_move, METH_VARARGS },
    { "end", (PyCFunction)trackball_end, METH_VARARGS },
    { "reset", (PyCFunction)trackball_reset, METH_VARARGS },
    { NULL, NULL, 0 }
};

static PyObject* trackball_getattr( TrackballObject* self, char* name )
{
    return Py_FindMethod( trackball_methods, (PyObject*)self, name );
}

static void trackball_dealloc( TrackballObject* self )
{
    PyObject_Del( self );
}

static PyObject* trackball_str( TrackballObject* self )
{
    char buffer[200];
    sprintf( buffer, "[ %8.3f %8.3f %8.3f %8.3f ]\n[ %8.3f %8.3f %8.3f %8.3f ]\n[ %8.3f %8.3f %8.3f %8.3f ]\n[ %8.3f %8.3f %8.3f %8.3f ]",
	     self->M[ 0], self->M[ 4], self->M[ 8], self->M[12],
	     self->M[ 1], self->M[ 5], self->M[ 9], self->M[13],
	     self->M[ 2], self->M[ 6], self->M[10], self->M[14],
	     self->M[ 3], self->M[ 7], self->M[11], self->M[15] );
    return PyString_FromString( buffer );
}

PyTypeObject TrackballType = {
    PyObject_HEAD_INIT(NULL)
    0,
    "Trackball",
    sizeof( TrackballObject ),
    0,
    (destructor)trackball_dealloc,         // tp_dealloc
    0,                    // tp_print
    (getattrfunc)trackball_getattr,         // tp_getattr
    0,                    // tp_setattr
    0,                    // tp_compare
    0,                    // tp_repr
    0,                    // tp_as_number
    0,                    // tp_as_sequence
    0,                    // tp_as_mapping
    0,                    // tp_hash
    0,                                 // tp_call 
    (reprfunc)trackball_str,           // tp_str 
    0,                                 // tp_getattro 
    0,                                 // tp_setattro 
    0,                                 // tp_as_buffer 
    Py_TPFLAGS_DEFAULT,                // tp_flags 
    0,                                 // tp_doc 
    0,                                 // tp_traverse 
    0,                                 // tp_clear 
    0,                                 // tp_richcompare 
    0,                                 // tp_weaklistoffset 
    0,             // tp_iter 
    0,                                 // tp_iternext 
};

static PyObject* trackball_new( PyObject* self, PyObject* args )
{
    TrackballObject* tbobj;
    int i;

    tbobj = PyObject_New( TrackballObject, &TrackballType );

    for ( i = 0; i < 16; ++i )
	tbobj->M[i] = ((i%5) == 0);
    tbobj->mode = MODE_OFF;
    
    return (PyObject*)tbobj;
}

static PyMethodDef module_methods[] = {
    { "new", (PyCFunction)trackball_new, METH_NOARGS },
    { NULL, NULL }
};

#ifdef WIN32
__declspec(dllexport)
#endif
void inittrackball( void )
{
    PyObject* m;

    TrackballType.ob_type = &PyType_Type;

    m = Py_InitModule( "trackball", module_methods );
}
