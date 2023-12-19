def desviacion_estandar(numeros):
    import math
    suma=0
    n=len(numeros)
    promedio=sum(numeros)/n 
    for i in numeros:
        suma=suma+(i-promedio)**2
    div=suma/(n-1)
    raiz=math.sqrt(div)
    print(raiz)


numeros=[4.0, 1.0, 11.0, 13.0, 2.0, 7.0] 

desviacion_estandar(numeros)