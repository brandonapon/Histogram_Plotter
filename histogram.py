import matplotlib.pyplot as pyplot
import numpy as numpy
import sys
import math

class histogram:
	def __init__(self):
		self.title_name = None
		self.read_in = []
		self.input_bins = []
		self.num_bins = 0
		self.num_histograms = 0

	def import_file(self, filename):
		#reads in .txt file and saves bin values
		file = open(filename, "r")
		self.read_in = file.read().split()
		index_full = 2

		while index_full < (self.num_bins*self.num_histograms*3):
				self.input_bins.append(int(self.read_in[index_full]))
				index_full+=3
		print ("Self.input_bins =", self.input_bins)

	def make_histogram(self, num_output, current_bin_list):
		#outputs histogram with name[num_output] as title
		pass

	def output_all_histograms(self):
		current_bin_list = []
		i = 0
		j = 0
		while i < self.num_histograms:
			while j < self.num_bins:
				current_bin_list.append(self.input_bins[i+j])
				j+=1
			i+=1

