def add_prefix_un(word):
    return "un" + word

def make_word_groups(vocab_words):
    prefijo = vocab_words[0]
    lista2 = [prefijo]
    for elemento in vocab_words[1:]:
        palabara = prefijo + elemento
        lista2.append(palabara)
    return ' :: '.join(lista2)

def remove_suffix_ness(word):
    lista = list(word)
    i = 0
    while i != 4:
        lista.pop(-1)
        i += 1
    
    if lista[-1] == 'i':
        lista.pop(-1)
        lista.append('y')
    return "".join(lista)

def adjective_to_verb(sentence, index):
    lista = sentence.split()
    palabra = lista[index].strip(".,?!")
    verbo = palabra + "en"
    return verbo
