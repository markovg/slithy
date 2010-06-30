from slithy.library import *

import facets

import slithy.slidereader as slidereader
images = slidereader.image_library['default']
fonts = slidereader.font_library['default']

lgreen = Color( 0.3, 0.6, 0.3 )

import common

# interaction which spins the drawable 
class spin(Controller):
    def create_objects( self ):
        self.d = Drawable( None, facets.facets, _alpha = 0.0 )
        return self.d

    def start( self ):
        fade_in( 0.5, self.d )
        Undulation(style='sawup')(self.d.theta,min=0.0,max=360.0,period=6.0)



def title2_anim():

    facets_cam = get_camera().bottom(0.5).left(0.33).inset(0.05)
    d = Interactive( facets_cam,
                      controller = spin)


    cap = Text( facets_cam.inset(0.1).bottom(0.2),
                color = white, font = fonts['facets'], size = 10, _alpha = 1.0,
                justify = 0.5, text='www.facets-project.org')

    title_cam = get_camera().top(0.5).bottom(0.65).inset(0.05)

    author_cam = get_camera().top(0.7).bottom(0.3).inset(0.1)


    cap1 = Text( title_cam,
                color = yellow, font = fonts['title'], size = 25, _alpha = 1.0,
                justify = 0.5, text=['Working with Neuroscience Ontologies Using ',fonts['facets'] ,'rdflib'])

    cap2 = Text( author_cam,
                color = white, font = fonts['title'], size = 16, _alpha = 1.0,
                justify = 0.5, text="Eilif Muller")


    neo_cam = get_camera().bottom(0.5).right(0.33).inset(0.05)
    bbp_cam = get_camera().bottom(0.5).right(0.66).left(0.5).inset(0.2)

    im1 = Image( neo_cam, image = images['neo_light'],_alpha=1)
    #im2 = Image( get_camera(), image = images['title_back'],_alpha=1)
    im3 = Image( bbp_cam, image = images['bbp'],_alpha=1)


    start_animation( common.bg,d,cap,cap1,cap2, im1, im3)


  
    #pause()
    
    return end_animation() 

title2_anim = title2_anim()



test_objects( title2_anim )
