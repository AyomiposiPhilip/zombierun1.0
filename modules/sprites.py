
import os, pygame

player = {
    'sprite1': pygame.image.load(os.path.join("data/gfx/guy.png")),
    'sprite2': pygame.image.load(os.path.join("data/gfx/bread.png")),
    'sprite3': pygame.image.load(os.path.join("data/gfx/black.png")),
    'sprite4': pygame.image.load(os.path.join("data/gfx/heart.png")),
    'sprite5': pygame.image.load(os.path.join("data/gfx/cupcake.png")),
    'sprite6': pygame.image.load(os.path.join("data/gfx/ghost.png")),
    'sprite7': pygame.image.load(os.path.join("data/gfx/herocat.png")),
    'allsprites': 7,
    'width': 100,
    'height': 100,
}

playerNames = {
    'name1': 'Jack',
    'name2': 'Bread',
    'name3': 'Black',
    'name4': 'Heart',
    'name5': 'Cupcake',
    'name6': 'Ghost',
    'name7': 'Cat named Hero',
}

chooseCharacter = {
    'left': pygame.image.load(os.path.join("data/gfx/left.png")),
    'right': pygame.image.load(os.path.join("data/gfx/right.png")),
}

ground = {
    'sprite': pygame.image.load(os.path.join("data/gfx/ground.png")),
    'width': 900,
    'height': 100,
    'x': 0,
    'y': 800,
}

gun = {
    'sprite': pygame.image.load(os.path.join("data/gfx/gun.png")),
    'width': 48,
    'height': 48,
}

cloud = {
    'sprite': pygame.image.load(os.path.join("data/gfx/cloud.png")),
    'width': 200,
    'height': 100,
    'y1': 150,
    'y2': 200,
    'y3': 250,
}

obstacles = {
    'rock': pygame.image.load(os.path.join("data/gfx/rock.png")),
    'log': pygame.image.load(os.path.join("data/gfx/log.png")),
    'spike': pygame.image.load(os.path.join("data/gfx/spikes.png")),
    'heal': pygame.image.load(os.path.join("data/gfx/heal.png")),
    'zombie': pygame.image.load(os.path.join("data/gfx/zombie.png")),
    'width': 100,
    'height': 100,
    'y': 700,
}

bullet = {
    'sprite': pygame.image.load(os.path.join("data/gfx/bullet.png")),
    'width': 26,
    'height': 16,
}

healthShadow = {
    'sprite': pygame.image.load(os.path.join("data/gfx/health_shadow.png")),
}

score = {
    'sprite': pygame.image.load(os.path.join("data/gfx/kills.png")),
}