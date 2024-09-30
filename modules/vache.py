from p5 import translate, scale, rect, ellipse, triangle

from utils.assertions import safe_fill
from utils.utils import assert_color

def vache(taille, pos_x, pos_y, couleur_corps=(255, 255, 255), couleur_tete=(255, 255, 255), couleur_yeux=(0, 0, 0),
          couleur_museau=(255, 192, 203), couleur_nez=(0, 0, 0), couleur_cornes=(160, 160, 1600), couleur_pattes=(255, 255, 255),
          couleur_taches=(0, 0, 0)):
    """
    Dessine une vache à l'écran avec les paramètres donnés

    :param taille: int - L'échelle de la vache
    :param pos_x: int - La position x de la vache
    :param pos_y: int - La position y de la vache
    :param couleur_corps: color_type - La couleur du corps de la vache
    :param couleur_tete: color_type - La couleur de la tête de la vache
    :param couleur_yeux: color_type - La couleur des yeux de la vache
    :param couleur_museau: color_type - La couleur du museau de la vache
    :param couleur_nez: color_type - La couleur du nez de la vache
    :param couleur_cornes: color_type - La couleur des cornes de la vache
    :param couleur_pattes: color_type - La couleur des pattes de la vache
    :param couleur_taches: color_type - La couleur des taches de la vache

    :return: None
    """

    # Assertions
    assert isinstance(taille, int) or isinstance(taille, float), "taille doit être un entier ou un réel"
    assert isinstance(pos_x, int), "pos_x doit être un entier"
    assert isinstance(pos_y, int), "pos_y doit être un entier"
    assert assert_color(couleur_corps), "couleur_corps doit être un tuple de 3 entiers."
    assert assert_color(couleur_tete), "couleur_tete doit être un tuple de 3 entiers."
    assert assert_color(couleur_yeux), "couleur_yeux doit être un tuple de 3 entiers."
    assert assert_color(couleur_museau), "couleur_museau doit être un tuple de 3 entiers."
    assert assert_color(couleur_nez), "couleur_nez doit être un tuple de 3 entiers."
    assert assert_color(couleur_cornes), "couleur_cornes doit être un tuple de 3 entiers."
    assert assert_color(couleur_pattes), "couleur_pattes doit être un tuple de 3 entiers."
    assert assert_color(couleur_taches), "couleur_taches doit être un tuple de 3 entiers."

    # Dessin de la vache
    translate(pos_x, pos_y)
    scale(taille)

    safe_fill(couleur_corps)    #corps
    rect(150, 200, 150, 100)

    safe_fill(couleur_tete)     #tête
    ellipse(270, 170, 60, 60)

    safe_fill(couleur_yeux)  #yeux
    ellipse(285, 150, 10, 10)

    safe_fill(couleur_museau)     #museau
    ellipse(295, 175, 40, 20)

    safe_fill(couleur_nez)                              #nez
    ellipse(299, 179, 10, 10)

    safe_fill(couleur_cornes)        #cornes
    triangle(260, 140, 280, 140, 260, 120)
    triangle(245, 150, 245, 125, 265, 138)

    safe_fill(couleur_pattes)     # pattes
    rect(165, 300, 20, 50)
    rect(265, 300, 20, 50)

    safe_fill(couleur_taches)                 #Taches sur le corps
    ellipse(180, 230, 30, 30)
    ellipse(220, 240, 30, 30)
    ellipse(200, 270, 30, 30)
    ellipse(260, 270, 30, 30)
    ellipse(280, 230, 30, 30)

    scale(1/taille)
    translate(-pos_x, -pos_y)
