
def calculardigito(rev,tamaño) :
    suma=0
    for i in range (2,tamaño+2) :
        if i<=7 :
            suma=suma+(int(rev[i-2])*i)
        elif i>7:
            suma=suma+(int(rev[i-2])*i-6)
    return suma
suma=0
digito=0
n=input("Ingrese el número : ")
rev = ''.join(reversed(n))
tamaño =len(rev)
digito=calculardigito(rev,tamaño)
modulo=digito%11
codigo=11-modulo
print(n,"-",codigo)  
 

