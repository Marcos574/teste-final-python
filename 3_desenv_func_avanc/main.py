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

def exibir_resultado(response):
    print("Resultado da Análise:")
    print("-" * 30)
    
    for chave, valor in response.items():
        if chave == 'media':
            valor = f"{float(valor):.2f}"
        print(f"{chave.capitalize()}: {valor}")
    
    print("-" * 30)


def main():

    entrada = input("Digite os números separados por espaço: \n")
    numeros = list(map(int, entrada.split()))

    exibir_resultado(analisar_numeros(numeros))


if __name__ == '__main__':
    main()
    