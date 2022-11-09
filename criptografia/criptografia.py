
texto = open( 'D:\DEV issues\criptografia\mensagem.txt', 'r' , encoding = 'utf-8' )
coded = open( 'D:\DEV issues\criptografia\encoded.txt' , 'w' , encoding = 'utf-8' )

for line in texto.readlines():
    for letra in line:
        if letra in 'a':
            coded.write('.1.')
        elif letra in 'p':
            coded.write('.14.')
        elif letra in 'i':
            coded.write('.5.')
        elif letra in 'k':
            coded.write('.7.')
        elif letra in 'o':
            coded.write('.p.')
        elif letra in 'e':
            coded.write('.9.')
        else:
            coded.write(letra)

texto.close()
coded.close()
