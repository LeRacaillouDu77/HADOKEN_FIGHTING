from conf import *


def get_random_piece():
    form = random.choice(list(TETROMINOS.keys()))
    return Piece(form)
class Piece:
    def __init__(self, name):
        self.name = name
        self.forms = TETROMINOS[name]
        self.color = COLORS_TETROMINOS[name]
        self.current_form_index = 0
        self.current_form = self.forms[0]
        self.position = [320 + (20 + MARGIN) * 4, 20]
        self.clock = pygame.time.Clock()
        self.start_time = pygame.time.get_ticks()
    def draw_piece(self, screen):
        for column in range(len(self.current_form)):
            for row in range(len(self.current_form[column])):
                color = COLORS_TETROMINOS[self.current_form[column][row]]
                pygame.draw.rect(screen, color, [(MARGIN + 20) * row + MARGIN + self.position[0], (MARGIN + 20) * column + MARGIN + self.position[1], 20, 20])
    def move_tetro(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.position[0] -= 20 + MARGIN
            if event.key == pygame.K_RIGHT:
                self.position[0] += 20 + MARGIN
            if event.key == pygame.K_SPACE:
                self.current_form_index = (self.current_form_index + 1) % len(self.forms)
                self.current_form = self.forms[self.current_form_index]
    def auto_fall(self):
        time_elapsed = pygame.time.get_ticks() - self.start_time
        print(time_elapsed)
        if time_elapsed > 300 and self.position[1] < 20 + 20 * 21:
            self.position[1] += 20 + MARGIN
            self.start_time = pygame.time.get_ticks()
            