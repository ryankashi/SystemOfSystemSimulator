import numpy as np
from math import floor
from Grid_helper import *
import pdb
from cs_helper import *
from moves import *
from neural_net import *
#import matplotlib.pyplot as plt
from sos import *


class Cop(ConstituientSystem):
	def __init__(self):
		super(Cop, self).__init__(2)
		self.attach_movement_object(NeuralNetwork())
		
	#need function to "start" the neural network before calling move
	#This includes attaching the movements available
	
	def get_observations(self,grid):
		#sets self.observations to be the input for the movement object
		
		masked_grid = mask_grid(self,grid,4)
		self.clean_observations = get_clean_grid(masked_grid)
		
		input_grid = turn_grid_into_neural_net(self, masked_grid)
		self.observations = input_grid
		return input_grid
	
	def start(self, w0file = None, w1file = None):
		#starts the neural network, and gets everything ready for move to be called.
		print 'Attaching movements to Neural Network'
		for i in range(len(self.move_list)):
			self.movement_object.add_output()
		if(w0file == None):
			print 'Initializing new weights'
			self.movement_object.initialize_weights()
		else:
			print 'Loading weights'
			self.movement_object.load_weights(w0file, w1file)
		
		print 'Cop ready for simulation'
			
	def move(self, grid):
		#returns the location that this sytem wants to move to
		#Computes output of neural network, and returns the list of locations it wants to move
		#Most preferred movement is the last index of the array
		self.get_observations(grid)
		output_weights = self.movement_object.get_output(self.observations)
		movement_list = self.movement_object.get_ordered_list_of_moves(output_weights)
		movement_locations = []
		for j in range(movement_list.size):
			move_index = movement_list[j]
			movement_locations.append(self.move_list[move_index](self.location, self.name))
		
		print self.name
		print output_weights
		print movement_locations
		return movement_locations
		
	def update_points(self, removed_piece = None):
		if(self.is_in_grid == True):
			if(removed_piece != None):
				self.turns_alive = self.turns_alive + 1
				if(removed_piece[1] == self.team):
					self.points = self.points - 30
				elif(removed_piece[1] == 2): #If the removed team belongs to the robbers
					self.points = self.points + float(-0.5) * float(self.turns_alive) + float(40)
				print str(self.name) + 'points: ' + str(self.points)
				
				
				
				
				
				
