import csv

def reader_csv(path):
    """
    Função para leitura e verificações se o arquivo csv recebido é válido.
    Ela lê o arquivo csv e retorna uma lista de dicionarios, onde cada dicionario é um produto,
    que contém as chaves "produto", "quantidade" e "preco", além de seus respectivos valores
    """

    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        expected_columns = {'produto', 'quantidade', 'preco'}
        actual_columns = set(reader.fieldnames)

        if len(reader.fieldnames) != 3:
            raise KeyError(f"O arquivo deve ter exatamente 3 colunas, mas encontrou {len(reader.fieldnames)} colunas.")
        
        if actual_columns != expected_columns:
            raise KeyError(f"As colunas no arquivo não são as esperadas. Encontrado: {actual_columns}, Esperado: {expected_columns}")
        
        products = []
        for row in reader:
            if len(row) != 3:
                raise ValueError(f"A linha tem mais ou menos de 3 colunas: {row}")
            if not row['produto'] or not row['quantidade'] or not row['preco']:
                raise ValueError("A linha está faltando um valor em 'produto', 'quantidade' ou 'preco'.")
            
            products.append(row)

        print("\nArquivo CSV válido!\n")
        return products
    
def total_products(products):
    """
    Função para calcular a arrecadação de cada produto.
    Ela recebe a lista de dicionarios de produtos e adiciona uma chave com "total" em cada posição item
    dessa lista, o total representa a multiplicação do valor com a quantidade do produto.
    Ela retorna a mesma lista, porém com a chave total e o valor total de cada produto.
    """

    for row in range(0, len(products)):
        products[row].update({'total':(float(products[row]['quantidade']) * float(products[row]['preco']))})

    return products

def more_profit_product(products):
    """
    Recebe a lista de produtos e identifica qual/quais produtos tem maior valor "total".
    Printa na tela quais produtos são os que mais arrecadaram, além de retornar uma lista com a posição desses produtos
    na lista que recebeu, caso seja do interesse do programador fazer algo a mais com esses produtos.
    """
    
    most_profit_product = 0
    num_prod_most_profit = 0
    most_profit_products_list = []

    for row in range(0, len(products)):
        if products[row]['total'] == products[most_profit_product]['total']:
            num_prod_most_profit += 1
        if products[row]['total'] > products[most_profit_product]['total']:
            most_profit_product = row
            most_profit_value = products[row]['total']
            most_profit_products_list.append(row)

    if num_prod_most_profit <= 1:
        print(f'O produto com maior valor arrecadado é {products[most_profit_product]["produto"]}, que arrecadou {products[most_profit_product]["total"]} R$')
    else:
        print('Os produtos com maior valor arrecadado são: ')
        for i in range(0, len(products)):
            if products[i]['total'] == most_profit_value:
                print(f'{products[i]["produto"]}, que arrecadou {products[i]["total"]} R$')

    print('\n')
    return most_profit_products_list

def main():

    products = reader_csv(path='teste2.csv')
    products_with_total = total_products(products)

    more_profit_product(products_with_total)

if __name__ == '__main__':
    main()
