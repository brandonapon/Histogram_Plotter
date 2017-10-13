import histogram
import matplotlib.pyplot as plt
import sys

if len(sys.argv) != 5:
	print ('Incorrect Format!')
	print ('python hisogram_run.py filename num_bins num_histograms plot_name')

else:
	filename = sys.argv[1]
	num_bins = int(sys.argv[2])
	num_histograms = int(sys.argv[3])
	plot_name = sys.argv[4]

	hist = histogram.histogram()
	hist.num_bins = num_bins
	hist.num_histograms = num_histograms
	hist.title_name = plot_name

	hist.import_file(filename)