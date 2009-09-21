from slithy.library import *
import slithy.objects
import math

def range_union( *r ):
    min, max = r[0]
    for s, t in r:
        if s < min: min = s
        if t > max: max = t
    return min, max


t1_2 = math.sqrt(1*2)
t2_5 = math.sqrt(2*5)
t5_10 = math.sqrt(5*10)

def pretty( min, max, divisions = 10 ):
    div = (max - min) / float(divisions)

    e = int(math.floor(math.log10( div )))
    f = div / 10 ** e

    if f < t1_2:
        div = 10 ** e
    elif f < t2_5:
        div = 2 * 10 ** e
    elif f < t5_10:
        div = 5 * 10 ** e
    else:
        div = 10 ** (e+1)

    i = int(math.floor( min / div ))
    x = div * i
    ticks = [x]
    while x < max:
        i += 1
        x = div * i
        ticks.append( x )

    if e < -4:
        ep = 10 ** e
        f = lambda x: (x,'%.1f x 10^%d' % (x / ep, e))
    elif e < 0:
        f = lambda x: (x,'%.*f' % (-e,x))
    elif e < 6:
        f = lambda x: (x,str(x))
    else:
        ep = 10 ** e
        f = lambda x: (x,'%.1f x 10^%d' % (x / ep, e))

    return map( f, ticks )



class Chart(slithy.objects.Element):
    def __init__( self, _viewport, **_params ):
        self._params = ( ('_alpha', 'scalar', 1.0),
                         ('font', object, None),
                         ('xticks', object, None),
                         )
        bad = slithy.objects.parameter_check( self._params, _params )
        if bad:
            raise ValueError, "no parameter '%s' for Barchart()" % (bad,)

        self._params = self._params + ( ('xmin', 'scalar', None),
                                        ('xmax', 'scalar', None),
                                        )
        
        self._defaults = _params
        self._viewport = _viewport

        self.objects = []
        self.xrange = None
        self.pieces = []
        self.yscales = []

        self.d = {}

        self.last_ticks = None

    def add_dataset( self, data, tag, **params ):
        p = Dataset( data )
        self.objects.append( p )

        if self.xrange is None:
            self.xrange = p.xrange
            self.xrange_v = p.xrange
        else:
            self.xrange = range_union( self.xrange, p.xrange )

        p.xrange_v = self.xrange_v
        p.id = tag

        suffix = '_' + tag
        
        self._params = self._params + (('color' + suffix, 'color', params.get('color',red) ),
                                       ('size' + suffix, 'scalar', params.get('size',None) ),
                                       ('alpha' + suffix, 'scalar', params.get('alpha',1.0) ),
                                       ('style' + suffix, 'string', params.get('style', 'scatter') ),
                                       ('lo' + suffix, 'scalar', params.get('lo',None) ),
                                       ('hi' + suffix, 'scalar', params.get('hi',None) ),
                                       ('ymin' + suffix, 'scalar', params.get('ymin',None) ),
                                       ('ymax' + suffix, 'scalar', params.get('ymax',None) ),
                                       ('right' + suffix, 'boolean', params.get('right',None) ),
                                       )

        self.d[tag] = p

        return p

    def position( self, *tags, **params ):
        newrange = range_union( *[self.d[t].yrange for t in tags] )
        if 'duration' in params and params['duration'] > 0.0:
            dur = params['duration']
            trans = params.get( 'interp', smooth )

            parallel()

            for t in tags:
                a = getattr( self, 'ymin_' + t )
                endpoint = params.get( 'ymin', newrange[0] )
                startpoint = get( a )
                if startpoint is None:
                    startpoint = newrange[0]
                trans( dur, a, startpoint, endpoint )
                
                a = getattr( self, 'ymax_' + t )
                endpoint = params.get( 'ymax', newrange[1] )
                startpoint = get( a )
                if startpoint is None:
                    startpoint = newrange[1]
                trans( dur, a, startpoint, endpoint )
                

                
            def assign( foo, default ):
                if foo in params:
                    x = params[foo]
                    for t in tags:
                        a = getattr( self, foo + '_' + t )
                        v = get( a )
                        if v is None:
                            v = default
                        trans( dur, a, v, x )

            def assign_set( foo ):
                if foo in params:
                    x = params[foo]
                    for t in tags:
                        set( getattr( self, foo + '_' + t ), x )

            assign( 'lo', 0.0 )
            assign( 'hi', 1.0 )
            assign_set( 'right' )

            end()
                    
                    
        else:
            for t in tags:
                set( getattr( self, 'ymin_' + t ), params.get( 'ymin', newrange[0] ) )
                set( getattr( self, 'ymax_' + t ), params.get( 'ymax', newrange[1] ) )

            def assign( foo ):
                if foo in params:
                    x = params[foo]
                    for t in tags:
                        set( getattr( self, foo + '_' + t ), x )

            assign( 'lo' )
            assign( 'hi' )
            assign( 'right' )


                

            
            

    def set_yspace( self, min, max, *objects ):
        newrange = range_union( *[o.yrange_v for o in objects] )
        for o in objects:
            o.yrange_v = newrange

        self.pieces.append( (min, max, objects) )
        self.yscales.append( (min, max, newrange) )
        

    def __str__( self ):
        return '<chart element>'

    def render( self, d, view, t ):
        push()
        try:
            ox, oy, width, utheta, aspect = view
            translate( ox, oy )
            rotate( utheta )

            xmin = d['xmin']
            if xmin is None:
                xmin = self.xrange[0]
            xmax = d['xmax']
            if xmax is None:
                xmax = self.xrange[1]
                
            xmin = float(xmin)
            xmax = float(xmax)

            height = width / aspect

            scales = {}

            for i in self.objects:

                lo = d['lo_' + i.id]
                hi = d['hi_' + i.id]
                if lo is None or hi is None:
                    continue

                lo = (height * 0.1) * (1.0 - lo) + height * lo
                hi = (height * 0.1) * (1.0 - hi) + height * hi

                ymin = d['ymin_' + i.id]
                if ymin is None:
                    ymin = i.yrange[0]
                ymax = d['ymax_' + i.id]
                if ymax is None:
                    ymax = i.yrange[1]
                i.yrange_v = (ymin, ymax)
                
                style = d['style_' + i.id]
                col = d['color_' + i.id]
                alpha = d['alpha_' + i.id]
                col = Color( col, alpha )
                size = d['size_' + i.id]
                right = not not d['right_' + i.id]
                
                i.xrange_v = xmin, xmax
                getattr( i, 'render_' + style )( width * 0.1, lo, width * 0.9, hi, col, size )

                key = (lo,hi,ymin,ymax,right)
                scales[key] = max( scales.get( key, 0.0 ), alpha )

            textsize = height * 0.025
            color( black )
            thickness( height / 300.0 )

            ticks = d['xticks']
            if not ticks:
                self.draw_xscale( xmin, xmax, width * 0.1, 0, width * 0.9, height * 0.1, d['font'], textsize )
            else:
                self.draw_xticks( ticks, xmin, xmax, width * 0.1, 0, width * 0.9, height * 0.1, d['font'], textsize )

            for (lo, hi, ymin, ymax, right), alpha in scales.iteritems():
                size = abs(hi-lo) / (height * 0.9)
                if size < 0.25:
                    numticks = 4
                elif size < 0.75:
                    numticks = 7
                else:
                    numticks = 10
                    
                color( black, alpha )
                if right:
                    self.draw_right_yscale( ymin, ymax, width * 0.9, lo, width, hi, d['font'], textsize,
                                            numticks )
                else:
                    self.draw_left_yscale( ymin, ymax, 0, lo, width * 0.1, hi, d['font'], textsize,
                                           numticks )
                
                
        finally:
            pop()

    def draw_xticks( self, ticks, min, max, x0, y0, x1, y1, font, textsize ):
        top = (y1-y0) * 0.9 + y0
        bottom = (y1-y0) * 0.6 + y0
        textpos = (y1-y0) * 0.5 + y0
        width = x1 - x0
        
        range = max - min

        for v, s in ticks:
            if min <= v <= max:
                x = (v - min) / range * width + x0
                line( x, bottom, x, top )
                text( x, textpos, s, font = font, size = textsize, anchor = 'n' )

    def draw_xscale( self, min, max, x0, y0, x1, y1, font, textsize ):
        top = (y1-y0) * 0.9 + y0
        bottom = (y1-y0) * 0.6 + y0
        textpos = (y1-y0) * 0.5 + y0
        width = x1 - x0
        
        range = max - min

        if self.last_ticks is not None and self.last_ticks[0] == (min,max):
            ticks = self.last_ticks[1]
        else:
            ticks = pretty( min, max, divisions = 6 )
            self.last_ticks = ((min,max),ticks)
            
        for v, s in ticks:
            if min <= v <= max:
                x = (v - min) / range * width + x0
                line( x, bottom, x, top )
                text( x, textpos, s, font = font, size = textsize, anchor = 'n' )

    def draw_left_yscale( self, min, max, x0, y0, x1, y1, font, textsize, numticks ):
        right = (x1-x0) * 0.9 + x0
        left = (x1-x0) * 0.7 + x0
        textpos = (x1-x0) * 0.6 + x0
        height = y1 - y0

        range = max - min

        ticks = pretty( min, max, divisions = numticks )
        for v, s in ticks:
            if min <= v <= max:
                y = (v - min) / range * height + y0
                line( left, y, right, y )
                text( textpos, y, s, font = font, size = textsize, anchor = 'e' )

    def draw_right_yscale( self, min, max, x0, y0, x1, y1, font, textsize, numticks ):
        right = (x1-x0) * 0.1 + x0
        left = (x1-x0) * 0.3 + x0
        textpos = (x1-x0) * 0.4 + x0
        height = y1 - y0

        range = max - min

        ticks = pretty( min, max, divisions = numticks )
        for v, s in ticks:
            if min <= v <= max:
                y = (v - min) / range * height + y0
                line( left, y, right, y )
                text( textpos, y, s, font = font, size = textsize, anchor = 'w' )

    def xview( self, min, max, duration = 0.0 ):
        if get(self.xmin) is None:
            set( self.xmin, self.xrange[0] )
            set( self.xmax, self.xrange[1] )

        if min is None:
            min = get(self.xmin)
        if max is None:
            max = get(self.xmax)

        if duration > 0.0:
            parallel()
            smooth( duration, self.xmin, min )
            smooth( duration, self.xmax, max )
            end()
        else:
            set( self.xmin, min )
            set( self.xmax, max )
            
class Dataset:
    def __init__( self, data ):
        self.data = data

        minx = maxx = data[0][0]
        miny = maxy = data[0][1]

        for x, y in data:
            if x < minx: minx = x
            elif x > maxx: maxx = x
            if y < miny: miny = y
            elif y > maxy: maxy = y

        self.xrange = float(minx), float(maxx)
        self.yrange = float(miny), float(maxy)

        self.xrange_v = self.xrange
        self.yrange_v = self.yrange

        self.active = self.data

    def render_scatter( self, vx0, vy0, vx1, vy1, c, size ):
        if size is None:
            r = abs(vy1-vy0) / 200.0
        else:
            r = size
        x0, x1 = self.xrange_v
        y0, y1 = self.yrange_v
        xlen = x1 - x0
        ylen = y1 - y0
        vxlen = vx1 - vx0
        vylen = vy1 - vy0
        
        color( c )
        for x, y in self.active:
            if x0 <= x <= x1 and y0 <= y <= y1:
                x = (x - x0) / xlen * vxlen + vx0
                y = (y - y0) / ylen * vylen + vy0
                dot( r, x, y )

    def render_line( self, vx0, vy0, vx1, vy1, c, size ):
        if size is None:
            thickness( abs(vx1-vx0) / 200.0 )
        else:
            thickness( size )
        x0, x1 = self.xrange_v
        y0, y1 = self.yrange_v
        xlen = x1 - x0
        ylen = y1 - y0
        vxlen = vx1 - vx0
        vylen = vy1 - vy0

        pts = [[]]
        color( c )
        for x, y in self.active:
            if x0 <= x <= x1 and y0 <= y <= y1:
                x = (x - x0) / xlen * vxlen + vx0
                y = (y - y0) / ylen * vylen + vy0
                pts[-1].append( x )
                pts[-1].append( y )
            elif len(pts[-1]) > 0:
                pts.append( [] )
        for i in pts:
            if i:
                line( *i )

    def render_spike( self, vx0, vy0, vx1, vy1, c, size ):
        if size is None:
            thickness( abs(vx1-vx0) / 100.0 )
        else:
            thickness( size )
        x0, x1 = self.xrange_v
        y0, y1 = self.yrange_v
        xlen = x1 - x0
        ylen = y1 - y0
        vxlen = vx1 - vx0
        vylen = vy1 - vy0

        zero = (0 - y0) / ylen * vylen + vy0
        if zero < vy0:
            zero = vy0
        elif zero > vy1:
            zero = vy1

        color( c )
        for x, y in self.active:
            if x0 <= x <= x1 and y0 <= y <= y1:
                x = (x - x0) / xlen * vxlen + vx0
                y = (y - y0) / ylen * vylen + vy0
                line( x, y, x, zero )
        

        
            
            
            
            
            
            
        
        
            
