def fibonacci(numero):
    Lista=[]
    a=0
    b=1
    c=a+b
    for i in range(numero):
        a = b
        b = c
        c = a+b
        Lista.append(a)
    return Lista

print(fibonacci(15))

