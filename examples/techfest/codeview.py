from slithy.library import *
from fonts import fonts

fontpath.append( 'fonts' )
thefont = fonts['mono']

class Blank: pass

class CodeViewer:
    def __init__( self, *textbits, **kw ):

        self.size = len(textbits)
        self.debug = debug = kw.get( 'debug', 0 )
        
        self.func_name = 'code viewer'
        self.func_code = Blank()
        self.func_code.co_argcount = len(textbits) * 2
        self.texts = []
        vn = []
        df = []
        j = 0
        for i in textbits:
            self.texts.append( i )
            vn.append( 'color' + str(j) )
            if debug:
                df.append( (SCALAR, 0, 1, 0) )
            else:
                df.append( (COLOR, black) )
            j += 1
        self.func_code.co_varnames = tuple( vn )
        self.func_defaults = tuple( df )

        teststring = ''.join(textbits)
        d = text( 0, 0, teststring, thefont, size = 1, anchor = 'nw', nodraw = 1 )
        w = kw.get( 'width', d['width'] )
        h = kw.get( 'height', d['height'] )

        self.camera = Rect( (d['left']-0.5, d['top']-h-0.5, w+1, 0, (w+1) / (h+1)) )

    def __call__( self, **kw ):
        msg = []
        set_camera( self.camera )
        if self.debug:
            for i in range(self.size):
                msg.append( black.interp( red, kw['color'+str(i)] ) )
                msg.append( self.texts[i] )
        else:
            for i in range(self.size):
                msg.append( kw['color'+str(i)] )
                msg.append( self.texts[i] )
        text( 0, 0, msg, thefont, size = 1, anchor = 'nw' )

