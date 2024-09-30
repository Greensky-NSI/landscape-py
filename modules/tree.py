from p5 import translate, scale, fill, beginShape, vertex, bezier_vertex, endShape, strokeWeight, stroke, line, bezier

from utils.types import color_type
from modules.cloud import cloud
from utils.utils import assert_size_factor, assert_color

def tree(*, x: int, y: int, tree_size: float = 1, trunc_color: color_type = (131, 90, 36), leaf_color: color_type = (0, 128, 0), leaf_color_variation: float = 5):
    """
    Dessine un arbre à l'écran à la position donnée avec la taille et les couleurs données

    :param x: int - Position x en bas à gauche de l'arbre
    :param y: int - Position y en bas à gauche de l'arbre
    :param tree_size: int | float - Échelle de l'arbre (par défaut : 1)
    :param trunc_color: Tuple[int, int int] - Couleur du tronc (par défaut : (131, 90, 36))
    :param leaf_color: Tuple[int, int int] - Couleur des feuilles (par défaut : (0, 128, 0))
    :param leaf_color_variation: float - Variation de la couleur des feuilels (par défaut: 5)

    :return: Rien
    """
    # Assertions
    assert isinstance(x, int), "x doit être un entier"
    assert isinstance(y, int), "y doit être un entier"
    assert assert_size_factor(tree_size), "cloud_size doit être un réel/entier et supérieur à 0"
    assert assert_color(trunc_color), "trunc_color doit être un tuple de 3 entiers."
    assert assert_color(leaf_color), "leaf_color doit être un tuple de 3 entiers."

    # Dessin de l'arbre
    translate(x, y)
    scale(tree_size)

    fill(*trunc_color)

    # Tronc
    beginShape()
    vertex(0, 0)
    bezier_vertex(50, -60, 43, -130, 45, -300)

    vertex(110, -300)
    bezier_vertex(110, -200, 120, -60, 160, 0)
    vertex(0, 0)

    endShape()

    strokeWeight(1)
    stroke(*trunc_color)
    line(45, -300, 110, -300)
    line(160, 0, 0, 0)

    # Rajouter de la texture

    lines = (
        ((50, -200), (60, -150)),
        ((100, -100), (110, -50)),
        ((75, -170), (85, -90))
    )

    stroke((1, 1, 1))
    for p1, p2 in lines:
        x1, y1 = p1
        x2, y2 = p2

        bezier(x1, y1, x1, y1 + 25, x2, y2 - 25, x2, y2)

    scale(1 / tree_size)
    translate(-x, -y)

    # Feuilles
    cloud(x=int(x + 40 * tree_size), y=int(y - 300 * tree_size), scalar=100, cloud_color=leaf_color, cloud_size=tree_size / 2, repeat_distance=tree_size / 2, color_variation=leaf_color_variation, cloud_color_variation_mode="maximum")
