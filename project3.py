import pygame
import time
import random
import sys
import winsound
import os
from multiprocessing import Process
from pygame import mixer

pygame.init()

class sprites(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        color = colors()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey(color.white)
        self.rect = self.image.get_rect(x=x, y=y)
        self.imageMask = pygame.mask.from_surface(self.image)
        self.health  = 100
        self.healthColor = color.green
        self.collision = False

class spriteNames:
    def __init__(self):
        self.backgroundSpace = sprites('space.png', 1, 1)
        self.hero = sprites('hero.png', 1, 1)
        self.meleeEnemy = sprites('meleeEnemy.png', 1, 1)
        self.rangedEnemy = sprites('rangedEnemy.png', 1, 1)
        self.bossEnemy = sprites('boss.png', 1, 1)
        self.aoeEnemy = sprites('aoeEnemy.png', 1, 1)
        self.powerUp = sprites('powerUp.png', 1, 1)
        self.fryingPan = sprites('fryingPan.png', 1, 1)
        self.bullet = sprites('bullet.png', 1, 1)
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

class colors:
    def __init__(self):
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.red = (255,0,0)
        self.green = (0,255,0)
        self.yellow = (255,255,0)
        
class MeleeEnemy:
    def __init__(self):
        pass
    def meleeEnemyAttack(self):
        pass
class RangedEnemy:
    def __init__(self):
        pass
    def rangedEnemyAttack(self):
        pass
class AOEEnemy:
    def __init__(self):
        pass
class BossEnemy:
    def __init__(self):
        pass

class userInput:
    def EnterHeroName(self):
        HeroName = ""
        while HeroName == "":
            HeroName = raw_input("Enter the name of your hero: ")
        return HeroName
        

class MapDesign:
    def GenerateRandomMap(self, sprite):
        RandomMapGenerator = random.randint(1,4)
        if RandomMapGenerator == 1:
            sprite.backgroundJakeHimself.rect.topleft = (110, 80)
            sprite.backgroundIceKing.rect.topleft = (620, 30)
            sprite.backgroundFinn.rect.topleft = (980, 55)
            sprite.backgroundJakeFinn.rect.topleft = (650, 360)
            sprite.backgroundFinnUnicorn.rect.topleft = (325, 600)
            sprite.backgroundPenguin.rect.topleft = (50, 450)
            sprite.backgroundCupcake.rect.topleft = (900, 550)
            sprite.backgroundPurpleCloud.rect.topleft = (950, 275)
            sprite.backgroundVampire.rect.topleft = (500, 275)
            sprite.backgroundPrincess.rect.topleft = (665, 600)
        if RandomMapGenerator == 2:
            sprite.backgroundJakeHimself.rect.topleft = (820, 50)
            sprite.backgroundIceKing.rect.topleft = (215, 40)
            sprite.backgroundFinn.rect.topleft = (750, 300)
            sprite.backgroundJakeFinn.rect.topleft = (160, 385)
            sprite.backgroundFinnUnicorn.rect.topleft = (100, 630)
            sprite.backgroundPenguin.rect.topleft = (430, 200)
            sprite.backgroundCupcake.rect.topleft = (950, 275)
            sprite.backgroundPurpleCloud.rect.topleft = (900, 550)
            sprite.backgroundVampire.rect.topleft = (465, 600)
            sprite.backgroundPrincess.rect.topleft = (650, 490)
        if RandomMapGenerator == 3:
            sprite.backgroundJakeHimself.rect.topleft = (700, 40)
            sprite.backgroundIceKing.rect.topleft = (210, 510)
            sprite.backgroundFinn.rect.topleft = (980, 30)
            sprite.backgroundJakeFinn.rect.topleft = (110, 80)
            sprite.backgroundFinnUnicorn.rect.topleft = (405, 440)
            sprite.backgroundPenguin.rect.topleft = (50, 350)
            sprite.backgroundCupcake.rect.topleft = (825, 520)
            sprite.backgroundPurpleCloud.rect.topleft = (950, 275)
            sprite.backgroundVampire.rect.topleft = (500, 175)
            sprite.backgroundPrincess.rect.topleft = (635, 600)
        if RandomMapGenerator == 4:
            sprite.backgroundJakeHimself.rect.topleft = (160, 340)
            sprite.backgroundIceKing.rect.topleft = (880, 510)
            sprite.backgroundFinn.rect.topleft = (110, 80)
            sprite.backgroundJakeFinn.rect.topleft = (820, 30)
            sprite.backgroundFinnUnicorn.rect.topleft = (350, 490)
            sprite.backgroundPenguin.rect.topleft = (120, 550)
            sprite.backgroundCupcake.rect.topleft = (870, 285)
            sprite.backgroundPurpleCloud.rect.topleft = (370, 80)
            sprite.backgroundVampire.rect.topleft = (590, 275)
            sprite.backgroundPrincess.rect.topleft = (680, 530)

class GameLoop: 
    def display(self, screen, sprite, lead_x_change, lead_y_change):
        screen.blit(sprite.hero.image, sprite.hero.rect.topleft)
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

        offset_x, offset_y = (sprite.meleeEnemy.rect.left - sprite.hero.rect.left), (sprite.meleeEnemy.rect.top - sprite.hero.rect.top) 
        if (sprite.hero.imageMask.overlap(sprite.meleeEnemy.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0] - lead_x_change, sprite.hero.rect.topleft[1])
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0], sprite.hero.rect.topleft[1] - lead_y_change)
            print 'Collision Detected!'

        offset_x, offset_y = (sprite.backgroundJakeHimself.rect.left - sprite.hero.rect.left), (sprite.backgroundJakeHimself.rect.top - sprite.hero.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.backgroundJakeHimself.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0] - lead_x_change, sprite.hero.rect.topleft[1])
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0], sprite.hero.rect.topleft[1] - lead_y_change)
            print 'Collision Detected!'

        offset_x, offset_y = (sprite.backgroundIceKing.rect.left - sprite.hero.rect.left), (sprite.backgroundIceKing.rect.top - sprite.hero.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.backgroundIceKing.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0] - lead_x_change, sprite.hero.rect.topleft[1])
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0], sprite.hero.rect.topleft[1] - lead_y_change)
            print 'Collision Detected!'

        offset_x, offset_y = (sprite.backgroundFinn.rect.left - sprite.hero.rect.left), (sprite.backgroundFinn.rect.top - sprite.hero.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.backgroundFinn.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0] - lead_x_change, sprite.hero.rect.topleft[1])
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0], sprite.hero.rect.topleft[1] - lead_y_change)
            print 'Collision Detected!'

        offset_x, offset_y = (sprite.backgroundJakeFinn.rect.left - sprite.hero.rect.left), (sprite.backgroundJakeFinn.rect.top - sprite.hero.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.backgroundJakeFinn.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0] - lead_x_change, sprite.hero.rect.topleft[1])
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0], sprite.hero.rect.topleft[1] - lead_y_change)
            print 'Collision Detected!'

        offset_x, offset_y = (sprite.backgroundFinnUnicorn.rect.left - sprite.hero.rect.left), (sprite.backgroundFinnUnicorn.rect.top - sprite.hero.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.backgroundFinnUnicorn.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0] - lead_x_change, sprite.hero.rect.topleft[1])
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0], sprite.hero.rect.topleft[1] - lead_y_change)
            print 'Collision Detected!'
        
        offset_x, offset_y = (sprite.backgroundPenguin.rect.left - sprite.hero.rect.left), (sprite.backgroundPenguin.rect.top - sprite.hero.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.backgroundPenguin.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0] - lead_x_change, sprite.hero.rect.topleft[1])
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0], sprite.hero.rect.topleft[1] - lead_y_change)
            print 'Collision Detected!'
            
        offset_x, offset_y = (sprite.backgroundCupcake.rect.left - sprite.hero.rect.left), (sprite.backgroundCupcake.rect.top - sprite.hero.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.backgroundCupcake.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0] - lead_x_change, sprite.hero.rect.topleft[1])
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0], sprite.hero.rect.topleft[1] - lead_y_change)
            print 'Collision Detected!'
            
        offset_x, offset_y = (sprite.backgroundPurpleCloud.rect.left - sprite.hero.rect.left), (sprite.backgroundPurpleCloud.rect.top - sprite.hero.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.backgroundPurpleCloud.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0] - lead_x_change, sprite.hero.rect.topleft[1])
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0], sprite.hero.rect.topleft[1] - lead_y_change)
            print 'Collision Detected!'
            
        offset_x, offset_y = (sprite.backgroundVampire.rect.left - sprite.hero.rect.left), (sprite.backgroundVampire.rect.top - sprite.hero.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.backgroundVampire.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0] - lead_x_change, sprite.hero.rect.topleft[1])
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0], sprite.hero.rect.topleft[1] - lead_y_change)
            print 'Collision Detected!'

        offset_x, offset_y = (sprite.backgroundPrincess.rect.left - sprite.hero.rect.left), (sprite.backgroundPrincess.rect.top - sprite.hero.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.backgroundPrincess.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0] - lead_x_change, sprite.hero.rect.topleft[1])
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0], sprite.hero.rect.topleft[1] - lead_y_change)
            print 'Collision Detected!' 
 
        offset_x, offset_y = (sprite.rangedEnemy.rect.left - sprite.hero.rect.left), (sprite.rangedEnemy.rect.top - sprite.hero.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.rangedEnemy.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0] - lead_x_change, sprite.hero.rect.topleft[1])
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0], sprite.hero.rect.topleft[1] - lead_y_change)
            print 'Collision Detected!' 
        offset_x, offset_y = (sprite.bossEnemy.rect.left - sprite.hero.rect.left), (sprite.bossEnemy.rect.top - sprite.hero.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.bossEnemy.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0] - lead_x_change, sprite.hero.rect.topleft[1])
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0], sprite.hero.rect.topleft[1] - lead_y_change)
            print 'Collision Detected!' 
        offset_x, offset_y = (sprite.aoeEnemy.rect.left - sprite.hero.rect.left), (sprite.aoeEnemy.rect.top - sprite.hero.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.aoeEnemy.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0] - lead_x_change, sprite.hero.rect.topleft[1])
            sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0], sprite.hero.rect.topleft[1] - lead_y_change)
            print 'Collision Detected!' 
        
        #Health Bars
        color = colors()
        displayWidth = 1200
        displayHeight = 800
        
        
        #sprite.powerUp.rect.topleft = (15, 15)

        if sprite.hero.health > 75:
            sprite.hero.healthColor = color.green
        elif sprite.hero.health > 50:
            sprite.hero.healthColor = color.yellow
        else:
           sprite.hero.healthColor = color.red

        playMusic = True
           
        if sprite.rangedEnemy.health > 0:
            pygame.draw.rect(screen, sprite.rangedEnemy.healthColor, [700, 10, sprite.rangedEnemy.health, 20])
            sprite.rangedEnemy.rect.topleft = (1150, 710)
            screen.blit(sprite.rangedEnemy.image, sprite.rangedEnemy.rect.topleft)
            #print sprite.rangedEnemy.health
            if sprite.rangedEnemy.health > 75:
                sprite.rangedEnemy.healthColor = color.green
                #print sprite.rangedEnemy.health
            elif sprite.rangedEnemy.health > 50:
                sprite.rangedEnemy.healthColor = color.yellow
                #print sprite.rangedEnemy.health
            elif sprite.rangedEnemy.health > 25:
                sprite.rangedEnemy.healthColor = color.red
                #print sprite.rangedEnemy.health
        else:
            if sprite.meleeEnemy.health > 0:
                pygame.draw.rect(screen, sprite.meleeEnemy.healthColor, [700, 10, sprite.meleeEnemy.health, 20])
                screen.blit(sprite.meleeEnemy.image, sprite.meleeEnemy.rect.topleft)
                sprite.rangedEnemy.rect.topleft = (0, 0)
                sprite.meleeEnemy.rect.topleft = (10, 710)
                #print sprite.meleeEnemy.health
                if sprite.meleeEnemy.health > 75:
                    sprite.meleeEnemy.healthColor = color.green
                    #print sprite.meleeEnemy.health
                elif sprite.meleeEnemy.health > 50:
                    sprite.meleeEnemy.healthColor = color.yellow
                    #print sprite.meleeEnemy.health
                elif sprite.meleeEnemy.health > 25:
                    sprite.meleeEnemy.healthColor = color.red
                    #print sprite.meleeEnemy.health
            else:
                if sprite.aoeEnemy.health > 0:
                    pygame.draw.rect(screen, sprite.aoeEnemy.healthColor, [700, 10, sprite.aoeEnemy.health, 20])
                    screen.blit(sprite.aoeEnemy.image, sprite.aoeEnemy.rect.topleft)
                    sprite.meleeEnemy.rect.topleft = (0, 0)
                    sprite.aoeEnemy.rect.topleft = (1150, 10)
                    #print sprite.aoeEnemy.health
                    if sprite.aoeEnemy.health > 75:
                        sprite.aoeEnemy.healthColor = color.green
                        #print sprite.aoeEnemy.health
                    elif sprite.aoeEnemy.health > 50:
                        sprite.aoeEnemy.healthColor = color.yellow
                        #print sprite.aoeEnemy.health
                    elif sprite.aoeEnemy.health > 25:
                        sprite.aoeEnemy.healthColor = color.red
                        #print sprite.aoeEnemy.health
                else:
                    if sprite.bossEnemy.health > 0:
                        pygame.draw.rect(screen, sprite.bossEnemy.healthColor, [700, 10, sprite.bossEnemy.health, 20])
                        screen.blit(sprite.bossEnemy.image, sprite.bossEnemy.rect.topleft)
                        sprite.aoeEnemy.rect.topleft = (0, 0)
                        sprite.bossEnemy.rect.topleft = (10, 230)
                        #print sprite.bossEnemy.health
                        if sprite.bossEnemy.health > 75:
                            sprite.bossEnemy.healthColor = color.green
                            #print sprite.bossEnemy.health
                        elif sprite.bossEnemy.health > 50:
                            sprite.bossEnemy.healthColor = color.yellow
                            #print sprite.bossEnemy.health
                        elif sprite.bossEnemy.health > 25:
                            sprite.bossEnemy.healthColor = color.red
                            #print sprite.bossEnemy.health
                    else:
                        screen.blit(sprite.powerUp.image, sprite.powerUp.rect.topleft)
                        sprite.powerUp.rect.topleft = (10, 230)
                        sprite.bossEnemy.rect.topleft = (0, 0)


        pygame.draw.rect(screen, sprite.hero.healthColor, [300, 10, sprite.hero.health, 20])
        
        pygame.display.update()
        return sprite

    def fryingPan(self, screen, sprite):
        screen.blit(sprite.backgroundSpace.image, sprite.backgroundSpace.rect.topleft)
        screen.blit(sprite.fryingPan.image, sprite.fryingPan.rect.topleft)
        
        offset_x, offset_y = (sprite.meleeEnemy.rect.left - sprite.fryingPan.rect.left), (sprite.meleeEnemy.rect.top - sprite.fryingPan.rect.top) 
        if (sprite.hero.imageMask.overlap(sprite.meleeEnemy.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.collision = True
            sprite.meleeEnemy.health = sprite.meleeEnemy.health - 25
            
        offset_x, offset_y = (sprite.rangedEnemy.rect.left - sprite.fryingPan.rect.left), (sprite.rangedEnemy.rect.top - sprite.fryingPan.rect.top) 
        if (sprite.hero.imageMask.overlap(sprite.rangedEnemy.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.collision = True
            sprite.rangedEnemy.health = sprite.rangedEnemy.health - 25
            
        offset_x, offset_y = (sprite.aoeEnemy.rect.left - sprite.fryingPan.rect.left), (sprite.aoeEnemy.rect.top - sprite.fryingPan.rect.top) 
        if (sprite.hero.imageMask.overlap(sprite.aoeEnemy.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.collision = True
            sprite.aoeEnemy.health = sprite.aoeEnemy.health - 25
            
        offset_x, offset_y = (sprite.bossEnemy.rect.left - sprite.fryingPan.rect.left), (sprite.bossEnemy.rect.top - sprite.fryingPan.rect.top) 
        if (sprite.hero.imageMask.overlap(sprite.bossEnemy.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.collision = True
            sprite.bossEnemy.health = sprite.bossEnemy.health - 25
            
        offset_x, offset_y = (sprite.backgroundJakeHimself.rect.left - sprite.fryingPan.rect.left), (sprite.backgroundJakeHimself.rect.top - sprite.fryingPan.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.backgroundJakeHimself.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.collision = True
            
        offset_x, offset_y = (sprite.backgroundIceKing.rect.left - sprite.fryingPan.rect.left), (sprite.backgroundIceKing.rect.top - sprite.fryingPan.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.backgroundIceKing.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.collision = True
            
        offset_x, offset_y = (sprite.backgroundFinn.rect.left - sprite.fryingPan.rect.left), (sprite.backgroundFinn.rect.top - sprite.fryingPan.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.backgroundFinn.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.collision = True
            
        offset_x, offset_y = (sprite.backgroundJakeFinn.rect.left - sprite.fryingPan.rect.left), (sprite.backgroundJakeFinn.rect.top - sprite.fryingPan.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.backgroundJakeFinn.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.collision = True
            
        offset_x, offset_y = (sprite.backgroundFinnUnicorn.rect.left - sprite.fryingPan.rect.left), (sprite.backgroundFinnUnicorn.rect.top - sprite.fryingPan.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.backgroundFinnUnicorn.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.collision = True
            
        offset_x, offset_y = (sprite.backgroundPenguin.rect.left - sprite.fryingPan.rect.left), (sprite.backgroundPenguin.rect.top - sprite.fryingPan.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.backgroundPenguin.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.collision = True
            
        offset_x, offset_y = (sprite.backgroundCupcake.rect.left - sprite.fryingPan.rect.left), (sprite.backgroundCupcake.rect.top - sprite.fryingPan.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.backgroundCupcake.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.collision = True
            
        offset_x, offset_y = (sprite.backgroundPurpleCloud.rect.left - sprite.fryingPan.rect.left), (sprite.backgroundPurpleCloud.rect.top - sprite.fryingPan.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.backgroundPurpleCloud.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.collision = True
            
        offset_x, offset_y = (sprite.backgroundVampire.rect.left - sprite.fryingPan.rect.left), (sprite.backgroundVampire.rect.top - sprite.fryingPan.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.backgroundVampire.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.collision = True
            
        offset_x, offset_y = (sprite.backgroundPrincess.rect.left - sprite.fryingPan.rect.left), (sprite.backgroundPrincess.rect.top - sprite.fryingPan.rect.top)
        if (sprite.hero.imageMask.overlap(sprite.backgroundPrincess.imageMask, (offset_x, offset_y)) != None):
            sprite.hero.collision = True
        return sprite
        
    def bullet(self, screen, sprite):
        screen.blit(sprite.backgroundSpace.image, sprite.backgroundSpace.rect.topleft)
        screen.blit(sprite.bullet.image, sprite.bullet.rect.topleft)
        
        offset_x, offset_y = (sprite.meleeEnemy.rect.left - sprite.bullet.rect.left), (sprite.meleeEnemy.rect.top - sprite.bullet.rect.top) 
        if (sprite.bullet.imageMask.overlap(sprite.meleeEnemy.imageMask, (offset_x, offset_y)) != None):
            sprite.bullet.collision = True
        offset_x, offset_y = (sprite.rangedEnemy.rect.left - sprite.bullet.rect.left), (sprite.rangedEnemy.rect.top - sprite.bullet.rect.top) 
        if (sprite.bullet.imageMask.overlap(sprite.rangedEnemy.imageMask, (offset_x, offset_y)) != None):
            sprite.bullet.collision = True
        offset_x, offset_y = (sprite.aoeEnemy.rect.left - sprite.bullet.rect.left), (sprite.aoeEnemy.rect.top - sprite.bullet.rect.top) 
        if (sprite.bullet.imageMask.overlap(sprite.aoeEnemy.imageMask, (offset_x, offset_y)) != None):
            sprite.bullet.collision = True
        offset_x, offset_y = (sprite.bossEnemy.rect.left - sprite.bullet.rect.left), (sprite.bossEnemy.rect.top - sprite.bullet.rect.top) 
        if (sprite.bullet.imageMask.overlap(sprite.bossEnemy.imageMask, (offset_x, offset_y)) != None):
            sprite.bullet.collision = True
        offset_x, offset_y = (sprite.backgroundJakeHimself.rect.left - sprite.bullet.rect.left), (sprite.backgroundJakeHimself.rect.top - sprite.bullet.rect.top)
        if (sprite.bullet.imageMask.overlap(sprite.backgroundJakeHimself.imageMask, (offset_x, offset_y)) != None):
            sprite.bullet.collision = True
        offset_x, offset_y = (sprite.backgroundIceKing.rect.left - sprite.bullet.rect.left), (sprite.backgroundIceKing.rect.top - sprite.bullet.rect.top)
        if (sprite.bullet.imageMask.overlap(sprite.backgroundIceKing.imageMask, (offset_x, offset_y)) != None):
            sprite.bullet.collision = True
        offset_x, offset_y = (sprite.backgroundFinn.rect.left - sprite.bullet.rect.left), (sprite.backgroundFinn.rect.top - sprite.bullet.rect.top)
        if (sprite.bullet.imageMask.overlap(sprite.backgroundFinn.imageMask, (offset_x, offset_y)) != None):
            sprite.bullet.collision = True
        offset_x, offset_y = (sprite.backgroundJakeFinn.rect.left - sprite.bullet.rect.left), (sprite.backgroundJakeFinn.rect.top - sprite.bullet.rect.top)
        if (sprite.bullet.imageMask.overlap(sprite.backgroundJakeFinn.imageMask, (offset_x, offset_y)) != None):
            sprite.bullet.collision = True
        offset_x, offset_y = (sprite.backgroundFinnUnicorn.rect.left - sprite.bullet.rect.left), (sprite.backgroundFinnUnicorn.rect.top - sprite.bullet.rect.top)
        if (sprite.bullet.imageMask.overlap(sprite.backgroundFinnUnicorn.imageMask, (offset_x, offset_y)) != None):
            sprite.bullet.collision = True
        offset_x, offset_y = (sprite.backgroundPenguin.rect.left - sprite.bullet.rect.left), (sprite.backgroundPenguin.rect.top - sprite.bullet.rect.top)
        if (sprite.bullet.imageMask.overlap(sprite.backgroundPenguin.imageMask, (offset_x, offset_y)) != None):
            sprite.bullet.collision = True
        offset_x, offset_y = (sprite.backgroundCupcake.rect.left - sprite.bullet.rect.left), (sprite.backgroundCupcake.rect.top - sprite.bullet.rect.top)
        if (sprite.bullet.imageMask.overlap(sprite.backgroundCupcake.imageMask, (offset_x, offset_y)) != None):
            sprite.bullet.collision = True
        offset_x, offset_y = (sprite.backgroundPurpleCloud.rect.left - sprite.bullet.rect.left), (sprite.backgroundPurpleCloud.rect.top - sprite.bullet.rect.top)
        if (sprite.bullet.imageMask.overlap(sprite.backgroundPurpleCloud.imageMask, (offset_x, offset_y)) != None):
            sprite.bullet.collision = True
        offset_x, offset_y = (sprite.backgroundVampire.rect.left - sprite.bullet.rect.left), (sprite.backgroundVampire.rect.top - sprite.bullet.rect.top)
        if (sprite.bullet.imageMask.overlap(sprite.backgroundVampire.imageMask, (offset_x, offset_y)) != None):
            sprite.bullet.collision = True
        offset_x, offset_y = (sprite.backgroundPrincess.rect.left - sprite.bullet.rect.left), (sprite.backgroundPrincess.rect.top - sprite.bullet.rect.top)
        if (sprite.bullet.imageMask.overlap(sprite.backgroundPrincess.imageMask, (offset_x, offset_y)) != None):
            sprite.bullet.collision = True
        return sprite
        
    def meleeAttack(self, direction, screen, sprite):
        color = colors()
        sprite.fryingPan.rect = sprite.fryingPan.image.get_rect()
        x = sprite.hero.rect.topleft[0]
        y = sprite.hero.rect.topleft[1]
        if direction == 1:
            #for y in range (y, 0, -10):
            sprite.fryingPan.rect.topleft = (sprite.hero.rect.topleft[0], y)
            screen.blit(sprite.backgroundSpace.image, sprite.backgroundSpace.rect.topleft)
            screen.blit(sprite.fryingPan.image, sprite.fryingPan.rect.topleft)
            self.display(screen, sprite, 0, 0)
        if direction == 2:
            #for x in range (x, 1200, 10):
            sprite.fryingPan.rect.topleft = (x, y)
            screen.blit(sprite.backgroundSpace.image, sprite.backgroundSpace.rect.topleft)
            screen.blit(sprite.fryingPan.image, sprite.fryingPan.rect.topleft)
            self.display(screen, sprite, 0, 0)
        if direction == 3:
            #for y in range (y, 800, 10):
            sprite.fryingPan.rect.topleft = (x, y)
            screen.blit(sprite.backgroundSpace.image, sprite.backgroundSpace.rect.topleft)
            screen.blit(sprite.fryingPan.image, sprite.fryingPan.rect.topleft)
            self.display(screen, sprite, 0, 0)
        if direction == 4:
            #for x in range (x, 0, -10):
            sprite.fryingPan.rect.topleft = (x, y)
            screen.blit(sprite.backgroundSpace.image, sprite.backgroundSpace.rect.topleft)
            screen.blit(sprite.fryingPan.image, sprite.fryingPan.rect.topleft)
            self.display(screen, sprite, 0, 0)
            offset_x, offset_y = (sprite.meleeEnemy.rect.left - sprite.fryingPan.rect.left), (sprite.meleeEnemy.rect.top - sprite.fryingPan.rect.top)    
    
    def rangeAttack(self, direction, screen, sprite):
        color = colors()
        damage = 0
        sprite.fryingPan.rect = sprite.fryingPan.image.get_rect()
        x = sprite.hero.rect.topleft[0]
        y = sprite.hero.rect.topleft[1]
        sprite.hero.collision = False
        if direction == 1:
            while not sprite.hero.collision:
                y = y - 10
                if y <= 0:
                    sprite.hero.collision = True
                sprite.fryingPan.rect.topleft = (x, y)
                sprite = self.fryingPan(screen, sprite)
                self.display(screen, sprite, 0, 0)

        if direction == 2:
            while not sprite.hero.collision:
                x = x + 10
                if x >= 1200:
                    sprite.hero.collision = True
                sprite.fryingPan.rect.topleft = (x, y)
                sprite = self.fryingPan(screen, sprite)
                self.display(screen, sprite, 0, 0)
                offset_x, offset_y = (sprite.meleeEnemy.rect.left - sprite.fryingPan.rect.left), (sprite.meleeEnemy.rect.top - sprite.fryingPan.rect.top)
        if direction == 3:
            while not sprite.hero.collision:
                y = y + 10
                if y >= 800:
                    sprite.hero.collision = True
                sprite.fryingPan.rect.topleft = (x, y)
                sprite = self.fryingPan(screen, sprite)
                self.display(screen, sprite, 0, 0)
                offset_x, offset_y = (sprite.meleeEnemy.rect.left - sprite.fryingPan.rect.left), (sprite.meleeEnemy.rect.top - sprite.fryingPan.rect.top)
        if direction == 4:
            while not sprite.hero.collision:
                x = x - 10
                if x <= 0:
                    sprite.hero.collision = True
                sprite.fryingPan.rect.topleft = (x, y)
                sprite = self.fryingPan(screen, sprite)
                self.display(screen, sprite, 0, 0)
                offset_x, offset_y = (sprite.meleeEnemy.rect.left - sprite.fryingPan.rect.left), (sprite.meleeEnemy.rect.top - sprite.fryingPan.rect.top)
        return sprite

    def AOEAttack(self, direction, screen, sprite):
        pass

    def enemyRangedAttack(self, direction, screen, sprite):
        color = colors()
        damage = 0
        sprite.bullet.rect = sprite.bullet.image.get_rect()
        sprite.bullet.collision = False
        x = 1150
        y = 710
        if direction == 1:
            while not sprite.bullet.collision:
                y = y - 10
                if y <= 0:
                    sprite.bullet.collision = True
                sprite.bullet.rect.topleft = (1150, y)
                sprite = self.bullet(screen, sprite)
                self.display(screen, sprite, 0, 0)
        if direction == 4:
            while not sprite.bullet.collision:
                x = x - 10
                if x <= 0:
                    sprite.bullet.collision = True
                sprite.bullet.rect.topleft = (x, 710)
                sprite = self.bullet(screen, sprite)
                self.display(screen, sprite, 0, 0)
        return sprite

    def RunGame(self):
        color = colors()
        displayWidth = 1200
        displayHeight = 800
        pygame.display.set_caption('Bacon Pancakes!')
        screen = pygame.display.set_mode([displayWidth, displayHeight])
        #message = MessageToScreen("", color)
      
        pygame.mixer.music.load('baconpancakes.wav')
        pygame.mixer.music.play(-1)
        
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
        sprite.hero.rect.topleft = (10,10)
        
        GenerateRandomBackground = MapDesign()
        RandomMapGenerator = GenerateRandomBackground.GenerateRandomMap(sprite)

        sprite.hero.health = 100

        sprite.rangedEnemy.rect.topleft = (1200, 0)
        sprite.meleeEnemy.rect.topleft = (1200, 0)
        sprite.aoeEnemy.rect.topleft = (1200, 0)
        sprite.bossEnemy.rect.topleft = (1200, 0)

        
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
                sprite.hero.rect.topleft = (0, sprite.hero.rect.topleft[1])
            if sprite.hero.rect.topleft[1] >= displayHeight:
                sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0],0)
            if sprite.hero.rect.topleft[0] <= 0:
                sprite.hero.rect.topleft = (0, sprite.hero.rect.topleft[1])
            if sprite.hero.rect.topleft[1] <= 0:
                sprite.hero.rect.topleft = (sprite.hero.rect.topleft[0],0)

            if sprite.hero.rect.topleft[0] == sprite.rangedEnemy.rect.topleft[0] and sprite.rangedEnemy.health > 0:
                self.enemyRangedAttack(1, screen, sprite)
            if sprite.hero.rect.topleft[1] == sprite.rangedEnemy.rect.topleft[1] and sprite.rangedEnemy.health > 0:
                self.enemyRangedAttack(4, screen, sprite)
                
            screen.blit(sprite.backgroundSpace.image, sprite.backgroundSpace.rect.topleft)
            self.display(screen, sprite, lead_x_change, lead_y_change)

            clock.tick(FPS)

if __name__ == "__main__":
    StartProgram = GameLoop()
    StartProgram.RunGame()
