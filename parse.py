import csv
from collections import Counter
import matplotlib.pyplot as plt 
import numpy as np
myFile="/home/sumit/new-coder/dataViz/data/sample_sfpd_incident_all.csv"

def parse(raw_file,delimiter):
	open_file=open(raw_file)
	csv_data = csv.reader(open_file,delimiter=delimiter)
	parse_data = []
	fields = csv_data.next()

	for row in csv_data:
		parse_data.append(dict(zip(fields,row)))

	open_file.close()
	return parse_data

def visualize_days():
	data_file = parse(myFile,",")

	counter=Counter([item["DayOfWeek"] for item in data_file])

	data_list=[
		counter["Monday"],
		counter["Tuesday"],
		counter["Wednesday"],
		counter["Thursday"],
		counter["Friday"],
		counter["Saturday"],
		counter["Sunday"]

	]

	day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

	plt.plot(data_list)
	plt.xticks(range(len(day_tuple)),day_tuple)

	plt.savefig("Days.png")
	plt.clf()


def visualize_type():
	data_file = parse(myFile,",")
	counter=Counter(item["Category"] for item in data_file)
	labels = tuple(counter.keys())
	xlocations = np.arange(len(labels))+0.5
	width = 0.5
	plt.bar(xlocations,counter.values(),width=width)
	plt.xticks(xlocations+width/2,labels,rotation=90)
	plt.subplots_adjust(bottom = 0.4)
	plt.rcParams["figure.figsize"] = 12,8
	plt.savefig("Type.png")
	plt.clf()

def main():
	#visualize_days()
	visualize_type()
if __name__=="__main__":
	main()

