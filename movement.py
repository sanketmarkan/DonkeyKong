import pygame,sys,board,character,objects,time,menu
from pygame.locals import *
class gameloop():

    def func(self):
        pygame.init()
        FPS=8
        fpsClock=pygame.time.Clock()
        size=50
        MAXwidth=1000
        MAXheight=700
        pygame.display.set_icon(pygame.image.load('gameicon.png'))
        pygame.display.set_caption('Donkey Kong')
        DISPLAYSURF = pygame.display.set_mode((MAXwidth, MAXheight), 0, 32)
        Black=(0,0,0)
        White=(255,255,255)
        Red=(255,0,0)

        pygame.mixer.music.load('bgm.mp3')
        pygame.mixer.music.play(-1, 0.0)

        bgimg=pygame.image.load('back.png')
        bgimg=pygame.transform.smoothscale(bgimg, (1000,700))
        bgrect=bgimg.get_rect()
        bgrect.x=0
        bgrect.y=0
        DISPLAYSURF.blit(bgimg,bgrect)

        stair_list=pygame.sprite.Group()
        coin_list=pygame.sprite.Group()
        line_list=pygame.sprite.Group()
        play_list=pygame.sprite.Group()
        ball_list=pygame.sprite.Group()
    
        pygame.key.set_repeat(10,10)
        def main():
            heart=[]
            level=1
            score=0
            life=3

            heart.append(objects.hearts('heart1.png'))
            heart[0].rect.x=860
            heart[0].rect.y=60

            heart.append(objects.hearts('heart1.png'))
            heart[1].rect.x=890
            heart[1].rect.y=60
        
            heart.append(objects.hearts('heart1.png'))
            heart[2].rect.x=920
            heart[2].rect.y=60
            main2(level,score,life,heart)

        def main2(level,score,life,heart):
            fl=0
            if level==1:
                line_list,stair_list=board.boards().gen_board()
            else:
                line_list,stair_list=board.boards().gen_board2()

            coin_list=objects.coins('coin.png').gen_coins()
            coin_list=objects.coins('coin.png').settle_coins(coin_list,line_list)
            
            play=character.Player('playerright.png',50,50)
            play.rect.x=50
            play.rect.y=626
            play_list.add(play)
    
        
            don=character.Donkey('donkey.png',75,80)
            don.rect.x=500
            don.rect.y=98
            don.dire=0
            c=0
            st=0

            img=pygame.image.load('princess.png')
            img=pygame.transform.scale(img,(50,50))
            while True:
                ll=0
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
			elif event.type==KEYDOWN:
				if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
					play.right()
				elif event.key==pygame.K_LEFT or event.key==pygame.K_a:
					play.left()
				elif event.key==pygame.K_DOWN or event.key==pygame.K_s:
                                    play.down(play_list,stair_list,fl)
				elif event.key==pygame.K_UP or event.key==pygame.K_w:
                                    play.up(fl,play_list,stair_list)
                                elif event.key==pygame.K_SPACE:
                                    if fl==0:
                                         up=-26
                                         fl=1
                                elif event.key==pygame.K_q:
                                    pygame.quit()
                                    sys.exit()
                if fl:
                    play.rect.y+=up
                    up+=13
                    if up==26:
                        fl=0
               
                if c%45==0:
                    ball_list.add(objects.fireball('fireball.png').gen_ball(don))

                if c%2==0:
                    if don.move(don.dire,level):
                        don.dire=1-don.dire
                    for ball in ball_list:
                        a=ball.move_ball(ball.di,stair_list)
                        if a[1]==True:
                            ball_list.remove(ball)
                        else:
                            if a[0]==True:
                                ball.di=1-ball.di
                            ball_list.remove(ball)
                            ball=objects.fireball('fireball.png').getlower(ball,line_list)
                            ball_list.add(ball)

                c=(c+1)%45
                play.rect.x,play.rect.y=play.get_lower(play.rect.x,play.rect.y,line_list,stair_list,play_list,fl)
                if play.rect.y==26 and play.rect.x<260:
                    play_list.empty()
                    ball_list.empty()
                    coin_list.empty()
                    line_list.empty()
                    stair_list.empty()
                    fontObj = pygame.font.Font('freesansbold.ttf', 64)
                    textSurfaceObj = fontObj.render("Yay!!! You saved the princess", True,Black)
                    rect = textSurfaceObj.get_rect()
                    rect.center = (500,350)
                    DISPLAYSURF.blit(textSurfaceObj,rect)
		    score+=50
                    pygame.display.update()
                    time.sleep(3)
                    main2(3-level,score,life,heart)
                aqw=objects.coins('coin.png').check_collision(coin_list,play_list)
                score+=aqw*5
                DISPLAYSURF.fill(White)
                DISPLAYSURF.blit(bgimg,bgrect)
                if objects.fireball('fireball.png').check(ball_list,play_list):
                    life-=1
                    ball_list.empty()
                    heart[life].change()
                    play.rect.x=150
                    play.rect.y=626
                    score-=25
                    score=max(score,0)
                    if life>0:
                        ll=1
                        fontObj = pygame.font.Font('freesansbold.ttf', 64)
                        textSurfaceObj = fontObj.render("Life Lost", True,Black)
                        rect = textSurfaceObj.get_rect()
                        rect.center = (500,350)
                        DISPLAYSURF.blit(textSurfaceObj,rect)
                    if life==0:
                        st=1
                        fontObj = pygame.font.Font('freesansbold.ttf', 64)
                        textSurfaceObj = fontObj.render("Game Over!!!", True,Black)
                        rect = textSurfaceObj.get_rect()
                        rect.center = (500,350)
                        DISPLAYSURF.blit(textSurfaceObj,rect)
               
                s='SCORE: '+str(score)
                fontObj = pygame.font.Font('freesansbold.ttf', 20)
                textSurfaceObj = fontObj.render(s, True,Black)
                rect = textSurfaceObj.get_rect()
                rect.center = (900,100)
                DISPLAYSURF.blit(textSurfaceObj,rect)

                line_list.draw(DISPLAYSURF)
                stair_list.draw(DISPLAYSURF)
                coin_list.draw(DISPLAYSURF)
                ball_list.draw(DISPLAYSURF)
                play_list.draw(DISPLAYSURF)

                DISPLAYSURF.blit(img,(250,26))
                DISPLAYSURF.blit(don.image,don.rect)

                for i in range(3):
                    DISPLAYSURF.blit(heart[i].image,heart[i].rect)
		pygame.display.update()
                if ll:
                    time.sleep(2)
                if st==1:#Game Over
                    del heart[0:3]
                    ball_list.empty()
                    stair_list.empty()
                    line_list.empty()
                    play_list.empty()
                    coin_list.empty()
                    time.sleep(2)
                    main()
                fpsClock.tick(FPS)
        main()

