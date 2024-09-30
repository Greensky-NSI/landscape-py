from math import floor, sqrt
from random import randint

from p5 import translate, scale, stroke, strokeWeight, line, noStroke, fill, ellipse, rect
from main import color_type, wheat_stem_default_color, wheat_cobs_default_color, positions_list
from utils.utils import assert_size_factor, assert_color

def wheat(*, x: int, y: int, wheat_size: float = 1, width: int, height: int, stem_color: color_type = (200, 150, 50), cobs_color: color_type = (255, 205, 105)):
    """
    Dessine un épi de blé avec sa tige

    :param x: int - La position x de l'épi de blé
    :param y: int - La position y de l'épi de blé
    :param wheat_size: float - L'échelle de taille du blé
    :param width: int - La largeur de la tige de blé
    :param height: int - La hauteur de la tige de blé
    :param stem_color: color_type - La couleur de la tige de blé
    :param cobs_color: color_type - La couleur de l'épi de blé

    :return: None
    """

    # Assertions
    assert isinstance(y, int), "y doit être un entier"
    assert isinstance(x, int), "x doit être un entier"
    assert assert_size_factor(wheat_size), "test_size doit être un réel supérieur à 0"
    assert isinstance(width, int), "width doit être un entier"
    assert isinstance(height, int), "height doit être un entier"
    assert assert_color(stem_color), "stem_color doit être un tuple de 3 entiers."
    assert assert_color(cobs_color), "cobs_color doit être un tuple de 3 entiers."

    # Dessin de l'épi de blé
    translate(x, y)
    scale(wheat_size)

    stroke(*stem_color)
    strokeWeight(width)
    line(0, 0, 0, -height)

    noStroke()
    fill(*cobs_color)
    for i in range(5):
        ellipse(0, -height - (i * 15), width * 2, width * 4)

    scale(1 / wheat_size)
    translate(-x, -y)


def wheat_field(*, x: int, y: int, wheat_size: float = 1, width: int, height: int, stem_color: color_type = wheat_stem_default_color, cobs_color: color_type = wheat_cobs_default_color, field_bg_color: color_type = (255, 176, 7), wheat_positions_list: positions_list = [], maximum_wheat: int = None):
    """
    Crée un champ de blé à partir de la fonction wheat.

    :param x: int - La position x du champ de blé
    :param y: int - La position y du champ de blé
    :param wheat_size: float - L'échelle de taille des tiges de blé. Par défaut : 1
    :param width: int - La largeur du champ de blé
    :param height: int - La hauteur du champ de blé
    :param stem_color: color_type - La couleur des tiges de blé. Par défaut : (200, 150, 50)
    :param cobs_color: color_type - La couleur des épis de blé. Par défaut : (255, 205, 105)
    :param field_bg_color: color_type - La couleur de fond du champ de blé. Par défaut : (255, 176, 7)
    :param wheat_positions_list: List[Tuple[int, int], ...] - La liste des positions des tiges de blé. Par défaut : []. Ne pas modifier, le système s'occupe de le remplir
    :param maximum_wheat: int | None - Le nombre maximum de tiges de blé. Par défaut : None, et calculé automatiquement

    :type wheat_positions_list: list

    :return: None
    """

    # Assertions
    assert isinstance(x, int), "x doit être un entier"
    assert isinstance(y, int), "y doit être un entier"
    assert assert_size_factor(wheat_size), "test_size doit être un réel/entier et supérieur à 0"
    assert isinstance(width, int), "width doit être un entier"
    assert isinstance(height, int), "height doit être un entier"
    assert assert_color(stem_color), "stem_color doit être un tuple de 3 entiers."
    assert assert_color(cobs_color), "cobs_color doit être un tuple de 3 entiers."
    assert assert_color(field_bg_color), "field_bg_color doit être un tuple de 3 entiers."
    assert isinstance(wheat_positions_list, list), "wheats_positions_list doit être une liste"
    assert maximum_wheat is None or assert_size_factor(maximum_wheat), "maximum_wheat doit être un entier ou None"

    # Dessin du champ de blé
    noStroke()
    fill(*field_bg_color)
    rect(x, y, width, height)

    # Calcul du nombre de tiges de blé maximum
    def tiges_maximum(rayon):
        return floor(height / rayon) * floor(width / rayon)

    ecartement = .1 * max(width, height) # Calcul de l'écartement entre les tiges de blé

    target_number = maximum_wheat if maximum_wheat is not None else floor(tiges_maximum(ecartement) * .8) # Calcul du nombre de tiges de blé

    counter = 0
    # Création des tiges de blé
    while len(wheat_positions_list) < target_number and counter < 1000:
        pos_x = randint(x, x + width)
        pos_y = randint(y, y + height)

        wheat_close = False
        for generated_wheat in wheat_positions_list:
            vectors_distance = sqrt((generated_wheat[0] - pos_x) ** 2 + (generated_wheat[1] - pos_y) ** 2)  # Calcul de la distance entre les tiges de blé, par un vecteur

            if vectors_distance <= ecartement:
                wheat_close = True
                break

        if not wheat_close:
            wheat_positions_list.append((pos_x, pos_y))

        counter += 1

    wheat_positions_list.sort(key=lambda position: position[1])  # Tri des tiges de blé par ordre croissant de position y, pour les dessiner dans l'ordre

    for generated_wheat in wheat_positions_list:
        hauteur_ble = ((generated_wheat[1] - y) * 40) / height + 80

        wheat(x = generated_wheat[0], y = generated_wheat[1], height = int(hauteur_ble), width = int(hauteur_ble * 8 / 100), stem_color=stem_color, cobs_color=cobs_color, wheat_size=wheat_size) # Dessin de la tige de blé
