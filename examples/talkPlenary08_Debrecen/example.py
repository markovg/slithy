from slithy.library import *

import facets

from fonts import fonts
import common

from images import images




def slide1_anim():

    cap = Text( get_camera().top(0.2).inset(0.1),
                color = yellow, font = fonts['times'], size = 22, _alpha = 1.0,
                justify = 0.5, text="Examples of convergence: " )


    start_animation( common.bg,cap)


    pause()

    bl = BulletedList( get_camera().bottom(0.9).inset(0.02),
                       font = fonts['times'], color = white,
                       bullet = [fonts['dingbats'], 'w'], size = 16 )

    enter(bl)

    bl.add_item( 0, 'Vogels+Abbott active states model:\nInhibitory conductances are 10 times too high (WP5-D16)' )

    pause()

    bl.add_item( 0, 'Natschlaeger et. al., 2003:\n Non-uniform random connectivity for a network of only 145 neurons? Cortex layer IV has 100000n/mm^3, dendrite length ~ 0.5 mm' )
    
    pause()

    bl.add_item( 0, "Many studies don't include adaptation or dynamic synapses.  OK for statics, certainly not for dynamics! (Muller et. al., 2007)")
    
    pause()


    bl.add_item( 0, 'Lanser et. al. "Huge-scale attractor networks" model non-random connection structure, Basket cells')

    #pause()
    
    #bl.add_item( 0, "Let's converge:\nresolve basic architectural differences accross FACETS ")

    #pause()

    #bl.add_item( 0, 'and contrain computational theories ...')





    

    return end_animation()

slide1_anim = slide1_anim()


def slide2_anim():

    start_animation(common.bg)

    c = white

    cap = Text( get_camera().top(0.3).inset(0.1).move_down(0.2),
                color = c, font = fonts['times'], size = 24, _alpha = 1.0,
                justify = 0.5, text="Let's converge:\nResolve basic architectural differences accross FACETS")

    enter(cap)


    pause()

    cap1 = Text( get_camera().bottom(0.6).top(0.5).move_down(0.1),
                color = c, font = fonts['times'], size = 24, _alpha = 0.0,
                justify = 0.5, text='constrain computational theories')

    enter(cap1)

    fade_in(1.0,cap1)

    pause()

    cap2 = Text( get_camera().bottom(0.6).bottom(0.5).move_up(0.2),
                 color = c, font = fonts['times'], size = 24, _alpha = 0.0,
                 justify = 0.5, text='justify a large-scale bottom-up model \n through simultaneous consistancy with many benchmarks.')

    enter(cap2)

    fade_in(1.0,cap2)


    return end_animation()

slide2_anim = slide2_anim()
    


test_objects(slide2_anim,slide1_anim)
