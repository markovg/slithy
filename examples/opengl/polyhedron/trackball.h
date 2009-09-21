#define INSTALL_TRACKBALL(tb)      {\
	PyObject* raw;\
	if ( tb && tb != Py_None )\
	{\
	    raw = PyObject_CallMethod( tb, "getmatrix", NULL );\
	    glMultMatrixd( PyCObject_AsVoidPtr( raw ) );\
	    Py_DECREF( raw );\
	}\
    }
