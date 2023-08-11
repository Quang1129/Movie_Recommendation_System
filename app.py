import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = "http://api.themoviedb.org/3/movie/{}?api_key=53e6481ea7f5215e01cac77f2e2543fa".format(movie_id)
    data = requests.get(url)
    data= data.json()
    poster_path = data['poster_path']
    full_path= "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path


movies = pickle.load(open("movies_list.pkl",'rb'))
similarity = pickle.load(open("similarity.pkl",'rb'))
movies_list= movies['title'].values

st.header("Movie Recommendation System")
selectvalue = st.selectbox("Select movie from dropdown", movies_list)

def fetch_poster(movie_id):
    url = "http://api.themoviedb.org/3/movie/{}?api_key=53e6481ea7f5215e01cac77f2e2543fa".format(movie_id)
    data = requests.get(url)
    data= data.json()
    poster_path = data['poster_path']
    full_path= "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path

def recommendation(movie):
    index= movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommendation_values= []
    recommendation_poster=[]
    for i in distance[1:6]:
        movies_id = movies.iloc[i[0]].id
        recommendation_values.append(movies.iloc[i[0]].title)
        recommendation_poster.append(fetch_poster(movies_id))
    return recommendation_values, recommendation_poster


if st.button("Show recommendation"):
    movie_name, movie_poster = recommendation(selectvalue)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])

    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])

    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])

    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])

    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])

