def FibonacciRecursivo(n):
    sequencia = [0,1]

    for i in range(2, n):
        sequencia.append(sequencia[i-1] + sequencia[i-2])
    return sequencia[:n]

n = int(input('Digite um numero para saber sua sequência de fibonacci: '))


print(f'Sequência de fibonacci: {FibonacciRecursivo(n)}')
