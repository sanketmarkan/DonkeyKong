import pygame
size=50
Black=(0,0,0)
stair_list=pygame.sprite.Group()
line_list=pygame.sprite.Group()
play_list=pygame.sprite.Group()
class level(pygame.sprite.Sprite):
    def  __init__(self,color,width,height):
        super(level,self).__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()


class Stair(pygame.sprite.Sprite):
    def  __init__(self):
        super(Stair,self).__init__()
        jump=pygame.image.load('ladder.png')
        jump=pygame.transform.scale(jump,(size,101))
        self.image=jump
        self.rect = self.image.get_rect()

class boards():
    def gen_board(self):
        for i in range(3):
            linee=level(Black,849,5)
            linee.rect.x=0
            linee.rect.y=176+i*200
            line_list.add(linee)

        for i in range(2):
            linee=level(Black,850,5)
            linee.rect.x=150
            linee.rect.y=276+i*200
            line_list.add(linee)

        linee=level(Black,400,5)
        linee.rect.x=250
        linee.rect.y=76
        line_list.add(linee)
        
        stair=Stair()
        stair.rect.x=550
        stair.rect.y=75
        stair_list.add(stair)


        stair=Stair()
        stair.rect.x=750
        stair.rect.y=175
        stair_list.add(stair)

        stair=Stair()
        stair.rect.x=250
        stair.rect.y=175
        stair_list.add(stair)


        stair=Stair()
        stair.rect.x=500
        stair.rect.y=275
        stair_list.add(stair)

        stair=Stair()
        stair.rect.x=300
        stair.rect.y=375
        stair_list.add(stair)

        stair=Stair()
        stair.rect.x=700
        stair.rect.y=475
        stair_list.add(stair)

        stair=Stair()
        stair.rect.x=450
        stair.rect.y=575
        stair_list.add(stair)

        linee=level(Black,1000,5)
        linee.rect.x=0
        linee.rect.y=676
        line_list.add(linee)
        return (line_list,stair_list)
    
    def gen_board2(self):
        for i in range(6):
            linee=level(Black,499+i*100,5)
            linee.rect.x=250-i*50
            linee.rect.y=176+i*100
            line_list.add(linee)

        linee=level(Black,400,5)
        linee.rect.x=250
        linee.rect.y=76
        line_list.add(linee)

        for i in range(5):
            stair=Stair()
            stair.rect.x=450-i*100
            stair.rect.y=175+i*100
            stair_list.add(stair)

        for i in range(4):
            stair=Stair()
            stair.rect.x=550+i*100
            stair.rect.y=275+i*100
            stair_list.add(stair)
        
        stair=Stair()
        stair.rect.x=+550
        stair.rect.y=75
        stair_list.add(stair)
        
        return (line_list,stair_list)
