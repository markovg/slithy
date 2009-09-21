from slithy.library import *

fontpath.append( './fonts' )
add_extra_characters( u'\u201c\u201d' )

fonts = { 'times' : search_font( 'times.slf' ),
          'ehrhardt' : search_font( 'ehrhardt.slf' ),
          'body' : search_font( 'minion.slf' ),
          'bodyi' : search_font( 'minion_i.slf' ),
          'title' : search_font('myriad_b.slf'),
          'roman' : search_font('myriad.slf'),
          'mono'  : search_font('courier_b.slf'),
          'dingbats' : search_font('wingding.slf' )
          }

