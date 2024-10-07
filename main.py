from conf import *
from map import *

pygame.init()

# Charger le GIF en utilisant Pillow
gif_path = 'menu.gif'  # Remplace par le chemin de ton GIF
gif = Image.open(gif_path)

# Extraire les frames du GIF
frames = [frame.copy() for frame in ImageSequence.Iterator(gif)]
frame_count = len(frames)

# Taille de la fenêtre (adaptée à la première frame du GIF)
width, height = frames[0].size
window = pygame.display.set_mode((width, height))

# Fonction pour convertir une image Pillow en surface Pygame
def pil_image_to_surface(pil_image):
    mode = pil_image.mode
    size = pil_image.size
    data = pil_image.tobytes()

    return pygame.image.fromstring(data, size, mode)

# Conversion de toutes les frames du GIF en surfaces Pygame
pygame_frames = [pil_image_to_surface(frame.convert("RGB")) for frame in frames]

# Définir le taux de rafraîchissement pour l'animation
clock = pygame.time.Clock()
frame_duration = 100  # Durée par frame en millisecondes (ajuste si nécessaire)
frame_index = 0

# Boucle principale Pygame
running = True
pygame.mixer.music.load("menu_theme.mp3")
pygame.mixer.music.set_volume(0.0)
pygame.mixer.music.play()
playmat = Map()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Afficher la frame actuelle
    window.blit(pygame_frames[frame_index], (0, 0))
    playmat.draw_map(window)
    pygame.display.update()

    # Passer à la frame suivante
    frame_index = (frame_index + 1) % frame_count

    # Attendre pour respecter la durée de la frame
    clock.tick(1000 // frame_duration)

# Quitter Pygame
pygame.quit()
