temp = int(input('insira a temperatura para conversão'))

medidor = input('insira se é celsius ou fahrenhein')

if medidor == "celsius":
    converted_temp= (temp * 1.8) +  32
    print(f'a temperatura em fahreinheit é de {converted_temp}')

elif medidor == "fahreinhein":
    converted_temp = (temp -32) * 5/9
    print(f'a temperatura convertida é de {converted_temp}')
## that's all folks