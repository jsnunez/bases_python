from datetime import datetime

print("Ingrese su fecha de nacimiento.")
dia=int(input("Dia:"))
mes=int(input("Mes:"))
anno=int(input("anno:"))
now = datetime.now()
diah=int(now.day)
mesh=int(now.month)
annoh=int(now.year)

total=annoh-anno
if mes>mesh :
    total=total-1
if  mes==mesh and dia>diah :
    total=total-1

print(total)