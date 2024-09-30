from p5 import *

from utils.assertions import safe_fill


def rock(x, y, couleur_rocher = (180, 180, 180), couleur_ombre = (150, 150, 150)):
    draw_rock(x, y, couleur_rocher)
    draw_shadow(x, y, couleur_ombre)

def draw_rock(x, y, couleur = (180, 180, 180)):
    """
    Dessine le rocher principal

    :param x Coordonnée x du centre du rocher
    :param y Coordonnée y du centre du rocher
    :param couleur Couleur du rocher
    """
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
    safe_fill(couleur)          # Couleur plus sombre pour l'ombre

    beginShape()
    vertex(x - 40, y + 20)       # Ombre gauche
    vertex(x - 60, y - 20)
    vertex(x - 30, y - 40)
    vertex(x + 30, y - 40)
    vertex(x + 60, y - 20)
    vertex(x + 40, y + 20)
    endShape(CLOSE)