from typing import Literal, Tuple

from p5 import fill

from main import color_type
from utils.utils import assert_color, assert_color_mode


def frame_number(number: int | float, *, maximum: int | float = 100, minimum: int | float = 0):
    """
    Encadre un nombre entre un minimum et un maximum donné

    :param number: int | float - le nombre à encadrer
    :param maximum: int | float - le maximum. Par défaut : 100
    :param minimum: int | float - le minimum. Par défaut : 0
    :return: int - le nombre encadré
    """

    # Assertions
    assert isinstance(number, int) or isinstance(number, float), "number doit être un entier ou un réel"
    assert isinstance(maximum, int) or isinstance(maximum, float), "maximum doit être un entier ou un réel"
    assert isinstance(minimum, int) or isinstance(minimum, float), "minimum doit être un entier ou un réel"

    # Encadrement
    if minimum >= maximum:
        minimum, maximum = maximum, minimum
    return max(minimum, min(number, maximum))


def parse_color(col: color_type, *, mode: Literal["maximum", "modulo"] = "maximum") -> color_type:
    """
    Analyse une couleur et la renvoie en fonction du mode donné

    :param col: color_type - La couleur à analyser
    :param mode: "maximum" | "modulo" - Le mode d'analyse. Par défaut : "maximum"

    :return: color_type - La couleur analysée, et valide
    """

    # Assertions
    assert mode in ["maximum", "modulo"], "Le mode doit être soit : \"maximum\", \"modulo\""
    assert assert_color(col), "couleur_corps doit être un tuple de 3 entiers."

    # Analyse
    def colors() -> Tuple[int, int, int]:
        if mode == "modulo":
            return max(0, col[0]) % 255, max(0, col[1]) % 255, max(0, col[2] % 255)
        elif mode == "maximum":
            return frame_number(col[0], maximum=255), frame_number(col[1], maximum=255), frame_number(col[2], maximum=255)
        else:
            raise ValueError(f"Invalid mode: {mode}")

    if len(col) == 3:
        return colors()
    else:
        cols = colors()
        if mode == "modulo":
            return cols[0], cols[1], cols[2], frame_number(col[3], maximum=255)
        else:
            return cols[0], cols[1], cols[2], frame_number(col[3], maximum=255, minimum=0)


def increase_color(col: color_type, increaser: int | float, *, mode: Literal["maximum", "modulo"] = "maximum") -> color_type:
    """
    Augmente la couleur donnée par un nombre donné

    :param col: color_type - La couleur à augmenter
    :param increaser: int | float - Le nombre à ajouter à chaque composante de la couleur
    :param mode: "maximum" | "modulo" - Le mode d'augmentation. Par défaut : "maximum"

    :return: color_type - La couleur augmentée, et valide
    """

    # Assertions
    assert assert_color(col), "couleur_corps doit être un tuple de 3 entiers."
    assert isinstance(increaser, int) or isinstance(increaser, float), "increaser doit être un entier ou un réel"
    assert assert_color_mode(mode), "Le mode doit être soit : \"maximum\", \"modulo\""

    # Parsing et ajout
    return parse_color((col[0] + increaser, col[1] + increaser, col[2] + increaser), mode=mode)


def safe_fill(col: color_type):
    """
    Remplit la couleur donnée en s'assurant qu'elle est valide

    :param col: color_type - La couleur à remplir
    :return: None
    """
    # Assertions
    assert assert_color(col), "couleur_corps doit être un tuple de 3 entiers."

    fill(*parse_color(col))
