import pygame,random
import board,time

coin_list=pygame.sprite.Group()

class objecta(pygame.sprite.Sprite):
    def __init__(self,image):
        super(objecta,self).__init__()
        jump=pygame.image.load(image)
        jump=pygame.transform.scale(jump,(20,20))
        self.image=jump
        self.rect = self.image.get_rect()
    
class hearts(objecta):

    def change(self):
        jump=pygame.image.load('heart2.png')
        jump=pygame.transform.scale(jump,(20,20))
        self.image=jump

class fireball(objecta):
    
    def gen_ball(self,don):
        ball=fireball('fireball.png')
        ball.rect.x,ball.rect.y=don.getpos()
        ball.down=0
        x=random.randrange(0,2)
        ball.di=x
        return ball

    def move(self,dire):
        if dire==0:
            if self.rect.x+30>1000:
                return (True,False)
            self.rect.x+=10
        else:
            if self.rect.x-10<0:
                return (True,False)
            self.rect.x-=10
        if self.rect.y==656 and self.rect.x<40:
            return (False,True)
        return (False,False)

    def ch(self,i):
        if self.rect.y+20>i.rect.y+100:
            self.down=0
            self.dire=random.randrange(0,2)
            return self.move(self.dire)
        self.rect.y+=10
        return (False,False)

    def move_ball(self,dire,stair_list):
        collide=pygame.sprite.spritecollide(self,stair_list,False)
        if self.down==1:
            if len(collide)>0:
                for i in collide:
                    return self.ch(i)
        if len(collide)>0:
            x=random.randrange(0,2)
            if x==1:
                self.down=1
                for i in collide:
                    return self.ch(i)
        return self.move(dire)

    def getlower(self,ball,line_list):
            if ball.down==1:
                return ball
            savey=ball.rect.y
            tempy=700
            for line in line_list:
                if line.rect.x<=ball.rect.x and line.rect.x+line.rect.width>=ball.rect.x:
                    if line.rect.y-20>=ball.rect.y and line.rect.y-20<=tempy:
                        tempy=line.rect.y-20
            ball.rect.y=tempy
            if tempy!=savey:
                ball.di=random.randrange(0,2)
            return ball

    def check(self,ball_list,game_list):
        collide=pygame.sprite.groupcollide(ball_list,game_list,True,False)
        if len(collide)>0:
            return True
        return False


class coins(objecta):

    def gen_coins(self):
        for i in range(20):
            c=coins('coin.png')
            c.rect.x=random.randrange(0,980)
            y=random.randrange(0,7)
            c.rect.y=y*100+54
            coin_list.add(c)
        return coin_list

    def settle_coins(self,coin_list,line_list):
        for coin in coin_list:
            tempy=700
            coin_list.remove(coin)
            for line in line_list:
                if line.rect.x<=coin.rect.x and line.rect.x+line.rect.width>=coin.rect.x:
                    if line.rect.y-20>=coin.rect.y and line.rect.y-20<=tempy:
                        tempy=line.rect.y-20
            coin.rect.y=tempy
            coin_list.add(coin)
        return coin_list

    def check_collision(self,coin_list,play_list):
        c=0
        collides=pygame.sprite.groupcollide(play_list,coin_list,False,True)
        if len(collides)>0:
            for i in collides.values():
                    c+=len(i)
                    a=pygame.mixer.Sound('coin.wav')
                    pygame.mixer.Sound.play(a)
        return c

