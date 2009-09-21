from slithy.library import *
from slithy.util import *
import math
from fonts import fonts
import common
labelfont = fonts['bold']
labelcolor = Color( 0, 0, 0.6 )

darkred = Color( 0.7, 0, 0 )

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

treb = truetype_outline( trebuchet_a )
frut = truetype_outline( frutiger_a )

t_outer = ( ( 740, 123, 37, 0, ),
            ( 626, -20, 6, 1, ),
            ( 391, -20, 35, 2, ),
            ( 265, -20, 34, 3, ),
            ( 80, 163, 38, 4, ),
            ( 80, 299, 53, 5, ),
            ( 80, 462, 52, 6, ),
            ( 365, 687, 36, 7, ),
            ( 586, 687, 51, 8, ),
            ( 646, 687, 50, 9, ),
            ( 722, 661, 23, 10, ),
            ( 722, 921, 16, 11, ),
            ( 490, 921, 35, 12, ),
            ( 312, 921, 34, 13, ),
            ( 216, 825, 7, 14, ),
            ( 136, 984, 39, 15, ),
            ( 190, 1028, 62, 16, ),
            ( 381, 1091, 62, 17, ),
            ( 468, 1091, 51, 18, ),
            ( 701, 1091, 50, 19, ),
            ( 912, 879, 22, 20, ),
            ( 912, 648, 21, 21, ),
            ( 912, 264, 17, 22, ),
            ( 912, 123, 20, 23, ),
            ( 996, 76, 23, 24, ),
            ( 996, -19, 21, 25, ),
            ( 880, -19, 34, 26, ),
            ( 765, 47, 38, 27,),
            )

f_outer = ( ( 985, 0, 33, 0, ),
            ( 805, 0, 35, 1, ),
            ( 805, 135, 53, 2, ),
            ( 801, 135, 35, 3, ),
            ( 687, -25, 6, 4, ),
            ( 477, -25, 35, 5, ),
            ( 300, -25, 34, 6, ),
            ( 201, 53, 39, 7, ),
            ( 94, 137, 38, 8, ),
            ( 94, 301, 53, 9, ),
            ( 94, 479, 52, 10, ),
            ( 262, 571, 55, 11, ),
            ( 396, 645, 54, 12, ),
            ( 580, 645, 51, 13, ),
            ( 709, 645, 50, 14, ),
            ( 784, 641, 23, 15, ),
            ( 784, 781, 52, 16, ),
            ( 728, 845, 39, 17, ),
            ( 667, 913, 38, 18, ),
            ( 526, 913, 35, 19, ),
            ( 350, 913, 34, 20, ),
            ( 223, 807, 7, 21, ),
            ( 213, 971, 39, 22, ),
            ( 378, 1069, 54, 23, ),
            ( 557, 1069, 51, 24, ),
            ( 777, 1069, 50, 25, ),
            ( 879, 960, 23, 26, ),
            ( 977, 855, 22, 27, ),
            ( 977, 637, 21, 28, ),
            ( 977, 205, 17, 29, ),
            ( 977, 61, 20, 30,),
            )

match = ( ( ( 0, 11, 100 ),
            ( 2, 13, -250 ),
            ( 5, 19, 200 ),
            ( 8, 22, 400 ),
            ( 10, 24, 650 ),
            ( 12, 26, 400 ),
            ( 14, 28, 600 ),
            ( 15, 28, -150 ),
            ( 18, 0, -350 ),
            ( 21, 5, 100 ),
            ( 22, 7, 100 ),
            ( 24, 9, -150 ),
            ( 25, 9, -50 ), ),
          ( ( 0, 17, 700 ),
            ( 2, 21,  550 ),
            ( 5, 24,  200 ),
            ( 8, 28,  500 ),
            ( 10, 28,  650 ),
            ( 12, 29,  0 ),
            ( 14, 1,  450 ),
            ( 15, 2,  -50 ),
            ( 18, 5,  50 ),
            ( 21, 9,  -450 ),
            ( 22, 11,  100 ),
            ( 24, 13,  300 ),
            ( 25, 15,  700 ), ),
          ( ( 0, 3, 1250 ),
            ( 2, 5,  1350 ),
            ( 5, 9,  1550 ),
            ( 8, 13,  1450 ),
            ( 10, 13,  750 ),
            ( 12, 19,  1550 ),
            ( 14, 21,  1450 ),
            ( 15, 21,  700 ),
            ( 18, 24,  1550 ),
            ( 21, 28,  1550 ),
            ( 22, 29,  1450 ),
            ( 24, 0,  1150 ),
            ( 25, 0,  1600 ), ),
          )

def curveto( (x0,y0,f0), (x1,y1,f1), (x2,y2,f2) ):
    r = []
    for i in range(1,6):
        u = i / 5.0
        up = 1-u
        r.append( (up*up*x0 + 2*up*u*x1 + u*u*x2, up*up*y0 + 2*up*u*y1 + u*u*y2, -1 ) )
    r[-1] = (x2,y2,f2)
    return r
        
        

def contour_to_segments( c ):
    pts = [(x,y,((f&1) and (n+1) or 0)-1) for x,y,f,n in c]

    size = len( c )
        
    start = 0
    for i in range(0,size):
        j = (i+1) % size
        k = (i+2) % size

        f = ((pts[i][2] >= 0) << 2) | ((pts[j][2] >= 0) << 1) | (pts[k][2] >= 0)

        if f == 6 or f == 7:
            if not start:
                out = [pts[i]]
                start = 1
            out.append( pts[j] )
            ij = (pts[i][0] + pts[j][0]) / 2.0, (pts[i][1] + pts[j][1]) / 2.0, -1

        elif f == 5:
            if not start:
                out = [pts[i]]
                start = 1
            out.extend( curveto( out[-1], pts[j], pts[k] ) )

        elif f == 4:
            if not start:
                out = [pts[i]]
                start = 1
            jk = (pts[j][0] + pts[k][0]) / 2.0, (pts[j][1] + pts[k][1]) / 2.0, -1
            out.extend( curveto( out[-1], pts[j], jk ) )

        elif f == 1:
            ij = (pts[i][0] + pts[j][0]) / 2.0, (pts[i][1] + pts[j][1]) / 2.0, -1
            if not start:
                out = [ij]
                start = 1
            out.extend( curveto( out[-1], pts[j], pts[k] ) )

        elif f == 0:
            ij = (pts[i][0] + pts[j][0]) / 2.0, (pts[i][1] + pts[j][1]) / 2.0, -1
            jk = (pts[j][0] + pts[k][0]) / 2.0, (pts[j][1] + pts[k][1]) / 2.0, -1
            if not start:
                out = [ij]
                start = 1
            out.extend( curveto( out[-1], pts[j], jk ) )

    length = 0
    for (x1,y1,f1),(x2,y2,f2) in zip( out[1:], out[:-1] ):
        length += math.sqrt( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) )

    ret = Outline()
    ret.pts = out
    ret.length = length

    return ret

def frac_length( o, f ):
    pts = o.pts
    f *= o.length
    
    last = pts[0]
    out = [last]
    d = 0

    for x,y,flag in pts[1:]:
        l = math.sqrt( (x-last[0])*(x-last[0]) + (y-last[1])*(y-last[1]) )
        if d+l < f:
            out.append( (x,y,flag) )
            d += l
        else:
            u = (f-d)/l
            x = last[0] * (1-u) + x * u
            y = last[1] * (1-u) + y * u
            out.append( (x,y,-1) )
            break
        last = x,y
            
    ret = Outline()
    ret.pts = out
    ret.length = f
    return ret

def straighten( o, f, s ):
    inpos = o.pts[0]
    outpos = o.pts[0]
    starttheta = theta = math.atan2( o.pts[1][1] - o.pts[0][1], o.pts[1][0] - o.pts[0][0] )

    out = [outpos]

    sdt = theta
    for i in o.pts[1:]:
        r = s * math.sqrt( (i[0]-inpos[0])*(i[0]-inpos[0]) + (i[1]-inpos[1])*(i[1]-inpos[1]) )
        newtheta = math.atan2( i[1]-inpos[1], i[0]-inpos[0] )

        dt = newtheta - theta
        while dt < -math.pi:
            dt += 2*math.pi
        while dt > math.pi:
            dt -= 2*math.pi
            
        theta = newtheta
        
        dt *= 1-f

        sdt += dt
        new = outpos[0] + r * math.cos( sdt ), outpos[1] + r * math.sin( sdt ), i[2]
        
        out.append( new )
        outpos = new
        inpos = i

    if f > 0:
        spin = -starttheta * f
        s = math.sin( spin )
        c = math.cos( spin )
        ox, oy = out[0][:2]
        out = [ (ox+((x-ox)*c)-((y-oy)*s), oy+((x-ox)*s)+((y-oy)*c), f) for x,y,f in out ]

    ret = Outline()
    ret.pts = out
    ret.length = o.length * s
    return ret
        
        

def make_path( o ):
    p = Path().moveto( *o.pts[0] )
    for i in o.pts[1:]:
        p.lineto( *i[:2] )
    return p

def extract_dots( o ):
    return [(x,y,f) for x,y,f in o.pts if f >= 0]

t_con = contour_to_segments( t_outer )
f_con = ( contour_to_segments( f_outer[11:] + f_outer[:11] ),
          contour_to_segments( f_outer[17:] + f_outer[:17] ),
          contour_to_segments( f_outer[3:] + f_outer[:3] ),
          )
          
    

def chapter4( fade = (SCALAR,0,1),
              tf = (SCALAR, 0, 1),
              ts = (SCALAR, 0, 1),
              ff = (SCALAR, 0, 1),
              fs = (SCALAR, 0, 1),
              fmatch = (INTEGER, 0, 2),
              show_match = (SCALAR, 0, 1),
              match_alpha = (SCALAR, 0, 1),
              show_score = (SCALAR, 0, 1),
              outline_alpha = (SCALAR, 0, 1),
              background = (BOOLEAN, 1),
              ):
    
    set_camera( Rect( -200, -200, 2800, 1069+175 ) )
    if background:
        clear( linen )

    color( black, 0.2 - 0.15 * fade )
    fill( treb.path )

    color( black, 0.3 - 0.15 * fade  )
    widestroke( treb.path, 10 )
    if not ts:
        color( 0.6 )
        for p in treb.oncurve[:-5]:
            dot( 25, p[0], p[1] )

    push()
    translate( 1500, 0 )

    color( black, 0.2 - 0.15 * fade  )
    fill( frut.path )

    color( black, 0.3 - 0.15 * fade  )
    widestroke( frut.path, 10 )
    if not fs:
        color( 0.6 )
        for p in frut.oncurve[:-7]:
            dot( 25, p[0], p[1] )
        
    pop()

    if tf > 0:
        tt = frac_length( t_con, tf )
        if tt.length > 0:
            sc = (tt.length * (1-ts) + 2500 * ts) / tt.length
            tt = straighten( tt, ts, sc )
            p = make_path( tt )

            tdx = (60 - tt.pts[0][0]) * ts
            tdy = (800 - tt.pts[0][1]) * ts
            push()
            translate( tdx, tdy )
    
            color( blue, outline_alpha )
            widestroke( p, 20 )

            color( black, outline_alpha )
            d = extract_dots( tt )
            for x,y,f in d:
                dot( 25, x, y )
            thickness( 15 )
            circle( 45, d[0][0], d[0][1] )
            circle( 70, d[0][0], d[0][1] )
            pop()
                
    push()
    translate( 1500, 0 )

    if ff > 0:
        ft = frac_length( f_con[fmatch], ff )
        if ft.length > 0:
            sc = (ft.length * (1-fs) + 2500 * fs) / ft.length
            ft = straighten( ft, fs, sc )
            p = make_path( ft )
    
            fdx = (-1500 + 60 - ft.pts[0][0]) * fs
            fdy = (400 - ft.pts[0][1]) * fs
            translate( fdx, fdy )
            
            color( blue, outline_alpha )
            widestroke( p, 20 )

            color( black, outline_alpha )
            d = extract_dots( ft )
            for x,y,f in d:
                dot( 25, x, y )
            thickness( 15 )
            circle( 45, d[0][0], d[0][1] )
            circle( 70, d[0][0], d[0][1] )
                
    pop()

    if show_match > 0.0 and match_alpha > 0.0:
        d = extract_matches( tt, ft, fmatch )

        thickness( 10 )
        for (x1,y1,x2,y2,score),a in zip( d, split_sequence_smooth( len(d), show_match, 0.7 ) ):
            if a > 0.0:
                color( darkred, a * match_alpha )
                line( x1+tdx, y1+tdy, 1500+x2+fdx, y2+fdy )

    if show_score > 0.0:
        val = (1600, 3700, 17350)[fmatch]
        color( labelcolor, show_score )
        text( 1300, -300, 'score: ' + str(val), font = labelfont, size = 200, anchor = 'c' )
        
def extract_matches( tt, ft, which ):
    tmap = dict( [(f,(x,y)) for x,y,f in tt.pts if f >= 0] )
    fmap = dict( [(f,(x,y)) for x,y,f in ft.pts if f >= 0] )
    
    ret = []
    for ti, fi, score in match[which]:
        tx, ty = tmap[ti]
        fx, fy = fmap[fi]
        ret.append( (tx, ty, fx, fy, score) )

    return ret


def show_chapter4():
    d = Drawable( get_camera(), chapter4 )

    start_animation( d )

    set( d.tf, 0.001 )
    set( d.ff, 0.001 )
    pause()
    smooth( 0.5, d.outline_alpha, 1.0 )
    parallel()
    smooth( 4.0, d.tf, 1.0 )
    smooth( 4.0, d.ff, 1.0 )
    end()
    wait( 0.5 )
    parallel()
    smooth( 2.0, d.fade, 1.0 )
    smooth( 2.0, d.ts, 1.0 )
    smooth( 2.0, d.fs, 1.0 )
    end()
    pause()
    set( d.match_alpha, 1.0 )
    smooth( 2.0, d.show_match, 1.0 )
    parallel()
    smooth( 2.0, d.ts, 0.0 )
    smooth( 2.0, d.fs, 0.0 )
    smooth( 2.0, d.fade, 0.0 )
    end()
    wait( 0.5 )
    smooth( 0.5, d.show_score, 1.0 )

    pause()

    parallel()
    smooth( 0.5, d.show_score, 0.0 )
    smooth( 0.5, d.match_alpha, 0.0 )
    smooth( 0.5, d.outline_alpha, 0.0 )
    end()
    set( d.show_match, 0.0 )

    set( d.fmatch, 1 )

    set( d.tf, 0.001 )
    set( d.ff, 0.001 )
    pause()
    smooth( 0.5, d.outline_alpha, 1.0 )
    parallel()
    smooth( 4.0, d.tf, 1.0 )
    smooth( 4.0, d.ff, 1.0 )
    end()
    wait( 0.5 )
    parallel()
    smooth( 2.0, d.fade, 1.0 )
    smooth( 2.0, d.ts, 1.0 )
    smooth( 2.0, d.fs, 1.0 )
    end()
    set( d.match_alpha, 1.0 )
    smooth( 2.0, d.show_match, 1.0 )
    parallel()
    smooth( 2.0, d.ts, 0.0 )
    smooth( 2.0, d.fs, 0.0 )
    smooth( 2.0, d.fade, 0.0 )
    end()
    wait( 0.5 )
    smooth( 0.5, d.show_score, 1.0 )

    pause()

    parallel()
    smooth( 0.5, d.show_score, 0.0 )
    smooth( 0.5, d.match_alpha, 0.0 )
    smooth( 0.5, d.outline_alpha, 0.0 )
    end()
    set( d.show_match, 0.0 )

    set( d.fmatch, 2 )

    set( d.tf, 0.001 )
    set( d.ff, 0.001 )
    smooth( 0.5, d.outline_alpha, 1.0 )
    parallel()
    smooth( 4.0, d.tf, 1.0 )
    smooth( 4.0, d.ff, 1.0 )
    end()
    wait( 0.5 )
    parallel()
    smooth( 2.0, d.fade, 1.0 )
    smooth( 2.0, d.ts, 1.0 )
    smooth( 2.0, d.fs, 1.0 )
    end()
    set( d.match_alpha, 1.0 )
    smooth( 2.0, d.show_match, 1.0 )
    parallel()
    smooth( 2.0, d.ts, 0.0 )
    smooth( 2.0, d.fs, 0.0 )
    smooth( 2.0, d.fade, 0.0 )
    end()
    wait( 0.5 )
    smooth( 0.5, d.show_score, 1.0 )

    return end_animation()
show_chapter4 = show_chapter4()
    

test_objects( show_chapter4, chapter4 )
