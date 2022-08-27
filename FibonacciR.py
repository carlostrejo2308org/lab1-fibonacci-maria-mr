#funcion recursiva
def fibonacci(numero):
    if(numero == 0 or numero==1):
        return 1
    else:
        return fibonacci(numero-1)+fibonacci(numero-2)
while  True:
    n=int(input("Ingrese un numero: "))

    if(n>=1):
        break
for i in range(n):
    print(fibonacci(i))

