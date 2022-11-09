o arquivo em si é um contador de palavras, utilizei o mussum Ipsum para gerar uma alta quantidade 
de palavras em um arquivo a fim de testes. Mas você pode alterar para contar as palavras que quiser
alterando o arquivo "mussum.txt" e inserindo o arquivo em formato .txt que desejar 
--------------------------------------------------------------------------------------------------------------

input_arquivo_files = open('mussum.txt', 'r', encoding="utf-8") // aqui está sendo efetuada a leitura do texto
--------------------------------------------------------------------------------------------------------------
output_arquivo_files = open('mussum.out', 'w', encoding="utf-8")// aqui está sendo realizado a escrita do 
                                                                //documento de saída

--------------------------------------------------------------------------------------------------------------
 
 
def arquivo_preparado(pline: str):                  // aqui foi criado uma função para tratar os dados por linha 
    prepared_line = pline.strip()                   // retirando os caractéres indesejados            
    prepared_line = prepared_line.replace(","," ")
    prepared_line = prepared_line.replace("!"," ")
    prepared_line = prepared_line.replace("."," ")
    prepared_line = prepared_line.replace("?"," ")
    prepared_line = prepared_line.replace("@"," ")
    return prepared_line

def process_qty_words(pwords: list, pdict_qty_words: dict):  // função responsável por separar em lista e dicionário e adicionar quantidade de repetições  
    for word in pwords:                                  //loop que puxa as palavras na lista pwords   
        if len(word) == 0:                              // se o tamanho da palavra for zero não é contabilizado, e continua o código
            continue
        if word in pdict_qty_words:                     // se a palavra estiver no dicionário vai ser adicionado
            qty = pdict_qty_words[word]                 // quantidade recebe a key
            qty += 1                                      //quantidade é contabilizada +1
            pdict_qty_words[word] = qty                 // quantidade de palavras preparadas [X] = quantidade
        else:
            pdict_qty_words[word] = 1                   // se a palavra não estiver no dicionario é contabilizada a palavra +1  

// exemplo palavra existente, pdict_qty_words[existente,2] = pdict_qty_words[existente, 3]
// exemplo palavra inexistente, pdict_qty_words[n/a] = pdict_qty_words[existe, 1]


dict_qty_words = {}

for line in input_arquivo_files.readlines():
    line = arquivo_preparado(line)
    if len(line) > 0:
        word = line.split()     //.split() é responsável de divisão de palavras, sendo por padrão dividido pelo espaço
        process_qty_words(word, dict_qty_words)

for word in sorted(dict_qty_words.keys()):
    output_arquivo_files.write(f'{word}:{dict_qty_words[word]}\n')

output_arquivo_files.close()
input_arquivo_files.close()
