import numpy as np
from math import floor
from Grid_helper import *
import pdb
from cs_helper import *
from moves import *
from neural_net import *
import matplotlib.pyplot as plt
from drawnow import drawnow
from sos import *
from cop import *
from robber import *
from time import sleep


def create_robber(t1, robber_w0, robber_w1):
	r1 = Robber()
	r1.attach_move(move_up)
	r1.attach_move(move_down)
	r1.attach_move(move_left)
	r1.attach_move(move_right)
	t1.add_system(r1)
	r1.start(robber_w0,robber_w1)
	
def create_cop(t1, cop_w0, cop_w1):
	c1 = Cop()
	c1.attach_move(move_up)
	c1.attach_move(move_down)
	c1.attach_move(move_left)
	c1.attach_move(move_right)
	t1.add_system(c1)
	c1.start(cop_w0,cop_w1)
	
def run():
	SHOW_FIG = True
	cop_w0 = 'cop_w0_new.npy'
	cop_w1 = 'cop_w1_new.npy'
	robber_w0 = 'robber_w0_new.npy'
	robber_w1 = 'robber_w1_new.npy'
	num_turns = 90
	silly_num = 0
	
	G = Grid(10)
	G.attach_move_checker(is_valid_move)
	print 'hi'
	t1 = Team(1)
	t2 = Team(2)
	r1 = Robber()
	r2 = Robber()
	r3 = Robber()
	#r4 = Robber()
	#r5 = Robber()
	
	r1.attach_move(move_up)
	r1.attach_move(move_down)
	r1.attach_move(move_left)
	r1.attach_move(move_right)
	
	r2.attach_move(move_up)
	r2.attach_move(move_down)
	r2.attach_move(move_left)
	r2.attach_move(move_right)
	
	r3.attach_move(move_up)
	r3.attach_move(move_down)
	r3.attach_move(move_left)
	r3.attach_move(move_right)
	
	#r4.attach_move(move_up)
	#r4.attach_move(move_down)
	#r4.attach_move(move_left)
	#r4.attach_move(move_right)
	
	#r5.attach_move(move_up)
	#r5.attach_move(move_down)
	#r5.attach_move(move_left)
	#r5.attach_move(move_right)
	
	#c1 = ConstituientSystem(2)
	c1 = Cop()
	c2 = Cop()
	c3 = Cop()
	#c4 = Cop()
	#c5 = Cop()
	
	c1.attach_move(move_up)
	c1.attach_move(move_down)
	c1.attach_move(move_left)
	c1.attach_move(move_right)
	
	c2.attach_move(move_up)
	c2.attach_move(move_down)
	c2.attach_move(move_left)
	c2.attach_move(move_right)
	
	c3.attach_move(move_up)
	c3.attach_move(move_down)
	c3.attach_move(move_left)
	c3.attach_move(move_right)
	
	#c4.attach_move(move_up)
	#c4.attach_move(move_down)
	#c4.attach_move(move_left)
	#c4.attach_move(move_right)
	
	#c5.attach_move(move_up)
	#c5.attach_move(move_down)
	#c5.attach_move(move_left)
	#c5.attach_move(move_right)

	t1.add_system(c1)
	t1.add_system(c2)
	t1.add_system(c3)
	#t1.add_system(c4)
	#t1.add_system(c5)
	
	t2.add_system(r1)
	t2.add_system(r2)
	t2.add_system(r3)
	#t2.add_system(r4)
	#t2.add_system(r5)
	
	c1.start(cop_w0,cop_w1)
	c2.start(cop_w0,cop_w1)
	c3.start(cop_w0,cop_w1)
	#c4.start(cop_w0,cop_w1)
	#c5.start(cop_w0,cop_w1)

	r1.start(robber_w0,robber_w1)
	r2.start(robber_w0,robber_w1)
	r3.start(robber_w0,robber_w1)
	#r4.start(robber_w0,robber_w1)
	#r5.start(robber_w0,robber_w1)
	
	create_cop(t1, cop_w0, cop_w1)
	create_cop(t1, cop_w0, cop_w1)
	create_cop(t1, cop_w0, cop_w1)
	create_cop(t1, cop_w0, cop_w1)
	create_cop(t1, cop_w0, cop_w1)
	create_cop(t1, cop_w0, cop_w1)
	
	create_robber(t2, robber_w0, robber_w1)
	create_robber(t2, robber_w0, robber_w1)
	create_robber(t2, robber_w0, robber_w1)
	
	tuple(np.random.randint(10,size=2))
	
	
	while(G.insert_system_into_grid(t1,1,tuple(np.random.randint(10,size=2))) == False):
		silly_num = silly_num + 1
		
	while(G.insert_system_into_grid(t1,2,tuple(np.random.randint(10,size=2))) == False):
		silly_num = silly_num + 1
	
	while(G.insert_system_into_grid(t1,3,tuple(np.random.randint(10,size=2))) == False):
		silly_num = silly_num + 1
	while(G.insert_system_into_grid(t1,4,tuple(np.random.randint(10,size=2))) == False):
		silly_num = silly_num + 1
	while(G.insert_system_into_grid(t1,5,tuple(np.random.randint(10,size=2))) == False):
		silly_num = silly_num + 1
	while(G.insert_system_into_grid(t1,6,tuple(np.random.randint(10,size=2))) == False):
		silly_num = silly_num + 1
	while(G.insert_system_into_grid(t1,7,tuple(np.random.randint(10,size=2))) == False):
		silly_num = silly_num + 1
	while(G.insert_system_into_grid(t1,8,tuple(np.random.randint(10,size=2))) == False):
		silly_num = silly_num + 1
	while(G.insert_system_into_grid(t1,9,tuple(np.random.randint(10,size=2))) == False):
		silly_num = silly_num + 1
	
	
	while(G.insert_system_into_grid(t2,1,tuple(np.random.randint(10,size=2))) == False):
		silly_num = silly_num + 1
	while(G.insert_system_into_grid(t2,2,tuple(np.random.randint(10,size=2))) == False):
		silly_num = silly_num + 1
		
	while(G.insert_system_into_grid(t2,3,tuple(np.random.randint(10,size=2))) == False):
		silly_num = silly_num + 1
	while(G.insert_system_into_grid(t2,4,tuple(np.random.randint(10,size=2))) == False):
		silly_num = silly_num + 1
	while(G.insert_system_into_grid(t2,5,tuple(np.random.randint(10,size=2))) == False):
		silly_num = silly_num + 1
	while(G.insert_system_into_grid(t2,6,tuple(np.random.randint(10,size=2))) == False):
		silly_num = silly_num + 1

	#G.insert_system_into_grid(t2,4,tuple(np.random.randint(10,size=2)))
	#G.insert_system_into_grid(t2,5,tuple(np.random.randint(10,size=2)))
	
	
	
	
	
	#What it takes for t1 to fully move
	#removed_piece = t1.move(G)
	#G.remove_piece_for_team(t1, removed_piece)
	#G.remove_piece_for_team(t2, removed_piece)
	#t2.add_points()
	#t1.add_points()
	#End what it takes for t1 to fully move
	
	
	#pdb.set_trace()
	clean_grid = get_clean_grid(G.grid)
	
	if SHOW_FIG:
		plt.ion()
		fig = plt.figure()
		ax = fig.add_subplot(111)
		sleep(1)
		line1 = ax.matshow(clean_grid)
	
	
	
	for turn in range(num_turns):
		#A move by t1
		removed_piece = t1.move(G)
		print removed_piece
		G.remove_piece_for_team(t1, removed_piece)
		G.remove_piece_for_team(t2, removed_piece)
		t2.add_points()
		t1.add_points()
		
		clean_grid = get_clean_grid(G.grid)
		
		if SHOW_FIG:
			line1.set_data(clean_grid)
			fig.canvas.draw()
			#sleep(10)
			pdb.set_trace()
			#sleep(0.5)
		
		#A move by t2
		removed_piece = t2.move(G)
		print removed_piece
		G.remove_piece_for_team(t2, removed_piece)
		G.remove_piece_for_team(t1, removed_piece)
		t1.add_points()
		t2.add_points()
		
		clean_grid = get_clean_grid(G.grid)
		if SHOW_FIG:
			line1.set_data(clean_grid)
			fig.canvas.draw()
			pdb.set_trace()
		#sleep(0.5)
		
	
	print get_clean_grid(G.grid)
	save_best_cs_net(t1, cop_w0 , cop_w1)
	save_best_cs_net(t2, robber_w0, robber_w1)
	clean_grid = get_clean_grid(G.grid)
	
	
	
if __name__ == "__main__":
	while True:
		run()
