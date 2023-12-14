p1=input("ingresar palabra1:")
p2=input("ingresar palabra2:")
t1=len(p1)
t2=len(p2)

if t1>t2 :
    val=t1-t2
    print(f"La palabra {p1} tiene {val} letras mas que {p2}. ")
elif t1<t2 :
        val=t2-t1
        print(f"La palabra {p2} tiene {val} letras mas que {p1}. ")
elif t1==t2 :
        print(f"La palabra {p2} es igual que {p1}. ")

