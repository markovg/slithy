CC = gcc

INCPATH = -I/uns/include/python2.2
LIBPATH = -L/usr/lib -L/uns/lib -L/usr/X11R6/lib
LIBS = -lGL -lGLU -ldl -lXext -lX11 -lm

CFLAGS = $(INCPATH) -g -O2

TARGETS = polyhedron.so trackball.so

all : $(TARGETS)

polyhedron.so : polyhedron.o slithygl.o
	gcc -shared -o $@ $^ $(LIBPATH) $(LIBS)

trackball.so : trackball.o
	gcc -shared -o $@ $^ $(LIBPATH) $(LIBS)
