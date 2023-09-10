idade = int(input('Digite sua idade: '))
falta = 18 - idade
mais = idade - 18

if idade < 18 and falta == 1:
    print(f'Você vai ter que se alistar daqui a {falta} ano')
elif idade < 18 and falta != 1:
    print(f'Você vai ter que se alistar daqui a {falta} anos')

elif idade == 18:
    print('Esse é o seu ano de alistamento!')

elif idade > 18 and mais == 1:
    print(f'Já passou {mais} ano do seu período de alistamento')
elif idade > 18 and mais != 1:
    print(f'Já se passaram {mais} anos do seu período de alistamento')
    