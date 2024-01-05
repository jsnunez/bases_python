correr=99
import json
with open('data.json') as file:
    data = json.load(file)

print(len(data["usuarios"]))    

users=len(data["usuarios"])
def mod_reg(i):
    with open('data.json') as file:
        data = json.load(file)        
        print("Ingrese los datos de la persona", i + 1)
        data["usuarios"].append({
        "id": input("id:"),
        "nombres" : input("Nombre: "),
        "Apellidos" : input ("Apellidos: "),
        "direccion" : input ("direccion: "),
        "acudiente" : input ("acudiente: "),
        "telefonos_celular" : input ("telefonos_celular: "),
        "telefonos_fijo" : input ("telefonos_fijo: "),
        "estado" :input("estado: ")
})
               
        with open('data.json', 'w') as file:
                json.dump(data, file)

        data =  open("data.json") 
        usuarios = json.load(data)

        for usuarios in usuarios['usuarios']:
            print("Nombre del usuario:",
                usuarios["id"] ,         
                usuarios["nombres"],
                usuarios["Apellidos"],
                usuarios["direccion"],
                usuarios["acudiente"],
                usuarios["estado"] )
        sig=input("desea ingresar un nuevo campers si o no")


        if sig=="si":
         x=1
        else:
           x=0                   
    return x                                  

def mod_prueba():
     
     x=0




while correr==99:  
    print("1. Registro de campers")
    print("3. Registro prueba")
    print("4. Registro area de entrenamiento")
    print("5. Creación de rutas de entrenamiento")
    print("6. asignacion de rutas de entrenamiento")
    print("7. asignacion de entrenadores")
    print("8. Gestor de matriculas")
    print("9. evaluacion campers")
    print("10. Estudiantes en riesgos")
    print("11. Modulo de reportes")
    x=int(input("selecione modulo a usar:  "))
    while x==1:
        x=mod_reg(users)
        
    if x==3:
         mod_prueba()