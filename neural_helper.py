import numpy as np
import pdb

def sigmoid(x):
	return 1/(1+np.exp(-x))



def save_best_cs_net(team, w0file, w1file):
	points_list = [None]
	for cs in team.list_of_systems[1:]:
		points_list.append(cs.points)
		
	indexarray = np.argsort(points_list)
	cs_id = indexarray[-1]
	
	best_cs = team.list_of_systems[cs_id]
	
	best_nn = best_cs.movement_object
	best_nn.save_weights(w0file, w1file)
	
		