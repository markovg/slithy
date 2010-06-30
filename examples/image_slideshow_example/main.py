
# export PYTHONPATH=$PYTHONPATH:$HOME/theway/project/slithy

from slithy.presentation import *
#from slithy.library import test_objects

# new slide reader
import slithy.slidereader as slidereader
from slithy.slidereader import load_env, include_slides

include_slides('content.yaml')

run_presentation()


