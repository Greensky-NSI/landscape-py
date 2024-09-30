from p5 import *

from utils.assertions import safe_fill
from utils.utils import assert_color


def mouton(x, y, couleur_corps = (255, 255, 255), couleur_tete = (255, 255, 255), couleur_yeux = (0, 0, 0), couleur_oreilles = (255, 255, 255),
           couleur_jambes = (0, 0, 0)):
    """
    Dessine un mouton

    :param x Coordonnée x du centre du mouton
    :param y Coordonnée y du centre du mouton
    :param couleur_corps Couleur du corps
    :param couleur_tete Couleur de la tête
    :param couleur_yeux Couleur des yeux
    :param couleur_oreilles Couleur des oreilles
    :param couleur_jambes Couleur des jambes
    """
    # Assertions
    assert isinstance(x, int) and isinstance(y, int), "Les coordonnées doivent être des entiers"
    assert assert_color(couleur_corps), "La couleur du corps doit être un tuple de 3 entiers"
    assert assert_color(couleur_tete), "La couleur de la tête doit être un tuple de 3 entiers"
    assert assert_color(couleur_yeux), "La couleur des yeux doit être un tuple de 3 entiers"
    assert assert_color(couleur_oreilles), "La couleur des oreilles doit être un tuple de 3 entiers"
    assert assert_color(couleur_jambes), "La couleur des jambes doit être un tuple de 3 entiers"

    # Dessin
    draw_body(x, y, couleur_corps)
    draw_head(x, y, couleur_tete)
    draw_eyes(x, y, couleur_yeux)
    draw_ears(x, y, couleur_oreilles)
    draw_legs(x, y, couleur_jambes)

def draw_body(x, y, couleur = (255, 255, 255)):
    """
    Dessine le corps du mouton

    :param x Coordonnée x du centre du corps
    :param y Coordonnée y du centre du corps
    :param couleur Couleur du corps
    """
    safe_fill(couleur)  # Couleur du corps (blanc)
    stroke(0)           # Couleur des contours (noir)
    strokeWeight(2)     # Épaisseur des contours
    ellipse(x, y, 100, 60)  # Corps principal
    ellipse(x - 40, y, 60, 60)  # Avant du corps
    ellipse(x + 40, y, 60, 60)  # Arrière du corps

def draw_head(x, y, couleur = (255, 255, 255)):
    """
    Dessine la tête du mouton

    :param x Coordonnée x du centre de la tête
    :param y Coordonnée y du centre de la tête
    :param couleur Couleur de la tête
    """
    # Assertions
    assert isinstance(x, int) and isinstance(y, int), "Les coordonnées doivent être des entiers"
    assert assert_color(couleur), "La couleur de la tête doit être un tuple de 3 entiers"

    # Dessin
    safe_fill(couleur)  # Couleur de la tête (blanc)
    ellipse(x, y - 40, 50, 50)  # Tête

def draw_eyes(x, y, couleur = (0, 0, 0)):
    """
    Dessine les yeux du mouton

    :param x Coordonnée x du centre de la tête
    :param y Coordonnée y du centre de la tête
    :param couleur Couleur des yeux
    """
    # Assertions
    assert isinstance(x, int) and isinstance(y, int), "Les coordonnées doivent être des entiers"
    assert assert_color(couleur), "La couleur des yeux doit être un tuple de 3 entiers"

    # Dessin
    safe_fill(couleur)  # Couleur des yeux (noir)
    ellipse(x - 15, y - 40, 10, 10)  # Œil gauche
    ellipse(x + 15, y - 40, 10, 10)  # Œil droit

def draw_ears(x, y, couleur = (255, 255, 255)):
    """
    Dessine les oreilles du mouton

    :param x Coordonnée x du centre de la tête
    :param y Coordonnée y du centre de la tête
    :param couleur Couleur des oreilles
    """
    # Assertions
    assert isinstance(x, int) and isinstance(y, int), "Les coordonnées doivent être des entiers"
    assert assert_color(couleur), "La couleur des oreilles doit être un tuple de 3 entiers"

    # Dessin
    safe_fill(couleur)  # Couleur des oreilles (blanc)
    triangle(x - 25, y - 50, x - 40, y - 30, x - 10, y - 30)  # Oreille gauche
    triangle(x + 25, y - 50, x + 40, y - 30, x + 10, y - 30)  # Oreille droite

def draw_legs(x, y, couleur = (0, 0, 0)):
    """
    Dessine les pattes du mouton

    :param x Coordonnée x du centre du corps
    :param y Coordonnée y du centre du corps
    :param couleur Couleur des pattes
    """
    # Assertions
    assert isinstance(x, int) and isinstance(y, int), "Les coordonnées doivent être des entiers"
    assert assert_color(couleur), "La couleur des pattes doit être un tuple de 3 entiers"

    # Dessin
    safe_fill(couleur)  # Couleur des pattes (noir)
    rect(x - 30, y + 20, 10, 30)  # Patte gauche avant
    rect(x + 20, y + 20, 10, 30)  # Patte droite avant
    rect(x - 30, y + 50, 10, 30)  # Patte gauche arrière
    rect(x + 20, y + 50, 10, 30)  # Patte droite arrière