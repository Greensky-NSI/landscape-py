from random import randint

from p5 import fill, ellipse

from utils.globals import variables
from custom_types import *

def etoiles(cielH, liste_etoiles_):
    while len(liste_etoiles_) < variables["nb_etoiles"]:
        x=randint(0,800)
        y=randint(0,cielH)

        liste_etoiles_.append((x, y))

    for x, y in liste_etoiles_:
        fill(255)
        ellipse(x,y,5,5)


def journuit():
    if key_is_pressed:
        if key == 'N' and variables["fond"][0] == variables["default_fond"][0]:
            variables["fond"] = (45, 45, 45)
            variables["nb_etoiles"] = randint(0, 100)
            variables["liste_etoiles"] = []
        elif key == 'J' and variables["fond"][0] == 45:
            variables["fond"] = variables["default_fond"]
