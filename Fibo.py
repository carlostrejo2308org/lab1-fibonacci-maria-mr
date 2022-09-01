print('Funcion Fibonacci: ')
#0 1 1 2 3 5 8 13 21 34 55 89....
#funcion iterativa
def fibonacci_iterativo(n):
    a=0
    b=1
    for i in range(n-1):
        a,b=b,a+b
    return b

def fibonacci_recursivo(n):
    
    if n ==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_recursivo(n-2)+fibonacci_recursivo(n-1)
resultado= fibonacci_iterativo(15)
print('Fibonaccio (iterativo): ', resultado)

resultado=fibonacci_recursivo(15)
print('Fibonaccio (recursivo): ', resultado)

