import pygame
MAXheight =700
MAXwidth=1000
size=50
class Person(pygame.sprite.Sprite):
    def  __init__(self,image,x,y):
        super(Person,self).__init__()
        jump=pygame.image.load(image)
        jump=pygame.transform.scale(jump,(x,y))
        self.image=jump
        self.rect = self.image.get_rect()

class Donkey(Person):
    def move(self,dire,level):
        if level==1:
            if dire==0:
                if self.rect.x+125>849:
                    return True
                self.rect.x+=50
            else:
                if self.rect.x<50:
                    return True
                self.rect.x-=50
            return False
        else:
            if dire==0:
                if self.rect.x+125>749:
                    return True
                self.rect.x+=50
            else:
                if self.rect.x-50<250:
                    return True
                self.rect.x-=50
            return False

    def getpos(self):
        return self.rect.x,self.rect.y


class Player(Person):

    def collide_stair(self,stair_list,play_list):
        collides=pygame.sprite.groupcollide(play_list,stair_list,False,False)
        if len(collides)>0:
            return True
        return False

    def get_lower(self,x,y,line_list,stair_list,play_list,flag):
        if flag:
            return (x,y)
        if self.collide_stair(stair_list,play_list):
            return (x,y)
        tempy=MAXheight+100
        for line in line_list:
            if line.rect.x<=x and line.rect.x+line.rect.width>=x and line.rect.y-size>=y and line.rect.y-size<=tempy:
                tempy=line.rect.y-size
        return (x,tempy)

    def valid_down(self,play_list,stair_list,flag):
        collides=pygame.sprite.groupcollide(play_list,stair_list,False,False)
        if flag==0:
            if len(collides)>0:
                for stai in collides.values():
                    if self.rect.y+75>stai[0].rect.y+stai[0].rect.height:
                        return False
                return True
        return False

    def down(self,play_list,stair_list,fl):
        if self.valid_down(play_list,stair_list,fl):
            self.rect.y+=size/2

    def up(self,flag,play_list,stair_list):
        collides=pygame.sprite.groupcollide(play_list,stair_list,False,False)
        if flag==0:
            if len(collides)>0:
                self.rect.y-=size/2

    def left(self):
        jump=pygame.image.load('playerleft.png')
        jump=pygame.transform.scale(jump,(size,size))
        self.image=jump
        if self.rect.x-size>=0:
            self.rect.x-=size

    def right(self):
        jump=pygame.image.load('playerright.png')
        jump=pygame.transform.scale(jump,(size,size))
        self.image=jump
        if self.rect.x+2*size<=MAXwidth:
            self.rect.x+=size
