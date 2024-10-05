import math

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
from utils.assertions import increase_color, parse_color, safe_fill
from utils.constants import wheat_cobs_default_color, wheat_stem_default_color
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

    # Calculs sur la seed
    seed_sum = sum([int(i) for i in variables["seed"]])

    # Création de la prairie en fond
    prairie_color_increaser = int(variables["seed"][int(variables["seed"][2])])

    safe_fill(increase_color((20, 150, 20), prairie_color_increaser))
    rect(0, variables["HEIGHT"] // 2, variables["WIDTH"], variables["HEIGHT"] // 2)

    # Calculation de la couleur des rochers
    base_rock_color = int(variables["seed"][-1]) * 10 ** 2 + int(variables["seed"][5]) + floor(cos(seed_sum) * 20)

    # Ferme
    rock(207, 282, .4, increase_color((180, 180, 180), base_rock_color, mode="modulo"), increase_color((150, 150, 150), base_rock_color, mode="modulo"))

    ## Teinte de la ferme
    ferme_teint = parse_color((int(variables["seed"][0:2]), int(variables["seed"][3:5]), int(variables["seed"][6:8])), mode="modulo")
    first_increaser_ferme = (int(variables["seed"][9]) + 50) * 2
    second_increaser_ferme = (int(variables["seed"][10]) + 30) * 2

    Ferme(200, 150, 200, 150, ferme_teint, ferme_teint, increase_color(ferme_teint, second_increaser_ferme, mode="modulo"), 270, 230, 60, 70, increase_color(ferme_teint, first_increaser_ferme, mode="modulo"), 220,
              180, 40, 40)

    # Arbres sur le côté gauche
    ## Récupération de la couleur des arbres selon la seed:
    base_tree_color_variation = int(variables["seed"][-1]) * 10 + int(variables["seed"][-2])
    base_tree_color = floor(log(int(variables["seed"][0:8])))

    tree(x = 10, y=300, leaf_color_variation=base_tree_color_variation + 5, tree_size=.6, leaf_color=increase_color((0, 128, 0), base_tree_color))
    tree(x = 0, y = 350, leaf_color_variation=base_tree_color_variation + 3, tree_size=.55, leaf_color=increase_color((0, 128, 0), base_tree_color - 20), trunc_color=increase_color((139, 69, 19), -10))
    tree(x = 80, y = 365, leaf_color_variation=base_tree_color_variation+ 10, tree_size=.67, trunc_color=increase_color((139, 69, 19), 15))
    tree(x = 35, y = 380, tree_size=.5, leaf_color_variation= base_tree_color_variation + 2)
    rock(100, 400, .8, increase_color((180, 180, 180), base_rock_color, mode="modulo"), increase_color((150, 150, 150), base_rock_color, mode="modulo"))
    tree(x = 3, y= 480, leaf_color_variation= base_tree_color_variation + 1, tree_size=.62)

    # Rivière
    ## Récupération de la couleur de la rivière selon la seed:
    base_river_color = floor(log(int(variables["seed"][2:16]), 2)) * (int(variables["seed"][0]) + 3)
    river(top_left=480, bottom_left=560, top_right = 200, bottom_right=300, river_color=increase_color((0, 0, 140), base_river_color, mode="modulo"))

    # Champ de blé
    ## Récupération de la couleur du blé selon la seed:
    base_wheat_color = floor(log(int(variables["seed"][0:8]), math.e)) * (int(variables["seed"][0]) + 3)

    wheat_field(x = 550, y = 400, width=300, height=200, maximum_wheat=30, wheat_size=.8, cobs_color=increase_color(wheat_cobs_default_color, base_wheat_color, mode="modulo"), stem_color=increase_color(wheat_stem_default_color, base_wheat_color, mode="modulo"))
    rock(495, 590, 0.8, increase_color((180, 180, 180), base_rock_color, mode="modulo"), increase_color((150, 150, 150), base_rock_color, mode="modulo"))

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
    flowers_color_increaser = floor(1.2 ** seed_sum)

    draw_fleur(510, 500, 10, 5, increase_color((255, 192, 203), flowers_color_increaser, mode="modulo"), increase_color((255, 105, 180), flowers_color_increaser, mode="modulo"))
    draw_fleur(112, 466, 8, 6, increase_color((255, 192, 203), -10 + flowers_color_increaser, mode="modulo"), increase_color((255, 105, 180), -70 + flowers_color_increaser, mode="modulo"))
    draw_fleur(184, 248, 9, 5, increase_color((205, 133, 63), 20 + flowers_color_increaser, mode="modulo"), increase_color((255, 105, 180), -100 + flowers_color_increaser, mode="modulo"))


    # Nuages
    cloud_variation = abs(floor(sin(int(variables["seed"][5:12])) * 10))
    cloud_decreaser = floor(log(int(variables["seed"][:])))

    cloud(x = 572, y = 33, cloud_size=.4, cloud_color=increase_color((242, 240, 244), -cloud_decreaser, mode="modulo"), color_variation=cloud_variation)
    cloud(x = 30, y = 42, cloud_size=.2, cloud_color=increase_color((240, 237, 241), -cloud_decreaser, mode="modulo"), color_variation=cloud_variation, cloud_color_variation_mode="maximum", repeat_distance=.3)

run()