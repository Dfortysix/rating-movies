from django.shortcuts import render
import requests
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMjI3OTA2OTM3YzBhZDZjNTMxZjI3NDE3ZDgxMWUwNCIsInN1YiI6IjY2MzI2M2E5YzA0NDI5MDEyYzhkY2I5YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TteZYwN_RqPnKSEOUbbjcmK4eB0iSGWoTNta4BFywrA"
}
tmdb_url = "https://image.tmdb.org/t/p/original"

# Create your views here.
def movie_detail(request,movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    cast_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?language=en-US"
    recommend_url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?language=en-US&page=1"
    video_url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?language=en-US"

    response = requests.get(url, headers=headers)
    data = response.json()

    casts_response = requests.get(cast_url, headers=headers)
    casts_data = casts_response.json()

    recommend_response = requests.get(recommend_url, headers=headers)
    recommend_data = recommend_response.json()

    video_response = requests.get(video_url, headers=headers)
    video_data = video_response.json()

    kinds = []
    movie_data = {
        "title": data["title"],
        "release_date": data["release_date"],
        "overview": data["overview"],
        "runtime": data["runtime"],
        "poster_path": tmdb_url + data["poster_path"],
        "backdrop_path": tmdb_url + data["backdrop_path"],
        "video": "https://www.youtube.com/embed/" + video_data["results"][-1]["key"]
    }
    for kind in data['genres']:
        kinds.append(kind['name'])

    casts =[]
    for cast in casts_data["cast"][0:9]:
        cast_data = {
            "name": cast["name"],
            "character": cast["character"],
            "cast_image": tmdb_url + str(cast["profile_path"])
        }
        casts.append(cast_data)

    recommendations = []
    for rec in recommend_data["results"]:
        recommendation_data = {
            "id" : rec["id"],
            "image": tmdb_url +str(rec["backdrop_path"]),
            "title": rec["title"],
            "year": rec["release_date"][0:4]
        }
        recommendations.append(recommendation_data)

    movie_data["kinds"] = kinds
    context = {"movie_data": movie_data, "casts": casts, "recs":recommendations}
    return render(request,'movies/movie_detail.html',context=context)