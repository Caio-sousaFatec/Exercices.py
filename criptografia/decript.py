
texto = open( 'D:\DEV issues\criptografia\encoded.txt', 'r' , encoding = 'utf-8' )
coded = open( 'D:\DEV issues\criptografia\decoded.txt' , 'w' , encoding = 'utf-8' )

for line in texto.readlines():
    for letra in line:
        if letra in '.1.':
            coded.write('a')
        elif letra in '.14.':
            coded.write('p')
        elif letra in '.5.':
            coded.write('i')
        elif letra in '.7.':
            coded.write('k')
        elif letra in '.p.':
            coded.write('o')
        elif letra in '.9.':
            coded.write('e')   
        else:
            coded.write(letra)

texto.close()
coded.close()
