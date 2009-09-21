""" Slithy standard fonts library in slithy.fonts.fonts dict """

from slithy.library import *
import slithy
import os



fontpath.append( os.path.join(slithy.__path__[0],'fonts') )
add_extra_characters( u'\u201c\u201d' )

fonts = { 'times' : search_font( 'times.slf' ),
          'ehrhardt' : search_font( 'ehrhardt.slf' ),
          'body' : search_font( 'minion.slf' ),
          'bodyi' : search_font( 'minion_i.slf' ),
          'title' : search_font('myriad_b.slf'),
          'titlei' : search_font('myriad_bi.slf'),
          'roman' : search_font('myriad.slf'),
          'mono'  : search_font('courier_b.slf'),
          'dingbats' : search_font('wingding.slf' ),
          'georgia_b' : search_font('georgia_b.slf' )
          }
