from slithy.library import *
from slithy.util import *
from rubbermap import split_sequence_rubber
import math
from fonts import fonts, images
import common
import unwrap
labelfont = fonts['bold']
labelcolor = Color( 0, 0, 0.6 )

trebuchet_a = (2,
               28,
               740, 123, 37, 0, 
               626, -20, 6, 1, 
               391, -20, 35, 2, 
               265, -20, 34, 3, 
               80, 163, 38, 4, 
               80, 299, 53, 5, 
               80, 462, 52, 6, 
               365, 687, 36, 7, 
               586, 687, 51, 8, 
               646, 687, 50, 9, 
               722, 661, 23, 10, 
               722, 921, 16, 11, 
               490, 921, 35, 12, 
               312, 921, 34, 13, 
               216, 825, 7, 14, 
               136, 984, 39, 15, 
               190, 1028, 62, 16, 
               381, 1091, 62, 17, 
               468, 1091, 51, 18, 
               701, 1091, 50, 19, 
               912, 879, 22, 20, 
               912, 648, 21, 21, 
               912, 264, 17, 22, 
               912, 123, 20, 23, 
               996, 76, 23, 24, 
               996, -19, 21, 25, 
               880, -19, 34, 26, 
               765, 47, 38, 27, 
               10,
               722, 526, 3, 28, 
               632, 546, 38, 29, 
               596, 546, 35, 30, 
               452, 546, 34, 31, 
               270, 398, 6, 32, 
               270, 297, 21, 33, 
               270, 130, 20, 34, 
               467, 130, 51, 35, 
               611, 130, 50, 36, 
               722, 267, 55, 37,
               1076, 80,
               )

frutiger_a = (2,
              31,
              985, 0, 33, 0, 
              805, 0, 35, 1, 
              805, 135, 53, 2, 
              801, 135, 35, 3, 
              687, -25, 6, 4, 
              477, -25, 35, 5, 
              300, -25, 34, 6, 
              201, 53, 39, 7, 
              94, 137, 38, 8, 
              94, 301, 53, 9, 
              94, 479, 52, 10, 
              262, 571, 55, 11, 
              396, 645, 54, 12, 
              580, 645, 51, 13, 
              709, 645, 50, 14, 
              784, 641, 23, 15, 
              784, 781, 52, 16, 
              728, 845, 39, 17, 
              667, 913, 38, 18, 
              526, 913, 35, 19, 
              350, 913, 34, 20, 
              223, 807, 7, 21, 
              213, 971, 39, 22, 
              378, 1069, 54, 23, 
              557, 1069, 51, 24, 
              777, 1069, 50, 25, 
              879, 960, 23, 26, 
              977, 855, 22, 27, 
              977, 637, 21, 28, 
              977, 205, 17, 29, 
              977, 61, 20, 30, 
              14,
              784, 406, 3, 31, 
              784, 498, 53, 32, 
              764, 498, 34, 33, 
              682, 502, 38, 34, 
              662, 502, 35, 35, 
              299, 502, 32, 36, 
              299, 301, 21, 37, 
              299, 224, 20, 38, 
              363, 175, 23, 39, 
              420, 131, 22, 40, 
              494, 131, 51, 41, 
              632, 131, 50, 42, 
              710, 210, 55, 43, 
              784, 284, 54, 44,
              1139, 94,
              )

source_hints = ( (4, 2, ),
                 (6, 2, 0),
                 (5, 0, 37),
                 (6, 2, 25),
                 (6, 25, 24),
                 (5, 2, 35),
                 (4, 18,),
                 (5, 18, 12),
                 (7, 35, 8),
                 (7, 8, 12),
                 (5, 8, 30),
                 (6, 8, 10),
                 (5, 10, 28),
                 (6, 18, 15),
                 (5, 15, 14),
                 (2, 38, 5),
                 (1, 5, 33),
                 (2, 5, 15),
                 (2, 15, 14),
                 (2, 39, 21),
                 (1, 21, 10),
                 (2, 21, 24),
                 (1, 21, 37),
                 (2, 37, 0),
                 )

target_hints = ( (4, 5,),
                 (6, 5, 2),
                 (5, 2, 43),
                 (6, 5, 0),
                 (6, 0, 0),
                 (5, 5, 41),
                 (4, 24,),
                 (5, 24, 19),
                 (7, 41, 13),
                 (7, 13, 19),
                 (5, 13, 35),
                 (6, 13, 15),
                 (5, 15, 32),
                 (6, 24, 22),
                 (5, 22, 21),
                 (2, 45, 9),
                 (1, 9, 37),
                 (2, 9, 22),
                 (2, 22, 21),
                 (2, 46, 28),
                 (1, 28, 15),
                 (2, 28, 0),
                 (1, 28, 31),
                 (2, 31, 2),
                 )

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


book_a_unhint = ((0, 0),(1, 0),(4, 0),(5, 0),(0, 1),(1, 1),(5, 1),(7,
1),(0, 2),(1, 2),(5, 2),(1, 3),(5, 3),(1, 4),(5, 4),(1, 5),(5, 5),(6,
5),(2, 6),(6, 6),(3, 7),(5, 7),(6, 7),)

book_a_dropout = ((0, 0),(1, 0),(4, 0),(5, 0),(6, 0),(0, 1),(1, 1),(2,
1),(5, 1),(7, 1),(0, 2),(1, 2),(3, 2),(4, 2),(5, 2),(1, 3),(5, 3),(1,
4),(5, 4),(1, 5),(5, 5),(6, 5),(2, 6),(6, 6),(3, 7),(4, 7),(5, 7),(6,
7),)

book_a_unhint_minus = ((0, 0),(4, 0),(0, 1),(0, 2),(5, 4),(1, 5),(5,
5),(5, 7),(6, 7),)

book_a_unhint_remain = ((1, 0),(5, 0),(1, 1),(5, 1),(7, 1),(1, 2),(5,
2),(1, 3),(5, 3),(1, 4),(6, 5),(2, 6),(6, 6),(3, 7),)

book_a_unhint_add = ((2, 0),(6, 0),(3, 1),(4, 2),(6, 4),(2, 5),(7,
7),(4, 8),(5, 8),(6, 8),(7, 8),)

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
    outline.pointsex = allpoints + [(0,0),(data[-2],0)]
    outline.oncurve = [i for (i,j) in zip(allpoints,allflags) if j]

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
treb = truetype_outline( trebuchet_a )
frut = truetype_outline( frutiger_a )

def partial_bezier( (x0,y0,x1,y1,x2,y2), end ):
    dne = 1.0 - end
    return (x0, y0,
            dne*x0 + end*x1, dne*y0 + end*y1,
            dne*dne*x0 + 2*dne*end*x1 + end*end*x2,
            dne*dne*y0 + 2*dne*end*y1 + end*end*y2)
             

cameras = (Rect(52,-39,124,15),
           Rect(10,-48,401,334),
           Rect(10,-48,905,992).outset( 0.1 ),
           Rect(10,-48,905,992).outset( 0.1 ).move_right( 0.3 ),
           Rect(947, 400, 1225, 753),
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
              small_grid = (SCALAR,0,1),
              big_pixels = (SCALAR,0,1),
              small_interior = (SCALAR,0,1),
              c = (SCALAR,0,4),
              big_pixel_alpha = (SCALAR,0,1,1),
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

    if big_grid > 0.0:
        color( 0, big_grid * 0.2 )
        grid( 2048/90.0, 2048/90.0, -2, -2, 40, 44 )

    if big_pixels > 0.0:
        f = 0
        push()
        scale( 2048/90.0, 2048/90.0 )
        color( 0, big_pixel_alpha )
        i = int(len(book_a_pix) * big_pixels)
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
        
    translate( 1000, 500 )
    scale( 0.2, 0.2 )

    if small_grid > 0.0:
        color( 0, small_grid * 0.2 )
        grid( 2048/18.0, 2048/18.0, -1, -1, 9, 10 )
    
    if small_interior > 0.0:
        push()
        color( 0.7, 0.5 * small_interior )
        fill( outline.path )
        pop()

cameras2 = ( Rect(947, 400, 1225, 753),
             Rect(947, 400, 1225, 753).move_right( 500, abs = 1 ),
             Rect(947, 400, 1225, 753).move_right( 1000, abs = 1 ),
             Rect(1250, 350, 2225, 1100),
             Rect(1250, 350, 2225, 1100).move_right( 1.0 ),
             Rect( 947, 350, 3200, 1100),
             )

def draw_pixlist( u, pix ):
    color( black )
    if u >= 1.0:
        for x,y in pix:
            rectangle( x, y, x+1, y+1 )
    elif u > 0.0:
        i = int(len(pix) * u)
        for x,y in pix[:i]:
            rectangle( x, y, x+1, y+1 )
        color( black, (len(pix) * u) - i )
        x, y = pix[i]
        rectangle( x, y, x+1, y+1 )
    
        
def chapter2( cam = (SCALAR, 0, 5),
              label_u = (SCALAR, 0, 1),
              pix_u = (SCALAR, 0, 1),
              fill_u = (SCALAR, 0, 1, 1),
              grid_u = (SCALAR, 0, 1, 1),
              label_d = (SCALAR, 0, 1),
              pix_d = (SCALAR, 0, 1),
              fill_d = (SCALAR, 0, 1, 1),
              grid_d = (SCALAR, 0, 1, 1),
              label_h = (SCALAR, 0, 1),
              pix_h1 = (SCALAR, 0, 1),
              pix_h2 = (SCALAR, 0, 1),
              fill_h = (SCALAR, 0, 1, 1),
              grid_h = (SCALAR, 0, 1, 1),
              squinch = (SCALAR, 0, 1.5),
              compare = (SCALAR, 0, 1),
              next_section = (SCALAR, 0, 1),
              ):
    set_camera( interp_cameralist( cam, cameras2 ) )
    clear( linen )

    translate( 1000, 500 )
    scale( 0.2, 0.2 )

    translate( 5000, 0 )

    if grid_h > 0.0:
        color( 0, 0.2 * grid_h )
        grid( 2048/18.0, 2048/18.0, -1, -1, 9, 10 )

    if fill_h > 0.0:
        color( 0.7, 0.5 * fill_h )
        fill( outline.path )

    push()
    scale( 2048 / 18.0 )
    draw_pixlist( 1.0, book_a_unhint_remain )
    draw_pixlist( 1.0 - pix_h1, book_a_unhint_minus )
    draw_pixlist( pix_h2, book_a_unhint_add )
    pop()
    
    if label_h > 0.0:
        color( labelcolor, label_h )
        text( 2048 / 18.0 * 4, -300, 'hinted', font = labelfont, anchor = 'c', size = 200 )
        
    translate( -2500 + 500 * squinch, 0 )

    if grid_d > 0.0:
        color( 0, 0.2 * grid_d )
        grid( 2048/18.0, 2048/18.0, -1, -1, 9, 10 )

    if fill_d > 0.0:
        color( 0.7, 0.5 * fill_d )
        fill( outline.path )

    push()
    scale( 2048 / 18.0 )
    draw_pixlist( pix_d, book_a_dropout )
    pop()
    

    if label_d > 0.0:
        color( labelcolor, label_d )
        text( 2048 / 18.0 * 4, -300, 'dropout control', font = labelfont, anchor = 'c', size = 200 )

    push()
    translate( 0, 1700 )
    if compare > 0.0:
        color( black, compare )
        fill( outline.path )
        color( red, compare )
        text( 2048 / 18.0 * 4, -300, 'ideal', font = labelfont, anchor = 'c', size = 200 )
    pop()
        
    translate( -2500 + 500 * squinch, 0 )
        
    if grid_u > 0.0:
        color( 0, 0.2 * grid_u )
        grid( 2048/18.0, 2048/18.0, -1, -1, 9, 10 )

    if fill_u > 0.0:
        color( 0.7, 0.5 * fill_u )
        fill( outline.path )

    push()
    scale( 2048 / 18.0 )
    draw_pixlist( pix_u, book_a_unhint )
    pop()

    if label_u > 0.0:
        color( labelcolor, label_u )
        text( 2048 / 18.0 * 4, -300, 'unhinted', font = labelfont, anchor = 'c', size = 200 )

    if next_section > 0.0:
        #color( labelcolor, next_section )
        #text( 8600 - 1000*squinch, 1200, 'Next\nsection', font = fonts['bold'], size = 500, anchor = 'c', justify = 0.5 )

        color( red )
        r = Rect(8550 - 1000*squinch, 1100, width = 4500, height = 4500*3.0/4)
        embed_object( r, unwrap.chapter4, { 'fade' : 0.0, 'tf' : 0.0, 'ts' : 0.0,
                                            'ff' : 0.0, 'fs' : 0.0, 'fmatch' : 0,
                                            'show_match' : 0.0, 'match_alpha' : 0.0,
                                            'show_score' : 0.0, 'outline_alpha' : 0.0,
                                            'background' : 0 }, _alpha = next_section )
        


def expand_hints( out, hints ):
    return tuple([ i[:1] + tuple([ out.pointsex[j] for j in i[1:] ]) for i in hints])

source_hints = expand_hints( treb, source_hints )
target_hints = expand_hints( frut, target_hints )

hcolors = (black, green, blue, black, black, purple, orange, Color( 0, 0.8, 0.5 ) )
def draw_hintlist( hints ):
    thickness( 20 )
    for i in hints:
        if i[0] == 4:
            x, y = i[1]
            color( red )
            dot( 45, x, y )
            rectangle( x-90, y-10, x+90, y+10 )
        else:
            x1, y1 = i[1]
            x2, y2 = i[2]
            color( hcolors[i[0]] )
            line( x1, y1, x2, y2 )
            

def interp_hintlist( s, t, offset, u, rubber ):
    if rubber:
        off = split_sequence_rubber( len(s), u, 0.8 )
    else:
        off = split_sequence_smooth( len(s), u, 0.8 )
    return tuple([ i[:1] + tuple([ (x1*(1.0-o)+(x2+offset)*o,y1*(1.0-o)+y2*o-400*math.sin(o*math.pi)) for (x1,y1),(x2,y2) in zip(i[1:],j[1:]) ]) for i,j,o in zip(s,t,off) if 1-o])
    

def chapter3( slide = (SCALAR,0,1),
              rubber = (BOOLEAN),
              ):
    set_camera( Rect( -200, -200, 2800, 1069+175 ) )
    clear( linen )

    color( black, 0.2 )
    fill( treb.path )

    color( black, 0.5 )
    widestroke( treb.path, 10 )
    draw_hintlist( source_hints )
    color( black )
    for p in treb.oncurve:
        dot( 25, p[0], p[1] )

    translate( 1500, 0 )

    color( black, 0.2 )
    fill( frut.path )
    
    color( black, 0.5 )
    widestroke( frut.path, 10 )
    if slide >= 1.0:
        draw_hintlist( target_hints )
    elif slide > 0.0:
        draw_hintlist( interp_hintlist( target_hints, source_hints, -1500, 1.0-slide, rubber ) )
    color( black )
    for p in frut.oncurve:
        dot( 25, p[0], p[1] )

def blank():
    clear( linen )
    

def expand_and_compress_good():
    d = Drawable( get_camera(), chapter1 )
    start_animation( d )
    
    set( d.show_controls, 1.0 )
    smooth( 0.5, d.decasteljau, 1.0 )
    smooth( 3.0, d.onecurve_u, 1.0 )
    smooth( 0.5, d.decasteljau, 0.0 )

    smooth( 3.0, d.c, 1.0 )
    smooth( 3.0, d.allcurves_u, 1.0 )
    set( d.onecurve_u, 0.0 )
    
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
    
    smooth( 1.0, d.big_grid, 1.0 )
    wait( 0.5 )
    smooth( 3.0, d.big_pixels, 1.0 )

    a = end_animation()
    return [scale_length( a[0], 10.0)]
expand_and_compress_good = expand_and_compress_good()

def expand_and_compress_bad():
    d = Drawable( get_camera(), chapter1 )
    start_animation( d )
    
    set( d.c, 1.0 )
    set( d.show_controls, 1.0 )
    smooth( 0.5, d.decasteljau, 1.0 )
    smooth( 3.0, d.onecurve_u, 1.0 )
    smooth( 0.5, d.decasteljau, 0.0 )

    #set( d.c, 1.0 )
    smooth( 3.0, d.allcurves_u, 1.0 )
    set( d.onecurve_u, 0.0 )
    
    parallel()
    
    smooth( 1.0, d.show_controls, 0.0 )
    
    sequence( 0.5 )
    smooth( 1.0, d.interior, 1.0 )
    smooth( 1.0, d.outline_alpha, 0.0 )
    end()

    end()
    
    #set( d.c, 2.0 )
    smooth( 1.0, d.big_grid, 1.0 )
    wait( 0.5 )
    smooth( 3.0, d.big_pixels, 1.0 )

    a = end_animation()
    return [scale_length( a[0], 10.0)]
expand_and_compress_bad = expand_and_compress_bad()

def overlays_good():
    d = Drawable( get_camera(), chapter1 )
    start_animation( d )

    set( d.show_controls, 1.0 )
    smooth( 0.5, d.decasteljau, 1.0 )
    smooth( 3.0, d.onecurve_u, 1.0 )
    smooth( 0.5, d.decasteljau, 0.0 )

    smooth( 3.0, d.c, 1.0 )
    smooth( 3.0, d.allcurves_u, 1.0 )
    set( d.onecurve_u, 0.0 )
    
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
    
    smooth( 1.0, d.big_grid, 1.0 )
    wait( 0.5 )
    smooth( 5.0, d.big_pixels, 1.0 )
    parallel()
    smooth( 1.0, d.interior, 0.0 )
    end()
    

    parallel()
    serial()
    smooth( 1.0, d.small_interior, 1.0 )
    smooth( 1.0, d.small_grid, 1.0 )
    end()
    smooth( 2.0, d.c, 3 )
    end()
    
    wait( 0.5 )
    parallel()
    smooth( 1.0, d.big_grid, 0.0 )
    smooth( 1.0, d.interior, 0.0 )
    smooth( 1.0, d.c, 4 )
    end()

    a = end_animation()
    return [scale_length( a[0], 10.0)]
overlays_good = overlays_good()    

def overlays_bad():
    d = Drawable( get_camera(), chapter1, big_pixel_alpha = 0.5 )
    start_animation( d )

    set( d.show_controls, 1.0 )
    set( d.decasteljau, 1.0 )
    set( d.interior, 1.0 )
    set( d.big_grid, 1.0 )
    set( d.big_pixels, 1.0 )
    set( d.small_grid, 1.0 )
    set( d.small_interior, 1.0 )
    
    smooth( 3.0, d.onecurve_u, 1.0 )
    #smooth( 0.5, d.decasteljau, 0.0 )

    smooth( 3.0, d.c, 1.0 )
    smooth( 3.0, d.allcurves_u, 1.0 )
    set( d.onecurve_u, 0.0 )
    
    parallel()
    
    #smooth( 1.0, d.show_controls, 0.0 )
    
    #sequence( 0.5 )
    #smooth( 1.0, d.interior, 1.0 )
    #end()

    #sequence( 3.0 )
    #smooth( 1.0, d.outline_alpha, 0.0 )
    #end()
    
    #sequence( 1.0 )
    smooth( 3.0, d.c, 2.0 )
    #end()
    
    end()
    
    #smooth( 1.0, d.big_grid, 1.0 )
    #wait( 0.5 )

    #smooth( 5.0, d.big_pixels, 1.0 )
    wait( 2.0 )
    
    parallel()
    serial()
    #smooth( 1.0, d.small_interior, 1.0 )
    #smooth( 1.0, d.small_grid, 1.0 )
    end()
    #smooth( 2.0, d.c, 3 )
    end()
    
    wait( 0.5 )
    parallel()
    #smooth( 1.0, d.big_grid, 0.0 )
    #smooth( 1.0, d.interior, 0.0 )
    smooth( 3.0, d.c, 4 )
    end()

    a = end_animation()
    return [scale_length( a[0], 10.0)]
overlays_bad = overlays_bad()    

def one_thing_at_a_time_bad():
    d = Drawable( get_camera(), chapter1 )
    start_animation( d )
    
    set( d.show_controls, 1.0 )
    smooth( 0.5, d.decasteljau, 1.0 )
    smooth( 3.0, d.onecurve_u, 1.0 )
    wait( -2.5 )
    smooth( 0.5, d.decasteljau, 0.0 )
    wait( -0.5 )

    parallel()
    smooth( 7.0, d.c, 2.0 )
    
    serial()
    #wait( -1.5 )
    smooth( 3.0, d.allcurves_u, 1.0 )
    set( d.onecurve_u, 0.0 )
    
    #wait( -1.0 )
    parallel()
    smooth( 1.0, d.show_controls, 0.0 )
    smooth( 1.0, d.interior, 1.0 )
    smooth( 1.0, d.outline_alpha, 0.0 )
    end()
    
    end()
    end()
    
    wait( -2.5 )
    parallel()
    smooth( 1.0, d.big_grid, 1.0 )
    smooth( 2.0, d.big_pixels, 1.0 )
    end()

    a = end_animation()
    return a
    #return [scale_length( a[0], 10.0)]
one_thing_at_a_time_bad = one_thing_at_a_time_bad()

def one_thing_at_a_time_good():
    d = Drawable( get_camera(), chapter1 )
    start_animation( d )
    
    set( d.show_controls, 1.0 )
    smooth( 0.5, d.decasteljau, 1.0 )
    wait( 0.5 )
    smooth( 3.0, d.onecurve_u, 1.0 )
    wait( 0.5 )
    smooth( 0.5, d.decasteljau, 0.0 )
    wait( 0.5 )

    smooth( 3.0, d.c, 1.0 )
    wait( 0.5 )
    smooth( 3.0, d.allcurves_u, 1.0 )
    set( d.onecurve_u, 0.0 )
    
    wait( 0.5 )
    parallel()
    
    smooth( 1.0, d.show_controls, 0.0 )
    
    sequence( 0.8 )
    smooth( 1.0, d.interior, 1.0 )
    end()

    sequence( 3.0 )
    smooth( 1.0, d.outline_alpha, 0.0 )
    end()
    
    sequence( 1.0 )
    smooth( 3.0, d.c, 2.0 )
    end()
    
    end()
    
    wait( 1.0 )
    smooth( 1.0, d.big_grid, 1.0 )
    wait( 1.0 )
    smooth( 3.0, d.big_pixels, 1.0 )

    a = end_animation()
    return [scale_length( a[0], 10.0)]
one_thing_at_a_time_good = one_thing_at_a_time_good()


def virtual_canvas_good():
    #d = Drawable( get_camera(), chapter1 )
    d2 = Drawable( get_camera(), chapter2 )
    start_animation( d2 )

    smooth( 1.0, d2.pix_u, 1.0 )
    smooth( 0.5, d2.label_u, 1.0 )
    parallel()
    smooth( 1.0, d2.fill_u, 0.0 )
    serial( 0.5 )
    smooth( 1.0, d2.grid_u, 0.0 )
    end()
    end()

    smooth( 1.0, d2.cam, 1 )
    wait( 0.5 )

    smooth( 1.0, d2.pix_d, 1.0 )
    smooth( 0.5, d2.label_d, 1.0 )
    parallel()
    smooth( 1.0, d2.fill_d, 0.0 )
    serial( 0.5 )
    smooth( 1.0, d2.grid_d, 0.0 )
    end()
    end()

    smooth( 1.0, d2.cam, 2 )
    wait( 0.5 )

    smooth( 1.0, d2.pix_h2, 1.0 )
    smooth( 1.0, d2.pix_h1, 1.0 )
    smooth( 0.5, d2.label_h, 1.0 )
    parallel()
    smooth( 1.0, d2.fill_h, 0.0 )
    serial( 0.5 )
    smooth( 1.0, d2.grid_h, 0.0 )
    end()
    end()

    parallel()
    smooth( 1.0, d2.squinch, 1.5 )
    smooth( 1.0, d2.cam, 3 )
    smooth( 1.0, d2.compare, 1.0 )
    end()
    

    a = end_animation()
    return [scale_length( a[0], 10.0)]
virtual_canvas_good = virtual_canvas_good()

def virtual_canvas_bad():
    #d = Drawable( get_camera(), chapter1 )
    bg = Fill( color = linen )
    d2 = Drawable( get_camera(), chapter2 )
    start_animation( bg, d2 )

    smooth( 1.0, d2.pix_u, 1.0 )
    smooth( 0.5, d2.label_u, 1.0 )
    parallel()
    smooth( 1.0, d2.fill_u, 0.0 )
    serial( 0.5 )
    smooth( 1.0, d2.grid_u, 0.0 )
    end()
    end()

    fade_out( 0.5, d2 )
    set( d2.cam, 1 )
    fade_in( 0.5, d2 )
    wait( 0.5 )

    smooth( 1.0, d2.pix_d, 1.0 )
    smooth( 0.5, d2.label_d, 1.0 )
    parallel()
    smooth( 1.0, d2.fill_d, 0.0 )
    serial( 0.5 )
    smooth( 1.0, d2.grid_d, 0.0 )
    end()
    end()

    fade_out( 0.5, d2 )
    set( d2.cam, 2 )
    fade_in( 0.5, d2 )
    wait( 0.5 )

    smooth( 1.0, d2.pix_h2, 1.0 )
    smooth( 1.0, d2.pix_h1, 1.0 )
    smooth( 0.5, d2.label_h, 1.0 )
    parallel()
    smooth( 1.0, d2.fill_h, 0.0 )
    serial( 0.5 )
    smooth( 1.0, d2.grid_h, 0.0 )
    end()
    end()

    fade_out( 0.5, d2 )
    set( d2.squinch, 1.5 )
    set( d2.cam, 3 )
    set( d2.compare, 1.0 )
    fade_in( 0.5, d2 )
    

    a = end_animation()
    return [scale_length( a[0], 10.0)]
virtual_canvas_bad = virtual_canvas_bad()

def transition_hierarchy_good():
    #d = Drawable( get_camera(), chapter1 )
    bg = Fill( color = linen )
    d2 = Drawable( get_camera(), chapter2 )
    start_animation( bg, d2 )

    smooth( 1.0, d2.pix_u, 1.0 )
    smooth( 0.5, d2.label_u, 1.0 )
    parallel()
    smooth( 1.0, d2.fill_u, 0.0 )
    serial( 0.5 )
    smooth( 1.0, d2.grid_u, 0.0 )
    end()
    end()

    smooth( 1.0, d2.cam, 1 )
    wait( 0.5 )

    smooth( 1.0, d2.pix_d, 1.0 )
    smooth( 0.5, d2.label_d, 1.0 )
    parallel()
    smooth( 1.0, d2.fill_d, 0.0 )
    serial( 0.5 )
    smooth( 1.0, d2.grid_d, 0.0 )
    end()
    end()

    smooth( 1.0, d2.cam, 2 )
    wait( 0.5 )

    smooth( 1.0, d2.pix_h2, 1.0 )
    smooth( 1.0, d2.pix_h1, 1.0 )
    smooth( 0.5, d2.label_h, 1.0 )
    parallel()
    smooth( 1.0, d2.fill_h, 0.0 )
    serial( 0.5 )
    smooth( 1.0, d2.grid_h, 0.0 )
    end()
    end()

    parallel()
    smooth( 1.0, d2.squinch, 1.5 )
    smooth( 1.0, d2.cam, 3 )
    smooth( 1.0, d2.compare, 1.0 )
    end()

    wait( 1.0 )
    fade_out( 0.5, d2 )
    set( d2.cam, 4 )
    set( d2.next_section, 1.0 )
    fade_in( 0.5, d2 )

    a = end_animation()
    return [scale_length( a[0], 10.0)]
transition_hierarchy_good = transition_hierarchy_good()

def transition_hierarchy_bad():
    #d = Drawable( get_camera(), chapter1 )
    d2 = Drawable( get_camera(), chapter2 )
    start_animation( d2 )

    smooth( 1.0, d2.pix_u, 1.0 )
    smooth( 0.5, d2.label_u, 1.0 )
    parallel()
    smooth( 1.0, d2.fill_u, 0.0 )
    serial( 0.5 )
    smooth( 1.0, d2.grid_u, 0.0 )
    end()
    end()

    smooth( 1.0, d2.cam, 1 )
    wait( 0.5 )

    smooth( 1.0, d2.pix_d, 1.0 )
    smooth( 0.5, d2.label_d, 1.0 )
    parallel()
    smooth( 1.0, d2.fill_d, 0.0 )
    serial( 0.5 )
    smooth( 1.0, d2.grid_d, 0.0 )
    end()
    end()

    smooth( 1.0, d2.cam, 2 )
    wait( 0.5 )

    smooth( 1.0, d2.pix_h2, 1.0 )
    smooth( 1.0, d2.pix_h1, 1.0 )
    smooth( 0.5, d2.label_h, 1.0 )
    parallel()
    smooth( 1.0, d2.fill_h, 0.0 )
    serial( 0.5 )
    smooth( 1.0, d2.grid_h, 0.0 )
    end()
    end()

    parallel()
    smooth( 1.0, d2.squinch, 1.5 )
    smooth( 1.0, d2.cam, 3 )
    smooth( 1.0, d2.compare, 1.0 )
    end()

    wait( 1.0 )
    set( d2.next_section, 1.0 )
    smooth( 1.0, d2.cam, 4 )
    pause()
    smooth( 1.0, d2.cam, 5 )
    
    

    a = end_animation()
    return [scale_length( a[0], 10.0), a[1]]
transition_hierarchy_bad = transition_hierarchy_bad()

def no_instantaneous_good():
    d = Drawable( get_camera(), chapter3 )
    start_animation( d )

    wait( 1.0 )
    linear( 8.0, d.slide, 1.0 )

    a = end_animation()
    return a
    #return [scale_length( a[0], 10.0)]
no_instantaneous_good = no_instantaneous_good()

def no_instantaneous_bad():
    d = Drawable( get_camera(), chapter3 )
    start_animation( d )

    pause()
    set( d.slide, 1.0 )

    a = end_animation()
    return a
    #return [scale_length( a[0], 10.0)]
no_instantaneous_bad = no_instantaneous_bad()
    
def extraneous_motion_bad():
    d = Drawable( get_camera(), chapter3, rubber = 1 )
    start_animation( d )

    wait( 1.0 )
    linear( 8.0, d.slide, 1.0 )

    a = end_animation()
    return a
    #return [scale_length( a[0], 10.0)]
extraneous_motion_bad = extraneous_motion_bad()
    


def character_animation( *times ):
    d = Drawable( get_camera(), chapter1, _alpha = 0.0 )
    d2 = Drawable( get_camera(), chapter2 )
    d3 = Drawable( get_camera(), chapter3, _alpha = 0.0 )
    d4 = Drawable( get_camera(), unwrap.chapter4, _alpha = 0.0 )
    start_animation( common.bg, d )

    set( d.show_controls, 1.0 )

    fade_in( 0.5, d )
    exit( common.bg )
    
    smooth( 0.5, d.decasteljau, 1.0 )
    smooth( 3.0, d.onecurve_u, 1.0 )
    smooth( 0.5, d.decasteljau, 0.0 )
    wait( 1.0 )
    smooth( 3.0, d.c, 1.0 )
    smooth( 3.0, d.allcurves_u, 1.0 )
    set( d.onecurve_u, 0.0 )
    wait( 1.0 )
    
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
    
    smooth( 1.0, d.big_grid, 1.0 )
    wait( 0.5 )
    smooth( 5.0, d.big_pixels, 1.0 )
    
    pause()

    parallel()
    serial()
    smooth( 1.0, d.small_interior, 1.0 )
    smooth( 1.0, d.small_grid, 1.0 )
    end()
    smooth( 2.0, d.c, 3 )
    end()
    
    wait( 0.5 )
    parallel()
    smooth( 1.0, d.big_grid, 0.0 )
    smooth( 1.0, d.interior, 0.0 )
    smooth( 1.0, d.c, 4 )
    end()

    exit( d )
    enter( d2 )

    smooth( 1.0, d2.pix_u, 1.0 )
    smooth( 0.5, d2.label_u, 1.0 )
    parallel()
    smooth( 1.0, d2.fill_u, 0.0 )
    serial( 0.5 )
    smooth( 1.0, d2.grid_u, 0.0 )
    end()
    end()

    wait( 1.0 )
    smooth( 1.0, d2.cam, 1 )
    wait( 0.5 )

    smooth( 1.0, d2.pix_d, 1.0 )
    smooth( 0.5, d2.label_d, 1.0 )
    parallel()
    smooth( 1.0, d2.fill_d, 0.0 )
    serial( 0.5 )
    smooth( 1.0, d2.grid_d, 0.0 )
    end()
    end()

    wait( 1.0 )
    smooth( 1.0, d2.cam, 2 )
    wait( 0.5 )

    smooth( 1.0, d2.pix_h2, 1.0 )
    smooth( 1.0, d2.pix_h1, 1.0 )
    smooth( 0.5, d2.label_h, 1.0 )
    parallel()
    smooth( 1.0, d2.fill_h, 0.0 )
    serial( 0.5 )
    smooth( 1.0, d2.grid_h, 0.0 )
    end()
    end()

    wait( 1.0 )
    parallel()
    smooth( 1.0, d2.squinch, 1.5 )
    smooth( 1.0, d2.cam, 3 )
    smooth( 1.0, d2.compare, 1.0 )
    end()

    pause()

    if 1:
        enter( d3 )
        fade_in( 0.5, d3 )
        exit( d2 )
    else:
        enter( d4 )
        fade_in( 0.5, d4 )
        exit( d2 )

    #     ##
    #     ## third match
    #     ##

    #     parallel()
    #     smooth( 0.5, d4.show_score, 0.0 )
    #     smooth( 0.5, d4.match_alpha, 0.0 )
    #     smooth( 0.5, d4.outline_alpha, 0.0 )
    #     end()
    #     set( d4.show_match, 0.0 )

        set( d4.fmatch, 2 )

        set( d4.tf, 0.001 )
        set( d4.ff, 0.001 )
        smooth( 0.5, d4.outline_alpha, 1.0 )
        parallel()
        smooth( 4.0, d4.tf, 1.0 )
        smooth( 4.0, d4.ff, 1.0 )
        end()
        wait( 0.5 )
        parallel()
        smooth( 2.0, d4.fade, 1.0 )
        smooth( 2.0, d4.ts, 1.0 )
        smooth( 2.0, d4.fs, 1.0 )
        end()
        set( d4.match_alpha, 1.0 )
        smooth( 2.0, d4.show_match, 1.0 )
        parallel()
        smooth( 2.0, d4.ts, 0.0 )
        smooth( 2.0, d4.fs, 0.0 )
        smooth( 2.0, d4.fade, 0.0 )
        end()
        wait( 0.5 )
        smooth( 0.5, d4.show_score, 1.0 )

        pause()

        enter( d3 )
        fade_in( 0.5, d3 )
        exit( d4 )

    wait( 1.0 )

    linear( 8.0, d3.slide, 1.0 )

    pause()
    
    enter( common.bg )
    lower( common.bg )
    fade_out( 0.5, d3 )

    a = end_animation()
    newa = []
    for t, anim in zip( times, a ):
        if t:
            newa.append( scale_length( anim, t ) )
        else:
            newa.append( anim )
    return newa

#character_animation = character_animation( None, None, None, None, None )
character_animation = character_animation( None, None, None, None )
hinting_one = character_animation[0].anim


oncolor = yellow
offcolor = Color( 0.6 )
    
def show_one( a, cap, text, good, bad ):
    set( cap.text, text )
    set( cap.color, oncolor )
    parallel()
    fade_in( 0.5, cap )
    a.fade_in_start( good, 0.5 )
    end()
    a.play( good )
    
    pause()
    
    parallel()
    smooth( 1.0, cap.color, offcolor )
    serial()
    a.fade_out_end( good, 0.5 )
    a.fade_in_start( bad, 0.5 )
    end()
    end()
    a.play( bad )

    pause()
    
    parallel()
    a.fade_out_end( bad, 0.5 )
    fade_out( 0.5, cap )
    end()

def demo_principles():
    a = Anim( get_camera().top(0.85).inset(0.05).restrict_aspect(4./3.).move_down(0.05) )
    cap = Text( get_camera().bottom(0.175).inset(0.04).move_down(0.15), font = fonts['altbold'], size = 24, _alpha = 0.0,
                justify = 0.5 )

    start_animation( common.bg, a, cap )

    show_one( a, cap, 'smoothly expand and compress detail', expand_and_compress_good, expand_and_compress_bad ) 
    show_one( a, cap, 'manage complexity with overlays', overlays_good, overlays_bad ) 
    show_one( a, cap, 'do one thing at a time', one_thing_at_a_time_good, one_thing_at_a_time_bad ) 
    show_one( a, cap, 'use a large virtual canvas', virtual_canvas_good, virtual_canvas_bad ) 
    show_one( a, cap, 'reflect structure with transitions', transition_hierarchy_good, transition_hierarchy_bad ) 
    show_one( a, cap, 'avoid instantaneous changes', no_instantaneous_good, no_instantaneous_bad ) 
    show_one( a, cap, 'avoid extraneous motion', no_instantaneous_good, extraneous_motion_bad ) 

    return end_animation()
demo_principles = demo_principles()

### -----------------------------------------------------------------------------------

def demo1():
    dloc = get_camera().top(0.85).inset(0.05).restrict_aspect(4./3.).move_down(0.05)
    d = Drawable( dloc, chapter1, _alpha = 0 )
    cap = Text( get_camera().bottom(0.175).inset(0.04).move_down(0.15),
                font = fonts['altbold'], size = 23, _alpha = 0.0, justify = 0.5 )
    yn = Image( dloc.left( 0.2 ).top( 0.2 ).move_left( 0.3 ).move_up( 0.3 ) )

    start_animation( common.bg, d, cap, yn )

    set( yn.image, images['yes'] )
    set( yn._alpha, 0.0 )
    
    set( d.show_controls, 1.0 )

    fade_in( 0.5, d )
    smooth( 0.5, d.decasteljau, 1.0 )
    smooth( 1.0, d.onecurve_u, 1.0 )
    smooth( 0.5, d.decasteljau, 0.0 )

    set( cap.text, 'smoothly expand and compress detail' )
    set( cap.color, yellow )
    parallel()
    fade_in( 0.5, cap, yn )
    smooth( 2.0, d.c, 1.0 )
    end()
    smooth( 1.0, d.allcurves_u, 1.0 )
    set( d.onecurve_u, 0.0 )
    
    parallel()
    
    smooth( 0.5, d.show_controls, 0.0 )
    smooth( 1.0, d.interior, 1.0 )
    smooth( 1.0, d.outline_alpha, 0.0 )
    
    sequence( 1.0 )
    smooth( 2.0, d.c, 2.0 )
    end()
    
    end()
    
    smooth( 0.5, d.big_grid, 1.0 )
    smooth( 1.0, d.big_pixels, 1.0 )

    pause()
    fade_out( 0.5, d, yn )
    exit( d )
    d = Drawable( dloc, chapter1, _alpha = 0 )
    set( yn.image, images['no'] )

    ###
    ###  single scale animation
    ### 
    
    enter( d )
    lift( yn )
    set( d.show_controls, 1.0 )
    set( d.c, 1.0 )
    fade_in( 0.5, d, yn )

    smooth( 0.5, d.decasteljau, 1.0 )
    smooth( 1.0, d.onecurve_u, 1.0 )
    smooth( 0.5, d.decasteljau, 0.0 )

    parallel()
    fade_in( 0.5, cap )
    end()
    smooth( 1.0, d.allcurves_u, 1.0 )
    set( d.onecurve_u, 0.0 )
    
    parallel()
    
    smooth( 0.5, d.show_controls, 0.0 )
    smooth( 1.0, d.interior, 1.0 )
    smooth( 1.0, d.outline_alpha, 0.0 )
    
    end()
    pause()
    set( d.c, 2 )
    
    smooth( 0.5, d.big_grid, 1.0 )
    smooth( 1.0, d.big_pixels, 1.0 )

    pause()
    
    fade_out( 0.5, d, cap, yn )

    return end_animation()
demo1 = demo1()

def demo2():
    dloc = get_camera().top(0.85).inset(0.05).restrict_aspect(4./3.).move_down(0.05)
    d = Drawable( dloc, chapter1, _alpha = 0 )
    cap = Text( get_camera().bottom(0.175).inset(0.04).move_down(0.15),
                font = fonts['altbold'], size = 23, _alpha = 0.0, justify = 0.5 )
    yn = Image( dloc.left( 0.2 ).top( 0.2 ).move_left( 0.3 ).move_up( 0.3 ),
                _alpha = 0 )

    start_animation( common.bg, d, cap, yn )

    set( d.show_controls, 1.0 )

    set( yn.image, images['no'] )
    set( cap.text, 'manage complexity with overlays' )
    set( cap.color, yellow )
    fade_in( 0.5, cap )
    fade_in( 0.5, d )
    smooth( 0.5, d.decasteljau, 1.0 )

    pause()
    set( d.big_pixel_alpha, 0.0 )
    set( d.big_pixels, 1.0 )
    fade_in( 0.5, yn )
    smooth( 0.5, d.interior, 1.0 )
    smooth( 0.5, d.big_grid, 1.0 )
    smooth( 0.5, d.big_pixel_alpha, 0.5 )
    pause()
    
    smooth( 1.0, d.onecurve_u, 1.0 )
    smooth( 0.5, d.decasteljau, 0.0 )

    parallel()
    smooth( 2.0, d.c, 1.0 )
    end()
    smooth( 1.0, d.allcurves_u, 1.0 )
    set( d.onecurve_u, 0.0 )

    pause()
    fade_out( 0.5, d, cap, yn )

    return end_animation()
demo2 = demo2()

def demo3():
    dloc = get_camera().top(0.85).inset(0.05).restrict_aspect(4./3.).move_down(0.05)
    d = Drawable( dloc, chapter1, _alpha = 0 )
    cap = Text( get_camera().bottom(0.175).inset(0.04).move_down(0.15),
                font = fonts['altbold'], size = 23, _alpha = 0.0, justify = 0.5 )
    yn = Image( dloc.left( 0.2 ).top( 0.2 ).move_left( 0.3 ).move_up( 0.3 ) )

    start_animation( common.bg, d, cap, yn )

    set( yn.image, images['no'] )
    set( cap.text, 'do one thing at a time' )
    set( cap.color, yellow )

    fade_in( 0.5, cap )
    fade_in( 0.5, d, yn )
    
    set( d.show_controls, 1.0 )
    smooth( 0.5, d.decasteljau, 1.0 )
    smooth( 3.0, d.onecurve_u, 1.0 )
    wait( -2.5 )
    smooth( 0.5, d.decasteljau, 0.0 )
    wait( -0.5 )

    parallel()
    smooth( 7.0, d.c, 2.0 )
    
    serial()
    #wait( -1.5 )
    smooth( 3.0, d.allcurves_u, 1.0 )
    set( d.onecurve_u, 0.0 )
    
    #wait( -1.0 )
    parallel()
    smooth( 1.0, d.show_controls, 0.0 )
    smooth( 1.0, d.interior, 1.0 )
    smooth( 1.0, d.outline_alpha, 0.0 )
    end()
    
    end()
    end()
    
    wait( -2.5 )
    parallel()
    smooth( 1.0, d.big_grid, 1.0 )
    smooth( 2.0, d.big_pixels, 1.0 )
    end()
    
    pause()

    fade_out( 0.5, d, yn )
    exit( d )
    d = Drawable( dloc, chapter1, _alpha = 0 )
    set( yn.image, images['yes'] )

    ###
    ###  good animation
    ### 
    
    enter( d )
    lift( yn )
    set( d.show_controls, 1.0 )
    fade_in( 0.5, d, yn )

    set( d.show_controls, 1.0 )

    fade_in( 0.5, d )
    smooth( 0.5, d.decasteljau, 1.0 )
    smooth( 1.0, d.onecurve_u, 1.0 )
    smooth( 0.5, d.decasteljau, 0.0 )

    parallel()
    smooth( 2.0, d.c, 1.0 )
    end()
    smooth( 1.0, d.allcurves_u, 1.0 )
    set( d.onecurve_u, 0.0 )
    
    parallel()
    
    smooth( 0.5, d.show_controls, 0.0 )
    smooth( 1.0, d.interior, 1.0 )
    smooth( 1.0, d.outline_alpha, 0.0 )
    
    sequence( 1.0 )
    smooth( 2.0, d.c, 2.0 )
    end()
    
    end()
    
    smooth( 0.5, d.big_grid, 1.0 )
    smooth( 1.0, d.big_pixels, 1.0 )

    pause()
    fade_out( 0.5, d, yn, cap )


    return end_animation()
demo3 = demo3()


def demo4():
    dloc = get_camera().top(0.85).inset(0.05).restrict_aspect(4./3.).move_down(0.05)
    d = Drawable( dloc, chapter2, _alpha = 0 )
    cap = Text( get_camera().bottom(0.175).inset(0.04).move_down(0.15),
                font = fonts['altbold'], size = 23, _alpha = 0.0, justify = 0.5 )
    yn = Image( dloc.left( 0.2 ).top( 0.2 ).move_left( 0.3 ).move_up( 0.3 ),
                _alpha = 0 )

    start_animation( common.bg, d, cap, yn )

    set( yn.image, images['yes'] )
    set( cap.text, 'use a large virtual canvas' )
    set( cap.color, yellow )
    fade_in( 0.5, cap )
    fade_in( 0.5, d, yn )

    smooth( 0.5, d.pix_u, 1.0 )
    parallel()
    smooth( 0.5, d.label_u, 1.0 )
    smooth( 0.5, d.fill_u, 0.0 )
    serial( 0.5 )
    smooth( 0.5, d.grid_u, 0.0 )
    end()
    end()

    parallel()
    smooth( 1.0, d.cam, 1 )
    end()
    wait( 0.5 )

    smooth( 0.5, d.pix_d, 1.0 )
    parallel()
    smooth( 0.5, d.label_d, 1.0 )
    smooth( 0.5, d.fill_d, 0.0 )
    serial( 0.5 )
    smooth( 0.5, d.grid_d, 0.0 )
    end()
    end()

    smooth( 1.0, d.cam, 2 )
    wait( 0.5 )

    smooth( 0.5, d.pix_h2, 1.0 )
    smooth( 0.5, d.pix_h1, 1.0 )
    parallel()
    smooth( 0.5, d.label_h, 1.0 )
    smooth( 0.5, d.fill_h, 0.0 )
    serial( 0.5 )
    smooth( 0.5, d.grid_h, 0.0 )
    end()
    end()

    parallel()
    smooth( 1.0, d.squinch, 1.5 )
    smooth( 1.0, d.cam, 3 )
    smooth( 1.0, d.compare, 1.0 )
    end()

    pause()
    fade_out( 0.5, d, yn )

    return end_animation()
demo4 = demo4()

def demo5():
    dloc = get_camera().top(0.85).inset(0.05).restrict_aspect(4./3.).move_down(0.05)
    d = Drawable( dloc, chapter2, _alpha = 0 )
    cap = Text( get_camera().bottom(0.175).inset(0.04).move_down(0.15),
                font = fonts['altbold'], size = 23, _alpha = 0.0, justify = 0.5 )
    yn = Image( dloc.left( 0.2 ).top( 0.2 ).move_left( 0.3 ).move_up( 0.3 ),
                _alpha = 0 )

    start_animation( common.bg, d, cap, yn )
    set( cap.text, 'use a large virtual canvas' )
    set( cap.color, yellow )
    set( cap._alpha, 1 )

    set( yn.image, images['no'] )
    fade_in( 0.5, d, yn )

    smooth( 0.5, d.pix_u, 1.0 )
    parallel()
    smooth( 0.5, d.label_u, 1.0 )
    smooth( 0.5, d.fill_u, 0.0 )
    serial( 0.5 )
    smooth( 0.5, d.grid_u, 0.0 )
    end()
    end()

    wait( 0.5 )
    set( d.cam, 1 )
    wait( 0.5 )

    smooth( 0.5, d.pix_d, 1.0 )
    parallel()
    smooth( 0.5, d.label_d, 1.0 )
    smooth( 0.5, d.fill_d, 0.0 )
    serial( 0.5 )
    smooth( 0.5, d.grid_d, 0.0 )
    end()
    end()

    wait( 0.5 )
    set( d.cam, 2 )
    wait( 0.5 )

    smooth( 0.5, d.pix_h2, 1.0 )
    smooth( 0.5, d.pix_h1, 1.0 )
    parallel()
    smooth( 0.5, d.label_h, 1.0 )
    smooth( 0.5, d.fill_h, 0.0 )
    serial( 0.5 )
    smooth( 0.5, d.grid_h, 0.0 )
    end()
    end()

    wait( 0.5 )
    
    set( d.squinch, 1.5 )
    set( d.cam, 3 )
    set( d.compare, 1.0 )

    pause()
    fade_out( 0.5, d, yn, cap )

    return end_animation()
demo5 = demo5()

def demo6():
    dloc = get_camera().top(0.85).inset(0.05).restrict_aspect(4./3.).move_down(0.05)
    d = Drawable( dloc, chapter2, _alpha = 0 )
    b = Drawable( dloc, blank )
    cap = Text( get_camera().bottom(0.175).inset(0.04).move_down(0.15),
                font = fonts['altbold'], size = 23, _alpha = 0.0, justify = 0.5 )
    yn = Image( dloc.left( 0.2 ).top( 0.2 ).move_left( 0.3 ).move_up( 0.3 ),
                _alpha = 0 )

    start_animation( common.bg, d, cap, yn )

    set( d.pix_u, 1.0 )
    set( d.label_u, 1.0 )
    set( d.fill_u, 1.0 )
    set( d.grid_u, 0.0 )
    set( d.pix_d, 1.0 )
    set( d.label_d, 1.0 )
    set( d.fill_d, 1.0 )
    set( d.grid_d, 0.0 )
    set( d.cam, 2 )
    
    set( yn.image, images['yes'] )
    set( cap.text, 'reflect structure in transitions' )
    set( cap.color, yellow )
    fade_in( 0.5, cap )
    fade_in( 0.5, d, yn )

    smooth( 0.5, d.pix_h2, 1.0 )
    smooth( 0.5, d.pix_h1, 1.0 )
    smooth( 0.5, d.label_h, 1.0 )
    parallel()
    smooth( 0.5, d.fill_h, 0.0 )
    serial( 0.5 )
    smooth( 0.5, d.grid_h, 0.0 )
    end()
    end()

    parallel()
    smooth( 0.5, d.squinch, 1.5 )
    smooth( 0.5, d.cam, 3 )
    smooth( 0.5, d.compare, 1.0 )
    end()

    pause()
    enter( b )
    lower( b, below = d )
    fade_out( 0.5, d )
    set( d.cam, 4 )
    set( d.next_section, 1.0 )
    fade_in( 0.5, d )
    exit( b )

    pause()
    fade_out( 0.25, d, yn )

    return end_animation()
demo6 = demo6()

def demo7():
    dloc = get_camera().top(0.85).inset(0.05).restrict_aspect(4./3.).move_down(0.05)
    d = Drawable( dloc, chapter2, _alpha = 0 )
    cap = Text( get_camera().bottom(0.175).inset(0.04).move_down(0.15),
                font = fonts['altbold'], size = 23, _alpha = 0.0, justify = 0.5 )
    yn = Image( dloc.left( 0.2 ).top( 0.2 ).move_left( 0.3 ).move_up( 0.3 ),
                _alpha = 0 )

    start_animation( common.bg, d, cap, yn )

    set( d.pix_u, 1.0 )
    set( d.label_u, 1.0 )
    set( d.fill_u, 1.0 )
    set( d.grid_u, 0.0 )
    set( d.pix_d, 1.0 )
    set( d.label_d, 1.0 )
    set( d.fill_d, 1.0 )
    set( d.grid_d, 0.0 )
    set( d.pix_h1, 1.0 )
    set( d.pix_h2, 1.0 )
    set( d.label_h, 1.0 )
    set( d.fill_h, 1.0 )
    set( d.grid_h, 0.0 )
    set( d.cam, 2 )
    
    set( yn.image, images['no'] )
    set( cap.text, 'reflect structure in transitions' )
    set( cap.color, yellow )
    set( cap._alpha, 1 )
    fade_in( 0.5, d, yn )

    parallel()
    smooth( 1.0, d.squinch, 1.5 )
    smooth( 1.0, d.cam, 3 )
    smooth( 1.0, d.compare, 1.0 )
    end()

    wait( 0.5 )

    set( d.next_section, 1.0 )
    smooth( 1.0, d.cam, 4 )
    pause()
    smooth( 1.0, d.cam, 5 )

    pause()
    fade_out( 0.25, d, yn, cap )

    return end_animation()
demo7 = demo7()

def demo8():
    dloc = get_camera().top(0.85).inset(0.05).restrict_aspect(4./3.).move_down(0.05)
    b = Drawable( dloc, blank )
    d = Drawable( dloc, chapter3, _alpha = 0 )
    cap = Text( get_camera().bottom(0.175).inset(0.04).move_down(0.15),
                font = fonts['altbold'], size = 23, _alpha = 0.0, justify = 0.5 )
    yn = Image( dloc.left( 0.2 ).top( 0.2 ).move_left( 0.3 ).move_up( 0.3 ),
                _alpha = 0 )

    start_animation( common.bg, d, cap, yn )

    set( yn.image, images['no'] )
    set( cap.text, 'avoid instantaneous changes' )
    set( cap.color, yellow )

    fade_in( 0.5, cap )
    fade_in( 0.5, d, yn )
    pause()
    set( d.slide, 1 )
    pause()
    enter( b )
    lower( b, below = d )
    fade_out( 0.5, d, cap )
    set( d.slide, 0 )
    set( cap.text, 'avoid extraneous motion' )
    fade_in( 0.5, cap )
    fade_in( 0.5, d )
    exit( b )
    
    set( d.rubber, 1 )
    linear( 10.0, d.slide, 1 )
    pause()
    enter( b )
    lower( b, below = d )
    fade_out( 0.5, d, cap, yn )
    set( d.slide, 0 )
    set( yn.image, images['yes'] )
    fade_in( 0.5, d, yn )
    exit( b )
    
    set( d.rubber, 0 )
    linear( 8.0, d.slide, 1 )
    pause()
    fade_out( 0.5, d, yn )

    return end_animation()
demo8 = demo8()

#test_objects( demo1, demo2, demo3, demo4, demo5, demo6, demo7, demo8 )

#test_objects( demo_principles )
test_objects( character_animation )

#test_objects( expand_and_compress_good, expand_and_compress_bad )
#test_objects( overlays_good, overlays_bad )
#test_objects( one_thing_at_a_time_good, one_thing_at_a_time_bad )
#test_objects( virtual_canvas_good, virtual_canvas_bad )
#test_objects( transition_hierarchy_good, transition_hierarchy_bad )
#test_objects( no_instantaneous_bad, no_instantaneous_good, extraneous_motion_bad )

#test_objects( chapter3 )   
#test_objects( chapter2, character_animation )
#test_objects( chapter2 )   
#test_objects( chapter1 )
