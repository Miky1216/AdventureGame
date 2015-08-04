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
    def RunGame(self):
        pygame.init()

        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)

        DisplayWidth = 800
        DisplayHeight = 600

        gameDisplay = pygame.display.set_mode((DisplayWidth,DisplayHeight))
        pygame.display.set_caption("Pancakes")

        BlockSize = 10
        FPS = 10

        gameExit = False

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
                        lead_x_change = -BlockSize
                    elif event.key == pygame.K_RIGHT:
                        lead_x_change = BlockSize
                    elif event.key == pygame.K_UP:
                        lead_y_change = -BlockSize
                    elif event.key == pygame.K_DOWN:
                        lead_y_change = BlockSize
   
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        lead_x_change = 0
                        lead_y_change = 0

            lead_x += lead_x_change
            lead_y += lead_y_change
 
            gameDisplay.fill(white)
            for x in range(0,255):
                pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,BlockSize,BlockSize])
                pygame.display.update()

                #clock.tick(FPS)

        pygame.quit()
        quit()

if __name__ == "__main__":
    StartProgram = GameLoop()
    StartProgram.RunGame()
