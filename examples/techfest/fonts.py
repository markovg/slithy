from slithy.library import *

fontpath.append( '.' )

create_slithy_fonts( ('wmr.pfb', 50, 'myriad.slf'),
                     ('wmb.pfb', 50, 'myriad_b.slf'),
                     ('wmbi.pfb', 50, 'myriad_bi.slf'),
                     ('wingding.ttf', 50, 'wingding.slf'),
                     ('courbd.ttf', 50, 'courier_b.slf'),
                     ('georgiab.ttf', 50, 'georgia_b.slf'),
                     )

myriad = search_font( 'myriad.slf' )
myriad_bold = search_font( 'myriad_b.slf' )
myriad_bolditalic = search_font( 'myriad_bi.slf' )
wingding = search_font( 'wingding.slf' )
courier_bold = search_font( 'courier_b.slf' )
georgia_bold = search_font( 'georgia_b.slf' )

fonts = { 'roman' : myriad,
          'bold' : myriad_bold,
          'bolditalic' : myriad_bolditalic,
          'title' : myriad_bold,
          'text' : myriad,
          'mono' : courier_bold,
          'dingbats' : wingding,

          'altbold' : myriad,

          'fancy' : georgia_bold,

          }

imagepath.append( '.' )

images = { #'escher' : search_image( 'escher.jpg' ),
           'yes' : search_image( 'yes.png' ),
           'no' : search_image( 'no.png' ),
           'proj' : search_image( 'projector.jpg' ),
           }
