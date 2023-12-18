alzat=0
n=int(input("Ingrese el número de dias : "))

for i in range (1,n+1):
    alza=int(input(f"Dia {i} :"))
    if i==1:
        alzaa=alza
    if alzaa<alza:
        alzat=alza-alzaa
    alzaa=alza
    print(alzat)