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
        piece.haut = haut
        piece.droite = droite
        piece.bas = bas
        piece.gauche = gauche