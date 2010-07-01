
# export PYTHONPATH=$PYTHONPATH:$HOME/theway/project/slithy

from slithy.presentation import *
#from slithy.library import test_objects

# new slide reader
import slithy.slidereader as slidereader
from slithy.slidereader import load_env, include_slides, imagefiles_to_images

# load the image and font environments
#load_env('globals.yaml')

# Parse images in directories instead of in globals
imagefiles_to_images('images/*')

# include slide content
include_slides('content.yaml')

run_presentation()


