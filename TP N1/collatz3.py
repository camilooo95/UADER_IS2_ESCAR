c0 = int(input('ingrese un numero mayor a 0 '))
pasos = 1

if c0 > 0:
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 / 2
        else:
            c0 = 3 * c0 + 1

        print (f'Paso {pasos}: c0 = {c0}')
        pasos += 1

else:
    print('debe ingresar un numero mayor a 0 ')

print(f'\n Resultado final de c0 = {c0}: pasos totales {pasos}')