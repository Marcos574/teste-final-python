# Repositório destinado à documentação do teste final em python

## Instruções

1. Todas as questões devem ser realizadas em uma IDE de sua preferência. 
2. Você deve submeter o código criado, devidamente comentado, junto com a saída 
do programa. 
3. Responda cada pergunta criando soluções funcionais e bem estruturadas. 
4. Você tem um prazo de 5 horas para finalizar e submeter o teste. 

## Questões

### 1. Manipulação de Dados em Python 
(Curso de Formação Python: Prioridade Alta)  
Escreva um programa em Python que receba um arquivo CSV contendo informações de 
vendas (colunas: "produto", "quantidade", "preço"). O programa deve:

• Ler os dados do arquivo.  
• Calcular o total arrecadado para cada produto.  
• Exibir o produto com maior valor arrecadado.  


### 2. Integração com LangChain 
(Curso de LangChain: Prioridade Alta)  
Utilizando a biblioteca LangChain, crie uma aplicação simples que: 

• Configure um modelo de linguagem para responder a perguntas sobre um texto 
fornecido pelo usuário.  
• Receba como entrada um texto qualquer digitado pelo usuário.  
• Permita ao usuário fazer perguntas sobre o texto e exiba as respostas geradas pelo 
modelo.  

Obs.: Documente as etapas necessárias para configurar o ambiente e instalar as 
dependências. 


### 3. Desenvolvimento de Funções Avançadas 
(Curso Python 3: Prioridade Baixa)  
Crie uma função Python chamada analisar_numeros() que receba uma lista de números 
como argumento. A função deve retornar: 

• A média dos números.  
• O maior e o menor número da lista.  
• Quantos números são pares.  

Inclua testes para validar a função com diferentes entradas. 


### 4. Engenharia de Prompts 
(Curso Mestre da IA: Prioridade Alta)   
Utilizando um modelo de linguagem de IA como o OpenAI GPT (ou similar), crie um script 
que: 

• Apresente um prompt inicial para o usuário descrevendo um problema.  
• Permita ao usuário refinar o problema com novas informações.  
• Gere três soluções alternativas para o problema descrito.  

Obs.: Explique como o script utiliza princípios de engenharia de prompts para melhorar as respostas do modelo. 


### 5. Automação com Python 
(Curso Formação Python: Prioridade Alta)  
Escreva um script que automatize o seguinte cenário: 

• Acesse uma API pública (por exemplo, de previsão do tempo ou cotação de 
moedas).  
• Busque informações relevantes.  
• Salve os dados obtidos em um arquivo JSON.  
• Exiba um resumo das informações no console. 

## Organização

O teste está organizado em pastas, onde cada pasta na raiz deste arquivo seria uma questão do teste. 
A instrução para execução de cada questão está dentro de sua respectiva pasta em um README, bem como possíveis testes, quando solicitados.

## Ambiente

A configuração básica de ambiente é a instalação das bibliotecas que estão no [requirements.txt](requirements.txt).

```
pip install -r requirements.txt
```

Além da criação de um arquivo .env na raiz no projeto para armazenar as variáveis de ambiente, com as chaves das apis da 
[meteo_blue](https://docs.meteoblue.com/en/weather-apis/free-weather-api/overview), 
do [gemini](https://ai.google.dev/gemini-api/docs?hl=pt-br) e 
da [together ai](https://docs.together.ai/docs/quickstart).

O arquivo .env deve se parecer com:

```
TOGETHER_API_KEY="SUA_CHAVE"
METEO_BLUE_API_KEY="SUA_CHAVE"
GEMINI_API_KEY="SUA_CHAVE"
```

## Execução

De forma geral basta entrar na pasta da questão e executar o script main.py

```bash
python main.py
```

Mais informações sobre oque cada questão utiliza está no README referente à questão em cada pasta.

## Entrega

Envie seus códigos e arquivos gerados em um repositório Git ou em um arquivo 
compactado (“zip”), com instruções para execução.