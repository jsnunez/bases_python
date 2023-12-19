def media_aritmetica(lista):
    suma=0
    n=len(lista)
    for i in lista:
        suma=suma+i
    print(suma/n)
    return(suma/n)

def media_armonica(lista):
    dem=0
    n=len(lista)
    for i in lista:
        dem=(1/i)+dem

    h=n/dem
    print(h)

def mediana(lista):
   lista.sort()
   print(lista)
   n=len(lista)
   mitad = n/2
   print(lista[round(mitad)-1])


media_aritmetica([6, 1, 4, 8])
media_armonica([6, 1, 4, 8])
mediana([5.0, 1.4, 3.2, 0.1])