import numpy as np
import pdb
from neural_helper import *
import os

class NeuralNetwork(object):
	def __init__(self):
		self.number_of_outputs = 0
		self.number_of_inputs = 100 * 5 				#FoW, obstacles, cops, robbers, self_location
		self.number_in_hidden_layer = 100
		self.weights0 = []
		self.weights1 = []
		self.points = 0
		
	def add_output(self):
		self.number_of_outputs = self.number_of_outputs + 1
		
	def initialize_weights(self, hidden_layer_size = None): #can only be called once all outputs are added
		if (hidden_layer_size != None):
			self.number_in_hidden_layer = hidden_layer_size
		
		self.weights0 = 0.01*np.random.normal(0, 0.1,(self.number_of_inputs, self.number_in_hidden_layer))
		
		self.weights1 = 0.01*np.random.normal(0, 0.1,(self.number_in_hidden_layer, self.number_of_outputs))
		
		
	def get_output(self,input_layer):
		hl = sigmoid(np.dot(input_layer,self.weights0))
		output = sigmoid(np.dot(hl, self.weights1))
		return output
		
		
	def load_weights(self, w0file, w1file):
		if os.path.isfile(w0file):
			print 'Loading weights'
			self.weights0 = np.load(w0file)
			self.weights0 = self.weights0 + 0.5*np.random.normal(0, 0.1, self.weights0.shape)
			self.weights1 = np.load(w1file)
			self.weights1 = self.weights1 + 0.5*np.random.normal(0, 0.1,self.weights1.shape)
		#load previously made weights
		else:
			self.initialize_weights()
		
	def save_weights(self, w0file, w1file):
		print 'Saving Weights'
		np.save(w0file, self.weights0)
		np.save(w1file, self.weights1)
		#save current weights to filename
		
		
	def get_ordered_list_of_moves(self,output_vals):
		exp_vals = np.zeros(output_vals.size)
		exp_probs = np.zeros(output_vals.size)
		ordered_list = np.zeros(output_vals.size)
		total_exp = 0
		#for i in range(output_vals.size):
		#	exp_vals[i] = np.exp(output_vals[i])
		exp_vals = np.exp(output_vals) - 1
		for j in range(output_vals.size -1, -1, -1):
			threshold = 0
			total_exp = exp_vals.sum()
			exp_probs = exp_vals / total_exp
			roll = np.random.random()
			for i in range(output_vals.size):
				threshold = exp_probs[i] + threshold
				if roll <= threshold:
					ordered_list[j] = i
					exp_vals[i] = 0
					break
	
	
		#ordered_list = np.argsort(output_vals)
		ordered_list = ordered_list.astype(int)
		return ordered_list
	
	