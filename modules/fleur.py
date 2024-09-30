from p5 import TWO_PI, no_stroke, push_matrix, translate, rotate, ellipse, pop_matrix

from utils.assertions import safe_fill


def draw_fleur(posx,posy, rayon, nb_petale,centre,petales):
    """
    La fonction draw_fleur prend cinq paramètres :
    posx: La coordonnée x du centre de la fleur
    posy: La coordonnée y du centre de la fleur
    rayon: Le rayon de la fleur et des pétales
    nb_petale: Le nombre de pétales de la fleur
    petales: La couleur des pétales
    centre: La couleur du centre de la fleur
    """
    angle = TWO_PI / nb_petale
    safe_fill(petales)  # Couleur des pétales
    no_stroke()

    # Dessiner les pétales
    for i in range(nb_petale):
        push_matrix()
        translate(posx,posy)
        rotate(i * angle)
        ellipse(0, rayon, rayon, rayon* 1.5)
        pop_matrix()

    # Dessiner le centre de la fleur
    safe_fill(centre)  # Couleur du centre
    ellipse(posx, posy, rayon, rayon )
