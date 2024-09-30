from p5 import *
from typing import Tuple, List, Union

import globals
from modules.nuit import etoiles, journuit

WIDTH = 800
HEIGHT = 600

# Code with p5 python
def setup():
    size(WIDTH, HEIGHT)
    background(0)

# Types
color_type = Union[Tuple[int, int, int], Tuple[int, int, int, int]]
positions_list = List[Tuple[int, int]]

# Constantes
wheat_stem_default_color: color_type = (200, 150, 50)
wheat_cobs_default_color: color_type = (255, 205, 105)

# Draw
def draw():
    journuit()
    background(globals.fond)

    if globals.fond == 45:
        etoiles(200, globals.liste_etoiles)


run()