import numpy as np
from math import floor
from Grid_helper import *
import pdb
from cs_helper import *
from moves import *
from neural_net import *
#import matplotlib.pyplot as plt
#from cop import *
#from robber import *

class Grid:
	#Stores the "playing field" Or location of all of the constituient systems.
	#Stored as a 2d array with tuples for each spot. The tuple consists of:
	#system_type, team, id
	def __init__(self, size):
		self.grid = np.full((size,size),(1,0,0), dtype=(int,3))
		self.grid = insert_obstacles(2,2,self.grid)
		self.recently_removed_piece = None
		self.move_checker = is_valid_move
		#print self.grid
		#pdb.set_trace()
	
	def insert_system_into_grid(self, team, id_number, location):
		#pdb.set_trace()
		if self.grid[location][0] != 0:
			print 'Cannot Place there'
			return False
		else:
			self.grid[location] = [team.list_of_systems[id_number].system_type, team.team_number, id_number]
			team.update_cs_location(id_number, location)
			#print self.grid
			return True
	
	def attach_move_checker(self,fn):
		self.move_checker = fn
	
	def remove_piece_for_team(self, team, name=None):
		if(name == None):
			return
		if name in team.system_names:
			print 'removed: ' + str(name)
			team.update_cs_location(name[2],False)
		
	
	def move_cs(self, team, id_number, location):
		#A team will call this from the Grid in order to move.
		#This will return false if that move is not valid
		#Otherwise, it will return the value of the piece that was removed
		
		#remove the piece from the grid before checking if it is moving to a valid location
		#this is to ensure that the move does not return False when not moving
		original_cs_location = np.copy(team.list_of_systems[id_number].location)
		original_cs_location = tuple(original_cs_location)
		original_cs_value = np.copy(self.grid[original_cs_location])
		self.grid[original_cs_location] = (0,0,0)
		if self.move_checker(self.grid, location):
			#pdb.set_trace()
			#original_cs_location = team.list_of_systems[id_number].location
			#self.grid[original_cs_location] = (0,0,0)
			old_grid_value = np.copy(self.grid[location])
			new_grid_value = (team.list_of_systems[id_number].system_type, team.team_number, id_number)
			self.grid[location] = new_grid_value
			self.recently_removed_piece = tuple(old_grid_value)
			return self.recently_removed_piece
		else:
			#If false, return the piece back to it's original spot
			self.grid[original_cs_location] = tuple(original_cs_value)
			
			#Return np.array([-1,-1,-1]) to signify that this move was invalid
			return np.array([-1, -1, -1])
	
	def get_grid(self):
		return self.grid
		
class Team:
	#Stores all of the constituient systems for a given team.
	#Communicates to the Grid
	#For cops + robbers, all of the constituient systems are the same type.
	#Is what "moves" when it is the given team's turn. The team selects which constituient
	#system is allowed to move. In the case of cops + robbers, each CS must move in an exact order
	def __init__(self, team_number):
		self.list_of_systems = [None]
		self.cs_id_turn = 1
		self.number_of_systems = 0
		self.system_locations = [None]
		self.system_names = [None]
		self.team_number = team_number
		self.recently_moved = None
		
	def __str__(self):
		print 'team number = ' +  str(self.team_number)
		print 'number of systems = ' + str(self.number_of_systems)
		print self.system_locations
		return 'done'
		
	def add_system(self, cs):
		self.number_of_systems = self.number_of_systems + 1
		cs.update_team(self.team_number, self.number_of_systems)
		cs.set_name()
		self.system_names.append(cs.get_name())
		self.list_of_systems.append(cs)
		self.system_locations.append(cs.location)
		
	
	def update_cs_location(self, id_number, location):
		if location != False:
			self.list_of_systems[id_number].update_location(location)
			self.system_locations[id_number] = location
			self.list_of_systems[id_number].enter_grid()
		else:
			self.list_of_systems[id_number].update_location((None,None)) #should work
			self.system_locations[id_number] = (None,None)
			self.list_of_systems[id_number].exit_grid()
	def move(self, G):
		#move one of the constituient systems here, or let the constituient system choose how to move
		if(self.cs_id_turn > self.number_of_systems):
			self.cs_id_turn = 1
		moving_cs = self.list_of_systems[self.cs_id_turn]
		if(moving_cs.is_in_grid == False):
			self.cs_id_turn = self.cs_id_turn + 1
			return
		
		movement_list = moving_cs.move(G.get_grid())
		move_number = len(movement_list) - 1
		#print move_number
		
		#Moves the piece here
		removed_piece = G.move_cs(self, self.cs_id_turn, movement_list[move_number])
		while((np.array(removed_piece) == [-1, -1, -1]).all()):
			move_number = move_number - 1
			#print move_number
			removed_piece = G.move_cs(self, self.cs_id_turn, movement_list[move_number])
		
		#Updates the location of the cs AND the team here
		self.update_cs_location(self.cs_id_turn, movement_list[move_number])
		self.recently_moved = moving_cs.name
		
		moving_cs.update_points(removed_piece)
		
		self.cs_id_turn = self.cs_id_turn + 1
		print get_clean_grid(G.grid)
		
		#test = get_clean_grid(G.grid)
		#plt.matshow(test)
		#plt.show()
		return removed_piece
	
	def add_points(self):
		
		for cs in self.list_of_systems[1:]:
			cs.update_points_team(0.0)
		
		
		
class ConstituientSystem(object):
	def __init__(self, system_type):
		self.team = None
		self.id_number = None #id number
		self.system_type = system_type
		self.location = (None, None)
		self.is_in_grid = False
		self.observations = None
		self.clean_observations = None
		self.move_list = [dont_move]
		self.points = float(0)
		self.turns_alive = 0
		self.movement_object = None
		self.name = None
		
	def update_team(self,team, number):
		self.team = team
		self.id_number = number
		
	def update_location(self,location):
		#Called by the team that it is associated with to notify the updated position of this
		self.location = location
	def enter_grid(self):
		self.is_in_grid = True
	
	def exit_grid(self):
		self.is_in_grid = False
	
	def get_observations(self,grid):
		self.observations = grid
	
	def attach_move(self,move_function):
		self.move_list.append(move_function)
	
	def attach_movement_object(self, movement_object):
		self.movement_object = movement_object
	
	def move(self, grid):
		print 'hi'
	
	def set_name(self):
		self.name = (self.system_type, self.team, self.id_number)
	
	def get_name(self):
		return self.name
	
	def update_points(self, extra_inputs = None):
			print 'Default CS does not use points'
			return 1
	
	def update_points_team(self, points_added):
		#This function should be used for the Team to add points for the system.
		self.points = self.points + points_added
		
		
