import requests

baseurl = "https://rickandmortyapi.com/api/"
endpoint = "character"
page = str(input("page: "))
result = requests.get(baseurl + endpoint + "/?page=" + page)
data = result.json()

counter = 0

amount = 0

for i in data['results']:
    specie = data['results'][counter]["species"]

    if specie == "Alien":
        print("id: " + str(data['results'][counter]["id"]))
        print("Name: " + data['results'][counter]["name"])
        print("Location: " + data['results'][counter]["location"]["name"])
        print("Species: " + data['results'][counter]["species"])

        specimen = "Alien"

        amount += 1

        print('\n')

    counter += 1

print(f"Total amount of {specimen} = {amount}\nOut of {counter}")
