from math import cos, sin
from typing import Literal

from p5 import HALF_PI, fill, translate, scale, noStroke, ellipse, PI, arc, TWO_PI

from utils.types import color_type
from utils.assertions import increase_color
from utils.utils import assert_color, assert_size_factor, assert_color_mode

def cloud(*, x: int = 0, y: int = 0, scalar: int = 100, cloud_color: color_type = (255, 255, 255), cloud_size: float = 1, repeat_distance = .4, repeated: bool = False, color_variation: float = 0, pi_count: int = 0, cloud_color_variation_mode: Literal["modulo", "maximum"] = "modulo"):
    """
    Dessine un nuage à l'écran à la position donnée avec la taille et la couleur données.

    :param x: int - La position x du nuage
    :param y: int - La position y du nuage
    :param scalar: int - L'échelle utilisée dans le calcul des nuages. Valeur par défaut/recommandée : 100
    :param cloud_color: color_type - La couleur du nuage. Par défaut : (255, 255, 255)
    :param cloud_size: float | int - C'est l'échelle utilisée lors du dessin du nuage. Par défaut : 1
    :param repeat_distance: float | int - La distance entre les nuages. Par défaut/Recommandée : 2/3
    :param color_variation: float - Facteur de variation de couleur. Par défaut : 0
    :param repeated: bool - Paramètre de machine pour s'appeler à la fin du nuage. Par défaut : False, ne pas modifier
    :param pi_count: int - Paramètre de machine pour garder une alternance. Par défaut : 0, ne pas modifier
    :param cloud_color_variation_mode: "modulo" | "maximum" - Mode de variation de couleur. Par défaut : "modulo"

    :return: Aucun
    """

    # Assertions
    assert isinstance(x, int), "x doit être un entier"
    assert isinstance(y, int), "y doit être un entier"
    assert isinstance(scalar, int) and scalar > 0, "scalar doit être un entier et supérieur à 0"
    assert assert_color(cloud_color), "cloud_color doit être un tuple de 3 entiers."
    assert assert_size_factor(cloud_size), "cloud_size doit être un réel/entier et supérieur à 0"
    assert assert_size_factor(repeat_distance), "repeat_distance doit être un réel/entier et 0 < repeat_distance"
    assert isinstance(repeated, bool), "repeated doit être un booléen"
    assert isinstance(pi_count, int) and pi_count >= 0, "pi_count doit être un entier et supérieur ou égal à 0"
    assert assert_color_mode(cloud_color_variation_mode), "cloud_color_variation_mode doit être soit : \"maximum\", \"modulo\""

    # Dessin du nuage
    color_scale_changer = cos(HALF_PI * pi_count) * color_variation
    computed_color_center = increase_color(cloud_color, color_scale_changer, mode=cloud_color_variation_mode)

    fill(*computed_color_center)

    particles = max(2, min(100, int(scalar / 6)))
    translate(x, y)
    scale(cloud_size)

    noStroke()

    ellipse(0, 0, scalar * 2, scalar * 2)

    trigonometrical_space = (particles - 3) * (2 * PI) / (100 - 3)
    current_number = 0
    count = 0
    divider = 1

    furthest = 0

    while count < particles:
        particle_x = cos(current_number) * scalar / divider
        particle_y = sin(current_number) * scalar / divider

        if particle_x > furthest:
            furthest = particle_x

        color_scale_changer = cos(HALF_PI * pi_count) * color_variation
        computed_color = increase_color(cloud_color, color_scale_changer, mode=cloud_color_variation_mode)

        fill(*computed_color)

        arc(particle_x, particle_y,scalar  + cos(current_number) * 3, scalar + sin(current_number) * 3, 0, TWO_PI)

        current_number += trigonometrical_space
        count += 1
        pi_count += 1


    scale(1 / cloud_size)
    translate(-x, -y)

    # Répéter le nuage en noir dessous pour faire les contours
    if not repeated:
        rayon = furthest + scalar / 2

        cloud(x = int(x + repeat_distance * rayon), y = int(y), scalar = scalar, cloud_color = cloud_color, repeated = True, cloud_size= cloud_size, pi_count=pi_count, color_variation=color_variation, cloud_color_variation_mode=cloud_color_variation_mode)
