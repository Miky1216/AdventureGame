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
    def GenerateRandomMap(self, backgroundImage1Rect, backgroundImage2Rect, backgroundImage3Rect, backgroundImage4Rect):
        #Quad1Coordinates = pygame.draw.rect(gameDisplay, white, [0,0])
        #Quad2Coordinates = pygame.draw.rect(gameDisplay, white, [400,0])
        #Quad3Coordinates = pygame.draw.rect(gameDisplay, white, [0,300])
        #Quad4Coordinates = pygame.draw.rect(gameDisplay, white, [400,600])

        backgroundImage1Rect.topleft = (110, 80)
        backgroundImage2Rect.topleft = (820, 30)
        backgroundImage3Rect.topleft = (210, 510)
        backgroundImage4Rect.topleft = (750, 490)
        RandomMapGenerator = random.randint(1,4)
        if RandomMapGenerator == 1:
            backgroundImage1Rect.topleft = (110, 80)
            backgroundImage2Rect.topleft = (820, 30)
            backgroundImage3Rect.topleft = (210, 510)
            backgroundImage4Rect.topleft = (750, 490)
        if RandomMapGenerator == 2:
            backgroundImage1Rect.topleft = (820, 30)
            backgroundImage2Rect.topleft = (110, 80)
            backgroundImage3Rect.topleft = (750, 490)
            backgroundImage4Rect.topleft = (210, 510)
        if RandomMapGenerator == 3:
            backgroundImage1Rect.topleft = (750, 490)
            backgroundImage2Rect.topleft = (210, 510)
            backgroundImage3Rect.topleft = (820, 30)
            backgroundImage4Rect.topleft = (110, 80)
        if RandomMapGenerator == 4:
            backgroundImage1Rect.topleft = (210, 510)
            backgroundImage2Rect.topleft = (750, 490)
            backgroundImage3Rect.topleft = (110, 80)
            backgroundImage4Rect.topleft = (820, 30)


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

        hero = sprites('hero.png', 1, 1)
        meleeEnemy = sprites('meleeEnemy.png', 1, 1)
        powerUp = sprites('powerUp.png', 1, 1)
        backgroundImage1 = sprites('QuadImage1.png', 1, 1)
        backgroundImage2 = sprites('QuadImage2.png', 1, 1)
        backgroundImage3 = sprites('QuadImage3.png', 1, 1)
        backgroundImage4 = sprites('QuadImage4.png', 1, 1)

        lead_x = 10
        lead_y = 10
        lead_x_change = 0
        lead_y_change = 0
        pixelMove = 10
        direction = 1

        heroRect = hero.image.get_rect()
        meleeEnemyRect = meleeEnemy.image.get_rect()
        powerUpRect = powerUp.image.get_rect()
        backgroundImage1Rect = backgroundImage1.image.get_rect()
        backgroundImage2Rect = backgroundImage2.image.get_rect()
        backgroundImage3Rect = backgroundImage3.image.get_rect()
        backgroundImage4Rect = backgroundImage4.image.get_rect()

        heroRect.topleft = (0, 400)
        meleeEnemyRect.topleft = (50, 50)
        powerUpRect.topleft = (600, 600)
        backgroundImage1Rect.topleft = (110, 80)
        backgroundImage2Rect.topleft = (820, 30)
        backgroundImage3Rect.topleft = (210, 510)
        backgroundImage4Rect.topleft = (750, 490)

        GenerateRandomBackground = MapDesign()
        RandomMapGenerator = GenerateRandomBackground.GenerateRandomMap(backgroundImage1Rect, backgroundImage2Rect, backgroundImage3Rect, backgroundImage4Rect)
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

            screen.fill(color.white)
            screen.blit(hero.image, heroRect.topleft)
            screen.blit(meleeEnemy.image, meleeEnemyRect.topleft)
            screen.blit(powerUp.image, powerUpRect.topleft)
            screen.blit(backgroundImage1.image, backgroundImage1Rect.topleft)
            screen.blit(backgroundImage2.image, backgroundImage2Rect.topleft)
            screen.blit(backgroundImage3.image, backgroundImage3Rect.topleft)
            screen.blit(backgroundImage4.image, backgroundImage4Rect.topleft)

            #Vertical Line
            pygame.draw.line(screen, color.black, [LinePointX1, LinePointY1], [LinePointX2, LinePointY2], LineThickness)
            #Horizontal Line
            pygame.draw.line(screen, color.black, [LinePointX3, LinePointY3], [LinePointX4, LinePointY4], LineThickness)

            offset_x, offset_y = (meleeEnemyRect.left - heroRect.left), (meleeEnemyRect.top - heroRect.top)
            if (hero.imageMask.overlap(meleeEnemy.imageMask, (offset_x, offset_y)) != None):
                lead_x -= lead_x_change
                lead_y -= lead_y_change
                print 'Collision Detected!'
            offset_x, offset_y = (backgroundImage1Rect.left - heroRect.left), (backgroundImage1Rect.top - heroRect.top)
            if (hero.imageMask.overlap(backgroundImage1.imageMask, (offset_x, offset_y)) != None):
                lead_x -= lead_x_change
                lead_y -= lead_y_change
                print 'Collision Detected!'
            offset_x, offset_y = (backgroundImage2Rect.left - heroRect.left), (backgroundImage2Rect.top - heroRect.top)
            if (hero.imageMask.overlap(backgroundImage2.imageMask, (offset_x, offset_y)) != None):
                lead_x -= lead_x_change
                lead_y -= lead_y_change
                print 'Collision Detected!'
            offset_x, offset_y = (backgroundImage3Rect.left - heroRect.left), (backgroundImage3Rect.top - heroRect.top)
            if (hero.imageMask.overlap(backgroundImage3.imageMask, (offset_x, offset_y)) != None):
                lead_x -= lead_x_change
                lead_y -= lead_y_change
                print 'Collision Detected!'
            offset_x, offset_y = (backgroundImage4Rect.left - heroRect.left), (backgroundImage4Rect.top - heroRect.top)
            if (hero.imageMask.overlap(backgroundImage4.imageMask, (offset_x, offset_y)) != None):
                lead_x -= lead_x_change
                lead_y -= lead_y_change
                print 'Collision Detected!'

            pygame.display.update()
            clock.tick(FPS)

if __name__ == "__main__":
    StartProgram = GameLoop()
    StartProgram.RunGame()
