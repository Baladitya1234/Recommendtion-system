import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

movies = pd.read_csv("movies.csv")

cv = CountVectorizer(stop_words='english')

vectors = cv.fit_transform(movies['genres']).toarray()

similarity = cosine_similarity(vectors)

pickle.dump(similarity, open("similarity.pkl", "wb"))
pickle.dump(movies, open("movie_list.pkl", "wb"))

print("Model Saved Successfully!")