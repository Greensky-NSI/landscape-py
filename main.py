from p5 import *

from utils import globals
from modules.nuit import etoiles, journuit

WIDTH = 800
HEIGHT = 600

# Code with p5 python
def setup():
    size(WIDTH, HEIGHT)
    background(0)

# Draw
def draw():
    journuit()
    background(globals.fond)

    if globals.fond == 45:
        etoiles(200, globals.liste_etoiles)


run()