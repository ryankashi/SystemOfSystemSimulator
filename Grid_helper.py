import numpy as np
import pdb

def insert_obstacles(road_width, obstacle_width, grid):
		total_width = road_width + obstacle_width
		down = grid.shape[0]
		right = grid.shape[1]
		
		iterator = 1
		for i in range(0,down):
			value = i%total_width
			if(value < road_width):
				#x = 5
				grid[i,:] = 0
			#else:
				#grid[i,:] = 1
		for i in range(0,right):
			value = i%total_width
			if(value < road_width):
				#x = 5
				grid[:,i] = 0
			#else:
			#	grid[:,i] = 1	
				
		return grid
	
def get_clean_grid(grid):
	nrows = grid.shape[0]
	ncols = grid.shape[1]
	fucking_stupid = np.zeros([nrows,ncols])
	for i in range(0,nrows):
		for j in range(0,ncols):
			fucking_stupid[i,j] = grid[i,j][0]
	return fucking_stupid

def is_valid_move(grid, location, name= None, original_location = None):
	grid_size = grid.shape
	
	#Make sure piece does not try to move off the grid
	if((location[0] < 0)|(location[0] >= grid_size[0])):
		return False
	elif((location[1] < 0)|(location[1] >= grid_size[1])):
		return False
	
	#If the piece is empty or is a robber, then it is okay
	elif((grid[location][0] == 0)|(grid[location][0] == 3)):
		return True
	
	#If not, return false
	else:
		return False
	
def pawn_move_diagonal(grid, location, name, original_location = None):
	grid_size = grid.shape
	
	#Make sure the piece does not try to move off the grid
	if((location[0] < 0)|(location[0] >= grid_size[0])):
		return False
	elif((location[1] < 0)|(location[1] >= grid_size[1])):
		return False
	
	#Can't move diagonal if the space is empty
	elif(grid[location][0] == 0):
		return False
	
	#If the piece where I want to move is an enemy, then it's okay
	elif(grid[location][1] != name[1]):
		return True
	
	#If not, return false
	else:
		return False
	
	
	
	