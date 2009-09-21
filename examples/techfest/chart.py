from slithy.library import *
from slithy.util import *
from fonts import fonts
import math

total_data = [ 5384, 6112, 5656, 5804, 5766, 6550, 6403, 6577, 6126, 7741 ]
breakdown_data = [ [ 2507, 2043, 1294, 509, 96, 128 ],
                   [ 2192, 2017, 1193, 501, 94, 129 ],
                   [ 2449, 2554, 1288, 1197, 90, 163 ] ]

breakdown = ( ('Desktop Applications', (0.3, 0.7, 0.2), (0.3, 0.7, 0.2) ),
              ('Desktop Platforms',    (0.9, 0.7, 0.0), (0.9, 0.9, 0.9) ),
              ('Enterprise Software & Services', (0.9, 0.0, 0.0), (0.9, 0.9, 0.9) ),
              ('Consumer Software, Services, & Devices', (0.2, 0.4, 0.8), (0.2, 0.4, 0.8) ),
              ('Consumer Commerce Investments', (0.6, 0.2, 0.8), (0.9, 0.9, 0.9) ),
              ('Other', (0.6,), (0.9,) ) )

def chart2( subdivide = (SCALAR,0,1),
            fatten = (SCALAR,0,1),
            emphasize = (SCALAR,0,1),
            bluelabels = (SCALAR,0,1),
            greenlabels = (SCALAR,0,1),
            expand = (SCALAR,0,1),
            percentlabels = (SCALAR,0,1),
            ):
    set_camera( Rect(-2.5716113618775331, -1.3073038892905311, 14.066710900404384, 0, 1.2433333333333332) )
    #clear( white )
    thickness( 0.03 )

    width = 1 + fatten * 0.5

    color( 0 )

    text( 5, 9, 'Quarterly Revenue', fonts['bold'], size = 0.8 )
    
    if percentlabels < 0.5:
        color( 0, 2*(0.5-percentlabels) )
        push()
        translate( -0.5, 0 )
        for i in range(2,9,2):
            line( -0.1, i, 0.1, i )
            text( -0.3, i, str(i*1000), fonts['roman'], size = 0.4, anchor = 'e' )
            
        translate( -1.5, 4 )
        rotate( 90 )
        text( 0, 0.2, 'revenue ($ millions)', fonts['roman'], size = 0.5 )
        pop()
    else:
        color( 0, 2*(percentlabels-0.5) )
        push()
        translate( -0.5, 0 )
        for i, j in zip(range(2,9,2), ('25%', '50%', '75%', '100%')):
            line( -0.1, i, 0.1, i )
            text( -0.3, i, j, fonts['roman'], size = 0.4, anchor = 'e' )
            
        translate( -1.5, 4 )
        rotate( 90 )
        text( 0, 0.2, 'revenue (% of total)', fonts['roman'], size = 0.5 )
        pop()
        

    color( 0 )
    push()
    for s in ('Q4', 'Q1', 'Q2'):
        text( 0.5*width, -0.3, s, fonts['roman'], size = 0.4 )
        translate( width, 0 )
    pop()
    text( 0.5 * width, -0.8, '2001', fonts['roman'], size = 0.4 )
    text( 2.0 * width, -0.8, '2002', fonts['roman'], size = 0.4 )
    line( 1.0 * width, -0.1, 1.0 * width, -1.0 )

    if subdivide < 1.0:
        push()
        color( 0.2, 0.5, 0.8 )
        for val in total_data[-3:]:
            rectangle( 0.2, 0.0, width-0.2, val / 1000.0 )
            translate( width, 0 )
        pop()

    last = -10.0
    if subdivide > 0.0:
        push()
        for height, bd, drawnames in zip( total_data[-3:], breakdown_data, (0,) * (len(breakdown_data)-1) + (1,) ):
            expansion = 1 + expand * ((8000.0/height)-1)
            total = 0.0
            for (name, c, c2), value in zip( breakdown, bd ):
                value *= expansion
                col = interpolate( emphasize, c, c2 )
                color( *(col + (subdivide,)) )
                rectangle( 0.2, total / 1000.0, width-0.2, (total + value) / 1000.0 )
                if drawnames:
                    center = (total + value/2) / 1000.0
                    if center < last + 0.4:
                        center = last + 0.4
                    last = center
                    text( width+.3, center, name, fonts['roman'], size = 0.4, anchor = 'w' )
                total += value
            translate( width, 0 )
        pop()

    expansions = map( lambda x: 1+expand*((8000.0/x)-1), total_data[-3:] )

    if bluelabels > 0.0:
        each = split_sequence_smooth( 3, bluelabels, 0.5 )
        color( 1, each[0] )
        text( 0.5 * width, 6.098 * expansions[0], '7%', fonts['bold'], size = 0.4 )
        color( 1, each[1] )
        text( 1.5 * width, 5.652 * expansions[1], '8%', fonts['bold'], size = 0.4 )
        color( 1, each[2] )
        text( 2.5 * width, 6.889 * expansions[2], '15%', fonts['bold'], size = 0.4 )
        
    if greenlabels > 0.0:
        each = split_sequence_smooth( 3, greenlabels, 0.5 )
        color( 1, each[0] )
        text( 0.5 * width, 1.253 * expansions[0], '38%', fonts['bold'], size = 0.4 )
        color( 1, each[1] )
        text( 1.5 * width, 1.096 * expansions[1], '35%', fonts['bold'], size = 0.4 )
        color( 1, each[2] )
        text( 2.5 * width, 1.224 * expansions[2], '31%', fonts['bold'], size = 0.4 )
            
    color( 0 )
    line( width*3, 0, -0.5, 0, -0.5, 8 )
        
def chart1( bars=(SCALAR,0,10),
           onebar = (SCALAR,0,1) ):
    set_camera( Rect(-2.5716113618775331, -1.3073038892905311, 14.066710900404384, 0, 1.2433333333333332) )
    #clear( white )
    thickness( 0.03 )

    color( black )

    text( 5, 9, 'Quarterly Revenue', fonts['bold'], size = 0.8 )

    push()
    translate( -0.5, 0 )
    for i in range(2,9,2):
        line( -0.1, i, 0.1, i )
        text( -0.3, i, str(i*1000), fonts['roman'], size = 0.4, anchor = 'e' )

    push()
    translate( -1.5, 4 )
    rotate( 90 )
    text( 0, 0.2, 'revenue ($ millions)', fonts['roman'], size = 0.5 )
    pop()
    pop()

    if onebar == 0.0:
        push()
        for i in ['Q1','Q2','Q3','Q4','Q1','Q2','Q3','Q4','Q1','Q2']:
            text( 0.5, -0.3, i, fonts['roman'], size = 0.4 )
            translate( 1, 0 )
        pop()
        text( 2.0, -0.8, '2000', fonts['roman'], size = 0.4 )
        text( 6.0, -0.8, '2001', fonts['roman'], size = 0.4 )
        text( 9.0, -0.8, '2002', fonts['roman'], size = 0.4 )
        line( 4.0, -0.1, 4.0, -1.0 )
        line( 8.0, -0.1, 8.0, -1.0 )

        baralpha = split_sequence_smooth( 10, bars/10.0 )
        push()
        for val, alpha in zip( total_data, baralpha ):
            color( 0.2, 0.5, 0.8, alpha )
            rectangle( 0.2, 0.0, 0.8, val / 1000.0 )
            translate( 1, 0 )
        pop()
            
        color( 0 )
        line( 10, 0, -0.5, 0, -0.5, 8 )
    else:
        baralpha = split_sequence_smooth( 7, onebar )

        push()
        translate( -7 * onebar, 0.0 )

        push()
        for s, a in zip(['Q1','Q2','Q3','Q4','Q1','Q2','Q3'], baralpha):
            color( 0, 1.0-a )
            text( 0.5, -0.3, s, fonts['roman'], size = 0.4 )
            translate( 1, 0 )
        color( 0 )
        for s in ['Q4', 'Q1', 'Q2']:
            text( 0.5, -0.3, s, fonts['roman'], size = 0.4 )
            translate( 1, 0 )
        pop()
        
        color( 0, 1.0 - baralpha[1] )
        text( 2.0, -0.8, '2000', fonts['roman'], size = 0.4 )
        color( 0 )
        text( 6.0 + 1.5 * onebar, -0.8, '2001', fonts['roman'], size = 0.4 )
        text( 9.0, -0.8, '2002', fonts['roman'], size = 0.4 )
        color( 0, 1.0 - baralpha[4] )
        line( 4.0, -0.1, 4.0, -1.0 )
        color( 0 )
        line( 8.0, -0.1, 8.0, -1.0 )


        for val, alpha in zip( total_data[:-3], baralpha ):
            color( 0.2, 0.5, 0.8, 1.0 - alpha )
            rectangle( 0.2, 0.0, 0.8, val / 1000.0 )
            translate( 1, 0 )
        color( 0.2, 0.5, 0.8 )
        for val in total_data[-3:]:
            rectangle( 0.2, 0.0, 0.8, val / 1000.0 )
            translate( 1, 0 )
        pop()
            
        color( 0 )
        line( 10 - 7*onebar, 0, -0.5, 0, -0.5, 8 )
        
def chart():
    d = Drawable( get_camera(), chart1, _alpha = 1.0 )
    d2 = Drawable( get_camera(), chart2 )

    start_animation( Fill(color=white), d )

    smooth( 0.5, d.bars, 4.0 )
    pause()

    smooth( 0.5, d.bars, 8.0 )
    pause()
            
    smooth( 0.5, d.bars, 10.0 )
    pause()

    smooth( 1.0, d.onebar, 1.0 )
    pause()
    enter( d2 )
    exit( d )
    
    parallel()
    smooth( 0.5, d2.fatten, 1.0 )
    smooth( 0.5, d2.subdivide, 1.0 )
    end()
    pause()

    smooth( 0.5, d2.emphasize, 1.0 )
    pause()

    parallel()
    smooth( 1.0, d2.percentlabels, 1.0 )
    sequence( 0.5 )
    smooth( 0.5, d2.expand, 1.0 )
    end()
    end()
    pause()
    
    linear( 0.5, d2.greenlabels, 1.0 )
    pause()

    linear( 0.5, d2.bluelabels, 1.0 )

    return end_animation()
chart = chart()
chart_one = chart[0].anim

def chart_fast():
    d = Drawable( get_camera(), chart1 )
    d2 = Drawable( get_camera(), chart2 )
    bg = Fill( color = white )

    start_animation( bg, d )

    smooth( 0.5, d.bars, 4.0 )
    pause()

    smooth( 0.5, d.bars, 8.0 )
    pause()
            
    smooth( 0.5, d.bars, 10.0 )
    pause()

    smooth( 0.5, d.onebar, 1.0 )
    exit( d )
    enter( d2 )
    
    parallel()
    smooth( 0.5, d2.fatten, 1.0 )
    smooth( 0.5, d2.subdivide, 1.0 )
    smooth( 0.5, d2.emphasize, 1.0 )
    smooth( 0.5, d2.percentlabels, 1.0 )
    smooth( 0.5, d2.expand, 1.0 )
    linear( 0.5, d2.greenlabels, 1.0 )
    linear( 0.5, d2.bluelabels, 1.0 )
    end()
    pause()

    #enter( bg )
    #lower( bg )
    fade_out( 0.5, d2 )
    exit(d2)
    set( d._alpha, 0.0 )
    set( d.onebar, 0.0 )
    enter(d)
    fade_in( 0.5, d )
    #exit( bg )

    pause()
    smooth( 1.0, d.onebar, 1.0 )
    pause()
    
    exit( d )

    set( d2.fatten, 0.0 )
    set( d2.subdivide, 0.0 )
    set( d2.emphasize, 0.0 )
    set( d2.percentlabels, 0.0 )
    set( d2.greenlabels, 0.0 )
    set( d2.bluelabels, 0.0 )
    set( d2.expand, 0.0 )
    set( d2._alpha, 1.0 )
    enter( d2 )
    
    parallel()
    smooth( 0.5, d2.fatten, 1.0 )
    smooth( 0.5, d2.subdivide, 1.0 )
    end()
    pause()

    smooth( 0.5, d2.emphasize, 1.0 )
    pause()

    parallel()
    smooth( 1.0, d2.percentlabels, 1.0 )
    sequence( 0.5 )
    smooth( 0.5, d2.expand, 1.0 )
    end()
    end()
    pause()
    
    linear( 0.5, d2.greenlabels, 1.0 )
    pause()

    linear( 0.5, d2.bluelabels, 1.0 )
    
    

    return end_animation()
chart_fast = chart_fast()

test_objects( chart, chart1, chart2 )

