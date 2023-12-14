
import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)

data = response.text

specifiek = json.loads(data)
title = specifiek["title"]
print("title =", title)

completed = specifiek["completed"]


if completed == True:
    print("good job")
if completed == False:
    print("er moet nog werk gedaan worden")


