import matplotlib.pyplot as plt
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
		#print ("Self.input_bins =", self.input_bins)

	def make_histogram(self, num_output, current_bin_list):
		#outputs histogram with name[num_output] as title
		bin_list = []
		for i in range(0,self.num_bins):
			bin_list.append(i)

		fig = plt.figure(1)
		print ("self.num_bins =", self.num_bins)
		plt.bar(bin_list, current_bin_list, color = "blue")

		plt.xlabel('Bins')
		plt.ylabel('Number of Samples')
		plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$') #fix this
		plt.axis([-1, 10, 0, 1500])
		plt.xticks(range(10))
		plt.tick_params(axis=u'both', which=u'both',length=0)
		plt.grid(True)
		name = self.title_name + '[' + str(num_output) + ']'
		fig.savefig(name)

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

