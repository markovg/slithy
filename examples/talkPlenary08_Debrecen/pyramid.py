from slithy.library import *
from slithy.util import *

from fonts import fonts

from images import images

import numpy.random

import math

# params for "facets members discussing computational paradigms"

numpy.random.seed(12345)

slogans = ("Liquid","Echo state","Kalman filter", "non-Turing", "Phrenology","Neural field", "Turing", "Active", "Dynamic", "Fractal", "Complex cells", "Synergetic", 'Markov process',"Qwerty","Gabor filter","Surround\ninhibtion","Attractors")

list_colors = (red,green,blue, orange,yellow,purple)

num_men = 17

men_x = numpy.random.uniform(-1.5,1.5,size=(num_men,))
men_y = numpy.random.uniform(-0.5,0.5,size=(num_men,))
men_c1 = [ list_colors[i] for i in numpy.random.randint(len(list_colors),size=(num_men,))]
men_c2 = [ list_colors[i] for i in numpy.random.randint(len(list_colors),size=(num_men,))]
#men_slogan = [ slogans[i] for i in numpy.random.randint(len(slogans),size=(num_men,))]

men_slogan = [ slogans[i%len(slogans)] for i in numpy.arange(0,num_men)]

men_x[0] = -1.2
men_y[0] = 0.0
men_x[1] = 0.0
men_y[1] = -0.2
men_x[2] = 0.8
men_y[2] = 0.2


import common

cameras = (
    Rect(0,0.0,1.0,0.1),
    Rect(0,0,1.0,1.0)
    )


slide_images = (images['jens1'],images['jens2'])

def slide1_diag():

    set_camera(Rect(0,0,1024.0,768.0))

    image(0,0,images['jens1'],width=1024.0,anchor='sw')
    color(red)
    text(1024.0/2.0,100.0,'(Slides: Jens Kremkow)', font = fonts['times'], size = 10.0, anchor = 'c', justify = 0.5)

def slide2_diag():

    set_camera(Rect(0,0,1024.0,768.0))

    image(0,0,images['jens2'],width=1024.0,anchor='sw')


def slide_diag(slide = (INTEGER,0,1)):

    
    set_camera(Rect(0,0,1024.0,768.0))
    #r = get_camera()

    image(0,0,slide_images[slide],width=1024.0,anchor='sw')

    color(red)

    if slide is 0:
        text(1024.0/2.0,90.0, '(Slides: Jens Kremkow)',
             font = fonts['times'], size = 40.0, anchor = 'c', justify = 0.5)



diags = (slide1_diag,slide2_diag)


def calc_flyin_rect(t):

    c = get_camera()

    w = c.width()
    h = c.height()

    # define aspect = width/height
    aspect = c.aspect()

    f = 0.2
    start_width = w*f
    
    #a = math.log(w/(start_width))
    a = math.log(1.0/f)
    
    twx = start_width*math.exp(a*t)
    twy = twx*aspect

    # trajectory width y at t =0
    #twy0 = 200.0/aspect

    ty = math.exp(a*t)/math.exp(a) * h/2.0

    return Rect((w-twx)/2.0, ty - twy/2.0,
                (w+twx)/2.0, ty + twy/2.0)


def enter_slide_diag(t = (SCALAR,0,1),diag = (INTEGER,0,1)):

    #set_camera(Rect(0,0,1024.0,768.0))
    
    r = calc_flyin_rect(t)
    
    embed_object(r,diags[diag],{},_alpha = 1.0 )


def draw_man(colors=(red,blue),slogan="Liquid"):

    color(colors[0])

    thickness(0.01)

    # head
    circle(0.1,0.5,0.8)
    # body
    line(0.5,0.7,0.5,0.5)
    # left leg
    line(0.5,0.5,0.4,0.3)
    # right leg
    line(0.5,0.5,0.6,0.3)
    # left arm
    line(0.5,0.7,0.43,0.63)
    line(0.43,0.63,0.4,0.55)
    # right arm
    line(0.5,0.7,0.57,0.63)
    line(0.57,0.63,0.65,0.68)

    color(colors[1])
    
    #p = roundrect(0.7,0.92,1.2,0.68,0.1)

    x = 0.75
    y = 0.8
    bb = text(0.75,0.8,slogan,font = fonts['times'], size = 0.1,
         anchor = 'w', justify = 0.5)

    d = 0.05
    dd = 0.05
    x1 = bb['left']-d
    x2 = bb['right']+d
    y2 = bb['top']+d
    y1 = bb['bottom']-d

    y3 = (y1+y2)/2.0
    x3 = 0.65
    r = 0.07


    p = Path()

    #p.moveto(x1,y+dd)
    #p.lineto(x1,y1)
    p.arc( x1+r, y1+r, 180, 270, r )
    p.arc( x2-r, y1+r, 270, 360, r )
    p.arc( x2-r, y2-r, 0, 90, r )
    p.arc( x1+r, y2-r, 90, 180, r )
    #p.lineto(x1+r,y-dd)
    p.lineto(x3,y3)
    p.closepath()


    widestroke(p,0.01)


    

    


def man_diag(text = (SCALAR,0,1), color1 = (SCALAR,0,1), color2 = (SCALAR,0,1)):

    lcolor1 = list_colors[int(len(list_colors[:-1])*color1)]
    lcolor2 = list_colors[int(len(list_colors[:-1])*color2)]
    ltext = slogans[int(len(slogans[:-1])*text)]

    c = Rect(0,0,1,1)
    set_camera(c)

    draw_man(colors =(lcolor1,lcolor2),slogan = ltext)



def comp_discuss_diag( x = (SCALAR,0,1) ):

    num = int((num_men)*x)

    c = Rect(-1.0,0.0,3.0,1.5)
    set_camera(c)

    color(white)
    text(1.0,1.2,'Short-cut to collaboration on \n computational paradigms?',font = fonts['times'], size = 0.15,
         anchor = 'c', justify = 0.5)

    for i in xrange(0,num):
    
        push()
        translate(men_x[i],men_y[i])
        draw_man(colors =(men_c1[i],men_c2[i]),slogan = men_slogan[i])
        pop()

    #embed_object(Rect(men_x[num],men_y[num],men_x[num]+0.5,men_y[num]+0.5),
    #man_diag, { 'x':x }, _alpha = 1.0 )



def draw_diag(alpha,colors):

    #color(colors[0],0.5*alpha)
    color(colors[0],0.5*alpha)
    polygon( 0.1, 0.1, 0.5, 0.7, 0.9, 0.1 )

    color(colors[1],1.0*alpha)
    
    w = 0.15
    s = 0.08
    text(0.5,0.15,'Simulation software',font = fonts['times'], size = s,
         anchor = 's', justify = 0.5)

    text(0.5,0.15+w,'Model implementation',font = fonts['times'], size = s,
         anchor = 's', justify = 0.5)
    
    text(0.5,0.15+2*w,"Benchmarks (what's that?)",font = fonts['times'], size = s,
         anchor = 's', justify = 0.5)

    text(0.5,0.15+3*w,'Computational paradigms',font = fonts['times'], size = s,
         anchor = 's', justify = 0.5)


def collab_diagram_partial( x = (SCALAR,0,1) ):

    set_camera( interp_cameralist( x, cameras ) )

    draw_diag(1.0, colors=(green,red))





def collab_diagram( x = (SCALAR,0,1) ) :

    r = Rect(0,0,1,1)

    set_camera(r)

    draw_diag(1.0, colors = (Color(0.8),Color(0.3)))

    #set_camera( interp_cameralist( x, cameras ) )

    embed_object(interp_cameralist( x, cameras ), collab_diagram_partial, { 'x':x }, _alpha = 1.0 )



cameras_next = (
    Rect(0,0,1.0,1.0),
    Rect(0,0,1.0,1.0).top(0.6).bottom(0.4),
    Rect(-0.1,0.2,1.0,0.4)
    )


def collab_diagram_next( x = (SCALAR,0,2), partial = (SCALAR,0,1),c=(SCALAR,0,1),pre=(SCALAR,0,1) ) :


    

    set_camera( interp_cameralist( x, cameras_next ) )

    pyramid_color = Color(0.8)

    text_color = Color(0.3)

    draw_diag(c, colors = (pyramid_color,text_color))

    #set_camera( interp_cameralist( x, cameras ) )

    embed_object(interp_cameralist( partial, cameras ), collab_diagram_partial, { 'x':partial }, _alpha = c )


    w = 0.15
    s = 0.08

    color(red)

    bb = text(0.5,0.15+w,'Model implementation',font = fonts['times'],
         size = s,anchor = 's', justify = 0.5, nodraw = 1)


    color(text_color,1.0)

    text(bb['right'],0.15+w,'Model implementation',font = fonts['times'], size = s,
         anchor = 'se', justify = 1.0)

    color(white,pre)

    text(bb['right'],0.15+w,'Common Model implementation',font = fonts['times'], size = s,
         anchor = 'se', justify = 1.0)





def collab_anim():

    c = Rect(0,0,1000,1000)

    # view port should grow with collab_diagram expose scalar 'x'
    # then move to top half of screen to make comments below
    
    dv = viewport.interp(get_camera(), get_camera().top(0.5))

    d = Drawable(dv, collab_diagram,_alpha = 1.0, x = 0.0)

    d2 = Drawable(get_camera().bottom(0.5),comp_discuss_diag, _alpha=1.0,x=0.0)

    cap = Text( get_camera().inset(0.05),
                color = white, font = fonts['times'], size = 20, _alpha = 0.0,
                justify = 0.5 )

    start_animation( common.bg, d,cap )

    set(cap.text, 'Pyramid of collaboration')

    set(cap._alpha, 1.0)
    
    pause()

    #fade_in(0.5,d)
    linear(2.0,d.x,0.743)

    pause()

    linear(1.0,dv.x,1.0)

    enter(d2)

    pause()

    linear(2.0, d2.x, 2.0/num_men + 0.5/num_men)

    pause()

    set(d2.x, 3.0/num_men + 0.5/num_men)
    
    pause()
    
    linear(5.0,d2.x,1.0)


    return end_animation()

collab_anim = collab_anim()


def what_next_anim():

    dv = viewport.interp(get_camera().top(0.5),get_camera())

    d = Drawable(dv, collab_diagram_next,_alpha = 1.0, x = 0.0,pre=0.0,partial = 0.743,c=1.0)

    cap = Text( get_camera().inset(0.05),
                color = white, font = fonts['times'], size = 20, _alpha = 1.0,
                justify = 0.5, text='Pyramid of collaboration' )

    start_animation( common.bg, d,cap )


    linear(2.0,dv.x,1.0)

    pause()

    fade_out(0.5,cap)
    
    wait(-0.5)

    parallel()
    get_camera_object().view(get_camera().move_down(0.47).inset(0.05),1.5)
    linear(1.5,d.c,0.0)
    end()

    pause()

    get_camera_object().view(get_camera().move_left(0.13),1.0)
    wait(-1.0)
    linear(1.0,d.pre,1.0)

    pause()

    # this does not work because viewport transforms have improper aspect
    #d = Drawable(get_camera().bottom(0.8).inset(0.02),slide_diag,slide=0,_alpha=0.0)
    # this is better
    d = Drawable(get_camera().move_down(0.1).inset(0.1),slide_diag,slide=0,_alpha=0.0)

    enter(d)
    fade_in(1.0,d)

    pause()

    get_camera_object().view(d._viewport,1.0)

    pause()

    d1 = Drawable(d._viewport,slide_diag,slide=1,_alpha=0.0)
    enter(d1)
    fade_out(1.0,d)
    wait(-1.0)
    fade_in(1.0,d1)
    



    return end_animation()

what_next_anim = what_next_anim()



def test_anim():

    d = Drawable(get_camera(),enter_slide_diag,diag = 0,t = 0.0,_alpha = 1.0)

    start_animation(d)

    smooth(2.0,d.t,1.0)

    pause()

    return end_animation()

test_anim = test_anim()
    


print calc_flyin_rect(0.0).width(),calc_flyin_rect(0.0).height() 
print calc_flyin_rect(1.0).width(), calc_flyin_rect(1.0).height()


test_objects( slide_diag,test_anim, enter_slide_diag,collab_diagram_next, collab_diagram, man_diag , comp_discuss_diag)
