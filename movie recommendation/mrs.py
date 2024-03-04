import streamlit as st
import altair as alt
import pickle
import pandas as pd
import numpy as np
import requests

def featch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#if data['poster_path'] == None else 

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    
    recommended_movie = []
    recommend_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movie.append(movies.iloc[i[0]].title)
        # featch posters from api
        recommend_movies_posters.append(featch_poster(movie_id))
    return recommended_movie,recommend_movies_posters   

#movies_dict = pickle.load(open('D:\Internships\growintern\movies_dict.pkl'))
with open('D:\\Internships\\growintern\\movies_dict.pkl', 'rb') as f:
    movies_dict = pickle.load(f, encoding='latin1')

movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('D:\Internships\growintern\similarity.pkl', 'rb'))

st.title("Movie Recommendation System")


selected_movie_name = st.selectbox( 
    'How would you like to be contacted?',
movies['title'].values)

st.write('You selected:', selected_movie_name)

if st.button('Recommend'):
    names,posters =recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
       
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

