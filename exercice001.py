old_payment = input('qual seu antigo salário?')
old_payment= float(old_payment)

taxa= input('qual a taxa de aumento recebida?')
taxa= float(taxa)

taxa /= 100
taxa += 1

new_payment = old_payment * taxa

print(f'seu salário antigo era de {old_payment}')
print(f'seu novo pagamento é de {new_payment}')