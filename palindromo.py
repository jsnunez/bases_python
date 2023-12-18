

def invertir_digitos(n) :
    rev = ''.join(reversed(n))
    return rev


n=input("Ingrese el número : ")
inve=invertir_digitos(n)

if n==inve:
    print("es palindromo")
else:
    print("no es palindromo")

print(inve)