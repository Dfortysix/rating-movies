from django.shortcuts import render
import requests


headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMjI3OTA2OTM3YzBhZDZjNTMxZjI3NDE3ZDgxMWUwNCIsInN1YiI6IjY2MzI2M2E5YzA0NDI5MDEyYzhkY2I5YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TteZYwN_RqPnKSEOUbbjcmK4eB0iSGWoTNta4BFywrA"
}

def home(request):

    tmdb_url = "https://image.tmdb.org/t/p/original"

    movies_url = "https://api.themoviedb.org/3/trending/movie/day?language=en-US"
    tv_url = "https://api.themoviedb.org/3/trending/tv/day?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMjI3OTA2OTM3YzBhZDZjNTMxZjI3NDE3ZDgxMWUwNCIsInN1YiI6IjY2MzI2M2E5YzA0NDI5MDEyYzhkY2I5YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TteZYwN_RqPnKSEOUbbjcmK4eB0iSGWoTNta4BFywrA"
    }

    movies_response = requests.get(movies_url, headers=headers)
    movies_data = movies_response.json()

    tv_response = requests.get(tv_url, headers=headers)
    tv_data = tv_response.json()

    movies = []
    tv = []
    for movie in movies_data["results"]:
        movie_data = {
            "id": movie["id"],
            "title": movie["original_title"],
            "release_date": movie["release_date"],
            "poster_path": tmdb_url + movie["poster_path"]
        }
        movies.append(movie_data)

    for movie in tv_data["results"]:
        movie_data = {
            "id": movie["id"],
            "title": movie["original_name"],
            "release_date": movie["first_air_date"],
            "poster_path": tmdb_url + movie["poster_path"]
        }
        tv.append(movie_data)
    context = {"movies": movies,
               "tv": tv}
    return render(request,'home.html',context=context)