from p5 import translate, scale, triangle, ellipse, strokeWeight, line

from utils.assertions import safe_fill
from utils.utils import assert_color

def papillon(taille, pos_x, pos_y, couleur_ailes=(255, 255, 255), couleur_corps=(255, 255, 255), couleur_antennes=(0, 0, 0),
             epaisseur_bordure=3):
    """
    Dessine un papillon à l'écran avec les paramètres donnés

    :param taille: int - L'échelle du papillon
    :param pos_x: int - La position x du papillon
    :param pos_y: int - La position y du papillon
    :param couleur_ailes: color_type - La couleur des ailes du papillon
    :param couleur_corps: color_type - La couleur du corps du papillon
    :param couleur_antennes: color_type - La couleur des antennes du papillon
    :param epaisseur_bordure: int - L'épaisseur de la bordure du papillon

    :return: None
    """

    # Assertions
    assert isinstance(taille, int) or isinstance(taille, float), "taille doit être un entier ou un réel"
    assert isinstance(pos_x, int), "pos_x doit être un entier"
    assert isinstance(pos_y, int), "pos_y doit être un entier"
    assert assert_color(couleur_ailes), "couleur_ailes doit être un tuple de 3 entiers."
    assert assert_color(couleur_corps), "couleur_corps doit être un tuple de 3 entiers."
    assert assert_color(couleur_antennes), "couleur_antennes doit être un tuple de 3 entiers."
    assert isinstance(epaisseur_bordure, int) and epaisseur_bordure >= 0, "epaisseur_bordure doit être un entier naturel"

    # Dessin du papillon
    translate(pos_x, pos_y)
    scale(taille)

    safe_fill(couleur_ailes)
    triangle(110, 235, 200, 180, 200, 270) # aile gauche
    triangle(90, 150, 180, 150, 180, 250)

    triangle(290, 235, 200, 180, 200, 270) #aile droite
    triangle(310, 150, 210, 150, 210, 260)

    safe_fill(couleur_corps)  #corps
    ellipse(200, 200, 50, 150)

    safe_fill(couleur_antennes)  #antennes
    strokeWeight(epaisseur_bordure)
    line(160, 90, 190, 130)
    line(240, 90, 210, 130)

    scale(1/taille)
    translate(-pos_x, -pos_y)
