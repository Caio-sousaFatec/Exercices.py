
input_arquivo_files = open('mussum.txt', 'r', encoding="utf-8")
output_arquivo_files = open('mussum.out', 'w', encoding="utf-8")



def arquivo_preparado(pline: str):
    prepared_line = pline.strip()
    prepared_line = prepared_line.replace(","," ")
    prepared_line = prepared_line.replace("!"," ")
    prepared_line = prepared_line.replace("."," ")
    prepared_line = prepared_line.replace("?"," ")
    prepared_line = prepared_line.replace("@"," ")
    return prepared_line

def process_qty_words(pwords: list, pdict_qty_words: dict):
    for word in pwords:
        if len(word) == 0:
            continue
        if word in pdict_qty_words:
            qty = pdict_qty_words[word]
            qty += 1
            pdict_qty_words[word] = qty
        else:
            pdict_qty_words[word] = 1


dict_qty_words = {}
for line in input_arquivo_files.readlines():
    line = arquivo_preparado(line)
    if len(line) > 0:
        word = line.split()
        process_qty_words(word, dict_qty_words)

for word in sorted(dict_qty_words.keys()):
    output_arquivo_files.write(f'{word}:{dict_qty_words[word]}\n')

output_arquivo_files.close()
input_arquivo_files.close()