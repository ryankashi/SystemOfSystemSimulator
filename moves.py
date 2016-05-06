import numpy as np
import pdb

def move_up(location, name = None):
	new_location = location
	new_location = list(new_location)
	new_location[0] = new_location[0] - 1
	new_location = tuple(new_location)
	return new_location

def move_down(location, name = None):
	new_location = location
	new_location = list(new_location)
	new_location[0] = new_location[0] + 1
	new_location = tuple(new_location)
	return new_location

def move_left(location, name = None):
	new_location = location
	new_location = list(new_location)
	new_location[1] = new_location[1] - 1
	new_location = tuple(new_location)
	return new_location

def move_right(location, name = None):
	new_location = location
	new_location = list(new_location)
	new_location[1] = new_location[1] + 1
	new_location = tuple(new_location)
	return new_location

def dont_move(location, name = None):
	new_location = location
	return new_location

def move_pawn_black(location, name = None):
	new_location = location
	new_location = list(new_location)
	new_location[0] = new_location[0] + 1
	new_location = tuple(new_location)
	return new_location

def attack_black_pawn_left(location, name = None):
	new_location = location
	new_location = list(new_location)
	new_location[0] = new_location[0] + 1
	new_location[1] = new_location[0] - 1
	new_location = tuple(new_location)
	return new_location