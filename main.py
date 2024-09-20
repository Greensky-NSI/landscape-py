from random import randint

from p5 import *
from typing import Tuple, List, Literal

from custom_types import *    # IMPORTANT importations utiles uniquement pour ceux qui utilisent PyCharm, avec le fichier en plus "custom_types.py" codé par David, car PyCharm ne recoonnait pas certaines variables de p5

WIDTH = 800
HEIGHT = 600

# Code with p5 python
def setup():
    size(WIDTH, HEIGHT)
    background(0)

# Types
color_type = Tuple[int, int, int]
positions_list = List[Tuple[int, int], ...]

# Constantes
weat_stem_default_color: color_type = (200, 150, 50)
weat_cobs_default_color: color_type = (255, 205, 105)

# Variables globales
fond=255
nb_etoiles = None
liste_etoiles = []

# Assert functions
def assert_color(col: color_type):
    return isinstance(col, tuple) and len(col) == 3 and all(isinstance(i, int) for i in col)

def assert_color_mode(mode: str):
    return mode in ["maximum", "modulo"]


# Utils
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
    assert assert_color(col), "col doit être un tuple de 3 entiers."

    # Analyse
    if mode == "modulo":
        return max(0, col[0]) % 255, max(0, col[1]) % 255, max(0, col[2] % 255)
    elif mode == "maximum":
        return frame_number(col[0], maximum=255), frame_number(col[1], maximum=255), frame_number(col[2], maximum=255)
    else:
        raise ValueError(f"Invalid mode: {mode}")

def increase_color(col: color_type, increaser: int | float, *, mode: Literal["maximum", "modulo"] = "maximum") -> color_type:
    """
    Augmente la couleur donnée par un nombre donné

    :param col: color_type - La couleur à augmenter
    :param increaser: int | float - Le nombre à ajouter à chaque composante de la couleur
    :param mode: "maximum" | "modulo" - Le mode d'augmentation. Par défaut : "maximum"

    :return: color_type - La couleur augmentée, et valide
    """

    # Assertions
    assert assert_color(col), "col doit être un tuple de 3 entiers."
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
    assert assert_color(col), "col doit être un tuple de 3 entiers."

    fill(*parse_color(col))

def journuit():
    global fond, nb_etoiles, liste_etoiles

    if key_is_pressed:
        if key == 'N' and fond==255:
            fond=45
            nb_etoiles = randint(0, 100)
            liste_etoiles=[]
        elif key == 'J' and fond==45:
            fond = 255

# Drawings
def river(*, top_left: int = 0, top_right: int = 0, bottom_left: int = HEIGHT, bottom_right: int = HEIGHT):
    """
    Dessine une rivière à l'écran avec les paramètres donnés

    :param top_left: int - La position y du coin supérieur gauche de la rivière
    :param top_right: int - La position y du coin supérieur droit de la rivière
    :param bottom_left: int - La position y du coin inférieur gauche de la rivière
    :param bottom_right: int - La position y du coin inférieur droit de la rivière

    :return: Aucun
    """
    # Assertions
    assert isinstance(top_left, int) and 0 <= top_left <= HEIGHT, "top_left doit être un entier, 0 <= top_left <= HEIGHT"
    assert isinstance(top_right, int) and 0 <= top_right <= HEIGHT, "top_right doit être un entier, 0 <= top_right <= HEIGHT"
    assert isinstance(bottom_left, int) and 0 <= bottom_left <= HEIGHT, "bottom_left doit être un entier, 0 <= bottom_left <= HEIGHT"
    assert isinstance(bottom_right, int) and 0 <= bottom_right <= HEIGHT, "bottom_right doit être un entier, 0 <= bottom_right <= HEIGHT"

    # Dessin de la rivière
    beginShape()

    safe_fill((173, 216, 230))

    third = (top_left + bottom_left) / 2
    moy = (top_left + bottom_right) / 2

    vertex(0, top_left)
    bezier_vertex(WIDTH / 3, third, WIDTH / 2, moy, WIDTH, top_right)

    vertex(WIDTH, bottom_right)
    bezier_vertex(WIDTH / 2, moy, WIDTH / 3, third * 2, 0, bottom_left)

    endShape(CLOSE)

def cloud(*, x: int = 0, y: int = 0, scalar: int = 100, cloud_color: color_type = (255, 255, 255), cloud_size: float = 1, repeat_distance = .4, repeated: bool = False, color_variation: float = 0, pi_count: int = 0, cloud_color_variation_mode: Literal["modulo", "maximum"] = "modulo"):
    """
    Dessine un nuage à l'écran à la position donnée avec la taille et la couleur données

    :param x: int - La position x du nuage
    :param y: int - La position y du nuage
    :param scalar: int - L'échelle utilisée dans le calcul des nuages. Valeur par défaut/recommandée : 100
    :param cloud_color: color_type - La couleur du nuage. Par défaut : (255, 255, 255)
    :param cloud_size: float | int - C'est l'échelle utilisée lors du dessin du nuage. Par défaut : 1
    :param repeat_distance: float | int - La distance entre les nuages. Par défaut/Recommandée : 2/3
    :param color_variation: float - Facteur de variation de couleur. Par défaut: 0
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
    assert (isinstance(cloud_size, float) or isinstance(cloud_size, int)) and cloud_size > 0, "cloud_size doit être un réel/entier et supérieur à 0"
    assert (isinstance(repeat_distance, float) or isinstance(repeat_distance, int)) and 0 < repeat_distance, "repeat_distance doit être un réel/entier et 0 < repeat_distance"
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
    assert (isinstance(tree_size, float) or isinstance(tree_size, int)) and tree_size > 0, "cloud_size doit être un réel/entier et supérieur à 0"
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

def weat_field(*, x: int, y: int, weat_field_size: float = 1, width: int, height: int, stem_color: color_type = weat_stem_default_color, cobs_color: color_type = weat_cobs_default_color, field_bg_color: color_type = (255, 176, 7), weats_positions_list: positions_list = []):
    noStroke()
    fill(*field_bg_color)
    rect(x, y, width, height)

    def tiges_maximum(rayon):
        return floor(height / rayon) * floor(width / rayon)

    ecartement = .1 * max(width, height)

    while len(weats_positions_list) < floor(tiges_maximum(ecartement) * .8):       # Version améliorée
    # while len(liste_positions) < 20:                                        # Version simplifiée
        pos_x = randint(x, x + width)
        pos_y = randint(y, y + height)

        # Permet de trouver si une tige de blé existe déjà à proximité de celle en train types'être créé.
        weat_close = False
        for generated_weat in weats_positions_list:
            # Vérification de la distance du nouveau point avec ceux déjà existants
            vectors_distance = sqrt((generated_weat[0] - pos_x) ** 2 + (generated_weat[1] - pos_y) ** 2)

            # Annulation de l'ajout si la distance est inférieure à ecartement pixels (de rayon)
            if vectors_distance <= ecartement:
                weat_close = True
                break

        if not weat_close:
            # Ajout des nouvelles positions
            weats_positions_list.append((pos_x, pos_y))

    weats_positions_list.sort(key=lambda position: position[1])

    for generated_weat in weats_positions_list:
        # La hauteur des tiges de blé variera entre 80 et 120 pixels
        hauteur_ble = ((generated_weat[1] - y) * 40) / height + 80

        weat(x = generated_weat[0], y = generated_weat[1], height = hauteur_ble, width = hauteur_ble * 8 / 100)


def weat(*, x: int, y: int, weat_size: float = 1, width: int, height: int, stem_color: color_type = (200, 150, 50), cobs_color: color_type = (255, 205, 105)):
    scale(weat_size)

    stroke(*stem_color)
    strokeWeight(width)
    line(x, y, x, y - height)

    noStroke()
    fill(*cobs_color)
    for i in range(5):
        ellipse(x, y - height - (i * 15), width * 2, width * 4)

    scale(1 / weat_size)

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

def draw_ferme(grgX, grgY, grgl, grgh, grgcl, toitcl):
    """
    La fonction draw_ferme prend six paramètres et dessine la ferme :
    grgX: La coordonnée x de la ferme
    grgY: La coordonnée y de la ferme
    grgl: La longueur de la ferme
    grgh: La hauteur de la ferme
    grgcl: La couleur du corps de la ferme
    toitcl: La couleur du toit de la ferme
    """
    # Dessiner le corps de la grange (rectangle)
    fill(grgcl)  # Couleur rouge de la grange
    rect(grgX, grgY, grgh, grgY)  # Position (x, y) et taille (largeur, hauteur)

    # Dessiner le toit (triangle)
    fill(toitcl)  # Couleur marron pour le toit
    triangle((grgX - (grgl * 0.9), grgY), (grgX + (grgl / 2), grgY - (grgh / 2)),
             (grgX + (grgl * 1.1), grgY))  # Sommets du triangle (gauche, centre, droite)
def draw_porte(prtcl,prtX,prtY,prtl,prth):
    """
    La fonction draw_porte prend cinq paramètres et dessine la porte :
    prtX: La coordonnée x de la porte
    porteY: La coordonnée y de la porte
    prtl: La longueur de la porte
    prth: La hauteur de la porte
    prtcl: La couleur du corps de la porte
    """
    # Dessiner la porte
    fill(prtcl)  # Couleur marron pour la porte
    rect(prtX,prtY,prtl,prth)  # Position (x, y) et taille (largeur, hauteur)
def draw_fenetre(fntcl, fntX, fntY, fntl, fnth):
    """
    La fonction draw_fenetre prend cinq paramètres et dessine la fenêtre :
    fntX: La coordonnée x de la fenêtre
    fntY: La coordonnée y de la fenêtre
    fntl: La longueur de la fenêtre
    fnth: La hauteur de la fenêtre
    fntcl: La couleur du corps de la fenêtre
    """
    # Dessiner les fenêtres
    fill(fntcl)  # Couleur blanche pour les fenêtres
    rect(fntX, fntY, fntl, fnth)  # Fenêtre gauche

    # Dessiner les barres des fenêtres
    stroke(0)
    line((fntX + (fntl / 2), fntY), (fntX + (fntl / 2), fntY + fnth))  # Ligne verticale fenêtre gauche
    line((fntX, fntY + (fnth / 2)), (fntX + fntl, fntY + (fnth / 2)))  # Ligne horizontale fenêtre gauche
def Ferme(grgX,grgY,grgl,grgh,grgcl,toitcl,prtcl,prtX,prtY,prtl,prth,fntcl,fntX,fntY,fntl,fnth):
    """
    La fonction Ferme prend seize paramètres :
    grgX: La coordonnée x de la ferme
    grgY: La coordonnée y de la ferme
    grgl: La longueur de la ferme
    grgh: La hauteur de la ferme
    grgcl: La couleur du corps de la ferme
    toitcl: La couleur du toit de la ferme
    prtX: La coordonnée x de la porte
    porteY: La coordonnée y de la porte
    prtl: La longueur de la porte
    prth: La hauteur de la porte
    prtcl: La couleur du corps de la porte
    fntX: La coordonnée x de la fenêtre
    fntY: La coordonnée y de la fenêtre
    fntl: La longueur de la fenêtre
    fnth: La hauteur de la fenêtre
    fntcl: La couleur du corps de la fenêtre
    """
    # Appeler les fonctions de la ferme
    draw_ferme(grgX,grgY,grgl,grgh,grgcl,toitcl)   # Grange
    draw_porte(prtcl,prtX,prtY,prtl,prth)   # Porte de la grange
    draw_fenetre(fntcl,fntX,fntY,fntl,fnth)  # Fenêtres de la grange

def etoiles(cielH, liste_etoiles_):
    while len(liste_etoiles_) < nb_etoiles:
        x=randint(0,800)
        y=randint(0,cielH)

        liste_etoiles_.append((x, y))

    for x, y in liste_etoiles_:
        fill(255)
        ellipse(x,y,5,5)

# Draw
def draw():
    global fond, liste_etoiles

    journuit()
    background(fond)

    if fond == 45:
        etoiles(200, liste_etoiles)


    # river(top_left=100, top_right=150, bottom_left=200, bottom_right=180)
    # cloud(x = WIDTH // 2, y = HEIGHT // 2, scalar=95, cloud_size=.5, repeat_distance=.31, color_variation=5, cloud_color=(150, 150, 150))
    # tree(x=WIDTH // 2, y=HEIGHT, cloud_size=1.5)

    weat_field(x = 200, y = 200, width = 100, height = 100)

    # Ferme(200, 150, 200, 150,'red','brown','brown',270, 230, 60, 70,'white',220, 180, 40, 40)


run()