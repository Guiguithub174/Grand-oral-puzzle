import pygame

class Puzzle:
    def __init__(puzzle):
        puzzle.pieces = []
        puzzle.taille = 0

    def ajouter_piece(puzzle, piece):
        puzzle.pieces.append(piece)
        puzzle.taille += 1

class PuzzlePiece:
    def __init__(piece, haut, droite, bas, gauche):
        piece.cotes = {"haut": haut, "droite": droite, "bas": bas, "gauche": gauche}
        piece.type = piece.get_type()
    def get_type(piece):
        compteur_de_vide = 0
        for cote in piece.cotes.values():
            if cote == ():
                compteur_de_vide += 1
        if compteur_de_vide == 0:
            return "centre"
        elif compteur_de_vide == 1:
            return "bord"
        return "coin"