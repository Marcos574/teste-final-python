def analisar_numeros(number_list):
    maior = number_list[0]
    menor = number_list[0]
    quant_pares = 0

    response = {'media':'', 'maior': '', 'menor':'', 'pares':''}    


    # Definindo a média dos valores da lista
    response['media'] = round(sum(number_list) / len(number_list), 2)


    for i in range(0, len(number_list)):
        
        # Definindo o maior valor da lista
        if number_list[i] >= maior:
            maior = number_list[i]

        # Definindo o menor valor da lista
        if number_list[i] <= menor:
            menor = number_list[i]

        # Definindo a quantidade de pares
        if number_list[i] % 2 == 0:
            quant_pares += 1

    response['maior'] = maior
    response['menor'] = menor
    response['pares'] = quant_pares

    return response


def main():

    numeros = [1, 3, 12, 15, 31, 20, 2]

    print(analisar_numeros(numeros))


if __name__ == '__main__':
    main()