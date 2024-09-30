from p5 import beginShape, vertex, bezier_vertex, endShape, CLOSE

from utils.assertions import safe_fill
from utils.globals import variables


def river(*, top_left: int = 0, top_right: int = 0, bottom_left: int = variables["HEIGHT"], bottom_right: int = variables["HEIGHT"]):
    """
    Dessine une rivière à l'écran avec les paramètres donnés

    :param top_left: int - La position y du coin supérieur gauche de la rivière
    :param top_right: int - La position y du coin supérieur droit de la rivière
    :param bottom_left: int - La position y du coin inférieur gauche de la rivière
    :param bottom_right: int - La position y du coin inférieur droit de la rivière

    :return: Aucun
    """
    # Assertions
    assert isinstance(top_left, int) and 0 <= top_left <= variables["HEIGHT"], "top_left doit être un entier, 0 <= top_left <= HEIGHT"
    assert isinstance(top_right, int) and 0 <= top_right <= variables["HEIGHT"], "top_right doit être un entier, 0 <= top_right <= HEIGHT"
    assert isinstance(bottom_left, int) and 0 <= bottom_left <= variables["HEIGHT"], "bottom_left doit être un entier, 0 <= bottom_left <= HEIGHT"
    assert isinstance(bottom_right, int) and 0 <= bottom_right <= variables["HEIGHT"], "bottom_right doit être un entier, 0 <= bottom_right <= HEIGHT"

    # Dessin de la rivière
    beginShape()

    safe_fill((173, 216, 230))

    third = (top_left + bottom_left) / 2
    moy = (top_left + bottom_right) / 2

    vertex(0, top_left)
    bezier_vertex(variables["WIDTH"] / 3, third, variables["WIDTH"] / 2, moy, variables["WIDTH"], top_right)

    vertex(variables["WIDTH"], bottom_right)
    bezier_vertex(variables["WIDTH"] / 2, moy, variables["WIDTH"] / 3, third * 2, 0, bottom_left)

    endShape(CLOSE)
