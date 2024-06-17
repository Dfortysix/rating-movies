from django.shortcuts import render
import requests
# Create your views here.


tmdb_url = "https://image.tmdb.org/t/p/original"
def tv_detail(request,tv_id):
    url = f"https://api.themoviedb.org/3/tv/{tv_id}?language=en-US"
    video_url = f"https://api.themoviedb.org/3/tv/{tv_id}/videos?language=en-US"
    cast_url = f"https://api.themoviedb.org/3/tv/{tv_id}/credits?language=en-US"
    recommend_url = f"https://api.themoviedb.org/3/tv/{tv_id}/recommendations?language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMjI3OTA2OTM3YzBhZDZjNTMxZjI3NDE3ZDgxMWUwNCIsInN1YiI6IjY2MzI2M2E5YzA0NDI5MDEyYzhkY2I5YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TteZYwN_RqPnKSEOUbbjcmK4eB0iSGWoTNta4BFywrA"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    video_response = requests.get(video_url,headers=headers)
    video_data = video_response.json()

    cast_response = requests.get(cast_url,headers=headers)
    cast_data = cast_response.json()

    recommend_response = requests.get(recommend_url, headers=headers)
    recommend_data = recommend_response.json()


    tv_data = {
        "title": data["name"],
        "release_date": data["first_air_date"][0:4],
        "overview": data["overview"],
        "poster_path": tmdb_url + data["poster_path"],
        "backdrop_path": tmdb_url + data["backdrop_path"],
        "video": "https://www.youtube.com/embed/" + video_data["results"][-1]["key"],
    }

    casts = []
    for cast in cast_data["cast"][0:9]:
        cast_data = {
            "name": cast["name"],
            "character": cast["character"],
            "cast_image": tmdb_url + str(cast["profile_path"])
        }
        casts.append(cast_data)

    recommendations = []
    for rec in recommend_data["results"]:
        recommendation_data = {
            "id": rec["id"],
            "image": tmdb_url + str(rec["backdrop_path"]),
            "title": rec["name"],
            "year": rec["first_air_date"][0:4]
        }
        recommendations.append(recommendation_data)



    kinds = []
    for kind in data['genres']:
        kinds.append(kind['name'])
    tv_data["kinds"] = kinds
    context = {"tv_data": tv_data, "casts": casts, "recs":recommendations}
    return render(request,'tvseries/tv_detail.html',context=context)
