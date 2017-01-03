#Import kmeans clustering from sci-kit-learn
from sklearn.cluster import KMeans
import numpy as numpy
import csv

#Load in the dataset as a 2d array for convenience
data = [];
file = open('dropped_movie_data.csv');
for line in file:
	data.append(line.strip().split(','));

#Pop the first row because it contains column headers
del(data[0]);


#Perform k-means clustering with k = 50
k = 40;
kmeans_objects = KMeans(n_clusters = k);
kmeans.fit(data);

cluster_assignments = kmeans.labels_;

ratio = 0.2;

clusters = [];
cluster = [];
cluster_nums = [];

newData = [];

#initialize double cluster array
for lists in range(0,k):
	cluster.append(0);
	clusters.append(cluster);
	cluster = [];

#Place each element into it's cluster
for n in range(0,len(cluster_assignments)):
	clusters[cluster_assignments[n]].append(data[n]);

#Count the number of elements in each cluster
for i in range(0,k):
	cluster_nums.append(len(clusters[i]));

#Randomly select a sample from each cluster proportional to that cluster size and 
# add it to a new data set
for m in range(0,len(cluster_nums)):
	rand = numpy.random.randint(cluster_nums[m],size=int(ratio*cluster_nums[m]));
	for rand_element in rand:
	 	entry = clusters[m][rand_element];
	 	if(entry != 0):
	 		newData.append(entry);

numpy.trim_zeros(newData);

new_csv_file = open('final_reduced_data.csv', 'w');
writer = csv.writer(new_csv_file);
for row in newData:
	writer.writerow(row);

new_csv_file.close()    