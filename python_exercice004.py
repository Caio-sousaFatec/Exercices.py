tipo = input('alcool ou gasolina?')
quantidade = int(input('quantos litros vai querer abastecer?'))

tipo.upper()

preco_A = 2.9
preco_G= 3.3

preco_total_G = quantidade*preco_G
preco_total_A = quantidade*preco_A

if tipo == 'gasolina':
    print(f'o total sem desconto é de {preco_total_G}')
elif tipo =='alcool' :
    print(f'o total sem desconto é de {preco_total_A}')

desconto_baixo_G = preco_total_G - (preco_total_G * 0.02)
desconto_alto_G = preco_total_G - (preco_total_G * 0.05)
desconto_baixo_A = preco_total_A - (preco_total_A * 0.04)
desconto_alto_A = preco_total_A - (preco_total_A * 0.06)

if tipo == 'gasolina':
    if quantidade >= 21 :
        print(f'com o desconto, ficará {round(desconto_alto_G ,2 )}')
        print('o desconto foi de ', round (preco_total_G * 0.05 , 2))
    else:
        print(f' com o desconto, ficará {round(desconto_baixo_G , 2)}')
        print('o desconto foi de ' , round(preco_total_G * 0.02 , 2) )
elif tipo == 'alcool':
    if quantidade >= 21 :
        print(f'com o desconto, ficará {round(desconto_alto_A , 2 )}')
        print('o desconto foi de ', round(preco_total_A * 0.06 , 2))
    else:
        print(f'com o desconto, ficará {round(desconto_baixo_A , 2)}')
        print('o desconto foi de ', round(preco_total_A * 0.04 , 2))
