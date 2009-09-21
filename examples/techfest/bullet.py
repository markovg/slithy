from slithy.library import *
from fonts import fonts
import random

import infinite
import ssort

titlecolor = Color(0.0, 0.3, 0.8)

bg = Fill( color = white )
title = Text( get_camera().inset(0.05).top(0.15), color = titlecolor, font = fonts['bold'],
              _alpha = 0.0, size = 24 )
bl = BulletedList( get_camera().inset(0.05).bottom(0.8), font = fonts['roman'], color = black,
                   size = 18.0, _alpha = 0.0, bullet = [fonts['dingbats'],'w'] )

# def show_chart( d ):
#     waittime = 0.5

#     fade_in( 0.5, d )
    
#     parallel()
#     smooth( 0.5, d.fatten, 1.0 )
#     smooth( 0.5, d.subdivide, 1.0 )
#     end()
#     wait( waittime )

#     smooth( 0.5, d.emphasize, 1.0 )
#     wait( waittime )

#     parallel()
#     smooth( 1.0, d.percentlabels, 1.0 )
#     sequence( 0.5 )
#     smooth( 0.5, d.expand, 1.0 )
#     end()
#     end()
#     wait( waittime )
    
#     linear( 0.5, d.greenlabels, 1.0 )
#     wait( waittime )

#     linear( 0.5, d.bluelabels, 1.0 )

    

def show_sort():
    values = [0.3, 0.5, 0.1, 0.9, 1.0, 0.55, 0.35, 0.8, 0.2, 0.15]
    sorter = ssort.SelectionSort( values )
    d = Drawable( get_camera(), sorter )

    start_animation( d )
    
    minspeed = 0.3
    maxspeed = 0.1
    mult = (maxspeed / minspeed) ** (1.0 / sorter.n)
    speed = minspeed
    for i in range( sorter.n ):
        parallel()
        smooth( speed, d.showpivot, 1.0 )
        serial( speed / 2 )
        smooth( speed, d.showmin, 1.0 )
        end()
        end()
        smooth( speed, d.swap, 1.0 )
        parallel()
        smooth( speed, d.showmin, 2.0 )
        smooth( speed, d.showpivot, 0.0 )
        end()
        set( d.showmin, 0.0 )
        set( d.swap, 0.0 )
        set( d.step, i+1 )
        speed *= mult

    return end_animation()
sort_one = show_sort()[0]
            

# def show_pythagoras( d ):
#     waittime = 0.15
    
#     set( d.textlabel, 1.0 )
#     fade_in( 0.5, d )
#     wait( waittime )
    
#     #smooth( 0.5, d.textlabel, 0.0 )
#     smooth( 0.5, d.linealpha, 1.0 )
#     wait( waittime )

#     smooth( 1.0, d.lineextend, 1.0 )
#     wait( waittime )

#     smooth( 1.0, d.subdivide, 0.8 )
#     wait( waittime )

#     parallel()
#     serial()
#     smooth( 0.5, d.slidea, 1 )
#     wait( waittime )
#     smooth( 0.5, d.slidea, 2 )
#     wait( waittime )
#     smooth( 0.5, d.slidea, 3 )
#     wait( waittime )
#     end()

#     serial( 1.2 )
#     smooth( 0.5, d.slideb, 1 )
#     wait( waittime )
#     smooth( 0.5, d.slideb, 2 )
#     wait( waittime )
#     smooth( 0.5, d.slideb, 3 )
#     wait( waittime )
#     end()
#     end()

#     smooth( 0.5, d.subdivide, 0 )



# def why_slithy():
#     values = [random.uniform( 0.1, 0.9 ) for i in range(10)]
#     sorter = ssort.SelectionSort( values )

#     drawrect = get_camera().right(0.6).bottom(0.6).inset(0.05)
#     d1 = Drawable( drawrect, pythagoras.pythagoras_d, _alpha = 0.0 )
#     d2 = Drawable( drawrect, sorter, _alpha = 0.0 )
#     d3 = Drawable( drawrect, chart.chart2, _alpha = 0.0 )
    
#     start_animation( bg, title, bl )

#     set( title.text, 'Animation in presentations' )
    
#     bl.add_item( 0, 'We believe animation can make all kinds of presentations more effective:', 0.5 )
    
#     fade_in( 0.5, title, bl )

#     pause()

#     bl.add_item( 1, 'in mathematics', 0.5 )
#     enter( d1 )
#     show_pythagoras( d1 )
#     pause()
#     fade_out( 0.5, d1 )
#     exit( d1 )

#     bl.add_item( 1, 'in computer science', 0.5 )
#     enter( d2 )
#     show_sort( sorter, d2 )
#     pause()
#     fade_out( 0.5, d2 )
#     exit( d2 )

#     bl.add_item( 1, 'and outside\nacademia, too', 0.5 )
#     enter( d3 )
#     show_chart( d3 )
#     pause()
#     fade_out( 0.5, d3 )
#     exit( d3 )

#     bl.add_item( 0, ['What makes animations ', fonts['italic'], titlecolor, 'effective', RESETCOLOR, '?'], 0.5 )
#     pause()
#     bl.add_item( 0, ['How do we ', fonts['italic'], titlecolor, 'create', RESET, ' them?'], 0.5 )
#     pause()

#     fade_out( 0.5, title, bl )

#     return end_animation()
# why_slithy = why_slithy()

# def iterative_approach():
#     start_animation( bg, title, bl )
#     set( title.text, 'An iterative approach' )
#     fade_in( 0.5, title, bl )
#     pause()

#     bl.add_item( 0, 'create some animated presentations', 0.5 )
#     pause()
#     bl.add_item( 0, 'identify things that work well', 0.5 )
#     pause()
#     bl.add_item( 1, ['what ', fonts['italic'], titlecolor, 'kinds', RESET, ' of animation'], 0.5 )
#     pause()
#     bl.add_item( 1, [fonts['italic'], titlecolor, 'techniques', RESET, ' for producing those animations'], 0.5 )
#     pause()
#     bl.add_item( 0, 'improve system to make authoring those things easier', 0.5 )
#     pause()
#     bl.add_item( 0, 'repeat', 0.5 )
#     pause()

#     fade_out( 0.5, title, bl )

#     return end_animation()
# iterative_approach = iterative_approach()
    

# def slideshow_container():
#     a = Anim( get_camera().inset( 0.05 ) )

#     start_animation( bg, a )
#     a.play( imagepan.slideshow, fade=1 )

#     return end_animation()
# slideshow_container = slideshow_container()
    
# def interaction_piechart():
#     i = Interactive( get_camera().bottom(0.625), controller = piechart.PiechartController )
    
#     start_animation( bg, title, bl )
#     set( title.text, 'Interactive controllers' )
#     fade_in( 0.5, title, bl )

#     bl.add_item( 0, 'This lets authors include interactive features in their presentations.', 0.5 )
#     pause()
#     enter( i )
#     pause()
    
#     return end_animation()
# interaction_piechart = interaction_piechart()
    


# # def opengl_interaction():
# #     camera = start_animation( [bg, title, bl] )
# #     camera.install( (0, 0, 400, 0, 4.0 / 3.0) )

# #     set( title.text, '3D via OpenGL' )
    
# #     bl.add_item( 0, '3D diagrams can be authored using C and OpenGL.' )
    
# #     fade_in( 0.5, title, bl )
# #     pause()

# #     fade_out( 0.5, title, bl )

# #     return end_animation()

# def playing_video():
#     start_animation( bg, title, bl )

#     set( title.text, 'Support for videos' )
    
#     bl.add_item( 0, 'Under Windows, Slithy can play videos using DirectShow.' )
    
#     fade_in( 0.5, title, bl )
#     v = Video( get_camera().bottom(0.6).inset(0.05), 'images/running.avi' )
#     enter( v )
#     pause()
#     exit( v )

#     fade_out( 0.5, title, bl )

#     return end_animation()
# playing_video = playing_video()

# def future_work2():
#     layout_pic = load_image( imagepath.search( 'layout4.png' ) )
#     badslide_pic = load_image( imagepath.search( 'badslide.jpg' ) )
    
#     im = Image( image = layout_pic,
#                 x1 = 20, x2 = 380, y1 = 20, y2 = 210, alpha = 0.0 )
#     camera = start_animation( [bg, title, bl, im] )
#     camera.install( (0, 0, 400, 0, 4.0 / 3.0) )

#     set( title.text, 'Future work' )

#     bl.add_item( 0, 'Interactive tools for authoring' )

#     fade_in( 0.5, title, bl )
#     fade_in( 0.5, im )

#     pause()

#     fade_out( 0.5, im )
#     bl.add_item( 0, ['What makes a ', fonts['bolditalic'], 'good', RESET, ' animated presentation?'] )
#     set( im.image, badslide_pic )
#     set( im.y2, 170 )
#     fade_in( 0.5, im )

#     pause()

#     fade_out( 0.5, title, bl, im )

#     return end_animation()

              
    

# def future_work():
#     camera = start_animation( [bg, title, bl] )
#     camera.install( (0, 0, 400, 0, 4.0 / 3.0) )

#     set( title.text, 'Future work' )
    
#     bl.add_item( 0, 'Creating presentations from templates' )
    
#     fade_in( 0.5, title, bl )
#     pause()

#     fade_out( 0.5, title, bl )

#     return end_animation()
    
# def the_end():
#     tx = Text( x = 200, y = 150, font = fonts['bold'], color = titlecolor, text = 'the end', size = 30, alpha = 0.0, anchor = 'c' )
    
#     camera = start_animation( [bg, tx] )
#     camera.install( (0, 0, 400, 0, 4.0 / 3.0) )

#     fade_in( 0.5, tx )
#     pause()
#     fade_out( 0.5, tx )

#     return end_animation()

def change_bullet( bl, newtext ):
    serial()
    fade_out( 0.25, bl )
    bl.remove_item()
    bl.add_item( 0, newtext )
    fade_in( 0.25, bl )
    end()
    
def drawing_canvas():
    dv = viewport.interp( get_camera(),
                          get_camera().bottom(0.65).inset(0.05),
                          get_camera().bottom(0.65).left(0.5).inset(0.05) )
    dv2 = viewport.interp( get_camera().bottom(0.65).inset(0.05),
                           get_camera().bottom(0.65).right(0.5).inset(0.05) )
    d = Drawable( dv, infinite.infinite_canvas )
    d2 = Drawable( dv2, infinite.infinite_canvas )
    
    start_animation( bg, title, bl, d )

    set( title.text, 'Infinite drawing canvas' )
    
    bl.add_item( 0, 'Parameterized diagrams draw on an infinite plane.' )

    fade_in( 0, title, bl, d )

    smooth( 0.5, d.grid, 1.0 )
    pause()

    parallel()
    change_bullet( bl, 'You can place a "window" onto this plane on your slide.' )
    smooth( 0.5, d.cam, 1.0 )
    #d.camera( 'centered', 0.5, smooth )
    smooth( 0.5, dv.x, 1.0 )
    #smooth( 0.5, d.x1, 100 )
    #smooth( 0.5, d.x2, 300 )
    #smooth( 0.5, d.y1, 20 )
    #smooth( 0.5, d.y2, 190 )
    end()

    pause()

    parallel()
    change_bullet( bl, 'The window can view any part of the diagram plane.' )
    smooth( 0.5, d.cam, 2.0 )
    #d.camera( 'blue', 0.5, smooth )
    end()

    pause()

    enter( d2 )
    set( d2.cam, 2.0 )
    #d2.camera( 'blue' )
    set( d2.grid, 1.0 )
    lower( d2, below = d )
    parallel()
    change_bullet( bl, 'Multiple windows can view different parts of the diagram.' )
    smooth( 0.5, dv.x, 2.0 )
    smooth( 0.5, dv2.x, 1.0 )
    #smooth( 0.5, d.x1, 20 )
    #smooth( 0.5, d.x2, 190 )
    #smooth( 0.5, d2.x1, 210 )
    #smooth( 0.5, d2.x2, 380 )
    end()
    smooth( 1.0, d2.cam, 3.0 )
    #d2.camera( 'green', 1.0, smooth )

    pause()
    
    parallel()
    change_bullet( bl, 'Or, the windows might view the diagram in different states.' )
    smooth( 1.0, d2.expand, 1.0 )
    end()
    smooth( 1.0, d.expand, -0.5 )
    

    return end_animation()
drawing_canvas = drawing_canvas()
infinite_one = drawing_canvas[0].anim

# def overview_bullets():
#     camera = start_animation( [bg, title, bl] )
#     camera.install( (0, 0, 400, 0, 4.0 / 3.0) )

#     set( title.text, 'Authoring in Slithy' )
    
#     bl.add_item( 0, 'Slithy is a set of libraries for the Python programming language.' )
    
#     fade_in( 0.5, title, bl )
#     pause()

#     bl.add_item( 0, ['First, you create a ', fonts['bolditalic'], titlecolor, 'parameterized diagram', RESET, '.'] )
#     bl.add_item( 1, 'makes a drawing based on some domain-specific parameters' )

#     pause()
    
#     fade_out( 0.5, title, bl )

#     pause()

#     fade_in( 0.5, title, bl )

#     pause()

#     bl.add_item( 0, ['Then, an ', fonts['bolditalic'], titlecolor, 'animation script', RESET, ' lays out how those parameters should change over time to create the desired animation.'] )

#     pause()

#     fade_out( 0.5, title, bl )

#     return end_animation()

# def make_full( d, all ):
#     lift( d )
#     parallel()
#     smooth( 0.5, d.x1, 0 )
#     smooth( 0.5, d.x2, 400 )
#     smooth( 0.5, d.y1, 0 )
#     smooth( 0.5, d.y2, 300 )
#     end()
#     for i in all:
#         if i is not d:
#             exit( i )
            

# def make_small( d, all, x1, y1, x2, y2 ):
#     for i in all:
#         if i is not d:
#             enter( i )
#     lift( d )
#     parallel()
#     smooth( 0.5, d.x1, x1 )
#     smooth( 0.5, d.x2, x2 )
#     smooth( 0.5, d.y1, y1 )
#     smooth( 0.5, d.y2, y2 )
#     end()


# def drawing_library_intro():
#     d1 = Diagram( x1 = 0, y1 = 100, x2 = 133, y2 = 200, draw = shapes.pretty_lines, alpha = 1.0 )
#     d2 = Diagram( x1 = 134, y1 = 100, x2 = 267, y2 = 200, draw = shapes.pretty_circles, alpha = 1.0 )
#     d3 = Diagram( x1 = 267, y1 = 100, x2 = 400, y2 = 200, draw = shapes.pretty_squares, alpha = 1.0 )
#     d4 = Diagram( x1 = 0, y1 = 0, x2 = 133, y2 = 100, draw = shapes.pretty_paths, alpha = 1.0 )
#     d5 = Diagram( x1 = 134, y1 = 0, x2 = 267, y2 = 100, draw = shapes.pretty_images, alpha = 1.0 )
#     d6 = Diagram( x1 = 267, y1 = 0, x2 = 400, y2 = 100, draw = shapes.pretty_text, alpha = 1.0 )
    
#     camera = start_animation( [bg, title, bl, d1, d2, d3, d4, d5, d6] )
#     camera.install( (0, 0, 400, 0, 4.0 / 3.0) )

#     set( title.text, 'Creating parameterized diagrams' )

#     set( d2.appear, 1.0 )
#     set( d6.line, 1 )
    
#     bl.add_item( 0, 'Drawing is done with a simple but fairly powerful 2D graphics library.' )
    
#     fade_in( 0.5, title, bl )
#     pause()

#     all = [d1, d2, d3, d4, d5, d6]

#     ##
#     ## lines
#     ##

#     make_full( d1, all )

#     smooth( 3.0, d1.appear, 1.0 )

#     wait( -1.0 )

#     parallel()
#     smooth( 3.0, d1.t, 10.0 )
#     serial( 0.5 )
#     smooth( 1.0, d1.fade, 1.0 )
#     end()
#     smooth( 3.5, d1.rot, 135.0 )
#     end()

#     make_small( d1, all, 0, 100, 133, 200 )

#     ##
#     ## circles
#     ##

#     make_full( d2, all )
    
#     parallel()
#     smooth( 2.0, d2.spread, 0.68 )
#     smooth( 2.0, d2.twist, 1000 )
#     end()

#     wait( 0.5 )
#     smooth( 2.0, d2.twist, 2347 )
#     wait( 0.5 )

#     parallel()
#     smooth( 2.0, d2.spread, -0.68 )
#     smooth( 2.0, d2.twist, -410 )
#     end()

#     make_small( d2, all, 134, 100, 267, 200 )

#     ##
#     ## squares
#     ##

#     make_full( d3, all )

#     smooth( 5.0, d3.drop, 1.0 )

#     #set( dmain.angle, 270.0 )
#     smooth( 4.0, d3.rot, 1.0 )

#     make_small( d3, all, 267, 100, 400, 200 )

#     ##
#     ## paths
#     ##

#     make_full( d4, all )

#     parallel()
#     serial()
#     smooth( 2.0, d4.x, 3.0 )
#     smooth( 2.0, d4.x, 2.0 )
#     smooth( 2.0, d4.x, -4.0 )
#     end()
#     serial()
#     smooth( 2.0, d4.y, -2.0 )
#     smooth( 2.0, d4.y, 2.0 )
#     smooth( 2.0, d4.y, -4.0 )
#     end()
#     serial()
#     smooth( 2.0, d4.r, 270.0 )
#     smooth( 2.0, d4.r, 630.0 )
#     smooth( 2.0, d4.r, 1080.0 )
#     end()
#     end()

#     make_small( d4, all, 0, 0, 133, 100 )

#     ##
#     ## images
#     ##

#     make_full( d5, all )

#     movetime = 0.5
#     pausetime = 0.2

#     smooth( movetime, d5.rot, 1 )
#     wait( pausetime )
#     smooth( movetime, d5.rot, 2 )
#     wait( pausetime )
#     smooth( movetime, d5.rot, 3 )
#     wait( pausetime )
#     parallel()
#     serial()
#     smooth( movetime, d5.rot, 4 )
#     wait( pausetime )
#     smooth( movetime, d5.rot, 5 )
#     wait( pausetime )
#     smooth( movetime, d5.rot, 6 )
#     wait( pausetime )
#     smooth( movetime, d5.rot, 7 )
#     wait( pausetime )
#     smooth( movetime, d5.rot, 8 )
#     wait( pausetime )
#     smooth( movetime, d5.rot, 9 )
#     wait( pausetime )
#     smooth( movetime, d5.rot, 10 )
#     wait( pausetime )
#     smooth( movetime, d5.rot, 11 )
#     wait( pausetime )
#     smooth( movetime, d5.rot, 12 )
#     end()
#     d5.camera( 'zoomout2', 2.0, smooth )
#     end()

#     make_small( d5, all, 134, 0, 267, 100 )

#     ##
#     ## text
#     ##

#     make_full( d6, all )

#     linear( 0.5, d6.line, 2.0 )
#     smooth( 0.5, d6.justify, 1.0 )
#     wait( 0.5 )
#     smooth( 0.5, d6.justify, 0.0 )

#     wait( 0.5 )

#     linear( 0.5, d6.line, 3.0 )
#     linear( 0.5, d6.showcolor, 1.0 )

#     wait( 0.5 )

#     linear( 0.5, d6.line, 4.0 )

#     wait( 0.5 )

#     make_small( d6, all, 267, 0, 400, 100 )

#     pause()
    

#     fade_out( 0.5, title, bl, d1, d2, d3, d4, d5, d6 )

#     return end_animation()

# def make_full_pair( dleft, dright, all ):
#     lift( dleft, dright )
#     parallel()
#     smooth( 0.5, dleft.x1, 0 )
#     smooth( 0.5, dleft.x2, 200 )
#     smooth( 0.5, dleft.y1, 0 )
#     smooth( 0.5, dleft.y2, 300 )
#     smooth( 0.5, dright.x1, 200 )
#     smooth( 0.5, dright.x2, 400 )
#     smooth( 0.5, dright.y1, 0 )
#     smooth( 0.5, dright.y2, 300 )
#     end()
#     for i in all:
#         if i is not dleft and i is not dright:
#             exit( i )
            

# def make_small_pair( dleft, dright, all, lx1, ly1, lx2, ly2, rx1, ry1, rx2, ry2 ):
#     for i in all:
#         if i is not dleft and i is not dright:
#             enter( i )
#     lift( dleft, dright )
#     parallel()
#     smooth( 0.5, dleft.x1, lx1 )
#     smooth( 0.5, dleft.x2, lx2 )
#     smooth( 0.5, dleft.y1, ly1 )
#     smooth( 0.5, dleft.y2, ly2 )
#     smooth( 0.5, dright.x1, rx1 )
#     smooth( 0.5, dright.x2, rx2 )
#     smooth( 0.5, dright.y1, ry1 )
#     smooth( 0.5, dright.y2, ry2 )
#     end()

    
# def drawing_library_intro_paired():
#     d1 = Diagram( x1 = 0, y1 = 100, x2 = 133, y2 = 200, draw = shapes.pretty_lines, alpha = 1.0 )
#     d2 = Diagram( x1 = 134, y1 = 100, x2 = 267, y2 = 200, draw = shapes.pretty_circles, alpha = 1.0 )
#     d3 = Diagram( x1 = 267, y1 = 100, x2 = 400, y2 = 200, draw = shapes.pretty_squares, alpha = 1.0 )
#     d4 = Diagram( x1 = 0, y1 = 0, x2 = 133, y2 = 100, draw = shapes.pretty_paths, alpha = 1.0 )
#     d5 = Diagram( x1 = 134, y1 = 0, x2 = 267, y2 = 100, draw = shapes.pretty_images, alpha = 1.0 )
#     d6 = Diagram( x1 = 267, y1 = 0, x2 = 400, y2 = 100, draw = shapes.pretty_text, alpha = 1.0 )
    
#     camera = start_animation( [bg, title, bl, d1, d2, d3, d4, d5, d6] )
#     camera.install( (0, 0, 400, 0, 4.0 / 3.0) )

#     set( title.text, 'Creating parameterized diagrams' )

#     set( d2.appear, 1.0 )
#     set( d6.line, 1 )
    
#     bl.add_item( 0, 'Drawing is done with a simple but fairly powerful 2D graphics library.' )
    
#     fade_in( 0.5, title, bl )
#     pause()

#     all = [d1, d2, d3, d4, d5, d6]


#     make_full_pair( d1, d4, all )

#     parallel()
    
#     ##
#     ## lines
#     ##
    
#     serial()
#     smooth( 3.0, d1.appear, 1.0 )

#     wait( -1.0 )

#     parallel()
#     smooth( 3.0, d1.t, 10.0 )
#     serial( 0.5 )
#     smooth( 1.0, d1.fade, 1.0 )
#     end()
#     smooth( 3.5, d1.rot, 135.0 )
#     end()
#     end()

#     ##
#     ## paths
#     ##

#     serial()
#     parallel()
#     serial()
#     smooth( 2.0, d4.x, 3.0 )
#     smooth( 2.0, d4.x, 2.0 )
#     smooth( 2.0, d4.x, -4.0 )
#     end()
#     serial()
#     smooth( 2.0, d4.y, -2.0 )
#     smooth( 2.0, d4.y, 2.0 )
#     smooth( 2.0, d4.y, -4.0 )
#     end()
#     serial()
#     smooth( 2.0, d4.r, 270.0 )
#     smooth( 2.0, d4.r, 630.0 )
#     smooth( 2.0, d4.r, 1080.0 )
#     end()
#     end()
#     end()

#     end()
    

#     make_small_pair( d1, d4, all, 0, 100, 133, 200, 0, 0, 133, 100 )


#     make_full_pair( d2, d5, all )
#     parallel()
    
#     ##
#     ## circles
#     ##
    
#     serial()
#     parallel()
#     smooth( 2.0, d2.spread, 0.68 )
#     smooth( 2.0, d2.twist, 1000 )
#     end()

#     wait( 0.5 )
#     smooth( 2.0, d2.twist, 2347 )
#     wait( 0.5 )

#     parallel()
#     smooth( 2.0, d2.spread, -0.68 )
#     smooth( 2.0, d2.twist, -410 )
#     end()
#     end()

#     ##
#     ## images
#     ##

#     serial()
#     movetime = 0.5
#     pausetime = 0.2

#     smooth( movetime, d5.rot, 1 )
#     wait( pausetime )
#     smooth( movetime, d5.rot, 2 )
#     wait( pausetime )
#     smooth( movetime, d5.rot, 3 )
#     wait( pausetime )
#     parallel()
#     serial()
#     smooth( movetime, d5.rot, 4 )
#     wait( pausetime )
#     smooth( movetime, d5.rot, 5 )
#     wait( pausetime )
#     smooth( movetime, d5.rot, 6 )
#     wait( pausetime )
#     smooth( movetime, d5.rot, 7 )
#     wait( pausetime )
#     smooth( movetime, d5.rot, 8 )
#     wait( pausetime )
#     smooth( movetime, d5.rot, 9 )
#     wait( pausetime )
#     smooth( movetime, d5.rot, 10 )
#     wait( pausetime )
#     smooth( movetime, d5.rot, 11 )
#     wait( pausetime )
#     smooth( movetime, d5.rot, 12 )
#     end()
#     d5.camera( 'zoomout2', 2.0, smooth )
#     end()
#     end()



#     end()
#     make_small_pair( d2, d5, all, 134, 100, 267, 200, 134, 0, 267, 100 )


#     make_full_pair( d3, d6, all )
#     parallel()

#     ##
#     ## squares
#     ##

#     serial()
#     smooth( 5.0, d3.drop, 1.0 )

#     #set( dmain.angle, 270.0 )
#     smooth( 3.0, d3.rot, 1.0 )
#     end()

#     ##
#     ## text
#     ##

#     serial()
#     linear( 0.5, d6.line, 2.0 )
#     smooth( 0.5, d6.justify, 1.0 )
#     wait( 0.5 )
#     smooth( 0.5, d6.justify, 0.0 )

#     wait( 0.5 )

#     linear( 0.5, d6.line, 3.0 )
#     linear( 0.5, d6.showcolor, 1.0 )

#     wait( 0.5 )

#     linear( 0.5, d6.line, 4.0 )

#     wait( 0.5 )

#     smooth( 2.0, d6.justify, 0.5 )
#     end()

#     end()

#     make_small_pair( d3, d6, all, 267, 100, 400, 200, 267, 0, 400, 100 )


#     pause()
    

#     fade_out( 0.5, title, bl, d1, d2, d3, d4, d5, d6 )

#     return end_animation()
    

# test_animations( drawing_library_intro_paired )

# def title_slide():
#     upper = Text( get_camera().top(0.5).inset( 0.05 ),
#                   text = 'Animation for Presentations',
#                   font = fonts['bold'], size = 24, color = titlecolor,
#                   justify = 0.5, vjustify = 0.5 )
#     lower = Text( get_camera().bottom(0.5).inset( 0.10 ),
#                   text = 'Doug Zongker\nDavid Salesin\n\nUniversity of Washington\nMicrosoft Research',
#                   font = fonts['roman'], size = 14, color = black,
#                   justify = 0.5 )

#     start_animation( upper, lower )

#     pause()
#     fade_out( 0.5, upper, lower )

#     return end_animation()
# title_slide = title_slide()

# test_objects( title_slide, playing_video, interaction_piechart, drawing_canvas, slideshow_container, iterative_approach, why_slithy )
