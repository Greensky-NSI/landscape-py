from p5 import TWO_PI, no_stroke, push_matrix, translate, rotate, ellipse, pop_matrix, rect, fill, noStroke

from utils.assertions import safe_fill
from utils.utils import assert_size_factor, assert_color


def draw_fleur(posx, posy, rayon, nb_petale, centre, petales, couleur_tige):
    """
    La fonction draw_fleur prend cinq paramètres :
    posx: La coordonnée x du centre de la fleur
    posy: La coordonnée y du centre de la fleur
    rayon: Le rayon de la fleur et des pétales
    nb_petale: Le nombre de pétales de la fleur
    petales: La couleur des pétales
    centre: La couleur du centre de la fleur
    couleur_tige: Couleur de la tige
    """
    # Assertions
    assert isinstance(posx, int), "posx doit être un entier"
    assert isinstance(posy, int), "posy doit être un entier"
    assert assert_size_factor(rayon), "rayon doit être un réel/entier et supérieur à 0"
    assert isinstance(nb_petale, int), "nb_petale doit être un entier"
    assert assert_color(centre), "centre doit être un tuple de 3 entiers."
    assert assert_color(petales), "petales doit être un tuple de 3 entiers."
    assert assert_color(couleur_tige), "couleur_tige doit être un tuple de 3 entiers."

    # Dessiner la tige
    tige(posx, posy, rayon, couleur_tige)

    # Calculer l'angle entre chaque pétale
    angle = TWO_PI / nb_petale
    safe_fill(petales)  # Couleur des pétales
    no_stroke()


    # Dessiner les pétales
    for i in range(nb_petale):
        push_matrix()
        translate(posx,posy)
        rotate(i * angle)
        ellipse(0, rayon, rayon, rayon* 1.5)
        translate(-posx, -posy)
        pop_matrix()

    # Dessiner le centre de la fleur
    safe_fill(centre)  # Couleur du centre
    ellipse(posx, posy, rayon, rayon )


def tige(x, y, taille, couleur):
    """
    Dessine la tige de la fleur

    :param x: Coordonnée x du milieu en haut
    :param y: Coordonnée y du milieu en haut
    :param taille: Taille de la tige
    :param couleur: Couleur de la tige
    :return: None
    """
    # Assertions
    assert isinstance(x, int), "x doit être un entier"
    assert isinstance(y, int), "y doit être un entier"
    assert assert_size_factor(taille), "taille doit être un réel/entier et supérieur à 0"
    assert assert_color(couleur), "couleur doit être un tuple de 3 entiers."

    # Dessin
    translate(x, y)

    noStroke()
    safe_fill(couleur)
    rect(-taille / 4, 0, taille / 2, taille * 5)

    translate(-x, -y)