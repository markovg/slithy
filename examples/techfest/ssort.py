from slithy.library import *
from slithy.util import *
import random



class Blank:
    pass

class SelectionSort:
    def __init__( self, values ):
        self.values = values
        self.n = len( values )
        self.margin = (1.0 / self.n) * 0.1
        self.barwidth = (1.0 / self.n) * 0.8

        self.func_name = 'selection sort [%d]' % (self.n,)
        self.func_code = Blank()
        self.func_code.co_argcount = 4
        self.func_code.co_varnames = ('step', 'showpivot', 'showmin', 'swap' )
        self.func_defaults = ( (INTEGER, 0, self.n),
                               (SCALAR, 0, 1),
                               (SCALAR, 0, 2),
                               (SCALAR, 0, 1),
                               )

        self.presort()

    def presort( self ):
        p = []
        c = self.values[:]
        for i in range(len(c)):
            b = Blank()
            b.bars = c[:]
            
            m = min( c[i:] )
            x = c[i:].index( m ) + i
            c[i], c[x] = c[x], c[i]

            b.pivot = i
            b.shortest = x

            p.append( b )

        b = Blank()
        b.bars = c
        b.pivot = -1
        b.shortest = -1
        p.append( b )

        self.pre = p

    def __call__( self, step, showpivot, showmin, swap ):
        tr = 1.0 / self.n
        b = self.pre[step]
        m = self.margin

        set_camera( Rect( -0.1, -0.1, 1.2, 0, 1 ) )
        clear( white )

        self.draw_bars( b, step )

        if step == self.n:
            return

        if b.pivot == b.shortest:
            push()
            if showmin <= 1.0:
                color( green.interp( Color(0.5,0.8,0.0), showpivot ).interp( blue, showmin ) )
            else:
                color( blue.interp( red, showmin - 1.0 ) )
            translate( interpolate( swap, b.shortest * tr, b.pivot * tr ), 0.0 )
            rectangle( m,0, m+self.barwidth, b.bars[b.shortest] )
            pop()

        else:
            push()
            color( green.interp( Color(0.5,0.8,0.0), showpivot ) )
            translate( interpolate( swap, b.pivot * tr, b.shortest * tr ), 0.3 * (0.25 - (0.5-swap)*(0.5-swap)) )
            rectangle( m,0, m+self.barwidth, b.bars[b.pivot] )
            pop()

            push()
            if showmin <= 1.0:
                color( green.interp( blue, showmin ) )
            else:
                color( blue.interp( red, showmin - 1.0 ) )
            translate( interpolate( swap, b.shortest * tr, b.pivot * tr ), -0.1 * (0.25 - (0.5-swap)*(0.5-swap)) )
            rectangle( m,0, m+self.barwidth, b.bars[b.shortest] )
            pop()
                  
    def draw_bars( self, b, locked ):
        i = 0
        tr = 1.0 / self.n
        push()
        color( red )
        translate( self.margin, 0 )
        for j in b.bars:
            if i == locked:
                color( green )
            if i != b.pivot and i != b.shortest:
                rectangle( 0,0, self.barwidth, j )
            translate( tr, 0 )
            i += 1
        pop()
        


if __name__ == '__main__':
    values = [random.uniform( 0.1, 0.9 ) for i in range(10)]
    sorter = SelectionSort( values )

    test_objects( sorter )
