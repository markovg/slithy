
import yaml

import slithy
import slithy.presentation as presenter
import slithy.library as sylib
import slithy.fonts

import common

import os

import slithy.diaimage as diaimage

import slithy.movie as movie

#this has to be configure by the user by load_env
image_library = {'default':{},'pdf':{},'svg':{},'image_files':{}}
font_library = {'default':slithy.fonts.fonts}
rst_config = {'rst_default_style':os.path.join(slithy.__path__[0],'rst2pdf_default.style')}


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

    if 'rst_config' in env:
        rst_config.update(env['rst_config'])



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
            
        if 'bg' in slide:
            background=slide['bg']

        if 'pdf' in slide and 'slides' in slide:
            images = pdf2ppm_cache(slide['pdf'],slide['slides'])
            p.play(load_image_slides(images,library='pdf',background=background, content=slide.get('content',None)))
            p.pause()
        elif 'svg' in slide:
            images = svg2png_cache(slide['svg'])
            p.play(load_image_slides(images,library='svg',background=background, content=slide.get('content',None)))
            p.pause()
        elif 'image_files' in slide:
            images = imagefiles_to_images(slide['image_files'])
            p.play(load_image_slides(images,library='image_files',background=background, content=slide.get('content',None)))
            p.pause()

        elif 'slideshow' in slide:
            images = imagefiles_to_images(slide['slideshow'])
            slideshow_anim = images_slideshow(images,
                                              library='image_files',
                                              background=background,
                                              delay=slide.get('delay',2.0),
                                              repeat=slide.get('repeat',1),
                                              fade_time=slide.get('fade_time',0.5))


            p.play(slideshow_anim)
            p.pause()

            
        elif 'images' in slide:
            if 'library' in slide:
                lib = slide['library']
            else:
                lib = 'default'
            p.play(load_image_slides(slide['images'],library=lib, background=background,
                                     content=slide.get('content',None)))
            p.pause()

        elif 'rst' in slide:
            images = rst2ppm_cache(i,slide.get('title',''),slide['rst'],slide.get('rst_style'))
            p.play(load_image_slides(images,library='pdf',
                                     background=background,content=slide.get('content',None)))
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
    ns['common'] = common

    return ns


def load_slide_content(content):
    """ returns the slide animation """
    import traceback,sys

    # get a clean slate
    ns = clean_slate()

    try:
        exec content in ns
    except Exception,e:
        print "Exception in user code:"
        print 'v'*60
        for i,line in enumerate(content.split('\n')):
            print "%d: %s" % (i+1,line)
        print '^'*60
        traceback.print_exc(file=sys.stdout)
        print '-'*60
        raise e
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

    import os.path
    import time

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

        # skip if cache exists and newer than pdf
        if os.path.exists(target_file) and os.path.getmtime(filename)<os.path.getmtime(target_file):
           print target_file," exists.  Skipping." 
        else:
            # remove target cuz otherwise
            # erroneous pdf2ppmnumbering is not caught below
            if os.path.exists(target_file):
                os.remove(target_file)
            final_cmd = cmd % (slide,slide)
            print final_cmd
            os.system(final_cmd)
            # fix problem with slides <10 coming out with 1 instead of 01 for slide # in filename 
            if not os.path.exists(target_file):
                print "Caught - pdf2ppm bad slide filename numbering"
                print "Expected %s" % target_file
                err_target_file = gen_err_ppm_name(cache_dir,pdf_name,slide)
                print "Erroneously as %s" % err_target_file
                os.rename(err_target_file, target_file)

            if not os.path.exists(target_file):
                raise RuntimeError, "problem getting expected slide file on pdf conversion"
                
                

        img = diaimage.get_image(target_file)
        print 'target_file: ', img
        image_library['pdf'][target_file] = img 
        images.append(target_file)
            
    return images


def svg2png_cache(svgs,library='svg'):

    width,height = 800,600

    cmd = "inkscape -w "+str(width)+" -h "+str(height)+" -e %s %s"

    images = []

    if type(svgs) == type(''):
        svgs = [svgs]
    
    for svg in svgs:
        

        # get only trailing pdf name
        svg_name = os.path.split(svg)[-1]

        # cache dir in image dir
        cache_dir = os.path.join(os.path.dirname(svg),'.svgcache')
        if not cache_dir in sylib.fontpath:
            sylib.fontpath.append(cache_dir)

        setup_cachedir(cache_dir)

        target_file = os.path.join(cache_dir,svg_name+'.png')
        if os.path.exists(target_file) and os.path.getmtime(svg)<os.path.getmtime(target_file):
           print target_file," exists and uptodate.  Skipping." 
        else:
            final_cmd = cmd % (target_file,svg)
            print final_cmd
            os.system(final_cmd)

        img = diaimage.get_image(target_file)
        print 'target_file: ', img
        image_library[library][target_file] = img 
        images.append(target_file)
            
    return images


def imagefiles_to_images(image_files):

    from glob import glob

    # list of images to fill and return
    images = []
    
    # if user sent 1 string instead of list
    if type(image_files)==str:
        image_files = [image_files]

    for wildcard in image_files:
        files = glob(wildcard)
        files.sort()

        for filename in files:

            img_dir = os.path.dirname(filename)

            ext = os.path.splitext(filename)
            
            # handle svgs
            
            if ext[-1]=='.svg':
                # replace filename with cached png of svg
                print "SVG: %s", filename
                filename = svg2png_cache(filename,library='image_files')[0]

            # add dir to image search path
            if not img_dir in sylib.fontpath:
                sylib.fontpath.append(img_dir)

            # get only trailing image name
            #img_name = os.path.basename(filename)

            print 'target_file: %s' % (filename,),
            img = diaimage.get_image(filename)
            print img
            image_library['image_files'][filename] = img 
            images.append(filename)
            
    return images



def rst2pdf(rst_file, pdf_file, style_file):
    # rst2pdf slides.rst -b1 -s slides.style

    cmd = "rst2pdf %s --fit-background-mode=scale -b1 -o %s -s %s" % (rst_file, pdf_file, style_file)
    print cmd

    os.system(cmd)
    

def parse_latex_opts(f):
    """ f is something like:
    '@ltx[repl=hello;align=center;scale=60%]@foo@ltx@'
    returns {'repl':'hello', 'align':"center,top", "scale":"60%"}"""

    # remove first '@ltx'
    op_str = f[4:]

    # get uptil first @
    op_str = op_str.split('@')[0]

    # case of no options
    if op_str=='':
        return {}

    # remove []
    assert op_str[0]=="["
    assert op_str[-1]=="]"
    op_str = op_str[1:-1]

    d = {}
    for x in op_str.split(','):
        key,val = map(str.strip,x.split('='))
        d[key] = val
    
    return d

    
    


def process_latex(rst_content, math_dir, prefix):
    """ Find @ltx@ eqn @ltx@ tokens, cut out the
    eqns, feed 'em to latexmath2pdf
    in the math_dir, and
    insert the files back into rst_content
    as images

    math_dir is typically './.slithy_rstcache/slideX/
    """
    
    import re, os
    import latexmath2pdf
    

    ltx_token = "@ltx@"
    ltx_head = "@ltx.*?@"
    p_ltx = re.compile(ltx_head+"(.*?)"+ltx_token,re.S)
    result = rst_content
    for i,f in enumerate(p_ltx.finditer(rst_content)):
        eqn = f.group(1)
        f = f.group()
        opts = parse_latex_opts(f)
        if 'align' not in opts:
            opts['align']='center'
        if 'scale' not in opts:
            opts['scale'] = '160%%'
        if 'repl' in opts:
            repl = opts['repl']
            del opts['repl']
            # align center -> align middle for repl
            if opts['align']=='center':
                opts['align']='middle'
                
        else:
            repl = None
        opts_str = "\n".join(["   :%s: %s" % (k,v) for k,v in opts.iteritems()])
        # size=1 is hard-coded for now.
        if repl==None:
            # use pdf, repl does not support pdf
            latexmath2pdf.math2img(eqn,math_dir,prefix=prefix,num=i,size=1,fmt='pdf')
            # filename of rendered pdf in rst
            #fn = os.path.join(math_dir, "%s%.4d.pdf" % (prefix,i))
            fn = "%s%.4d.pdf" % (prefix,i)
            replace = ".. image:: %s\n%s" % (fn,opts_str)
        else:
            latexmath2pdf.math2img(eqn,math_dir,prefix=prefix,num=i,size=0.4,fmt='png')
            fn = "%s%.4d.png" % (prefix,i)
            replace = ".. |%s| image:: %s\n%s" % (repl,fn,opts_str)
        
        result = result.replace(f,replace)

    return result


def rst2ppm_cache(slide_num,slide_title, rst_content, style_file=None):

    if not style_file:
        style_file = rst_config['rst_default_style']

    # directory for caching rst files, etc
    cache_dir = './.slithy_rstcache'
    if not cache_dir in sylib.fontpath:
        sylib.fontpath.append(cache_dir)

    setup_cachedir(cache_dir)

    # rst target filename
    base_filename = 'slide%d' % slide_num

    # clear white space
    slide_title = slide_title.strip()
    
    # len of title for rst underline
    underline = '-'*len(slide_title)

    slide_template = """
%(title)s
%(underline)s

%(content)s
"""
    
    slide_text_ltx = slide_template % {'title':slide_title, 'underline':underline,'content':rst_content}

    rst_target = os.path.join(cache_dir, base_filename+'.rst')
    rst_target_ltx = os.path.join(cache_dir, base_filename+'.rst_ltx')
    pdf_target = os.path.join(cache_dir, base_filename+'.pdf')

    def write_rst():
        # write rst_ltx
        f = file(rst_target_ltx,'w')
        f.write(slide_text_ltx)
        f.close()

        # Process math expressions
        setup_cachedir(os.path.join(cache_dir,base_filename))
        if '@ltx@' in slide_text_ltx:
            slide_text = process_latex(slide_text_ltx,cache_dir,prefix=os.path.join(base_filename,"ltx_"))
        else:
            slide_text = slide_text_ltx
        #slide_text = slide_template % {'title':slide_title, 'underline':underline,'content':rst_content}
        # write new content
        f = file(rst_target,'w')
        f.write(slide_text)
        f.close()
    
    # logic below to set changed to False 
    # if pdf doesn't need updating
    changed = True
    # check if rst_ltx content file differs from slide_text.
    if os.path.exists(rst_target_ltx):
        f = file(rst_target_ltx,'r')
        old_slide_text_ltx = f.read()
        f.close()

        if old_slide_text_ltx==slide_text_ltx:
            changed = False
        else:
            # write new content
            write_rst()
    else:
        # write rst ... it doesn't exists
        write_rst()

    # if somehow pdf is missing, force generate
    if not os.path.exists(pdf_target):
        changed = True
    
    # generate pdf if 'changed', i.e. needs updating
    if changed:
        rst2pdf(rst_target, pdf_target, style_file)
        

    return pdf2ppm_cache(pdf_target,[1])

    



def load_image_slides(images,library='default',background='bg',content=None):
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

    # do external slithy content if any
    if content:
        exec content in ns
       
    exec "anim = end_animation()" in ns

    return ns['anim']



def images_slideshow(images,library='default',background='bg',delay=2.0,fade_time=0.5,repeat=1):
    """ returns sequence of image slides animation """
    
    # get a clean slate
    ns = clean_slate()

    exec "old_image = None" in ns
    exec "fade_time = %f" % (fade_time,) in ns
    exec "delay = %f" % (delay,) in ns

    try:
        if background is not None:
            background = common.__getattribute__(background)
    except AttributeError:
        print "Warning slidereader.py - image_slideshow: Background common.%s not defined." % background
        background=None

    if background is not None:
        ns['bg'] = background
        exec "start(bg)" in ns
    else:
        exec "start()" in ns


    cmd = """
      
new_image = Image(get_camera(), '%s', library='%s',_alpha=0.0)
enter(new_image)

fade_in(fade_time,new_image)

if old_image:
  wait(-fade_time)
  fade_out(fade_time,old_image)

wait(delay)

if old_image:
  exit(old_image)
  

old_image = new_image


"""

    for image in images*repeat:
       exec cmd % (image, library) in ns 
        
    exec "anim = end_animation()" in ns

    return ns['anim']



