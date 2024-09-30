from p5 import *
from typing import Tuple, List, Union

from modules.nuit import etoiles, journuit
from modules.papillon import papillon

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

# Variables globales
fond: int = 255
nb_etoiles: int = 0
liste_etoiles: List[int] = []

# Draw
def draw():
    global fond, liste_etoiles

    journuit()
    background(fond)

    if fond == 45:
        etoiles(200, liste_etoiles)


    # river(top_left=100, top_right=150, bottom_left=200, bottom_right=180)
    # cloud(x = WIDTH // 2, y = HEIGHT // 2, scalar=95, cloud_size=.5, repeat_distance=.31, color_variation=5, cloud_color=(150, 150, 150))
    # tree(x=WIDTH // 2, y=HEIGHT, cloud_size=1.5)

    # wheat_field(x = 200, y = 200, width = 400, height = 300, wheat_size = .8)

    # Ferme(200, 150, 200, 150,'red','brown','brown',270, 230, 60, 70,'white',220, 180, 40, 40)

    # vache(1, 100, 100)
    papillon(1, 100, 100)

run()