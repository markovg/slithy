
from slithy.library import *


gradient = Fill( style = 'horz', color2 = black, color = Color(0,0,0.5) )
white = Fill( color = white )
black = Fill( color = black )

# set default background
bg = black


# cameras:
class cam:
    pass

cam.body = get_camera().bottom(0.85)
cam.title = get_camera().top(0.10)
