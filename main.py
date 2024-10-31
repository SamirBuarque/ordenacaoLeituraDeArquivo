def insertion_sort(lista: list) -> list:
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista


def ordenar_numeros(arquivo_entrada, arquivo_saida):
    ordenada = []
    with open(arquivo_entrada, 'r') as file:
        numeros = file.readlines()

    numeros = [int(numero.strip()) for numero in numeros]
    ordenada = insertion_sort(numeros)

    with open(arquivo_saida, 'w') as file:
        for numero in ordenada:
            file.write(f"{numero}\n")

ordenar_numeros('exemplo.txt', 'ordenado.txt')

