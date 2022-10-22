from django.shortcuts import render, redirect
import requests


def index(request):
    if request.method == "POST":
        page = request.POST['page']
        endpoint = f"https://rickandmortyapi.com/api/character/?page={page}"
        result = requests.get(endpoint).json()

        counter = 0
        character_list = []

        for i in result['results']:
            character = {
                "name": result['results'][counter]["name"],
                "specie": result['results'][counter]["species"],
                "image": result['results'][counter]["image"],

            }
            character_list.append(character)
            counter += 1        

        data = {
            "page": page,
            "pages": result['info']['pages'],
            "character": character_list
        }
    else:
        data = {}
    return render(request, "index.html", data)


def error_500(request):
    return render(request, "500.html")