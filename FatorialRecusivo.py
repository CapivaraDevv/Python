def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)

n = int(input('Digite um número para saber seu fatorial: '))

print(f'O fatorial de {n} é {fatorial(n)}')
