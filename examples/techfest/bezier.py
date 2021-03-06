from slithy.library import *
import math
import common
from fonts import fonts

thefont = fonts['mono']

darkblue = Color( 0, 0, 0.6 )
lightblue = Color( 0.3, 0.6, 0.8 )
darkred = Color( 0.8, 0, 0 )

class Foo:
    def __init__( self ):
        self.controls = [ (10,10), (10,90), (90,90), (60, 40) ]
        self.curve_dirty = 1

def reduce( p, u ):
    if len(p) < 2:
        return p
    return [(x1*(1-u)+x2*u, y1*(1-u)+y2*u) for (x1,y1),(x2,y2) in zip( p[:-1], p[1:] )]

def map_to_line( x, y, (px,py), (qx,qy) ):
    u = ((x - px) * (qx - px ) + (y - py) * (qy - py)) / ((qx-px)*(qx-px)+(qy-py)*(qy-py))
    if u < 0:
        return 0
    if u > 1:
        return 1
    return u

def compute_curve( info ):
    if len(info.controls) == 0:
        info.curve_dirty = 0
        return None
    p = [ (0,)+info.controls[0] ]
    for i in range(1,100):
        u = i / 100.0
        q = info.controls
        while len(q) > 1:
            q = reduce( q, u )
        p.append( (u,)+q[0] )
    p.append( (1,)+info.controls[-1] )
    info.curve = p
    info.curve_dirty = 0

def bezier( info = (OBJECT, Foo()),
            u = (SCALAR, 0, 1),
            show_const = (BOOLEAN, 0),
            show_curve = (BOOLEAN, 0),
            const_reveal = (SCALAR, 0, 10),
            ):
    #print camera()[4], visible()[4]
    set_camera( Rect(0,0,100,100) )
    clear( white )
    id( -1 )

    c = info.controls
    if show_curve and info.curve_dirty:
        compute_curve( info )

    if len(c) > 1:
        i = 1000
        push()
        for (x1,y1),(x2,y2) in zip( c[:-1], c[1:] ):
            id( i )
            thickness( 3 )
            color( invisible )
            line( x1, y1, x2, y2 )
            thickness( 0.5 )
            color( 0.7 )
            line( x1, y1, x2, y2 )
            i += 1
        pop()

    id( -1 )
    if show_const:
        p = c
        levels = len(p)-2
        i = 0
        while len(p) > 1:
            if levels > 1:
                thecolor = darkblue.interp( lightblue, float(i) / (levels-1) )
            else:
                thecolor = darkblue

            if const_reveal < i*2:
                thecolor = invisible
            elif const_reveal < i*2+1:
                thecolor = Color( thecolor, const_reveal - i*2 )

            if const_reveal < i*2+1:
                linefrac = 0
            elif const_reveal < i*2+2:
                linefrac = const_reveal - (i*2+1)
            else:
                linefrac = 1
                                  
            p = reduce( p, u )
            if len(p) > 1:
                color( 0.8 )
                thickness( 0.5 )
                for (x1,y1),(x2,y2) in zip( p[:-1], p[1:] ):
                    x2 = x2 * linefrac + x1 * (1-linefrac)
                    y2 = y2 * linefrac + y1 * (1-linefrac)
                    line( x1, y1, x2, y2 )
                color( thecolor )
                if i == 0:
                    j = 3000
                    for x, y in p:
                        id( j )
                        dot( 1.5, x, y )
                        j += 1
                    id( -1 )
                else:
                    for x, y in p:
                        dot( 1.5, x, y )
            i += 1

        if levels*2 <= const_reveal < levels*2+1:
            color( darkred, const_reveal - levels*2 )
            dot( 2, p[0][0], p[0][1] )
        elif levels*2+1 <= const_reveal:
            color( darkred )
            dot( 2, p[0][0], p[0][1] )

    id( -1 )
    if show_curve and info.curve:
        v = info.curve
        p = Path().moveto( v[0][1], v[0][2] )
        for vu,x,y in v[1:]:
            if vu > u:
                break
            p.lineto( x, y )
        color( darkred )
        widestroke( p, 1 )
            
    i = 2000
    push()
    color( green )
    for x, y in info.controls:
        id( i )
        dot( 2, x, y )
        i += 1
    pop()



    if show_const:
        if const_reveal < 1:
            color( black, const_reveal )
        else:
            color( black )
        text( 50, 5, 'u = %.2f' % (u,), thefont, size = 5, anchor = 'fc' )
        

    info.last_coords = mark('')
        

class BezierDemo(Controller):
    def create_objects( self ):
        self.d = Drawable( None, bezier, info = self )
        return self.d

    def start( self ):
        self.last_coords = None
        self.drag = None
        self.controls = []
        self.curve_dirty = 1
        self.steps = 0

    def mousedown( self, x, y, m ):
        what, = query_id( x, y )

        if 3000 <= what < 4000:
            self.drag = what
            what -= 3000
            x, y = unproject( x, y, self.last_coords )
            u = map_to_line( x, y, self.controls[what], self.controls[what+1] )
            set( self.d.show_const, 1 )
            set( self.d.u, u )
        elif 2000 <= what < 3000:
            self.drag = what

    def mousemove( self, x, y, m ):
        if self.drag is None:
            return

        if 2000 <= self.drag < 3000:
            self.controls[self.drag-2000] = unproject( x, y, self.last_coords )
            self.curve_dirty = 1
        elif 3000 <= self.drag < 4000:
            what = self.drag - 3000
            x, y = unproject( x, y, self.last_coords )
            u = map_to_line( x, y, self.controls[what], self.controls[what+1] )
            set( self.d.show_const, 1 )
            set( self.d.u, u )
            

    def mouseup( self, x, y, m ):
        if not self.last_coords:
            return

        what, = query_id( x, y )
        x, y = unproject( x, y, self.last_coords )

        if what == 0 and self.drag is None:
            # clicked in the background; add a control point
            self.controls.append( (x, y) )
            self.curve_dirty = 1
        elif 1000 <= what < 2000:
            # clicked a control polygon line
            what -= 1000
            u = map_to_line( x, y, self.controls[what], self.controls[what+1] )
            set( self.d.show_const, 1 )
            set( self.d.u, u )
            smooth( 1.0, self.d.const_reveal, 0, 1 )
            self.steps = 1

        self.drag = None

    def key( self, k, x, y, m ):
        if k == 'g':
            if len(self.controls) > 1:
                set( self.d.show_const, 1 )
                set( self.d.show_curve, 1 )
                set( self.d.u, 0.0 )
                smooth( 0.5, self.d.const_reveal, len(self.controls) * 2 - 3 )
                smooth( 5.0, self.d.u, 1.0 )

                smooth( 0.5, self.d.const_reveal, 0 )
                set( self.d.show_const, 0 )
                self.steps = 0
        elif k == 'c':
            set( self.d.show_const, 0 )
            set( self.d.const_reveal, 0 )
        elif k == 'v':
            set( self.d.show_curve, 0 )
        elif k == 'd':
            if len(self.controls) > 0:
                self.controls.pop()
                self.curve_dirty = 1
        elif k == 'a':
            self.steps += 1
            smooth( 1.0, self.d.const_reveal, self.steps )
        
                
def bezier_anim():
    tx = Text( get_camera().left(0.5).inset(0.05).top( 0.1 ), font = fonts['bold'],
               text = 'Bezier curves', color = yellow, size = 24, _alpha = 0.0 )
    bl = BulletedList( get_camera().left(0.5).inset(0.05).bottom( 0.85 ), font = fonts['text'],
                       color = white, size = 18, bullet = [fonts['dingbats'],'w'] )
    vi = viewport.interp( get_camera().inset( 0.1 ),
                          get_camera().right(0.5).inset(0.05) )
    i = Interactive( vi, controller = BezierDemo, _alpha = 0.0 )
    #i = Drawable( vi, bezier )

    start_animation( common.bg, i )
    fade_in( 0.5, i )
    pause()
    smooth( 1.0, vi.x, 1 )
    wait( -0.5 )
    enter( tx, bl )
    fade_in( 0.5, tx )
    pause()

    bl.add_item( 0, 'de Casteljau construction' )
    pause()

    bl.add_item( 0, 'infinitely differentiable' )
    pause()

    bl.add_item( 0, 'global control' )
    pause()

    bl.add_item( 0, 'non-interpolating' )
    pause()

    
    
    fade_out( 0.5, i, tx, bl )
    return end_animation()
bezier_anim = bezier_anim()

        



test_objects( bezier_anim, BezierDemo )
