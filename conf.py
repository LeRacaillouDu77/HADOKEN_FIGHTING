import pygame
from PIL import Image, ImageSequence
import random

EMPTY = (0, 0, 0)
MARGIN = 3

COLORS_TETROMINOS = {'I': (98, 122, 157),
                     'O': (231, 199, 31),
                     'T': (187, 86, 149),
                     'S': (175, 54, 60),
                     'Z': (70, 148, 73),
                     'J': (224, 163, 46),
                     'L': (87, 108, 67),
                     'E': (0, 0, 0)}
TETROMINOS = {
    'I': [
        [['I', 'I', 'I', 'I']],  # Ligne horizontale
        [['I'], ['I'], ['I'], ['I']],  # Ligne verticale
    ],
    'O': [
        [['O', 'O'],
         ['O', 'O']],  # Carré 2x2
    ],
    'T': [
        [['E', 'T', 'E'],
         ['T', 'T', 'T']],  # Orientation normale (vers le haut)
        [['T', 'E'],
         ['T', 'T'],
         ['T', 'E']],  # Rotation 9'E'° à droite
        [['T', 'T', 'T'],
         ['E', 'T', 'E']],  # Rotation 18'E'°
        [['E', 'T'],
         ['T', 'T'],
         ['E', 'T']],  # Rotation 27'E'° à droite
    ],
    'S': [
        [['E', 'S', 'S'],
         ['S', 'S', 'E']],  # Orientation normale
        [['S', 'E'],
         ['S', 'S'],
         ['E', 'S']],  # Rotation 9'E'°
    ],
    'Z': [
        [['Z', 'Z', 'E'],
         ['E', 'Z', 'Z']],  # Orientation normale
        [['E', 'Z'],
         ['Z', 'Z'],
         ['Z', 'E']],  # Rotation 9'E'°
    ],
    'J': [
        [['J', 'E', 'E'],
         ['J', 'J', 'J']],  # Orientation normale (base gauche)
        [['J', 'J'],
         ['J', 'E'],
         ['J', 'E']],  # Rotation 9'E'°
        [['J', 'J', 'J'],
         ['E', 'E', 'J']],  # Rotation 18'E'°
        [['E', 'J'],
         ['E', 'J'],
         ['J', 'J']],  # Rotation 27'E'°
    ],
    'L': [
        [['E', 'E', 'L'],
         ['L', 'L', 'L']],  # Orientation normale (base droite)
        [['L', 'E'],
         ['L', 'E'],
         ['L', 'L']],  # Rotation 9'E'°
        [['L', 'L', 'L'],
         ['L', 'E', 'E']],  # Rotation 18'E'°
        [['L', 'L'],
         ['E', 'L'],
         ['E', 'L']],  # Rotation 270°
    ]
}