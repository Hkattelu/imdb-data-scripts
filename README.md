# imdb-data-scripts
A collection of python scripts I used to clean, reduce, and use data for the Kaggle imdb dataset

###Scripts

I created these scripts using python. I used the numpy, pandas, and sci-kit-learn libraries. A brief description
of what each script does is as follows:

- Unique_values.py: Print all unique values in a specified column from the data
- Drop.py: Drop each row in the dataset that contains any empty value
- Assignment.py: Replace strings from the data with unique identification numbers
- Reduction.py: Use K-means clustering to perform stratified sampling and reduce dataset size
- Pca.py: Transform data along the principal axes.
- Biplot.py: Obtain the vectors for the principal axes.
- MDS_data.py: Use the MDS algorithm to transform data to 2 dimensions
- MDS_attributes.py: Use the MDS algorithm to transform attributes to 2 dimensions based on their correlation distance
