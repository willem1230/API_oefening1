
import requests
import json

nsfw = input("wil je nsfw te zien krijgen of niet? (ja of nee)")

if nsfw == "ja":
    response = requests.get("https://moppenbot.nl/api/random/?nsfw=true")
    data = response.text
    specifiek = json.loads(data)
    joke = specifiek["joke"]
    joke1 = joke["joke"]
    print(joke1)

else:
    response = requests.get("https://moppenbot.nl/api/random/")
    data = response.text
    specifiek = json.loads(data)
    joke = specifiek["joke"]
    joke1 = joke["joke"]
    print(joke1)
