CC = gcc

INCPATH = -I/uns/include/python2.2
LIBPATH = -L/usr/lib -L/uns/lib -L/usr/X11R6/lib
LIBS = -lGL -lGLU

CFLAGS = $(INCPATH) -g -O2

TARGETS = skeleton.so

all : $(TARGETS)

skeleton.so : skeleton.o slithygl.o
	gcc -shared -o $@ $^ $(LIBPATH) $(LIBS)
