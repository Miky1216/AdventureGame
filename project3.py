import pygame
import time
import random
import sys

class sprites(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect(x=x, y=y)
        self.imageMask = pygame.mask.from_surface(self.image)

class spriteNames:
    def __init__(self):
        self.hero = sprites('hero.png', 1, 1)
        self.meleeEnemy = sprites('meleeEnemy.png', 1, 1)
        self.powerUp = sprites('powerUp.png', 1, 1)
        self.fryingPan = sprites('fryingPan.png', 1, 1)
        self.backgroundImage1 = sprites('QuadImage1.png', 1, 1)
        self.backgroundImage2 = sprites('QuadImage2.png', 1, 1)
        self.backgroundImage3 = sprites('QuadImage3.png', 1, 1)
        self.backgroundImage4 = sprites('QuadImage4.png', 1, 1)

class userInput:
    def EnterHeroName(self):
        HeroName = ""
        while HeroName is "":
            HeroName = raw_input("Enter the name of your hero: ")
        return HeroName

class MapDesign:
    def GenerateRandomMap(self, sprite):
        RandomMapGenerator = random.randint(1,4)
        if RandomMapGenerator == 1:
            sprite.backgroundImage1.rect.topleft = (110, 80)
            sprite.backgroundImage2.rect.topleft = (820, 30)
            sprite.backgroundImage3.rect.topleft = (210, 510)
            sprite.backgroundImage4.rect.topleft = (750, 490)
        if RandomMapGenerator == 2:
            sprite.backgroundImage1.rect.topleft = (820, 30)
            sprite.backgroundImage2.rect.topleft = (110, 80)
            sprite.backgroundImage3.rect.topleft = (750, 490)
            sprite.backgroundImage4.rect.topleft = (210, 510)
        if RandomMapGenerator == 3:
            sprite.backgroundImage1.rect.topleft = (750, 490)
            sprite.backgroundImage2.rect.topleft = (210, 510)
            sprite.backgroundImage3.rect.topleft = (820, 30)
            sprite.backgroundImage4.rect.topleft = (110, 80)
        if RandomMapGenerator == 4:
            sprite.backgroundImage1.rect.topleft = (210, 510)
            sprite.backgroundImage2.rect.topleft = (750, 490)
            sprite.backgroundImage3.rect.topleft = (110, 80)
            sprite.backgroundImage4.rect.topleft = (820, 30)

class GameLoop:
    def display(self, screen, sprite):
        screen.blit(sprite.hero.image, sprite.hero.rect.topleft)
        screen.blit(sprite.meleeEnemy.image, sprite.meleeEnemy.rect.topleft)
        #screen.blit(powerUp.image, powerUp.rect.topleft)
        screen.blit(sprite.backgroundImage1.image, sprite.backgroundImage1.rect.topleft)
        screen.blit(sprite.backgroundImage2.image, sprite.backgroundImage2.rect.topleft)
        screen.blit(sprite.backgroundImage3.image, sprite.backgroundImage3.rect.topleft)
        screen.blit(sprite.backgroundImage4.image, sprite.backgroundImage4.rect.topleft)
        pygame.display.update()
    def meleeAttack(self, direction, lead_x, lead_y, screen, sprite):
        pass
    def rangeAttack(self, direction, lead_x, lead_y, screen, sprite):
        sprite.fryingPan.rect = sprite.fryingPan.image.get_rect()
        if direction == 1:
            for lead_y in range (lead_y, 0, -1):
                sprite.fryingPan.rect.topleft = (lead_x, lead_y)
                screen.fill((255,255,255))
                screen.blit(sprite.fryingPan.image, sprite.fryingPan.rect.topleft)
                self.display(screen, sprite)
        if direction == 2:
            for lead_x in range (lead_x, 1200):
                sprite.fryingPan.rect.topleft = (lead_x, lead_y)
                screen.fill((255,255,255))
                screen.blit(sprite.fryingPan.image, sprite.fryingPan.rect.topleft)
                self.display(screen, sprite)
        if direction == 3:
            for lead_y in range (lead_y, 800):
                sprite.fryingPan.rect.topleft = (lead_x, lead_y)
                screen.fill((255,255,255))
                screen.blit(sprite.fryingPan.image, sprite.fryingPan.rect.topleft)
                self.display(screen, sprite)
        if direction == 4:
            for lead_x in range (lead_x, 0, -1):
                sprite.fryingPan.rect.topleft = (lead_x, lead_y)
                screen.fill((255,255,255))
                screen.blit(sprite.fryingPan.image, sprite.fryingPan.rect.topleft)
                self.display(screen, sprite)
    def AOEAttack(self, direction, lead_x, lead_y, screen, sprite):
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
        gameExit = False
        heroMelee = False
        heroRanged = True
        heroAOE = False

        #hero = sprites('hero.png', 1, 1)
        #meleeEnemy = sprites('meleeEnemy.png', 1, 1)
        #powerUp = sprites('powerUp.png', 1, 1)
        #backgroundImage1 = sprites('QuadImage1.png', 1, 1)
        #backgroundImage2 = sprites('QuadImage2.png', 1, 1)
        #backgroundImage3 = sprites('QuadImage3.png', 1, 1)
        #backgroundImage4 = sprites('QuadImage4.png', 1, 1)

        lead_x = 200
        lead_y = 400
        lead_x_change = 0
        lead_y_change = 0
        pixelMove = 10
        direction = 2

        sprite = spriteNames()
        sprite.meleeEnemy.rect.topleft = (800, 400)
        sprite.powerUp.rect.topleft = (400, 400)
        screen.fill((255,255,255))

        GenerateRandomBackground = MapDesign()
        RandomMapGenerator = GenerateRandomBackground.GenerateRandomMap(sprite)
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
                            self.meleeAttack(direction, lead_x, lead_y, screen, sprite)
                        if heroRanged:
                            self.rangeAttack(direction, lead_x, lead_y, screen, sprite)
                        if heroAOE:
                            self.AOEAttack(direction, lead_x, lead_y, screen, sprite)

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
 
            sprite.hero.rect.topleft = (lead_x, lead_y)
            screen.fill((255,255,255))
            self.display(screen, sprite)

            #Vertical Line
            #pygame.draw.line(screen, color.black, [LinePointX1, LinePointY1], [LinePointX2, LinePointY2], LineThickness)
            #Horizontal Line
            #pygame.draw.line(screen, color.black, [LinePointX3, LinePointY3], [LinePointX4, LinePointY4], LineThickness)

            offset_x, offset_y = (sprite.meleeEnemy.rect.left - sprite.hero.rect.left), (sprite.meleeEnemy.rect.top - sprite.hero.rect.top) 
            if (sprite.hero.imageMask.overlap(sprite.meleeEnemy.imageMask, (offset_x, offset_y)) != None):
                print 'Collision Detected!'
            else:
                print 'None'
            offset_x, offset_y = (sprite.backgroundImage1.rect.left - sprite.hero.rect.left), (sprite.backgroundImage1.rect.top - sprite.hero.rect.top)
            if (sprite.hero.imageMask.overlap(sprite.backgroundImage1.imageMask, (offset_x, offset_y)) != None):
                print 'Collision Detected!'
            else:
                print 'None'
            offset_x, offset_y = (sprite.backgroundImage2.rect.left - sprite.hero.rect.left), (sprite.backgroundImage2.rect.top - sprite.hero.rect.top)
            if (sprite.hero.imageMask.overlap(sprite.backgroundImage2.imageMask, (offset_x, offset_y)) != None):
                print 'Collision Detected!'
            else:
                print 'None'
            offset_x, offset_y = (sprite.backgroundImage3.rect.left - sprite.hero.rect.left), (sprite.backgroundImage3.rect.top - sprite.hero.rect.top)
            if (sprite.hero.imageMask.overlap(sprite.backgroundImage3.imageMask, (offset_x, offset_y)) != None):
                print 'Collision Detected!'
            else:
                print 'None'
            offset_x, offset_y = (sprite.backgroundImage4.rect.left - sprite.hero.rect.left), (sprite.backgroundImage4.rect.top - sprite.hero.rect.top)
            if (sprite.hero.imageMask.overlap(sprite.backgroundImage4.imageMask, (offset_x, offset_y)) != None):
                print 'Collision Detected!'
            else:
                print 'None'

            clock.tick(FPS)

if __name__ == "__main__":
    StartProgram = GameLoop()
    StartProgram.RunGame()
