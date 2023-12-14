
import requests
import json
import urllib.request
from PIL import Image

keuze = input("wil je de foto opslaan? (ja) anders word deze weergegeven in webbrouwser")


foto_request = requests.get("https://dog.ceo/api/breeds/image/random")

data = foto_request.text

specifiek = json.loads(data)
afbeelding_url = specifiek["message"]

if keuze == "ja":
    urllib.request.urlretrieve(afbeelding_url, "afbeelding_random.png")
    my_img = Image.open("afbeelding_random.png")
    my_img.show()
else:
    print(afbeelding_url)




