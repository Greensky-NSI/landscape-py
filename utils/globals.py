from typing import List

from utils.utils import generate_seed

seed = generate_seed()
default_fond = (int(seed[0]) * 100 + int(seed[2]) * 10 + int(seed[3])) % 255

# Variables globales
variables = {
    "fond": default_fond,
    "default_fond": default_fond,
    "nb_etoiles": 0,
    "liste_etoiles": [],
    "WIDTH": 800,
    "HEIGHT": 600,
    "seed": seed
}
fond: int = 255
nb_etoiles: int = 0
liste_etoiles: List[int] = []
