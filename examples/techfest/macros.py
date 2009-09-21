from slithy.library import *

_fontdir = None
_colordir = None
_fade_interval = 0.5

def _plain_rectangle():
    color( 0.8, 0, 0.6, 0.4 )
    rectangle( visible(), se = (0, 0, 1, 0.4), nw = (1, 1, 0, 0.4), ne = Color(green, 0.4) )

def set_styles( **kw ):
    global _fontdir, _colordir, _fade_interval
    _fontdir = kw.get( "fonts", _fontdir )
    _colordir = kw.get( "colors", _colordir )
    _fade_interval = kw.get( "fade_interval", _fade_interval )

def add_title( text, fade = 0 ):
    size = get_camera().height() / 12
    r = get_camera().top( 0.2 ).bottom( 0.85 )
    r = r.inset( 0.05 )
    tx = Text( r, text = text, font = _fontdir['title'], size = size, justify = 0.0,
               _alpha = not fade, color = _colordir['title'] )
    enter( tx )
    if fade:
        fade_in( _fade_interval, tx )
    return tx

def add_bulleted_list():
    size = get_camera().height() / 15
    r = get_camera().bottom( 0.85 ).inset( 0.05 ).left(0.475)
    bl = BulletedList( r, font = _fontdir['roman'], color = _colordir['body'],
                       bullet = [_fontdir['dingbats'], 'w'],
                       size = size )
    enter( bl )

    return bl

def interp_cameralist( c, cameras ):
    if c <= 0.0:
        return cameras[0]
    elif c >= len(cameras)-1:
        return cameras[-1]

    i = int(c)
    f = c - i
    return cameras[i].interp( cameras[i+1], f )
