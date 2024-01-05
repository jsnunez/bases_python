import json


data =  open("rutas.json") 
usuarios = json.load(data)

for usuarios in usuarios['rutas']:
    print("Nombre del usuario:", usuarios)
