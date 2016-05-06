import numpy as np
import pdb
from Grid_helper import *


def find_robbers(clean_grid):
	
	robber_locations = []
	indicies = np.where(clean_grid==2)
	if len(indicies[0]) == 0:
		print 'no robbers found'
		return False
	else:
		for i in range(0,len(indicies[0])):
			robber_locations.append((indicies[0][i], indicies[1][i]))
	return robber_locations

def mask_grid(self,grid, vision_radius=2):
	
	full_grid = grid
	nrows = grid.shape[0]
	ncols = grid.shape[1]
	masked_grid = np.full((nrows,ncols),(9,9,9), dtype=(int,3))
	#vision_radius = 2
	for i in range(0,nrows):
		for j in range(0,ncols):
			if full_grid[i,j][1] == self.team:
				for n in range(-vision_radius, vision_radius+1):
					for k in range(-vision_radius +abs(n), vision_radius+1 -abs(n)):
						if((n+i >=0)&(n+i < nrows)):
							if((k+j >= 0)&(k+j < nrows)):
								masked_grid[n+i,k+j] = full_grid[n+i,k+j]
								
	return masked_grid

def turn_grid_into_neural_net(self, grid):
	clean_grid = get_clean_grid(grid)
	clean_grid[self.location] = 0 #Remove the location of this CS from the grid to properly allocate input
	
	my_input = np.zeros(clean_grid.shape)
	my_input[self.location] = 1
	my_input = my_input.reshape(my_input.size)
	clean_grid = clean_grid.reshape(clean_grid.size)
	
	unseen_input = np.zeros(clean_grid.size)
	unseen_input[np.where(clean_grid == 9)] = 1
	
	blocks_input = np.zeros(clean_grid.size)
	blocks_input[np.where(clean_grid == 1)] = 1
	
	cops_input = np.zeros(clean_grid.size)
	cops_input[np.where(clean_grid == 2)] = 1
	
	robbers_input = np.zeros(clean_grid.size)
	robbers_input[np.where(clean_grid == 3)] = 1
	
	
	#Fow, obstacles, cops, robbers, cs_location
	unseen_input = np.append(unseen_input, blocks_input)
	unseen_input = np.append(unseen_input, cops_input)
	unseen_input = np.append(unseen_input, robbers_input)
	unseen_input = np.append(unseen_input, my_input)
	
	return unseen_input
