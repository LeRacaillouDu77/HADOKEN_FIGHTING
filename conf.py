import pygame
from PIL import Image, ImageSequence

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
        [[0, 'T', 0],
         ['T', 'T', 'T']],  # Orientation normale (vers le haut)
        [['T', 0],
         ['T', 'T'],
         ['T', 0]],  # Rotation 90° à droite
        [['T', 'T', 'T'],
         [0, 'T', 0]],  # Rotation 180°
        [[0, 'T'],
         ['T', 'T'],
         [0, 'T']],  # Rotation 270° à droite
    ],
    'S': [
        [[0, 'S', 'S'],
         ['S', 'S', 0]],  # Orientation normale
        [['S', 0],
         ['S', 'S'],
         [0, 'S']],  # Rotation 90°
    ],
    'Z': [
        [['Z', 'Z', 0],
         [0, 'Z', 'Z']],  # Orientation normale
        [[0, 'Z'],
         ['Z', 'Z'],
         ['Z', 0]],  # Rotation 90°
    ],
    'J': [
        [['J', 0, 0],
         ['J', 'J', 'J']],  # Orientation normale (base gauche)
        [['J', 'J'],
         ['J', 0],
         ['J', 0]],  # Rotation 90°
        [['J', 'J', 'J'],
         [0, 0, 'J']],  # Rotation 180°
        [[0, 'J'],
         [0, 'J'],
         ['J', 'J']],  # Rotation 270°
    ],
    'L': [
        [[0, 0, 'L'],
         ['L', 'L', 'L']],  # Orientation normale (base droite)
        [['L', 0],
         ['L', 0],
         ['L', 'L']],  # Rotation 90°
        [['L', 'L', 'L'],
         ['L', 0, 0]],  # Rotation 180°
        [['L', 'L'],
         [0, 'L'],
         [0, 'L']],  # Rotation 270°
    ]
}