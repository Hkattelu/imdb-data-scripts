import pandas as pandas

movie_df = pandas.read_csv("transformed_movie_data.csv");

#Colors
colors = {"Color":1," Black and White":2};

#Languages
languages = {"Kazakh":1,"Korean":2
			,"Russian":3,"Dzhongka":4
			,"German":5,"Chinese":6,
			 "Japanese":7,"Czech":8
			 ,"Hindi":9,"Danish":10
			 ,"Romanian":11,"Swedish":12
			 ,"Urdu":13,"Filipino":14,
			 "Norwegian":15,"None":16,
			 "English":17,"Zulu":18,
			 "Spanish":19,"French":20
			 ,"Greek":21,"Thai":22,
			 "Vietnamese":23,"Aramaic":24,
			 "Mandarin":25,"Nan":26,
			 "Indonesian":27,"Dari":28,
			 "Dutch":29,"Mongolian":30,
			 "Maya":31,"Cantonese":32,
			 "Hungarian":33,"Portuguese":34,
			 "Persian":35,"Swahili":36,
			 "Aboriginal":37,"Panjabi":38,
			 "Slovenian":39,"Arabic":40,
			 "Polish":41,"Kannada":42,
			 "Tamil":43,"Bosnian":44,
			 "Hebrew":45,"Telugu":46,
			 "Icelandic":47,"Italian":48}

#Content ratings
ratings = {'':1, 'NC-17':2, 'TV-Y':3, 'G':4, 'GP':5,
		 'TV-14':6,'M':8, 'PG-13':9, 'Approved':10, 
		 'TV-Y7':11, 'R':12, 'Not Rated':13, 'PG':14, 'Passed':15, 'X':16, 'TV-MA':17,
		  'TV-PG':18, 'TV-G':19, 'Unrated':20}

#Countries
countries = {'Canada':1, '':2, 'Argentina':3, 'Italy':4, 'Czech Republic':5, 'USA':6, "Afghanistan":7,
			'Panama':8, 'Kyrgyzstan':9, 'Cambodia':10,'France':11, 'Bahamas':12, 'West Germany':13
			 , 'Georgia':14, 'Aruba':15,'Peru':16, 'United Arab Emirates':17, 'Nigeria':18, 'Norway':19, 
			 'Thailand':20, 'Kenya':21, 'Slovakia':22,  'Australia':23, 'Iran':24, 'Indonesia':25, 
			 'Iceland':26, 'Official site':27, 'New Line':28, 'Slovenia':29, 
			   'China':30, 'Chile':31, 'Belgium':32, 'Germany':33, 'Dominican Republic':34, 'Bulgaria':35
			   , 'Hong Kong':36, 'Taiwan':37, 'Spain':38, 'Ireland':39, 'Netherlands':40, 'Colombia':41,
			    'Libya':42, 'Denmark':43, 'Poland':44,'Finland':45, 'Israel':46, 'Cameroon':47, 'Turkey':48,
			     'Philippines':49, 'Sweden':50, 'Hungary':51, 'Switzerland':52,'New Zealand':53,
			      'Russia':54, 'Brazil':55, 'Soviet Union':56, 'Pakistan':57, 'Romania':58, 
		      'Mexico':59, 'Egypt':60, 'South Africa':61, 'India':62, 'UK':63, 'Greece':64, 'Japan':65,
		       'South Korea':66}

# Assign ID's to colors
movie_df = movie_df.applymap(lambda x: colors[x] if x in colors else x);

# Assign ID's to languages
movie_df = movie_df.applymap(lambda x: languages[x] if x in languages else x);

# Assign ID's to ratings
movie_df = movie_df.applymap(lambda x: ratings[x] if x in ratings else x);

# Assign ID's to countries
movie_df = movie_df.applymap(lambda x: countries[x] if x in countries else x);


movie_df.to_csv("numerical_movie_data.csv");
