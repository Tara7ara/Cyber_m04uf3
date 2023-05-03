#!/usr/bin/python3

import requests
import sys

if len(sys.argv) < 2:
	print("ERROR: falta el nombre de usuario")
	print("\t"+sys.argv[0]+" NOMBRE_USUARIO")
	exit()


api_url = "https://api.github.com/users/Tara7ara"+sys.argv[1]

response = requests.get(api_url)

info = response.json()

#print(info["id"])
print(info)
