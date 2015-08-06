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
        self.backgroundSpace = sprites('space.png', 1, 1)
        self.hero = sprites('hero.png', 1, 1)
        self.meleeEnemy = sprites('meleeEnemy.png', 1, 1)
        self.powerUp = sprites('powerUp.png', 1, 1)
        self.fryingPan = sprites('fryingPan.png', 1, 1)
        self.backgroundImage1 = sprites('QuadImage1.png', 1, 1)
        self.backgroundJakeHimself = sprites('QuadImage1.png', 1, 1)
        self.backgroundIceKing = sprites('QuadImage2.png', 1, 1)
        self.backgroundFinn = sprites('QuadImage3.png', 1, 1)
        self.backgroundJakeFinn = sprites('QuadImage4.png', 1, 1)
        self.backgroundFinnUnicorn = sprites('QuadImage5.png', 1, 1)
        self.backgroundPenguin = sprites('QuadImage6.png', 1, 1)
        self.backgroundCupcake = sprites('QuadImage7.png', 1, 1)
        self.backgroundPurpleCloud = sprites('QuadImage8.png', 1, 1)
        self.backgroundVampire = sprites('QuadImage9.png', 1, 1)
        self.backgroundPrincess = sprites('QuadImage10.png', 1, 1)

class userInput:
    def EnterHeroName(self):
        HeroName = ""
        while HeroName is "":
            HeroName = raw_input("Enter the name of your hero: ")
        return HeroName

class MapDesign:
    def GenerateRandomMap(self, sprite):
        RandomMapGenerator = random.randint(1,2)
        if RandomMapGenerator == 1:
            sprite.backgroundJakeHimself.rect.topleft = (110, 80)
            sprite.backgroundIceKing.rect.topleft = (620, 30)
            sprite.backgroundFinn.rect.topleft = (980, 80)
            sprite.backgroundJakeFinn.rect.topleft = (650, 410)
            sprite.backgroundFinnUnicorn.rect.topleft = (350, 500)
            sprite.backgroundPenguin.rect.topleft = (50, 450)
            sprite.backgroundCupcake.rect.topleft = (900, 600)
            sprite.backgroundPurpleCloud.rect.topleft = (950, 275)
            sprite.backgroundVampire.rect.topleft = (500, 275)
            sprite.backgroundPrincess.rect.topleft = (665, 600)
        if RandomMapGenerator == 2:
            sprite.backgroundJakeHimself.rect.topleft = (820, 30)
            sprite.backgroundIceKing.rect.topleft = (110, 80)
            sprite.backgroundFinn.rect.topleft = (750, 300)
            sprite.backgroundJakeFinn.rect.topleft = (210, 510)
            sprite.backgroundFinnUnicorn.rect.topleft = (50, 650)
            sprite.backgroundPenguin.rect.topleft = (350, 500)
            sprite.backgroundCupcake.rect.topleft = (950, 275)
            sprite.backgroundPurpleCloud.rect.topleft = (1000, 500)
            sprite.backgroundVampire.rect.topleft = (665, 600)
            sprite.backgroundPrincess.rect.topleft = (500, 275)

class GameLoop:
    def display(self, screen, sprite):
        screen.blit(sprite.hero.image, sprite.hero.rect.topleft)
        screen.blit(sprite.meleeEnemy.image, sprite.meleeEnemy.rect.topleft)
        screen.blit(sprite.hero.image, sprite.hero.rect.topleft)
        screen.blit(sprite.meleeEnemy.image, sprite.meleeEnemy.rect.topleft)
        #screen.blit(sprite.powerUp.image, sprite.powerUp.rect.topleft)
        screen.blit(sprite.backgroundJakeHimself.image, sprite.backgroundJakeHimself.rect.topleft)
        screen.blit(sprite.backgroundIceKing.image, sprite.backgroundIceKing.rect.topleft)
        screen.blit(sprite.backgroundFinn.image, sprite.backgroundFinn.rect.topleft)
        screen.blit(sprite.backgroundJakeFinn.image, sprite.backgroundJakeFinn.rect.topleft)
        screen.blit(sprite.backgroundFinnUnicorn.image, sprite.backgroundFinnUnicorn.rect.topleft)
        screen.blit(sprite.backgroundPenguin.image, sprite.backgroundPenguin.rect.topleft)
        screen.blit(sprite.backgroundCupcake.image, sprite.backgroundCupcake.rect.topleft)
        screen.blit(sprite.backgroundPurpleCloud.image, sprite.backgroundPurpleCloud.rect.topleft)
        screen.blit(sprite.backgroundVampire.image, sprite.backgroundVampire.rect.topleft)
        screen.blit(sprite.backgroundPrincess.image, sprite.backgroundPrincess.rect.topleft)
        pygame.display.update()
    def meleeAttack(self, direction, screen, sprite):
        pass
    def rangeAttack(self, direction, screen, sprite):
        sprite.fryingPan.rect = sprite.fryingPan.image.get_rect()
        x = sprite.hero.rect.topleft[0]
        y = sprite.hero.rect.topleft[1]
        if direction == 1:
            for y in range (y, 0, -10):
                sprite.fryingPan.rect.topleft = (sprite.hero.rect.topleft[0], y)
                screen.blit(sprite.backgroundSpace.image, sprite.backgroundSpace.rect.topleft)
                screen.blit(sprite.fryingPan.image, sprite.fryingPan.rect.topleft)
                self.display(screen, sprite)
        if direction == 2:
            for x in range (x, 1200, 10):
                sprite.fryingPan.rect.topleft = (x, y)
                screen.blit(sprite.backgroundSpace.image, sprite.backgroundSpace.rect.topleft)
                screen.blit(sprite.fryingPan.image, sprite.fryingPan.rect.topleft)
                self.display(screen, sprite)
        if direction == 3:
            for y in range (y, 800, 10):
                sprite.fryingPan.rect.topleft = (x, y)
                screen.blit(sprite.backgroundSpace.image, sprite.backgroundSpace.rect.topleft)
                screen.blit(sprite.fryingPan.image, sprite.fryingPan.rect.topleft)
                self.display(screen, sprite)
        if direction == 4:
            for x in range (x, 0, -10):
                sprite.fryingPan.rect.topleft = (x, y)
                screen.blit(sprite.backgroundSpace.image, sprite.backgroundSpace.rect.topleft)
                screen.blit(sprite.fryingPan.image, sprite.fryingPan.rect.topleft)
                self.display(screen, sprite)
    def AOEAttack(self, direction, screen, sprite):
        pass
    def RunGame(self):
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
        lead_x_change = 0
        lead_y_change = 0
        pixelMove = 10
        direction = 2
        sprite = spriteNames()
        sprite.hero.rect.topleft = (200,400)
        sprite.meleeEnemy.rect.topleft = (800, 400)
        sprite.powerUp.rect.topleft = (400, 400)
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
                            self.meleeAttack(direction, screen, sprite)
                        if heroRanged:
                            self.rangeAttack(direction, screen, sprite)
                        if heroAOE:
                            self.AOEAttack(direction, screen, sprite)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        lead_x_change = 0
                        lead_y_change = 0

            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0] + lead_x_change, sprite.hero.rect.topleft[1])
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0], sprite.hero.rect.topleft[1] + lead_y_change)
            
            if sprite.hero.rect.topleft[0] >= displayWidth:
                sprite.hero.rect.topleft[0] = displayWidth-pixelMove
            if sprite.hero.rect.topleft[1] >= displayHeight:
                sprite.hero.rect.topleft[1] = displayHeight-50
            if sprite.hero.rect.topleft[0] <= 0:
                sprite.hero.rect.topleft = (0, sprite.hero.rect.topleft[1])
            if sprite.hero.rect.topleft[1] <= 0:
                sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0],0)
            
            screen.blit(sprite.backgroundSpace.image, sprite.backgroundSpace.rect.topleft)
            self.display(screen, sprite)

            offset_x, offset_y = (sprite.meleeEnemy.rect.left - sprite.hero.rect.left), (sprite.meleeEnemy.rect.top - sprite.hero.rect.top) 
            if (sprite.hero.imageMask.overlap(sprite.meleeEnemy.imageMask, (offset_x, offset_y)) != None):
                print 'Collision Detected!'
            offset_x, offset_y = (sprite.backgroundJakeHimself.rect.left - sprite.hero.rect.left), (sprite.backgroundJakeHimself.rect.top - sprite.hero.rect.top)
            if (sprite.hero.imageMask.overlap(sprite.backgroundJakeHimself.imageMask, (offset_x, offset_y)) != None):
                print 'Collision Detected!'
            offset_x, offset_y = (sprite.backgroundIceKing.rect.left - sprite.hero.rect.left), (sprite.backgroundIceKing.rect.top - sprite.hero.rect.top)
            if (sprite.hero.imageMask.overlap(sprite.backgroundIceKing.imageMask, (offset_x, offset_y)) != None):
                print 'Collision Detected!'
            offset_x, offset_y = (sprite.backgroundFinn.rect.left - sprite.hero.rect.left), (sprite.backgroundFinn.rect.top - sprite.hero.rect.top)
            if (sprite.hero.imageMask.overlap(sprite.backgroundFinn.imageMask, (offset_x, offset_y)) != None):
                print 'Collision Detected!'
            offset_x, offset_y = (sprite.backgroundJakeFinn.rect.left - sprite.hero.rect.left), (sprite.backgroundJakeFinn.rect.top - sprite.hero.rect.top)
            if (sprite.hero.imageMask.overlap(sprite.backgroundJakeFinn.imageMask, (offset_x, offset_y)) != None):
                print 'Collision Detected!'

            clock.tick(FPS)

if __name__ == "__main__":
    StartProgram = GameLoop()
    StartProgram.RunGame()
