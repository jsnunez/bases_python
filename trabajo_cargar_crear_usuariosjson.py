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
    with open('data.json') as file:
        data = json.load(file)
        data =  open("data.json") 
        usuarios = json.load(data)
        data1 = {}
        data1['usuarios'] = []
    for usuarios in usuarios['usuarios']:
        print("Nombre del usuario:",
            usuarios["id"] ,         
            usuarios["nombres"],
            usuarios["Apellidos"],
            usuarios["direccion"],
            usuarios["acudiente"],
            usuarios["estado"] )
#        data1["usuarios"].append(usuarios)
 #       if "9518479" == usuarios["id"]:
  #          usuarios["nota"]=100
    with open('data.json') as file:
        data = json.load(file)
        data =  open("data.json") 
        usuarios = json.load(data)
    seletuser=input("escriba id para agregar notas: ")
    for usuarios in usuarios['usuarios']:
        if seletuser == usuarios["id"] and "inscrito" ==usuarios["estado"]:
            usuarios["notat"]=input("ingrese nota teorica 0-100: ")
            usuarios["notap"]=input("ingrese nota practica 0-100: ")
            promedionota=(int(usuarios["notat"])+int(usuarios["notap"]))/2
            if promedionota>=60:
                usuarios["pruebas"]="aprovado"

        data1["usuarios"].append(usuarios)
    with open('data.json', 'w') as file:
        json.dump(data1, file)


    sig=input("desea ingresar un nueva nota campers si o no: ")
    if sig=="si":
        x=3
    else:
        x=0    
    return x

def mod_cruta():
    data =  open("rutas.json") 
    rutas = json.load(data)

   
    i=len(rutas)
    print(i)
    rutas.append("Fundamentos de programación")
    print("rutas:", rutas)
    x=0
    return x

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
        
    while x==3:
        x=mod_prueba()
    while x==5:
        x=mod_cruta()