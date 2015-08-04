import pygame
import time
import random
import sys

class UserInput:
    def EnterHeroName(self):
        HeroName = ""
        while HeroName is "":
            HeroName = raw_input("Enter the name of your hero: ")
        return HeroName

class GameBackground:
    def DesignedBackground(self):
        GameDisplay.fill(blue)
    def FirstQuadrantBackground(self):
        pass
    def SecondQuadrantBackground(self): 
        pass
    def ThirdQuadrantBackground(self):
        pass
    def FourthQuadrantBackground(self):
        pass

class GameLoop:
    def heroMelee(self):
        pass
    def meleeAttack(self):
        pass
    def rangeAttack(self):
        pass
    def AOEAttack(self):
        pass

    def RunGame(self):
        pygame.init()

        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)

        displayWidth = 800
        displayHeight = 600

        heroSize = 10
        enemySize = 10
        FPS = 30
        
        gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
        pygame.display.set_caption("Pancakes")
        RandLocationX = round(random.randrange(0, displayWidth-heroSize)/10.0)*10.0
        RandLocationY = round(random.randrange(0, displayHeight-heroSize)/10.0)*10.0

        gameExit = False
        heroFire = False
        heroMelee = False
        heroRanged = False
        heroAOE = False

        #PlayerName = UserInput()

        lead_x = 300
        lead_y = 300
        lead_x_change = 0
        lead_y_change = 0

        clock = pygame.time.Clock()

        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        lead_x_change = -heroSize
                    elif event.key == pygame.K_RIGHT:
                        lead_x_change = heroSize
                    elif event.key == pygame.K_UP:
                        lead_y_change = -heroSize
                    elif event.key == pygame.K_DOWN:
                        lead_y_change = heroSize
                    elif event.key == pygame.K_SPACE:
                        heroFire = True

                if heroFire:
                    if heroMelee:
                        meleeAttack()
                    if heroRanged:
                        rangeAttack()
                    if heroAOE:
                        AOEAttack()
   
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        lead_x_change = 0
                        lead_y_change = 0

            lead_x += lead_x_change
            lead_y += lead_y_change
 
            gameDisplay.fill(white)
            pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,heroSize,heroSize])
            pygame.draw.rect(gameDisplay, red, [RandLocationX, RandLocationY, enemySize, enemySize])
            pygame.display.update()

            clock.tick(FPS)

        pygame.quit()
        quit()

if __name__ == "__main__":
    StartProgram = GameLoop()
    StartProgram.RunGame()
