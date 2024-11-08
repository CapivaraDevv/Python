print("Qual conversão deseja fazer?")
n = input("1 - Celsius para Fahrenheit\n2 - Fahrenheit para Celsius\n")
int_n = int(n)
if int_n==1:
    celsius = float(input("Digite o valor para fazer a conversão: "))
    fahrenheit = (celsius * (9/5)) + 32
    print(f'{celsius} graus Celsius é igual a {fahrenheit} graus Fahrenheit')
elif int_n==2:
    fahrenheit = float(input("Digite o valor para fazer a conversão: "))
    celsius = (fahrenheit - 32)  * (5/9)
    print(f'{fahrenheit} graus Fahrenheit é igual a {celsius} graus Celsius')
else:
    print('Opção invalida, Escolha uma das disponiveis')     