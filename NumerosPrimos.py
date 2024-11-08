def ehPrimo(n):
    if n<2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n%1 ==0:
            return False
    return True

n = int(input('Digite um número para saber se ele é primo ou não: '))

if ehPrimo(n):
    print(f'O número {n} é um número primo!')
else:
    print(f'O número {n} não é um número primo!')