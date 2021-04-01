def test():
    """ Esta funcion retorna si un string es heterograma """
    texto = input("Ingrese una palabra o frase para analizar si es Heterograma: ")
    texto_lista = list(texto.lower())
    for letra in texto_lista:
        if letra.isalpha() and texto_lista.count(letra) > 1:
            print('No es un heterograma.')
            print(f'La letra [{letra}] se encuentra repetida en la frase ingresada.')
            return
    print('La frase ingresada SI es un heterograma.')
    
test()