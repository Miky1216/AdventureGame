import pygame
import time
import random
import sys

class sprites(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        color = colors()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey(color.white)
        self.rect = self.image.get_rect(x=x, y=y)
        self.imageMask = pygame.mask.from_surface(self.image)

class colors:
    def __init__(self):
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.red = (255,0,0)

class userInput:
    def EnterHeroName(self):
        HeroName = ""
        while HeroName == "":
            HeroName = raw_input("Enter the name of your hero: ")
        return HeroName

class MapDesign:
    def GenerateRandomMap(self, backgroundSpaceRect, backgroundJakeHimselfRect, backgroundIceKingRect, backgroundFinnRect, backgroundJakeFinnRect, backgroundFinnUnicornRect, backgroundPenguinRect, backgroundCupcakeRect, backgroundPurpleCloudRect, backgroundVampireRect, backgroundPrincessRect):
        """backgroundSpace.topleft = (0,0)
        backgroundImage1Rect.topleft = (110, 80)
        backgroundImage2Rect.topleft = (620, 50)
        backgroundImage3Rect.topleft = (80, 400)
        backgroundImage4Rect.topleft = (650, 410)
        backgroundImage5Rect.topleft = (350, 500)
        backgroundImage6Rect.topleft = (50, 650)
        backgroundImage7Rect.topleft = (900, 550)
        backgroundImage8Rect.topleft = (950, 275)
        backgroundImage9Rect.topleft = (500, 275)
        backgroundImage10Rect.topleft = (665, 600)"""
         
        RandomMapGenerator = random.randint(1,4)
        if RandomMapGenerator == 1:
            backgroundJakeHimselfRect.topleft = (110, 80)
            backgroundIceKingRect.topleft = (620, 30)
            backgroundFinnRect.topleft = (980, 80)
            backgroundJakeFinnRect.topleft = (650, 360)
            backgroundFinnUnicornRect.topleft = (325, 600)
            backgroundPenguinRect.topleft = (50, 450)
            backgroundCupcakeRect.topleft = (900, 550)
            backgroundPurpleCloudRect.topleft = (950, 275)
            backgroundVampireRect.topleft = (500, 275)
            backgroundPrincessRect.topleft = (665, 600)
        if RandomMapGenerator == 2:
            backgroundJakeHimselfRect.topleft = (820, 30)
            backgroundIceKingRect.topleft = (110, 80)
            backgroundFinnRect.topleft = (750, 300)
            backgroundJakeFinnRect.topleft = (160, 385)
            backgroundFinnUnicornRect.topleft = (100, 630)
            backgroundPenguinRect.topleft = (350, 200)
            backgroundCupcakeRect.topleft = (950, 275)
            backgroundPurpleCloudRect.topleft = (900, 550)
            backgroundVampireRect.topleft = (465, 600)
            backgroundPrincessRect.topleft = (650, 490)
        if RandomMapGenerator == 3:
            backgroundJakeHimselfRect.topleft = (700, 40)
            backgroundIceKingRect.topleft = (210, 510)
            backgroundFinnRect.topleft = (980, 30)
            backgroundJakeFinnRect.topleft = (110, 80)
            backgroundFinnUnicornRect.topleft = (405, 440)
            backgroundPenguinRect.topleft = (50, 350)
            backgroundCupcakeRect.topleft = (825, 520)
            backgroundPurpleCloudRect.topleft = (950, 275)
            backgroundVampireRect.topleft = (500, 175)
            backgroundPrincessRect.topleft = (635, 600)
        if RandomMapGenerator == 4:
            backgroundJakeHimselfRect.topleft = (160, 340)
            backgroundIceKingRect.topleft = (880, 510)
            backgroundFinnRect.topleft = (110, 80)
            backgroundJakeFinnRect.topleft = (820, 30)
            backgroundFinnUnicornRect.topleft = (350, 490)
            backgroundPenguinRect.topleft = (120, 550)
            backgroundCupcakeRect.topleft = (870, 285)
            backgroundPurpleCloudRect.topleft = (370, 80)
            backgroundVampireRect.topleft = (590, 275)
            backgroundPrincessRect.topleft = (680, 530)


class GameLoop:
    def meleeAttack(self, direction, lead_x, lead_y, screen):
        pass
    def rangeAttack(self, direction, lead_x, lead_y, screen):
        color = colors()
        fryingPan = sprites('fryingPan.png', 1, 1)
        fryingPanRect = fryingPan.image.get_rect()
        if direction == 1:
            for lead_y in range (lead_y, 0, -1):
                fryingPanRect.topleft = (lead_x, lead_y)
                screen.fill((color.white))
                screen.blit(fryingPan.image, fryingPanRect.topleft)
                pygame.display.update()
        if direction == 2:
            for lead_x in range (lead_x, 1200):
                fryingPanRect.topleft = (lead_x, lead_y)
                screen.fill((color.white))
                screen.blit(fryingPan.image, fryingPanRect.topleft)
                pygame.display.update()
        if direction == 3:
            for lead_y in range (lead_y, 800):
                fryingPanRect.topleft = (lead_x, lead_y)
                screen.fill((color.white))
                screen.blit(fryingPan.image, fryingPanRect.topleft)
                pygame.display.update()
        if direction == 4:
            for lead_x in range (lead_x, 0, -1):
                fryingPanRect.topleft = (lead_x, lead_y)
                screen.fill((color.white))
                screen.blit(fryingPan.image, fryingPanRect.topleft)
                pygame.display.update()
    def AOEAttack(self, direction, lead_x, lead_y, screen):
        pass
    def RunGame(self):
        LinePointX1 = 600
        LinePointY1 = 0
        LinePointX2 = 600
        LinePointY2 = 800

        LineThickness = 1

        LinePointX3 = 0
        LinePointY3 = 400
        LinePointX4 = 1200
        LinePointY4 = 400

        pygame.init()

        displayWidth = 1200
        displayHeight = 800
        pygame.display.set_caption('Bacon Pancakes!')
        screen = pygame.display.set_mode([displayWidth, displayHeight])
        clock = pygame.time.Clock()

        FPS = 30
        color = colors()
        gameExit = False
        heroMelee = False
        heroRanged = True
        heroAOE = False

        backgroundSpace = sprites('space.png', 1, 1)
        hero = sprites('hero.png', 1, 1)
        meleeEnemy = sprites('meleeEnemy.png', 1, 1)
        powerUp = sprites('powerUp.png', 1, 1)
        backgroundJakeHimself = sprites('QuadImage1.png', 1, 1)
        backgroundIceKing = sprites('QuadImage2.png', 1, 1)
        backgroundFinn = sprites('QuadImage3.png', 1, 1)
        backgroundJakeFinn = sprites('QuadImage4.png', 1, 1)
        backgroundFinnUnicorn = sprites('QuadImage5.png', 1, 1)
        backgroundPenguin = sprites('QuadImage6.png', 1, 1)
        backgroundCupcake = sprites('QuadImage7.png', 1, 1)
        backgroundPurpleCloud = sprites('QuadImage8.png', 1, 1)
        backgroundVampire = sprites('QuadImage9.png', 1, 1)
        backgroundPrincess = sprites('QuadImage10.png', 1, 1)
        lead_x = 10
        lead_y = 10
        lead_x_change = 0
        lead_y_change = 0
        pixelMove = 10
        direction = 1

        heroRect = hero.image.get_rect()
        meleeEnemyRect = meleeEnemy.image.get_rect()
        powerUpRect = powerUp.image.get_rect()
        backgroundSpaceRect = backgroundSpace.image.get_rect()
        backgroundJakeHimselfRect = backgroundJakeHimself.image.get_rect()
        backgroundIceKingRect = backgroundIceKing.image.get_rect()
        backgroundFinnRect = backgroundFinn.image.get_rect()
        backgroundJakeFinnRect = backgroundJakeFinn.image.get_rect()
        backgroundFinnUnicornRect = backgroundFinnUnicorn.image.get_rect()
        backgroundPenguinRect = backgroundPenguin.image.get_rect()
        backgroundCupcakeRect = backgroundCupcake.image.get_rect()
        backgroundPurpleCloudRect = backgroundPurpleCloud.image.get_rect()
        backgroundVampireRect = backgroundVampire.image.get_rect()
        backgroundPrincessRect = backgroundPrincess.image.get_rect()

        heroRect.topleft = (0, 400)
        meleeEnemyRect.topleft = (50, 50)
        #powerUpRect.topleft = (600, 600)
        
        GenerateRandomBackground = MapDesign()
        RandomMapGenerator = GenerateRandomBackground.GenerateRandomMap(backgroundSpaceRect, backgroundJakeHimselfRect, backgroundIceKingRect, backgroundFinnRect, backgroundJakeFinnRect, backgroundFinnUnicornRect, backgroundPenguinRect, backgroundCupcakeRect, backgroundPurpleCloudRect, backgroundVampireRect, backgroundPrincessRect)
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        lead_x_change = -pixelMove
                        direction = 4
                    elif event.key == pygame.K_RIGHT:
                        lead_x_change = pixelMove
                        direction = 2
                    elif event.key == pygame.K_UP:
                        lead_y_change = -pixelMove
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        lead_y_change = pixelMove
                        direction = 3
                    elif event.key == pygame.K_SPACE:
                        if heroMelee:
                            self.meleeAttack(direction, lead_x, lead_y, screen)
                        if heroRanged:
                            self.rangeAttack(direction, lead_x, lead_y, screen)
                        if heroAOE:
                            self.AOEAttack(direction, lead_x, lead_y, screen)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        lead_x_change = 0
                        lead_y_change = 0

            lead_x += lead_x_change
            lead_y += lead_y_change
            if lead_x >= displayWidth:
                lead_x = displayWidth-pixelMove
            if lead_y >= displayHeight:
                lead_y = displayHeight-50
            if lead_x <= 0:
                lead_x = 0
            if lead_y <= 0:
                lead_y = 0

            #meleeEnemyRect.topleft = pygame.mouse.get_pos()
            heroRect.topleft = (lead_x, lead_y)

            screen.blit(backgroundSpace.image, backgroundSpaceRect.topleft)
            #screen.fill(color.white)
            screen.blit(hero.image, heroRect.topleft)
            screen.blit(meleeEnemy.image, meleeEnemyRect.topleft)
            screen.blit(powerUp.image, powerUpRect.topleft)
            screen.blit(backgroundJakeHimself.image, backgroundJakeHimselfRect.topleft)
            screen.blit(backgroundIceKing.image, backgroundIceKingRect.topleft)
            screen.blit(backgroundFinn.image, backgroundFinnRect.topleft)
            screen.blit(backgroundJakeFinn.image, backgroundJakeFinnRect.topleft)
            screen.blit(backgroundFinnUnicorn.image, backgroundFinnUnicornRect.topleft)
            screen.blit(backgroundPenguin.image, backgroundPenguinRect.topleft)
            screen.blit(backgroundCupcake.image, backgroundCupcakeRect.topleft)
            screen.blit(backgroundPurpleCloud.image, backgroundPurpleCloudRect.topleft)
            screen.blit(backgroundVampire.image, backgroundVampireRect.topleft)
            screen.blit(backgroundPrincess.image, backgroundPrincessRect.topleft)
            
            #Vertical Line
            #pygame.draw.line(screen, color.black, [LinePointX1, LinePointY1], [LinePointX2, LinePointY2], LineThickness)
            #Horizontal Line
            #pygame.draw.line(screen, color.black, [LinePointX3, LinePointY3], [LinePointX4, LinePointY4], LineThickness)

            offset_x, offset_y = (meleeEnemyRect.left - heroRect.left), (meleeEnemyRect.top - heroRect.top)
            if (hero.imageMask.overlap(meleeEnemy.imageMask, (offset_x, offset_y)) != None):
                lead_x -= lead_x_change
                lead_y -= lead_y_change
                print 'Collision Detected!'
            offset_x, offset_y = (backgroundJakeHimselfRect.left - heroRect.left), (backgroundJakeHimselfRect.top - heroRect.top)
            if (hero.imageMask.overlap(backgroundJakeHimself.imageMask, (offset_x, offset_y)) != None):
                lead_x -= lead_x_change
                lead_y -= lead_y_change
                print 'Collision Detected!'
            offset_x, offset_y = (backgroundIceKingRect.left - heroRect.left), (backgroundIceKingRect.top - heroRect.top)
            if (hero.imageMask.overlap(backgroundIceKing.imageMask, (offset_x, offset_y)) != None):
                lead_x -= lead_x_change
                lead_y -= lead_y_change
                print 'Collision Detected!'
            offset_x, offset_y = (backgroundFinnRect.left - heroRect.left), (backgroundFinnRect.top - heroRect.top)
            if (hero.imageMask.overlap(backgroundFinn.imageMask, (offset_x, offset_y)) != None):
                lead_x -= lead_x_change
                lead_y -= lead_y_change
                print 'Collision Detected!'
            offset_x, offset_y = (backgroundJakeFinnRect.left - heroRect.left), (backgroundJakeFinnRect.top - heroRect.top)
            if (hero.imageMask.overlap(backgroundJakeFinn.imageMask, (offset_x, offset_y)) != None):
                lead_x -= lead_x_change
                lead_y -= lead_y_change
                print 'Collision Detected!'

            pygame.display.update()
            clock.tick(FPS)

if __name__ == "__main__":
    StartProgram = GameLoop()
    StartProgram.RunGame()