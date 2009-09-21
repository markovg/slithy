from slithy.library import *
import slithy.objects

class ScalarTuple(tuple):
    def interp( self, other, u ):
        if len(self) != len(other):
            raise ValueError, "can't interp ScalarTuples of different size"
        up = 1.0 - u
        return ScalarTuple( [x*up + y*u for x,y in zip(self,other)] )
    

class KenBurns(slithy.objects.Element):
    fade_time = 0.5
    default_box = ScalarTuple((0,0,1,1))
    
    def __init__( self, _viewport, **_params ):
        self._params = ( ('image', 'object', None),
                         ('_alpha', 'scalar', 1.0),
            )

        bad = slithy.objects.parameter_check( self._params, _params )
        if bad:
            raise ValueError, "no parameter '%s' for Barchart()" % (bad,)

        if _params.get( 'image', None ) is None:
            defintalpha = 0.0
        else:
            defintalpha = 1.0

        self._params = self._params + ( ('internal_alpha', 'scalar', defintalpha),
                                        ('image2', 'object', None),
                                        ('internal_alpha2', 'scalar', 0.0),
                                        ('box', 'scalartuple', self.default_box ),
                                        ('box2', 'scalartuple', self.default_box ),
                                        )
        
        self._defaults = _params
        self._viewport = _viewport

        self.current_image = self._defaults.get( 'image', None )

    def __str__( self ):
        return '<kenburns element>'

    def render( self, d, view, t ):
        im = d['image']
        im2 = d['image2']
        if not im and not im2:
            return

        push()
        token = clip( view )
        try:
            ox, oy, ulen, utheta, aspect = view
            translate( ox, oy )
            rotate( utheta )
            scale( ulen )

            if im is not None:
                a = d['internal_alpha']
                if a > 0.0:
                    self.show_image( im, d['box'], d['_alpha'] * a, aspect )
                       
            if im2 is not None:
                a = d['internal_alpha2']
                if a > 0.0:
                    self.show_image( im2, d['box2'], d['_alpha'] * a, aspect )

        finally:
            unclip( token )
            pop()

    def show_image( self, im, (x1,y1,x2,y2), alpha, aspect ):
        boxaspect = (x2-x1) / (y2-y1) * im.aspect

        push()
        if boxaspect > aspect:
            translate( 0, (1/aspect-1/boxaspect)/2 )
            scale( 1.0 / (x2-x1) )
            image( -x1, -y1 / im.aspect, im,
                   anchor = 'sw', alpha = alpha, width = 1.0 )

        else:
            translate( (1-boxaspect/aspect)/2, 0 )
            scale( 1.0 / (aspect * (y2-y1)) )
            image( -x1 * im.aspect, -y1, im,
                   anchor = 'sw', alpha = alpha, height = 1.0 )

        pop()

    def flip( self, image, box = default_box, duration=fade_time ):
        if not isinstance( box, ScalarTuple ):
            box = ScalarTuple(box)
            
        if self.current_image:
            duration /= 2
            linear( duration, self.internal_alpha, 0.0 )
        set( self.image, image )
        set( self.box, box )
        
        self.current_image = image
        linear( duration, self.internal_alpha, 1.0 )

    def clear( self ):
        if self.current_image:
            linear( self.fade_time, self.internal_alpha, 0.0 )
            set( self.image, None )
            set( self.box, self.default_box )
            self.current_image = None
            
    def crossfade( self, newimage, newbox = default_box, startbox=None, duration=fade_time ):
        if not isinstance( newbox, ScalarTuple ):
            newbox = ScalarTuple(newbox)

        parallel()
        set( self.internal_alpha, 1.0 )
        set( self.image2, newimage )
        set( self.internal_alpha2, 0.0 )
        linear( duration, self.internal_alpha2, 1.0 )
        if startbox is not None:
            if not isinstance( startbox, ScalarTuple ):
                startbox = ScalarTuple(startbox)
            set( self.box2, startbox )
            smooth( duration, self.box2, newbox )
        else:
            set( self.box2, newbox )
        end()

        set( self.box, newbox )
        set( self.image, newimage )
        set( self.image2, None )
        self.current_image = newimage
        
    def pan( self, newbox, duration = fade_time ):
        if not self.current_image:
            return
        if not isinstance( newbox, ScalarTuple ):
            newbox = ScalarTuple(newbox)
            
        smooth( duration, self.box, newbox )

    def appear( self, image, box = default_box ):
        if not isinstance( box, ScalarTuple ):
            box = ScalarTuple( box )
        set( self.image, image )
        set( self.box, box )
        set( self.internal_alpha, 1.0 )
        self.current_image = image
