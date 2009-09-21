from slithy.library import *

#from fonts import fonts
#from images import images
import slithy.slidereader as slidereader
if __name__ == '__main__':
    slidereader.load_env('globals.yaml')


images = slidereader.image_library['default']
fonts = slidereader.font_library['default']


def mozaik_diag():

    set_camera(Rect(0,0,1,0.5))

    color(white)
    text(0.5,0.35,'This is becoming known as', font = fonts['title'], size = 0.1, anchor = 'c', justify = 0.5)

    
    text(0.5,0.15,[yellow,'M',red,'o',green,'z',white,'a',purple,'i',blue,'k'], font = fonts['title'], size = 0.15, anchor = 'c', justify = 0.5)




import common


def mozaik_def_anim():

    d = Drawable( get_camera().top(0.4), mozaik_diag, _alpha = 0.0 )

    bl = BulletedList( get_camera().bottom(0.6),
                     font = fonts['title'], color = yellow,
                     bullet = [fonts['dingbats'], 'w'], size = 22, _alpha = 1.0 )

    start_animation(common.bg, d, bl)

    fade_in(1.0,d)

    pause()

    bl.add_item( 0, 'A component-based shared software infrastructure', 0.5 )
    pause()
    
    bl.add_item( 0, 'highly abstracted', 0.5 )

    pause()
    bl.add_item( 0, 'reusable [V1 modeling]', 0.5 )

    pause()
    bl.add_item( 0, 'necessary condition for V1 model collaboration', 0.5 )

    return end_animation()
    
mozaik_def_anim = mozaik_def_anim()


def quiz_anim():

    bl = BulletedList( get_camera().inset(0.1),
                     font = fonts['title'], color = yellow,
                     bullet = [fonts['dingbats'], ''], size = 28, _alpha = 1.0 )

    start_animation(common.bg, bl)

    bl.add_item( 0, 'Unit 1 - Pop Quiz', 0.5 )
    pause()
    bl.add_item( 1, [red,'Q:',white,'Mozaik will be implemented in which language?'], 0.5 )


    return end_animation()
    
quiz_anim = quiz_anim()



def neo_overview_anim():

    #set_camera(Rect(0,0,1.024,0.768))

    im = Image( get_camera(), image = images['neo-site'], _alpha = 0 )

    start_animation( im)

    fade_in(1.0,im)
    
    
    pause()
    r = get_camera().inset(0.14).move_left(0.24)
    get_camera_object().view(r,1.0)
    pause()
    get_camera_object().view(get_camera().move_down(0.3),1.0)

    return end_animation()


neo_overview_anim = neo_overview_anim()



def pin_overview_anim():

    #set_camera(Rect(0,0,1.024,0.768))

    im = Image( get_camera(), image = images['pin-si'], _alpha = 0 )

    start_animation( im)

    fade_in(1.0,im)
    
    
    pause()
    r = get_camera().inset(0.28).move_up(0.24)
    get_camera_object().view(r,1.0)
    #pause()
    #get_camera_object().view(get_camera().move_down(0.3),1.0)

    return end_animation()


pin_overview_anim = pin_overview_anim()



def mozaik_overview_anim():

    #set_camera(Rect(0,0,1.024,0.768))

    im1 = Image( get_camera(), image = images['visual-system'], _alpha = 0 )
    im2 = Image( get_camera(), image = images['visual-system-code'], _alpha = 0 )

    start_animation( im2,im1)
    r = get_camera().inset(0.22).move_right(0.33)
    r1 = get_camera()
    get_camera_object().view(r,0.0)

    fade_in(0.5,im1)
    #wait(-0.5)
    #fade_in(0.5,im2)
    
    pause()
    
    get_camera_object().view(r1,1.0)
    wait(-1.0)
    fade_in(1.0,im2)


    #pause()
    #get_camera_object().view(get_camera().move_down(0.3),1.0)

    return end_animation()


mozaik_overview_anim = mozaik_overview_anim()




def quiz_anim():

    bl = BulletedList( get_camera().inset(0.1),
                     font = fonts['title'], color = yellow,
                     bullet = [fonts['dingbats'], ''], size = 28, _alpha = 1.0 )

    start_animation(common.bg, bl)

    bl.add_item( 0, 'Unit 1 - Pop Quiz', 0.5 )
    pause()
    bl.add_item( 1, [red,'Q:',white,'Mozaik will be implemented in which language?'], 0.5 )


    return end_animation()
    
quiz_anim = quiz_anim()



def neo_overview_anim():

    #set_camera(Rect(0,0,1.024,0.768))

    im = Image( get_camera(), image = images['neo-site'], _alpha = 0 )

    start_animation( im)

    fade_in(1.0,im)
    
    
    pause()
    r = get_camera().inset(0.14).move_left(0.24)
    get_camera_object().view(r,1.0)
    pause()
    get_camera_object().view(get_camera().move_down(0.3),1.0)

    return end_animation()


neo_overview_anim = neo_overview_anim()



def pin_overview_anim():

    #set_camera(Rect(0,0,1.024,0.768))

    im = Image( get_camera(), image = images['pin-si'], _alpha = 0 )

    start_animation( im)

    fade_in(1.0,im)
    
    
    pause()
    r = get_camera().inset(0.28).move_up(0.24)
    get_camera_object().view(r,1.0)
    #pause()
    #get_camera_object().view(get_camera().move_down(0.3),1.0)

    return end_animation()


pin_overview_anim = pin_overview_anim()



def prebrainon_anim():

    #set_camera(Rect(0,0,1.024,0.768))

    cap = Text( get_camera(),
                color = white,text=['How is FACETS leveraging this\n',green,'Neuroscience Software\n',yellow,'Full Monty in Python?'], font = fonts['title'], size = 30, _alpha = 0.0,
                justify = 0.5,vjustify=0.5 )

    

    start_animation( common.bg, cap)

    fade_in(1.0,cap)

    return end_animation()

prebrainon_anim = prebrainon_anim()

if __name__ == '__main__':
    #slidereader.load_end('globals.yaml')
    test_objects( neo_overview_anim, mozaik_overview_anim, pin_overview_anim )

