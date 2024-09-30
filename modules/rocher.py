from p5 import *

from utils.assertions import safe_fill
from utils.utils import assert_color, assert_size_factor


def rock(x, y, taille, couleur_rocher = (180, 180, 180), couleur_ombre = (150, 150, 150)):
    """
    Dessine un rocher avec son ombre

    :param x Coordonnée x du centre du rocher
    :param y Coordonnée y du centre du rocher
    :param taille Taille du rocher
    :param couleur_rocher Couleur du rocher
    :param couleur_ombre Couleur de l'ombre
    """
    # Assertions
    assert isinstance(x, int) and isinstance(y, int), "Les coordonnées doivent être des entiers"
    assert assert_size_factor(taille), "La taille doit être un réel/entier et supérieur à 0"
    assert assert_color(couleur_rocher), "La couleur du rocher doit être un tuple de 3 entiers"
    assert assert_color(couleur_ombre), "La couleur de l'ombre doit être un tuple de 3 entiers"

    # Dessin
    translate(x, y)
    scale(taille)

    draw_rock(0, 0, couleur_rocher)
    draw_shadow(0, 0, couleur_ombre)

    scale(1/taille)
    translate(-x, -y)

def draw_rock(x, y, couleur = (180, 180, 180)):
    """
    Dessine le rocher principal

    :param x Coordonnée x du centre du rocher
    :param y Coordonnée y du centre du rocher
    :param couleur Couleur du rocher
    """
    # Assertions
    assert isinstance(x, int) and isinstance(y, int), "Les coordonnées doivent être des entiers"
    assert assert_color(couleur), "La couleur du rocher doit être un tuple de 3 entiers"

    # Dessin
    safe_fill(couleur)          # Couleur gris pour le rocher
    stroke(100)                  # Couleur des contours (gris foncé)
    strokeWeight(2)              # Épaisseur des contours

    beginShape()
    vertex(x - 60, y + 40)       # Point bas gauche
    vertex(x - 80, y - 20)       # Point haut gauche
    vertex(x - 30, y - 60)       # Point haut milieu
    vertex(x + 30, y - 60)       # Point haut droite
    vertex(x + 80, y - 20)       # Point bas droite
    vertex(x + 60, y + 40)       # Point bas droite
    endShape(CLOSE)

def draw_shadow(x, y, couleur = (150, 150, 150)):
    """
    Dessine l'ombre du rocher pour donner du volume

    :param x Coordonnée x du centre du rocher
    :param y Coordonnée y du centre du rocher
    :param couleur Couleur de l'ombre
    """
    # Assertions
    assert isinstance(x, int) and isinstance(y, int), "Les coordonnées doivent être des entiers"
    assert assert_color(couleur), "La couleur de l'ombre doit être un tuple de 3 entiers"

    # Dessin
    safe_fill(couleur)          # Couleur plus sombre pour l'ombre

    beginShape()
    vertex(x - 40, y + 20)       # Ombre gauche
    vertex(x - 60, y - 20)
    vertex(x - 30, y - 40)
    vertex(x + 30, y - 40)
    vertex(x + 60, y - 20)
    vertex(x + 40, y + 20)
    endShape(CLOSE)