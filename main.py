import pygame, random, os
from modules import sprites,colors,screen,health,sounds
from modules.player import Player
from modules.fonts import createFont, fonts
import math, time
pygame.mixer.init()


window = pygame.display.set_mode((screen.screenWidth,screen.screenHeight))
pygame.display.set_caption("Zombie Run")
pygame.display.set_icon(pygame.image.load(os.path.join("data/icon/icon.ico")))

screens = {
    'mainGameScreen': False,
    'pregameScreen': False,
    'loadingScreen': True,
    'endScreen': False,
}

clouds = []
obstacles = []
bullets = []
playerHealth = 10
totalPlayerHealth = 300
playerHealthColor = (0,196,24)
bulletMax = 2
obstacleSpeed = 4
score = 0
playerSpriteNumber = 1

userplayer = Player(sprites.player['width'], sprites.player['height'], 150, 700)


def loading_draw_window(loader, zombie_x):
    window.fill(colors.skyColor)
    window.blit(sprites.ground['sprite'], (sprites.ground['x'],sprites.ground['y']))

    createFont(fonts['Poppins'], 20).render_to(window, (5,5), f"© Phil and Nini", colors.black)

    createFont(fonts['Wesay'], 160).render_to(window, (350,160), f"ZOMBIE", colors.black)
    createFont(fonts['Wesay'], 160).render_to(window, (350,150), f"ZOMBIE", colors.red)
    
    createFont(fonts['Wesay'], 130).render_to(window, (500,310), f"RUN", colors.black)
    createFont(fonts['Wesay'], 130).render_to(window, (500,300), f"RUN", colors.red)

    createFont(fonts['Newake'], 40).render_to(window, (550,500), f"Loading", colors.black)
    pygame.draw.rect(window, colors.grey, pygame.Rect(200, 550, 800, 50))
    pygame.draw.rect(window, colors.black, pygame.Rect(200, 550, loader, 50))

    window.blit(sprites.obstacles['zombie'], (zombie_x, 700))

    pygame.display.update()


def pregame_draw_window(playerrect):
    userplayer.setCoordinates(playerrect.x, playerrect.y)

    window.fill(colors.skyColor)
    window.blit(sprites.player[f'sprite{playerSpriteNumber}'], (userplayer.x, userplayer.y))
    window.blit(sprites.ground['sprite'], (sprites.ground['x'],sprites.ground['y']))

    window.blit(sprites.chooseCharacter['left'], (playerrect.x - 80,playerrect.y + 15))
    window.blit(sprites.chooseCharacter['right'], (playerrect.x + playerrect.width + 10,playerrect.y + 15))
    
    createFont(fonts['Newake'], 40).render_to(window, (450,500), f"Press Enter to Play", colors.black)

    createFont(fonts['Newake'], 60).render_to(window, (playerrect.x + playerrect.width + 100,playerrect.y + 30), f"{sprites.playerNames[f'name{playerSpriteNumber}']}", colors.black)

    createFont(fonts['Wesay'], 160).render_to(window, (350,160), f"ZOMBIE", colors.black)
    createFont(fonts['Wesay'], 160).render_to(window, (350,150), f"ZOMBIE", colors.red)
    createFont(fonts['Wesay'], 130).render_to(window, (500,310), f"RUN", colors.black)
    createFont(fonts['Wesay'], 130).render_to(window, (500,300), f"RUN", colors.red)

    pygame.display.update()


def draw_window(playerrect):
    userplayer.setCoordinates(playerrect.x, playerrect.y)

    window.fill(colors.skyColor)
    window.blit(sprites.player[f'sprite{playerSpriteNumber}'], (userplayer.x, userplayer.y))
    window.blit(sprites.gun['sprite'], ((userplayer.x + sprites.player['width']) - 15, (userplayer.y) + (userplayer.height / 2) - (sprites.gun['width'] / 4)))

    window.blit(sprites.ground['sprite'], (sprites.ground['x'],sprites.ground['y']))

    window.blit(sprites.healthShadow['sprite'], (12,12))
    pygame.draw.rect(window, playerHealthColor, (10,10,(playerHealth/totalPlayerHealth) * 350,50))
    createFont(fonts['Newake'], 40).render_to(window, (20,20), f"{playerHealth}", colors.black)

    window.blit(sprites.score['sprite'], ((screen.screenWidth - 265),15))
    createFont(fonts['MouldyCheese'], 40).render_to(window, (screen.screenWidth - 170,50), f"{int(score)}", colors.black)

    for cloud in clouds:
        window.blit(sprites.cloud['sprite'], (cloud.x, cloud.y))
    
    for obstacle in obstacles:
        window.blit(sprites.obstacles[obstacle[1]], (obstacle[0].x, obstacle[0].y))
    
    for bullet in bullets:
        window.blit(sprites.bullet['sprite'], (bullet.x, bullet.y))


    pygame.display.update()


def endscreen_draw_window():
    window.fill(colors.skyColor)
    window.blit(sprites.ground['sprite'], (sprites.ground['x'],sprites.ground['y']))

    createFont(fonts['Wesay'], 160).render_to(window, (350,160), f"ZOMBIE", colors.black)
    createFont(fonts['Wesay'], 160).render_to(window, (350,150), f"ZOMBIE", colors.red)
    
    createFont(fonts['Wesay'], 130).render_to(window, (500,310), f"RUN", colors.black)
    createFont(fonts['Wesay'], 130).render_to(window, (500,300), f"RUN", colors.red)

    createFont(fonts['MouldyCheese'], 40).render_to(window, (400,500), f"SCORE : {int(score)}", colors.black)
    createFont(fonts['Newake'], 40).render_to(window, (400,600), f"Press P to Play Again", colors.black)
    createFont(fonts['Newake'], 40).render_to(window, (400,650), f"Press E to Quit Game", colors.black)

    pygame.display.update()


def playerHealthColorChange():
    global playerHealthColor
    if playerHealth > 200:
        playerHealthColor = (0,196,24)
    elif playerHealth >= 100 and playerHealth < 200:
        playerHealthColor = (223,183,0)
    elif playerHealth < 100:
        playerHealthColor = (255,77,15)


def createObstacles():
    if obstacles.__len__() < 2:
        obstacleType = "rock"
        obstacleHealth = 50
        obstacleDamage = 10
        rand = random.randint(0, 15)
        if rand >= 0 and rand <= 3:
            obstacleType = "rock"
            obstacleHealth = 50
            obstacleDamage = 25
        elif rand >= 4 and rand <= 6:
            obstacleType = "spike"
            obstacleHealth = 75
            obstacleDamage = 60
        elif rand >= 7 and rand <= 9:
            obstacleType = "log"
            obstacleHealth = 25
            obstacleDamage = 5
        elif rand >= 10 and rand <= 12:
            obstacleType = "zombie"
            obstacleHealth = 100
            obstacleDamage = 150
        elif rand >= 13 and rand <= 15:
            obstacleType = "heal"
            obstacleHealth = 100
            obstacleDamage = -100
        
        if obstacles.__len__() > 0 and obstacles[-1][0].x < screen.screenWidth - (sprites.obstacles['width'] + 400):
            obstacle = pygame.Rect(screen.screenWidth, sprites.obstacles['y'], sprites.obstacles['width'], sprites.obstacles['height'])
            obstacles.append([obstacle, obstacleType, obstacleHealth, obstacleDamage])
        elif obstacles.__len__() == 0:
            obstacle = pygame.Rect(screen.screenWidth, sprites.obstacles['y'], sprites.obstacles['width'], sprites.obstacles['height'])
            obstacles.append([obstacle, obstacleType, obstacleHealth, obstacleDamage])


def moveObstacles():
    global score
    for obstacle in obstacles:
        if obstacle[0].x < (0 - sprites.obstacles['width']):
            obstacles.remove(obstacle)
        elif obstacle[2] <= 0:
            obstacles.remove(obstacle)
            score += obstacle[3] / 5
        else:
            obstacle[0].x -= obstacleSpeed


def createClouds():
    xdiff = 50
    if clouds.__len__() < 6:
        yname = "y1"
        newy = random.randint(0, 9)
        if newy >= 0 and newy <= 3:
            yname = "y1"
        elif newy >= 4 and newy <= 6:
            yname = "y2"
        elif newy >= 7 and newy <= 9:
            yname = "y3"

        if clouds.__len__() > 0 and clouds[-1].x <= (screen.screenWidth - sprites.cloud['width']) - xdiff:
            cloud = pygame.Rect(screen.screenWidth, sprites.cloud[yname], sprites.cloud['width'], sprites.cloud['height'])
            clouds.append(cloud)
        elif clouds.__len__() == 0:
            cloud = pygame.Rect(screen.screenWidth, sprites.cloud[yname], sprites.cloud['width'], sprites.cloud['height'])
            clouds.append(cloud)


def moveClouds():
    for cloud in clouds:
        if cloud.x < (0 - sprites.cloud['width']):
            clouds.remove(cloud)
        else:
            cloud.x -= 1


def createBullet():
    if bullets.__len__() < bulletMax:
        if bullets.__len__() > 0 and bullets[-1].x >= (userplayer.x + sprites.player['width'] + sprites.gun['width'] - 13 + 52):
            bullet = pygame.Rect(userplayer.x + sprites.player['width'] + sprites.gun['width'] - 13, (userplayer.y) + (userplayer.height / 2) - (sprites.gun['width'] / 4) + 8, sprites.bullet['width'], sprites.bullet['height'])
            bullets.append(bullet)
        elif bullets.__len__() == 0:
            bullet = pygame.Rect(userplayer.x + sprites.player['width'] + sprites.gun['width'] - 13, (userplayer.y) + (userplayer.height / 2) - (sprites.gun['width'] / 4) + 8, sprites.bullet['width'], sprites.bullet['height'])
            bullets.append(bullet)
        pygame.mixer.music.load(sounds.sounds['shoot'])
        pygame.mixer.music.play()


def moveBullet():
    for bullet in bullets:
        if bullet.x > (screen.screenWidth - sprites.bullet['width']):
            bullets.remove(bullet)
        else:
            bullet.x += 5


def bulletObstacleCollision():
    for bullet in bullets:
        for obstacle in obstacles:
            if bullet.colliderect(obstacle[0]):
                obstacle[2] -= 25
                bullets.remove(bullet)


def playerObstacleCollision(playerrect):
    global playerHealth
    for obstacle in obstacles:
        if playerrect.colliderect(obstacle[0]):
            playerHealth -= obstacle[3]
            if playerHealth > totalPlayerHealth:
                playerHealth = totalPlayerHealth
            elif playerHealth < 0:
                playerHealth = 0
            obstacles.remove(obstacle)

            if obstacle[1] == "heal":
                pygame.mixer.music.load(sounds.sounds['getheal'])
                pygame.mixer.music.play()
            else:
                pygame.mixer.music.load(sounds.sounds['hit'])
                pygame.mixer.music.play()


def makeHarder():
    global score, obstacleSpeed
    if score > 1000:
        obstacleSpeed += 1


def changePlayerCharacterChoice(left, right):
    global playerSpriteNumber
    if left == True:
        if playerSpriteNumber == 1:
            playerSpriteNumber = sprites.player['allsprites']
        elif playerSpriteNumber > 1:
            playerSpriteNumber -= 1
    elif right == True:
        if playerSpriteNumber == sprites.player['allsprites']:
            playerSpriteNumber = 1
        elif playerSpriteNumber < sprites.player['allsprites']:
            playerSpriteNumber += 1
    pygame.mixer.music.load(sounds.sounds['choose'])
    pygame.mixer.music.play()


def loadingScreenMain():
    loader = 1
    zombiex = screen.screenWidth - 110
    zombiemoveleft = True
    while screens['loadingScreen']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if loader < 800:
            loader = loader + 20
        else:
            screens['loadingScreen'] = False
            screens['endScreen'] = False
            screens['mainGame'] = False
            screens['pregameScreen'] = True
            pregameScreenMain()
        
        if zombiex <= 0:
            zombiemoveleft = False
        elif zombiex >= (screen.screenWidth - sprites.obstacles['width']):
            zombiemoveleft = True
        
        if zombiemoveleft == True:
            zombiex -= 10
        elif zombiemoveleft == False:
            zombiex += 10
        
        loading_draw_window(loader, zombiex)
        
    pygame.quit()


def pregameScreenMain():
    global playerSpriteNumber
    playerrect = pygame.Rect(250, 700, sprites.player['width'], sprites.player['height'])
    while screens['pregameScreen']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keypressed = pygame.key.get_pressed()
        leftClick = pygame.mouse.get_pressed()[0]

        if leftClick:
            mouse_x = pygame.mouse.get_pos()[0]
            mouse_y = pygame.mouse.get_pos()[1]
            if mouse_y > playerrect.y + 15 and mouse_y < playerrect.y + 85:
                if mouse_x > playerrect.x - 80 and mouse_x < playerrect.x - 10:
                    changePlayerCharacterChoice(True, False)
                elif mouse_x > playerrect.x + playerrect.width + 10 and mouse_x < playerrect.x + playerrect.width + 80:
                    changePlayerCharacterChoice(False, True)
                time.sleep(0.2)
                pygame.mixer.music.unload()
        
        if keypressed[pygame.K_LEFT]:
            changePlayerCharacterChoice(True, False)
            time.sleep(0.2)
        elif keypressed[pygame.K_RIGHT]:
            changePlayerCharacterChoice(False, True)
            time.sleep(0.2)
        
        if keypressed[pygame.K_RETURN]:
            screens['loadingScreen'] = False
            screens['endScreen'] = False
            screens['mainGame'] = True
            screens['pregameScreen'] = False
            pygame.mixer.music.load(sounds.sounds['select'])
            pygame.mixer.music.play()
            time.sleep(0.2)
            main()
        
        pregame_draw_window(playerrect)
        
    pygame.quit()


def main():
    global score, playerHealth
    score = 0
    playerHealth = totalPlayerHealth
    jumpheight = 20
    jumpvelocity = jumpheight
    gravity = 1
    run = True
    jumping = False
    playerrect = pygame.Rect(150, 700, sprites.player['width'], sprites.player['height'])
    pygame.mixer.music.unload()
    while screens['mainGame']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        leftClicked = pygame.mouse.get_pressed()[0]
        if leftClicked:
            createBullet()
        
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_SPACE]:
            jumping = True
            pygame.mixer.music.load(sounds.sounds['jump'])
            pygame.mixer.music.play()

        if jumping == True:
            playerrect.y -= round(jumpvelocity)
            jumpvelocity -= 0.5
            if jumpvelocity < -jumpheight:
                jumping = False
                jumpvelocity = jumpheight
                userplayer.setPlayery(playerrect.y)
        
        if score >= 5000:
            score = 0
        
        if playerHealth == 0:
            screens['loadingScreen'] = False
            screens['endScreen'] = True
            screens['mainGame'] = False
            screens['pregameScreen'] = False
            endScreenMain()

        playerHealthColorChange()
        createClouds()
        moveClouds()
        createObstacles()
        moveObstacles()
        moveBullet()
        bulletObstacleCollision()
        makeHarder()
        playerObstacleCollision(playerrect)

        draw_window(playerrect)
        
    pygame.quit()


def endScreenMain():
    while screens['endScreen']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keypressed = pygame.key.get_pressed()
        
        if keypressed[pygame.K_p]:
            screens['loadingScreen'] = False
            screens['endScreen'] = False
            screens['mainGame'] = False
            screens['pregameScreen'] = True
            pregameScreenMain()
        elif keypressed[pygame.K_e]:
            screens['loadingScreen'] = False
            screens['endScreen'] = False
            screens['mainGame'] = False
            screens['pregameScreen'] = False
            main()
        
        endscreen_draw_window()
        
    pygame.quit()


if __name__ == "__main__":
    loadingScreenMain()