#ifndef _UTIL_H
#define _UTIL_H

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
#endif

PyObject* make_opengl_diagram( PyObject* module, char* fnname );
void add_scalar_parameter( PyObject* plist, char* pname, double min, double max, double def );
void add_color_parameter( PyObject* plist, char* pname, double r, double g, double b, double a );
void add_string_parameter( PyObject* plist, char* pname, char* def );
void add_integer_parameter( PyObject* plist, char* pname, int min, int max, int def );
void add_boolean_parameter( PyObject* plist, char* pname, int def );
void add_object_parameter( PyObject* plist, char* pname, PyObject* def );

double get_scalar( PyObject* obj, char* keyname );
int get_integer( PyObject* obj, char* keyname );
char* get_string( PyObject* obj, char* keyname );
void get_color( PyObject* obj, char* keyname, double color[4] );
int get_boolean( PyObject* obj, char* keyname );
PyObject* get_object( PyObject* obj, char* keyname );

void opengl_clear_blank( void );
void opengl_clear_color( void );

PyObject* mark_projection( void );


#endif
