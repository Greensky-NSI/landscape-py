from p5 import fill, rect, triangle, stroke, line

from utils.assertions import safe_fill


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
    safe_fill(grgcl)  # Couleur rouge de la grange
    rect(grgX, grgY, grgh, grgY)  # Position (x, y) et taille (largeur, hauteur)

    # Dessiner le toit (triangle)
    safe_fill(toitcl)  # Couleur marron pour le toit
    triangle((grgX -(grgl * 0.3), grgY), (grgX + (grgl / 2), grgY - (grgh / 2)),
             (grgX +grgl+(grgl * 0.1), grgY))  # Sommets du triangle (gauche, centre, droite)


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
    safe_fill(prtcl)  # Couleur marron pour la porte
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
    safe_fill(fntcl)  # Couleur blanche pour les fenêtres
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
