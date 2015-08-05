import pygame
import time
import random
import sys

class sprites(pygame.sprite.Sprite):
    def __init__(self, image, x, y, color):
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
        while HeroName is "":
            HeroName = raw_input("Enter the name of your hero: ")
        return HeroName

class GameBackground:
    def DesignedBackground(self):
        pass
    def FirstQuadrantBackground(self):
        pass
    def SecondQuadrantBackground(self): 
        pass
    def ThirdQuadrantBackground(self):
        pass
    def FourthQuadrantBackground(self):
        pass

class GameLoop:
    def meleeAttack(self):
        pass
    def rangeAttack(self):
        pass
    def AOEAttack(self):
        pass
    def RunGame(self):
        pygame.init()

        displayWidth = 1200
        displayHeight = 800
        pygame.display.set_caption('Bacon Pancakes!')
        screen = pygame.display.set_mode([displayWidth, displayHeight])
        clock = pygame.time.Clock()

        FPS = 30
        color = colors()
        gameExit = False
        heroFire = False
        heroMelee = False
        heroRanged = False
        heroAOE = False

        hero = sprites('hero.png', 1, 1, color)
        enemy = sprites('meleeEnemy.png', 1, 1, color)
        powerUp = sprites('powerUp.png', 1, 1, color)
        #PlayerName = UserInput()

        lead_x = 300
        lead_y = 300
        lead_x_change = 0
        lead_y_change = 0
        pixelMove = 10
        
        heroRect = hero.image.get_rect()
        enemyRect = enemy.image.get_rect()
        powerUpRect = powerUp.image.get_rect()

        heroRect.topleft = (0, 400)
        enemyRect.topleft = (0, 0)
        powerUpRect.topleft = (600, 600)
        
        pygame.mouse.set_visible(False)
 
        while not gameExit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        lead_x_change = -pixelMove
                    elif event.key == pygame.K_RIGHT:
                        lead_x_change = pixelMove
                    elif event.key == pygame.K_UP:
                        lead_y_change = -pixelMove
                    elif event.key == pygame.K_DOWN:
                        lead_y_change = pixelMove
                    elif event.key == pygame.K_SPACE:
                        heroFire = True

                    print "hero x: " + str(lead_x), "y: " + str(lead_y), "    enemy: " + str(pygame.mouse.get_pos())

                if heroFire:
                    if heroMelee:
                        self.meleeAttack()
                    if heroRanged:
                        self.rangeAttack()
                    if heroAOE:
                        self.AOEAttack()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        lead_x_change = 0
                        lead_y_change = 0

            lead_x += lead_x_change
            lead_y += lead_y_change
            if lead_x >= displayWidth:
                lead_x = displayWidth-pixelMove
            if lead_y >= displayHeight:
                lead_y = displayHeight-pixelMove
            if lead_x <= 0:
                lead_x = 0
            if lead_y <= 0:
                lead_y = 0

            enemyRect.topleft = pygame.mouse.get_pos()
            heroRect.topleft = (lead_x, lead_y)
            
            screen.fill(color.white)
            screen.blit(hero.image, heroRect.topleft)
            screen.blit(enemy.image, enemyRect.topleft)
            screen.blit(powerUp.image, powerUpRect.topleft)

            offset_x, offset_y = (enemyRect.left - heroRect.left), (enemyRect.top - heroRect.top)
            if (hero.imageMask.overlap(enemy.imageMask, (offset_x, offset_y)) != None):
                print 'Collision Detected!'
            else:
                print 'None'

            pygame.display.update()
            clock.tick(FPS)

if __name__ == "__main__":
    StartProgram = GameLoop()
    StartProgram.RunGame()
