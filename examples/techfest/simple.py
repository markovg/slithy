from slithy.library import *
from images import KenBurns, ScalarTuple
resources = {
    'image0000' : load_image( 'simple_files/aaanskri.jpg' ),
    'image0001' : load_image( 'simple_files/lbjukcop.jpg' ),
    'image0002' : load_image( 'simple_files/zdmxeljx.jpg' ),
    'image0003' : load_image( 'simple_files/cprdedqe.jpg' ),
}
def slideshow():
    kb = KenBurns( get_camera().restrict_aspect( 1.3333 ).inset( 0.05 ) )
    start_animation( Fill(color=white), kb )
    kb.appear( resources['image0000'], ScalarTuple((0.4143, 0.3191, 0.9854, 0.9640)) )
    pause()
    kb.pan( ScalarTuple((0.1093, 0.0163, 0.9429, 0.9577)), duration = 6.5000 )
    pause()
    kb.crossfade( resources['image0001'], ScalarTuple((0.0320, 0.0000, 0.9175, 1.0000)), ScalarTuple((0.9175, 0.0000, 1.8029, 1.0000)), duration = 2.1000 )
    wait( 2.0 )
    pause()
    kb.crossfade( resources['image0002'], ScalarTuple((0.0000, 0.0108, 0.8759, 1.0000)), ScalarTuple((-0.8759, 0.0108, 0.0000, 1.0000)), duration = 2.1000 )
    pause()
    kb.pan( ScalarTuple((0.4875, 0.0000, 1.0000, 0.5789)), duration = 4.5000 )
    pause()
    kb.crossfade( resources['image0003'], ScalarTuple((0.1330, 0.0208, 1.0000, 1.0000)), duration = 3.2000 )
    pause()
    return end_animation()
slideshow = slideshow()
slideshow_one = slideshow[0].anim
test_objects( slideshow )
##
# image0000 c2ltcGxlX2ZpbGVzL2FhYW5za3JpLmpwZw== MDIxMjA3LTE0MzQzOC0yMzcuanBn
# image0001 c2ltcGxlX2ZpbGVzL2xianVrY29wLmpwZw== MDIxMjA4LTA5NTQ1OS0wNzEuanBn
# image0002 c2ltcGxlX2ZpbGVzL3pkbXhlbGp4LmpwZw== MDIxMjA4LTA5NDM0Ni0wNTIuanBn
# image0003 c2ltcGxlX2ZpbGVzL2NwcmRlZHFlLmpwZw== MDIxMjA3LTE0MDY0Ny0yMDQuanBn
##
# image appear image0000 0.1000 0.4143 0.3191 0.9854 0.9640
# image pan image0000 6.5000 0.1093 0.0163 0.9429 0.9577
# image fade_right image0001 2.1000 0.0320 0.0000 0.9175 1.0000
# image fade_left image0002 2.1000 0.0000 0.0108 0.8759 1.0000
# image pan image0002 4.5000 0.4875 0.0000 1.0000 0.5789
# image crossfade image0003 3.2000 0.1330 0.0208 1.0000 1.0000
##
