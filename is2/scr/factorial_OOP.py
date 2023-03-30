def factorial(n):
    if n > 4 and n < 8:
        f = 1
        for i in range(2, n + 1):
            f = f * i

        return f
    else:
        print('el valor es incorrecto')
parametr1 = int(input("Introduce el primer número entre 4 y 8:"))
parametr2 = int(input("Introduce el segundo número entre 4 y 8:"))
f1 = factorial(parametr1)
print(f"Factorial de {parametr1} = {f1}")
f2 = factorial(parametr2)
print(f"Factorial de {parametr2} = {f2}")
print(f1 + f2)
    
