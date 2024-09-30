from random import randint

from p5 import fill, ellipse

from custom_types import key_is_pressed, key
from main import nb_etoiles

def etoiles(cielH, liste_etoiles_):
    while len(liste_etoiles_) < nb_etoiles:
        x=randint(0,800)
        y=randint(0,cielH)

        liste_etoiles_.append((x, y))

    for x, y in liste_etoiles_:
        fill(255)
        ellipse(x,y,5,5)


def journuit():
    global fond, nb_etoiles, liste_etoiles

    if key_is_pressed:
        if key == 'N' and fond==255:
            fond=45
            nb_etoiles = randint(0, 100)
            liste_etoiles=[]
        elif key == 'J' and fond==45:
            fond = 255
