import Image
import JpegImagePlugin
import PngImagePlugin
Image._initialized = 1


from slithy.presentation import *



import powerpoint
import iteration
import morehint
import authoring
import system
import many
import common
import bezier

bookmark( 'start' )
play( powerpoint.title )
pause()
play( powerpoint.powerpoint )
pause()
play( powerpoint.pythagorases )
bookmark( 'hinting' )
play( morehint.character_animation )
bookmark( 'authoring principles' )
play( iteration.iteration1 )
play( authoring.authoring_principles )
play( many.two_by_two )
bookmark( 'slithy' )
play( system.show_parameterized_diagram )
pause()
play( system.show_animation )
play( system.interactive_animation )
bookmark( 'bezier demo' )
play( bezier.bezier_anim )
bookmark( 'finale' )
play( many.three_by_three )

bookmark( 'animation principles' )
play( iteration.iteration2 )
play( morehint.demo1 )
play( morehint.demo2 )
play( morehint.demo3 )
play( morehint.demo4 )
play( morehint.demo5 )
play( morehint.demo6 )
play( morehint.demo7 )
play( morehint.demo8 )
play( common.to_black )



run_presentation()

