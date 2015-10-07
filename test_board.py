import pytest
import board

def test_stair():
	try:
		a=board.Stair()
	except:
		pytest.fail('stair Not Created')

def test_level():
	try:
		a=board.level((0,0,0),10,15)
	except:
		pytest.fail('level Not Created')