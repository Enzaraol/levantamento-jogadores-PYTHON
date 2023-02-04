salario = float(input('Digite seu salário: '))
valor = float(input('Digite o valor da casa: '))
anos = int(input('Em quantos anos pretende pagar por ela? '))
base = valor/(anos*12)
if salario*0.3 > base:
    print('\033[4;33mAPROVADO!\033[m')
    print(f'O valor a pagar será de R${base:.2f} durante {anos} anos!')
else:
    print('NEGADO!')
