
import pygame,os
import pygame.freetype
pygame.freetype.init()

fonts = {
    'DanceToday': os.path.join("data/fonts/DanceToday.otf"),
    'Newake': os.path.join("data/fonts/Newake.otf"),
    'Poppins': os.path.join("data/fonts/Poppins.ttf"),
    'MouldyCheese': os.path.join("data/fonts/MouldyCheese.ttf"),
    'Wesay': os.path.join("data/fonts/Wesay.otf"),
}
    
def createFont(fontname, size):
    font = pygame.freetype.Font(fontname, size)
    return font