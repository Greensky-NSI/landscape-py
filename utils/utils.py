from utils.types import color_type
from typing import List
from random import randint

def assert_color(col: color_type, *, allow_floats: bool = False):
    return isinstance(col, tuple) and (len(col) == 3 or len(col) == 4) and all((isinstance(i, int) or (isinstance(i, float) and allow_floats)) for i in col)

def assert_color_mode(mode: str):
    return mode in ["maximum", "modulo"]

def assert_size_factor(test_size):
    return (isinstance(test_size, float) or isinstance(test_size, int)) and test_size > 0

def generate_seed():
    seed_length = randint(16, 20)
    seed = ""

    for _ in range(seed_length):
        seed += str(randint(0, 9))

    return seed

def get_color_from_seed(seed: str) -> color_type:
    working_seed = str(seed)  # On évite les conflits d'overriding de variables
    if len(working_seed) < 9:
        working_seed = str(int(working_seed) ** 2)

    cols: List[str] = []
    counter = 0  # On évite les boucles infinies
    while len(cols) < 9 and counter < 100:
        cols.append(working_seed[0])
        working_seed = working_seed[1:]

        counter += 1

    if len(cols) < 9:
        missing_chars = 9 - len(cols)
        cols += [cols[0] for _ in range(missing_chars)]

    return int("".join(cols[0:3])), int("".join(cols[3:6])), int("".join(cols[6:9]))