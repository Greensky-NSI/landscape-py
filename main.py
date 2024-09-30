from p5 import *
from custom_types import *
from modules.cloud import cloud

from modules.ferme import Ferme
from modules.fleur import draw_fleur
from modules.mouton import mouton
from modules.papillon import papillon
from modules.river import river
from modules.vache import vache
from modules.wheat import wheat_field
from modules.nuit import etoiles, journuit
from modules.tree import tree
from utils.assertions import increase_color
from utils.globals import variables
from modules.rocher import rock


# Code with p5 python
def setup():
    size(variables["WIDTH"], variables["HEIGHT"])
    background(0)

# Draw
def draw():
    journuit()
    background(variables["fond"])

    if variables["fond"] == 45:
        etoiles(200, variables["liste_etoiles"])

    # Ferme
    rock(207, 282, .4)
    Ferme(200, 150, 200, 150, (139, 0, 0), (165, 42, 42), (165, 42, 42), 270, 230, 60, 70, (245, 245, 220), 220,
              180, 40, 40)

    # Arbres sur le côté gauche
    tree(x = 10, y=300, leaf_color_variation=5, tree_size=.6)
    tree(x = 0, y = 350, leaf_color_variation=3, tree_size=.55, leaf_color=increase_color((0, 128, 0), -20), trunc_color=increase_color((139, 69, 19), -10))
    tree(x = 80, y = 365, leaf_color_variation=10, tree_size=.67, trunc_color=increase_color((139, 69, 19), 15))
    tree(x = 35, y = 380, tree_size=.5, leaf_color_variation=2)
    rock(100, 400, .8)
    tree(x = 3, y= 480, leaf_color_variation=1, tree_size=.62)

    # Rivière
    river(top_left=480, bottom_left=560, top_right = 200, bottom_right=300)

    # Champ de blé
    wheat_field(x = 550, y = 400, width=300, height=200, maximum_wheat=30, wheat_size=.8)
    rock(495, 590, 0.8)

    # Animaux
    ## Vache
    vache(.5, 312, 100)
    vache(.46, 455, 92)
    vache(.44, 400, 180)

    ## Mouton
    mouton(320, 340, .5)

    ## Papillon
    papillon(.2, 700, 200, (127, 123, 98), increase_color((127, 123, 98), 30))
    papillon(.2, 100, 200, (98, 201, 57), increase_color((98, 201, 57), 41), (0, 0, 0), 2)


    # Fleurs
    draw_fleur(510, 500, 10, 5, (255, 192, 203), (255, 105, 180))
    draw_fleur(112, 466, 8, 6, increase_color((255, 192, 203), -10), increase_color((255, 105, 180), -70))
    draw_fleur(184, 248, 9, 5, increase_color((205, 133, 63), 20), increase_color((255, 105, 180), -100))


    # Nuages
    cloud(x = 572, y = 33, cloud_size=.4, cloud_color=(242, 240, 244), color_variation=0)
    cloud(x = 30, y = 42, cloud_size=.2, cloud_color=(240, 237, 241), color_variation=1, cloud_color_variation_mode="maximum", repeat_distance=.3)

run()