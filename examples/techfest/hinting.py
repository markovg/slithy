from slithy.library import *
import math

book_a = (2,
          40,
          826, 968, 1, 0,
          849, 953, 23, 1,
          751, 613, 2, 2,
          697, 350, 3, 3,
          666, 198, 6, 4,
          666, 151, 21, 5,
          666, 132, 20, 6,	
          682, 112, 22, 7,
          696, 112, 51, 8,
          729, 112, 50, 9,
          845, 209, 55, 10,
          857, 163, 23, 11,
          749, 68, 6, 12,
          649, 11, 7, 13,
          600, -16, 6, 14,
          564, -16, 35, 15,
          537, -16, 34, 16,
          511, 15, 38, 17,
          511, 50, 53, 18,
          511, 132, 52, 19,
          579, 391, 19, 20,
          571, 392, 39, 21,
          429, 186, 6, 22,
          269, 59, 7, 23,
          161, -27, 6, 24,
          111, -27, 35, 25,
          81, -27, 34, 26,
          64, 3, 39, 27,
          39, 49, 38, 28,
          39, 136, 53, 29,
          39, 284, 52, 30,
          158, 694, 18, 31,
          220, 781, 55, 32,
          267, 847, 54, 33,
          403, 922, 55, 34,
          488, 969, 54, 35,
          580, 969, 51, 36,
          620, 969, 50, 37,
          711, 951, 22, 38,
          762, 933, 23, 39,
          18,  
          673, 837, 7, 40,
          629, 854, 46, 41,
          551, 870, 46, 42,
          516, 870, 35, 43,
          438, 870, 34, 44,
          375, 843, 7, 45,
          357, 834, 6, 46,
          329, 777, 7, 47,
          274, 663, 6, 48,
          185, 311, 2, 49,
          185, 177, 21, 50,
          185, 141, 20, 51,
          206, 111, 22, 52,
          221, 111, 51, 53,
          262, 111, 50, 54,
          481, 321, 54, 55,
          544, 433, 55, 56,
          628, 584, 54, 57,
          909, 39)

book_a_pix = ((3, -1), (4, -1), (5, -1), (6, -1), (24, -1), (25, -1), (3, 0),
(4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (23, 0), (24, 0), (25, 0), (26, 0), (27, 0), (28,
0), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (22, 1), (23, 1), (24,
1), (25, 1), (26, 1), (27, 1), (28, 1), (29, 1), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7,
2), (8, 2), (9, 2), (10, 2), (11, 2), (22, 2), (23, 2), (24, 2), (25, 2), (26, 2), (27, 2),
(28, 2), (29, 2), (30, 2), (31, 2), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3),
(9, 3), (10, 3), (11, 3), (12, 3), (23, 3), (24, 3), (25, 3), (26, 3), (27, 3), (28, 3),
(29, 3), (30, 3), (31, 3), (32, 3), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4),
(9, 4), (10, 4), (11, 4), (12, 4), (13, 4), (23, 4), (24, 4), (25, 4), (26, 4), (27, 4),
(28, 4), (29, 4), (30, 4), (31, 4), (32, 4), (33, 4), (2, 5), (3, 5), (4, 5), (5, 5), (6,
5), (7, 5), (8, 5), (11, 5), (12, 5), (13, 5), (14, 5), (23, 5), (24, 5), (25, 5), (26, 5),
(27, 5), (28, 5), (29, 5), (32, 5), (33, 5), (34, 5), (35, 5), (2, 6), (3, 6), (4, 6), (5,
6), (6, 6), (7, 6), (13, 6), (14, 6), (15, 6), (23, 6), (24, 6), (25, 6), (26, 6), (27, 6),
(28, 6), (34, 6), (35, 6), (36, 6), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (14, 7),
(15, 7), (16, 7), (23, 7), (24, 7), (25, 7), (26, 7), (27, 7), (28, 7), (35, 7), (36, 7),
(37, 7), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (15, 8), (16, 8), (17, 8), (23, 8),
(24, 8), (25, 8), (26, 8), (27, 8), (28, 8), (36, 8), (2, 9), (3, 9), (4, 9), (5, 9), (6,
9), (7, 9), (16, 9), (17, 9), (18, 9), (24, 9), (25, 9), (26, 9), (27, 9), (28, 9), (29,
9), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (17, 10), (18, 10), (19, 10),
(24, 10), (25, 10), (26, 10), (27, 10), (28, 10), (29, 10), (2, 11), (3, 11), (4, 11),
(5, 11), (6, 11), (7, 11), (18, 11), (19, 11), (20, 11), (24, 11), (25, 11), (26, 11),
(27, 11), (28, 11), (29, 11), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (19,
12), (20, 12), (21, 12), (24, 12), (25, 12), (26, 12), (27, 12), (28, 12), (29, 12), (2,
13), (3, 13), (4, 13), (5, 13), (6, 13), (7, 13), (8, 13), (20, 13), (21, 13), (24, 13),
(25, 13), (26, 13), (27, 13), (28, 13), (29, 13), (3, 14), (4, 14), (5, 14), (6, 14), (7,
14), (8, 14), (21, 14), (22, 14), (25, 14), (26, 14), (27, 14), (28, 14), (29, 14), (3,
15), (4, 15), (5, 15), (6, 15), (7, 15), (8, 15), (22, 15), (23, 15), (25, 15), (26, 15),
(27, 15), (28, 15), (29, 15), (30, 15), (3, 16), (4, 16), (5, 16), (6, 16), (7, 16), (8,
16), (22, 16), (23, 16), (24, 16), (25, 16), (26, 16), (27, 16), (28, 16), (29, 16),
(30, 16), (3, 17), (4, 17), (5, 17), (6, 17), (7, 17), (8, 17), (23, 17), (24, 17), (25,
17), (26, 17), (27, 17), (28, 17), (29, 17), (30, 17), (4, 18), (5, 18), (6, 18), (7,
18), (8, 18), (24, 18), (25, 18), (26, 18), (27, 18), (28, 18), (29, 18), (30, 18), (4,
19), (5, 19), (6, 19), (7, 19), (8, 19), (9, 19), (24, 19), (25, 19), (26, 19), (27, 19),
(28, 19), (29, 19), (30, 19), (31, 19), (4, 20), (5, 20), (6, 20), (7, 20), (8, 20), (9,
20), (25, 20), (26, 20), (27, 20), (28, 20), (29, 20), (30, 20), (31, 20), (4, 21), (5,
21), (6, 21), (7, 21), (8, 21), (9, 21), (25, 21), (26, 21), (27, 21), (28, 21), (29,
21), (30, 21), (31, 21), (5, 22), (6, 22), (7, 22), (8, 22), (9, 22), (26, 22), (27, 22),
(28, 22), (29, 22), (30, 22), (31, 22), (5, 23), (6, 23), (7, 23), (8, 23), (9, 23), (10,
23), (26, 23), (27, 23), (28, 23), (29, 23), (30, 23), (31, 23), (5, 24), (6, 24), (7,
24), (8, 24), (9, 24), (10, 24), (26, 24), (27, 24), (28, 24), (29, 24), (30, 24), (31,
24), (32, 24), (6, 25), (7, 25), (8, 25), (9, 25), (10, 25), (27, 25), (28, 25), (29,
25), (30, 25), (31, 25), (32, 25), (6, 26), (7, 26), (8, 26), (9, 26), (10, 26), (11,
26), (27, 26), (28, 26), (29, 26), (30, 26), (31, 26), (32, 26), (6, 27), (7, 27), (8,
27), (9, 27), (10, 27), (11, 27), (27, 27), (28, 27), (29, 27), (30, 27), (31, 27), (32,
27), (7, 28), (8, 28), (9, 28), (10, 28), (11, 28), (28, 28), (29, 28), (30, 28), (31,
28), (32, 28), (33, 28), (7, 29), (8, 29), (9, 29), (10, 29), (11, 29), (12, 29), (28,
29), (29, 29), (30, 29), (31, 29), (32, 29), (33, 29), (8, 30), (9, 30), (10, 30), (11,
30), (12, 30), (28, 30), (29, 30), (30, 30), (31, 30), (32, 30), (33, 30), (8, 31), (9,
31), (10, 31), (11, 31), (12, 31), (28, 31), (29, 31), (30, 31), (31, 31), (32, 31),
(33, 31), (9, 32), (10, 32), (11, 32), (12, 32), (13, 32), (29, 32), (30, 32), (31, 32),
(32, 32), (33, 32), (34, 32), (9, 33), (10, 33), (11, 33), (12, 33), (13, 33), (29, 33),
(30, 33), (31, 33), (32, 33), (33, 33), (34, 33), (10, 34), (11, 34), (12, 34), (13,
34), (14, 34), (29, 34), (30, 34), (31, 34), (32, 34), (33, 34), (34, 34), (11, 35),
(12, 35), (13, 35), (14, 35), (29, 35), (30, 35), (31, 35), (32, 35), (33, 35), (34,
35), (35, 35), (12, 36), (13, 36), (14, 36), (15, 36), (30, 36), (31, 36), (32, 36),
(33, 36), (34, 36), (35, 36), (13, 37), (14, 37), (15, 37), (16, 37), (17, 37), (27,
37), (28, 37), (29, 37), (30, 37), (31, 37), (32, 37), (33, 37), (34, 37), (35, 37),
(14, 38), (15, 38), (16, 38), (17, 38), (18, 38), (19, 38), (20, 38), (21, 38), (22,
38), (23, 38), (24, 38), (25, 38), (26, 38), (27, 38), (28, 38), (29, 38), (30, 38),
(31, 38), (32, 38), (33, 38), (34, 38), (35, 38), (16, 39), (17, 39), (18, 39), (19,
39), (20, 39), (21, 39), (22, 39), (23, 39), (24, 39), (25, 39), (26, 39), (27, 39),
(28, 39), (29, 39), (30, 39), (31, 39), (32, 39), (33, 39), (34, 39), (35, 39), (36,
39), (18, 40), (19, 40), (20, 40), (21, 40), (22, 40), (23, 40), (24, 40), (25, 40),
(26, 40), (27, 40), (28, 40), (29, 40), (30, 40), (31, 40), (32, 40), (33, 40), (34,
40), (35, 40), (36, 40), (20, 41), (21, 41), (22, 41), (23, 41), (24, 41), (25, 41),
(26, 41), (27, 41), (28, 41), (29, 41), (30, 41), (31, 41), (34, 41), (35, 41), (36,
41), (24, 42), (25, 42), (26, 42))

def is_edge_pixel( (x,y) ):
    return (x,y-1) not in book_a_pix or (x-1,y) not in book_a_pix or \
           (x+1,y) not in book_a_pix or (x,y+1) not in book_a_pix 

edge_pix = []
notedge_pix = []
for i in book_a_pix:
    if is_edge_pixel(i):
        edge_pix.append( i )
    else:
        notedge_pix.append( i )


class Outline:
    pass

def truetype_outline( data ):
    p = Path()
    curvelist = []
    allpoints = []
    allflags = []

    d = 1
    dl = len( data )

    nc = data[0]

    for contour in range(0,nc):
        pts = []
        flags = []
        size, d = data[d], d+1
        for i in range(0,size):
            pts.append( (data[d], data[d+1]) )
            flags.append( data[d+2] & 1 )
            d += 4
        allpoints += pts
        allflags += flags

        start = 0
        for i in range(0,size):
            j = (i+1) % size
            k = (i+2) % size

            f = (flags[i] << 2) | (flags[j] << 1) | flags[k]

            if f == 6 or f == 7:
                if not start:
                    p.moveto( pts[i] )
                    start = 1
                p.lineto( pts[j] )
                ij = (pts[i][0] + pts[j][0]) / 2.0, (pts[i][1] + pts[j][1]) / 2.0
                curvelist.append( pts[i] + ij + pts[j] )
                
            elif f == 5:
                if not start:
                    p.moveto( pts[i] )
                    start = 1
                p.qcurveto( pts[j], pts[k] )
                curvelist.append( pts[i] + pts[j] + pts[k] )
                
            elif f == 4:
                if not start:
                    p.moveto( pts[i] )
                    start = 1
                jk = (pts[j][0] + pts[k][0]) / 2.0, (pts[j][1] + pts[k][1]) / 2.0
                p.qcurveto( pts[j], jk )
                curvelist.append( pts[i] + pts[j] + jk )
                
            elif f == 1:
                ij = (pts[i][0] + pts[j][0]) / 2.0, (pts[i][1] + pts[j][1]) / 2.0
                if not start:
                    p.moveto( ij )
                    start = 1
                p.qcurveto( pts[j], pts[k] )
                curvelist.append( ij + pts[j] + pts[k] )
                
            elif f == 0:
                ij = (pts[i][0] + pts[j][0]) / 2.0, (pts[i][1] + pts[j][1]) / 2.0
                jk = (pts[j][0] + pts[k][0]) / 2.0, (pts[j][1] + pts[k][1]) / 2.0
                if not start:
                    p.moveto( ij )
                    start = 1
                p.qcurveto( pts[j], jk )
                curvelist.append( ij + pts[j] + jk )
                
        p.closepath()

    outline = Outline()
    outline.path = p
    outline.curvelist = curvelist
    outline.points = allpoints
    outline.flags = allflags

    return outline

def load_pixlist( fn ):
    f = open( fn )
    data = map( int, f.read().split() )
    f.close()

    out = []
    for i in range(0,data[0]):
        out.append( (data[i*2+1], data[i*2+2]) )

    return out

outline = truetype_outline( book_a )

def partial_bezier( (x0,y0,x1,y1,x2,y2), end ):
    dne = 1.0 - end
    return (x0, y0,
            dne*x0 + end*x1, dne*y0 + end*y1,
            dne*dne*x0 + 2*dne*end*x1 + end*end*x2,
            dne*dne*y0 + 2*dne*end*y1 + end*end*y2)
             

cameras = (Rect(52,-39,124,15),
           Rect(10,-48,401,334),
           Rect(10,-48,905,992),
           Rect(265,183,769,561),
           Rect(52,-39,124,15),
           )

def interp_cameralist( c, cameras ):
    if c <= 0.0:
        return cameras[0]
    elif c >= len(cameras)-1:
        return cameras[-1]

    i = int(c)
    f = c - i
    return cameras[i].interp( cameras[i+1], f )

swidth = 1.5

def chapter1( onecurve_u = (SCALAR,0,1),
              decasteljau = (SCALAR,0,1),
              allcurves_u = (SCALAR,0,1),
              show_controls = (SCALAR,0,1),
              interior = (SCALAR,0,1),
              outline_alpha = (SCALAR,0,1,1),
              big_grid = (SCALAR,0,1),
              big_pixels = (SCALAR,0,1),
              c = (SCALAR,0,3),
              separate_pixels = (SCALAR,0,1),
              show_edge = (SCALAR, 0, 1),
              ):
    
    set_camera( interp_cameralist( c, cameras ) )
    clear( linen )

    thickness( 0.5 )

    if interior > 0.0:
        color( 0.7, 0.5 * interior )
        fill( outline.path )

    curve = outline.curvelist[15]
    curves = outline.curvelist[:15] + outline.curvelist[16:]
    
    if allcurves_u > 0.0:
        color( 0, 0, 0, 0.25 * outline_alpha )
        if allcurves_u >= 1.0:
            widestroke( outline.path, swidth )
        else:
            for i in curves:
                j = partial_bezier( i, allcurves_u )
                widestroke( Path().moveto(*j[:2]).qcurveto(*j[2:]), swidth )

#      if big_grid > 0.0:
#          color( 0, big_grid * 0.2 )
#          thickness( 1 )
#          grid( 2048/90.0, 2048/90.0, -2, -2, 40, 44 )

    if big_pixels > 0.0:
        f = separate_pixels * 0.05
        push()
        scale( 2048/90.0, 2048/90.0 )
        color( 0 )
        i = int(len(book_a_pix) * big_pixels)
        if show_edge > 0.0:
            for x,y in notedge_pix:
                rectangle( x+f, y+f, x+1-f, y+1-f )
            color( black.interp(red,show_edge) )
            for x,y in edge_pix:
                rectangle( x+f, y+f, x+1-f, y+1-f )
        else:
            for x,y in book_a_pix[:i]:
                rectangle( x+f, y+f, x+1-f, y+1-f )
        pop()

    if decasteljau > 0.0:
        color( 0, 0, 0.7, decasteljau )
        line( *curve )
        m1x = curve[0] * (1-onecurve_u) + curve[2] * onecurve_u
        m1y = curve[1] * (1-onecurve_u) + curve[3] * onecurve_u
        m2x = curve[2] * (1-onecurve_u) + curve[4] * onecurve_u
        m2y = curve[3] * (1-onecurve_u) + curve[5] * onecurve_u
        line( m1x, m1y, m2x, m2y )
        
        m3x = m1x * (1-onecurve_u) + m2x * onecurve_u
        m3y = m1y * (1-onecurve_u) + m2y * onecurve_u
        dot( .75, m3x, m3y )

    if show_controls > 0.0:
        for p,f in zip(outline.points, outline.flags):
            if f:
                color( 0, show_controls )
            else:
                color( 0.7, show_controls )
            dot( 3, p[0], p[1] )

    if onecurve_u > 0.0 and allcurves_u < 1.0:
        color( 0, 0, 0, 0.25 )
        j = partial_bezier( curve, onecurve_u )
        widestroke( Path().moveto(*j[:2]).qcurveto(*j[2:]), swidth )
        
    push()
    translate( 1005.9, 431.11 )
    scale( 0.2, 0.2 )

        
    pop()


def character_animation():
    d = Drawable( get_camera(), chapter1 )
    start_animation( d )

    set( d.show_controls, 1.0 )
    smooth( 0.5, d.decasteljau, 1.0 )
    smooth( 3.0, d.onecurve_u, 1.0 )
    smooth( 0.5, d.decasteljau, 0.0 )
    pause()
    smooth( 3.0, d.c, 1.0 )
    smooth( 3.0, d.allcurves_u, 1.0 )
    set( d.onecurve_u, 0.0 )
    pause()
    
    parallel()
    
    smooth( 1.0, d.show_controls, 0.0 )
    
    sequence( 0.5 )
    smooth( 1.0, d.interior, 1.0 )
    end()

    sequence( 3.0 )
    smooth( 1.0, d.outline_alpha, 0.0 )
    end()
    
    sequence( 1.0 )
    smooth( 3.0, d.c, 2.0 )
    end()
    
    end()
    
    smooth( 5.0, d.big_pixels, 1.0 )
    pause()
    smooth( 2.0, d.c, 3.0 )
    linear( 0.25, d.separate_pixels, 1.0 )
    smooth( 1.0, d.show_edge, 1.0 )
    smooth( 0.5, d.interior, 0.0 )

    pause()

    set( d.allcurves_u, 0.0 )
    set( d.onecurve_u, 0.0 )
    set( d.outline_alpha, 1.0 )
    smooth( 1.0, d.c, 4.0 )
    set( d.c, 0.0 )
    parallel()
    smooth( 1.0, d.show_controls, 1.0 )
    serial( 0.3 )
    smooth( 1.0, d.decasteljau, 1.0 )
    end()
    serial( 0.6 )
    smooth( 1.0, d.interior, 1.0 )
    end()
    end()
    smooth( 1.0, d.onecurve_u, 1.0 )
    smooth( 1.0, d.c, 1.0 )
    smooth( 3.0, d.allcurves_u, 1.0 )
    set( d.onecurve_u, 0.0 )
    
    
    
    

    return end_animation()
character_animation = character_animation()
    
test_objects( character_animation, chapter1 )
