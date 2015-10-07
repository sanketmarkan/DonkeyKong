import pytest
import pygame
import board
import random
import character
y=character.Player('playerright.png',50,50)
play_list=pygame.sprite.Group()
play_list.add(y)

line_list,stair_list = board.boards().gen_board()

def test_donkey():
	try:
		a=character.Donkey('donkey.png',20,30)
	except:
		pytest.fail('Donkey Not Created')

def test_person():
	try:
		y=character.Player('playerright.png',50,50)
	except:
		pytest.fail('Player Not Created')

def test_get_pos():
	y=character.Donkey('donkey.png',20,30)
	c=0
	while c<100:
		x = random.randrange(0,900)
		z = random.randrange(0,500)
		y.rect.x=x
		y.rect.y=z
		a,b = y.getpos()
		assert a==x
		assert b==z
		c=c+1

def test_get_lower():
	c=0
	while c<1000:
		x = random.randrange(0,900)
		z = random.randrange(0,500)
		y.rect.x=x
		y.rect.y=z
		print x,z
		a,b=y.get_lower(x,z,line_list,stair_list,play_list,0)
		if y.collide_stair(stair_list,play_list):
			assert int(a)==x
			assert int(b)==z
		else:
			assert int(a)==x
			assert int(b)%100==26
		c+=1


def test_collide_stair():
	y.rect.x=575
	y.rect.y=101
	assert y.collide_stair(stair_list,play_list)==True
	
	y.rect.x=500
	y.rect.y=101
	assert y.collide_stair(stair_list,play_list)==False

	y.rect.x=325
	y.rect.y=450
	assert y.collide_stair(stair_list,play_list)==True
	
	y.rect.x=0
	y.rect.y=50
	assert y.collide_stair(stair_list,play_list)==False


def test_valid_down():
	y.rect.x=0
	y.rect.y=50
	assert y.valid_down(play_list,stair_list,0)==False

	y.rect.x=550
	y.rect.y=126
	assert y.valid_down(play_list,stair_list,0)==False

	y.rect.x=550
	y.rect.y=100
	assert y.valid_down(play_list,stair_list,0)==True

	y.rect.x=550
	y.rect.y=124
	assert y.valid_down(play_list,stair_list,1)==False	
