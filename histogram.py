import matplotlib.pyplot as plt
import numpy as numpy
import sys
import math
import pandas as pd


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
		#print ("Self.input_bins =", self.input_bins)

	def make_histogram(self, num_output, current_bin_list):
		#outputs histogram with name[num_output] as title
		bin_list = []
		labels = []
		X_axis = []
		name = self.title_name + '[' + str(num_output) + ']'
		for i in range(0,self.num_bins):
			bin_list.append(i)
			labels.append(current_bin_list[i])
			X_axis.append(i)


		freq_series = pd.Series.from_array(current_bin_list)

		fig = plt.figure(1)

		plt.figure(figsize=(12, 8))
		ax = freq_series.plot(kind='bar')
		ax.set_title(name)
		ax.set_xlabel("Bin")
		ax.set_ylabel("Frequency")
		ax.set_xticklabels(X_axis)
		

		rects = ax.patches
		for rect, label in zip(rects, labels):
		    height = rect.get_height()
		    ax.text(rect.get_x() + rect.get_width()/2, height + 5, label, ha='center', va='bottom')

		plt.savefig(name)

	def output_all_histograms(self):
		current_bin_list = []
		i = 0
		j = 0
		while i < self.num_histograms:
			j = 0
			while j < self.num_bins:
				current_bin_list.append(self.input_bins[self.num_histograms*j+i])
				j+=1
			print("Current_bin_list = ", current_bin_list)
			self.make_histogram(i, current_bin_list)
			i+=1
			del current_bin_list[:]
			#clear List

