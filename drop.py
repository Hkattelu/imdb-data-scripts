import pandas as pandas
import numpy as numpy

movie_df = pandas.read_csv("numerical_movie_data.csv");

movie_df.replace('', numpy.nan, inplace=True);

movie_df.dropna(inplace = True);

movie_df.to_csv("dropped_movie_data.csv");