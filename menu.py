import pygame,sys,movement
from pygame.locals import *
pygame.init()
pygame.display.set_icon(pygame.image.load('gameicon.png'))
pygame.display.set_caption('Donkey Kong')
DISPLAYSURF = pygame.display.set_mode((1000,700), 0, 32)
Red=(255,0,0)
White=(255,255,255)
Black=(0,0,0)
class menu():
    def par(self,s1,s2):
        a=1
        while True:
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==pygame.K_DOWN:
                        a+=1
                    elif event.key==pygame.K_UP:
                        a=1
                    elif event.key==pygame.K_RETURN:
                        if a==1:
                            movement.gameloop().func()
                        else:
                            pygame.quit()
                            sys.exit()
            c1=Black
            c2=Black
            if a==1:
                c1=Red
            else:
                c2=Red
            DISPLAYSURF.fill(White)
            fontObj = pygame.font.Font('freesansbold.ttf', 72)
            textSurfaceObj = fontObj.render(s1, True, c1)
            rect = textSurfaceObj.get_rect()
            rect.center = (500,300)
            DISPLAYSURF.blit(textSurfaceObj,rect)

            fontObj = pygame.font.Font('freesansbold.ttf',72)
            textSurfaceObj = fontObj.render(s2, True, c2)
            rect = textSurfaceObj.get_rect()
            rect.center = (500,400)
            DISPLAYSURF.blit(textSurfaceObj,rect)
            pygame.display.update()

    def pause(self):
        menu().par('Resume','Quit')

    def start(self):
        menu().par('Start','Quit')
