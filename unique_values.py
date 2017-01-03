#Load in the dataset as a 2d array for convenience
data = [];
file = open('transformed_movie_data.csv');
for line in file:
	data.append(line.strip().split(','));

column_num = 10;
dictionary = {};
i = 0;

for line in data:
	if (not dictionary.has_key(line[column_num])):
		dictionary[line[column_num]] = i;
		i = i + 1;

print(i);
print (dictionary.keys());
