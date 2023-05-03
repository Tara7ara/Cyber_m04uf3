#!/usr/bin/python3

import requests

generador = "Generando un usuario random"
print(generador)
print("-"*len(generador))

api_url = "https://randomuser.me/api"

response = requests.get(api_url)

info = (response.json())

user_name = info["results"][0]["name"]
location = info["results"][0]["location"]
profile = info["results"][0]["picture"]

print("Nombre: "+ user_name["first"] +" "+ user_name["last"])
print("Calle: " + location["street"]["name"])
print("Ciudad: " + location["city"])
print("País: " + location["country"])
print("Profile: " + profile["large"])
