
import yaml

import slithy.presentation as presenter
import slithy.library as sylib
import slithy.fonts

import common

import os

import slithy.diaimage as diaimage

import slithy.movie as movie

#this has to be configure by the user by load_env
image_library = {'default':{},'pdf':{},'svg':{}}
font_library = {'default':slithy.fonts.fonts}

#from yamlclasses import *

# Use image library
class Image(sylib.Image):
    def __init__(self,  camera, image_name, library='default',**kwargs):
        sylib.Image.__init__(self,camera,image=image_library[library][image_name],**kwargs)


class Text(sylib.Text):
    def __init__(self,  camera, library='default',**kwargs):
        if 'font' in kwargs:
            font = kwargs['font']
            del kwargs['font']
            sylib.Text.__init__(self,camera,font=font_library[library][font],**kwargs)
        else:
            sylib.Text.__init__(self,camera,**kwargs)
            



def load_image_library(libs):

    global image_library
    # load image search paths
    for path in libs['path']:
        sylib.imagepath.append(path)
    
    keys = libs.keys()
    keys.remove('path')

    for lib in keys:
        d = image_library.get(lib,{})
        for img in libs[lib]:
            d[img] = sylib.search_image(libs[lib][img])

        # do not recreate dict object if it already exists
        #l = image_library.setdefault(lib,{})
        # clear it before filling
        #l.clear()
        #l.update(d)
        image_library[lib] = d



def load_font_library(libs):

    global font_library
    # load image search paths
    for path in libs['path']:
        sylib.fontpath.append(path)
    
    keys = libs.keys()
    keys.remove('path')

    for lib in keys:
        d = font_library.get(lib,{})
        for fnt in libs[lib]:
            d[fnt] = sylib.search_font(libs[lib][fnt])
        #font_library[lib] = d
        font_library[lib] = d



def load_env(filename):

    env = yaml.load(file(filename))

    if 'image_library' in env:
        load_image_library(env['image_library'])

    if 'font_library' in env:
        load_font_library(env['font_library'])



def include_slides(filename):
    """ loads efficient yaml slide definitions as slides to be put in your main presentation definition"""
    p = presenter

    slides = yaml.load_all(file(filename)) 

    background='bg'

    for i,slide in enumerate(slides):
        if slide==None:
            continue
        if 'bookmark' in slide:
            p.bookmark(slide['bookmark'])
        elif 'title' in slide:
            p.bookmark(slide['title'])
        elif 'bmark' in slide:
            p.bookmark(slide['bmark'])
        else:
            p.bookmark(filename+' - '+str(i))

        if 'background' in slide:
            background=slide['background']
            
        if 'pdf' in slide and 'slides' in slide:
            images = pdf2ppm_cache(slide['pdf'],slide['slides'])
            p.play(load_image_slides(images,library='pdf',background=background))
            p.pause()
        elif 'svg' in slide:
            images = svg2png_cache(slide['svg'])
            p.play(load_image_slides(images,library='svg',background=background))
            p.pause()
            
        elif 'images' in slide:
            if 'library' in slide:
                lib = slide['library']
            else:
                lib = 'default'
            p.play(load_image_slides(slide['images'],library=lib, background=background))
            p.pause()
            
                
        else:
            p.play(load_slide_content(slide['content']))
            p.pause()



def clean_slate():
    """ create a clean namespace to run the animation
    def script in."""
    from copy import copy

    ns = copy(sylib.__dict__)
    ns['Image'] = Image
    ns['fonts'] = font_library['default']
    ns['start'] = ns['start_animation']
    ns['times'] = font_library['default']['times']
    ns['bg'] = common.bg
    ns['Text'] = Text
    ns['Movie'] = movie.Movie
    
    return ns


def load_slide_content(content):
    """ returns the slide animation """
    
    # get a clean slate
    ns = clean_slate()

    exec content in ns
    exec "anim = end_animation()" in ns

    return ns['anim']


def gen_ppm_name(cache_dir,filename,slide):
        return os.path.join(cache_dir,filename+'_-%.2d.ppm' % slide)

def gen_err_ppm_name(cache_dir,filename,slide):
        return os.path.join(cache_dir,filename+'_-%.1d.ppm' % slide)
    

def setup_cachedir(path):

    import os

    if os.path.exists(path):
        if os.path.isdir(path):
            return
        else:
            raise OSError, "cache dir %s exists but is not directory." % path
    else:
        os.mkdir(path)
        
    


def pdf2ppm_cache(filename,slides):

    cache_dir = './.slithy_pdfcache'
    if not cache_dir in sylib.fontpath:
        sylib.fontpath.append(cache_dir)

    setup_cachedir(cache_dir)

    # get only trailing pdf name
    pdf_name = os.path.split(filename)[-1]

    width,height = 800,600

    cmd = "pdftoppm -scale-to "+str(width)+" -H "+str(height)+" -f %d -l %d "+filename+" "+os.path.join(cache_dir,pdf_name+"_")

    images = []
    
    for slide in slides:
        
        target_file = gen_ppm_name(cache_dir,pdf_name,slide)
        if os.path.exists(target_file):
           print target_file," exists.  Skipping." 
        else:
            final_cmd = cmd % (slide,slide)
            print final_cmd
            os.system(final_cmd)
            # fix problem with slides <10 coming out with 1 instead of 01 for slide # in filename 
            if not os.path.exists(target_file):
                print "Caught - pdf2ppm bad slide filename numbering"
                err_target_file = gen_err_ppm_name(cache_dir,pdf_name,slide)
                os.rename(err_target_file, target_file)

            if not os.path.exists(target_file):
                raise RuntimeError, "problem getting expected slide file on pdf conversion"
                
                

        img = diaimage.get_image(target_file)
        print 'target_file: ', img
        image_library['pdf'][target_file] = img 
        images.append(target_file)
            
    return images


def svg2png_cache(svgs):

    cache_dir = './.slithy_svgcache'
    if not cache_dir in sylib.fontpath:
        sylib.fontpath.append(cache_dir)

    setup_cachedir(cache_dir)

    width,height = 800,600

    cmd = "inkscape -w "+str(width)+" -h "+str(height)+" -e %s %s"

    images = []

    if type(svgs) == type(''):
        svgs = [svgs]
    
    for svg in svgs:
        

        # get only trailing pdf name
        svg_name = os.path.split(svg)[-1]

        target_file = os.path.join(cache_dir,svg_name+'.png')
        if os.path.exists(target_file):
           print target_file," exists.  Skipping." 
        else:
            final_cmd = cmd % (target_file,svg)
            print final_cmd
            os.system(final_cmd)

        img = diaimage.get_image(target_file)
        print 'target_file: ', img
        image_library['svg'][target_file] = img 
        images.append(target_file)
            
    return images




def load_image_slides(images,library='default',background='bg'):
    """ returns sequence of image slides animation """
    
    # get a clean slate
    ns = clean_slate()

    exec "image = None" in ns

    try:
        if background is not None:
            background = common.__getattribute__(background)
    except AttributeError:
        print "Warning slidereader.py - load_image_slides: Background common.%s not defined." % background
        background=None

    if background is not None:
        ns['bg'] = background
        exec "start(bg)" in ns
    else:
        exec "start()" in ns


    cmd = """
if image:
  pause()
  #fade_out(0.5,image)
  #exit(image)
      
new_image = Image(get_camera(), '%s', library='%s',_alpha=1.0)
enter(new_image)
#fade_in(0.5,image)

if image:
  exit(image)

image = new_image


"""

    for image in images:
       exec cmd % (image, library) in ns 
        
    exec "anim = end_animation()" in ns

    return ns['anim']


