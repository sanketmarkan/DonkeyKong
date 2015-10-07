import objects
import board
import random
import character
import pygame
y=character.Player('playerright.png',50,50)
play_list=pygame.sprite.Group()
play_list.add(y)


line_list,stair_list=board.boards().gen_board()
pygame.init()

def test_fireball():
	try:
		a=objects.fireball('fireball.png')
	except:
		pytest.fail('Donkey Not Created')

def test_coins():
	try:
		a=objects.coins('coin.png')
	except:
		pytest.fail('Donkey Not Created')

def test_gen_coins():
	a=objects.coins('coin.png').gen_coins()
	c=0
	for i in a:
		assert int(i.rect.y)%100==54
		c+=1
	assert c==20

def test_getlower():
 	a=objects.fireball('fireball.png')
 	a.down=0
 	a.di=0
 	c=0
 	while c<1000:
	 	x=10
 		y=195
	 	a.rect.x=x
 		a.rect.y=y
	 	a=a.getlower(a,line_list)
 		assert int(a.rect.x)==x
 		assert int(a.rect.y)%100==56
 		c+=1

def test_settle_coins():
	coin_list=objects.coins('coin.png').gen_coins()
	coinss=objects.coins('coin.png').settle_coins(coin_list,line_list)
	for coin in coinss:
		assert int(coin.rect.y)%100==56
