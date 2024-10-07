from conf import *


def draw_background_rect(screen):
    s = pygame.Surface((20 * 10 + MARGIN * 11, 20 * 20 + MARGIN * 21))
    s.set_alpha(110)
    s.fill((255, 255, 255))
    screen.blit(s, (320, 20))
class Map:
    def __init__(self):
        self.length = 10
        self.height = 20
        self.tab = [['E'] * 10] * 20
    def draw_map(self, screen):
        draw_background_rect(screen)
        for column in range(self.height):
            for row in range(self.length):
                color = COLORS_TETROMINOS[self.tab[column][row]]
                pygame.draw.rect(screen,
                             color,
                             [(MARGIN + 20) * row + MARGIN + 320,
                              (MARGIN + 20) * column + MARGIN + 20,
                              20,
                              20])
