def collatz(num):
    while num > 1:
        if num % 2 == 0:
            num //=2
        else:
            num = num*3+1
    if num == 1:
        return True
    else:
        return False

for i in range (1,1_000_001):
    if i % 100_00 == 0:
        print('comprobado hasta el ',i)
    if not collatz(i):
        print('no se cumple para el',i)
        break
else:
    print('se cumple para todos los numeros')