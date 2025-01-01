# Questão 4 - Engenharia de prompts

## Instrução

(Curso Mestre da IA: Prioridade Alta) 
Utilizando um modelo de linguagem de IA como o OpenAI GPT (ou similar), crie um script 
que: 

• Apresente um prompt inicial para o usuário descrevendo um problema. 
• Permita ao usuário refinar o problema com novas informações. 
• Gere três soluções alternativas para o problema descrito. 

Obs.: Explique como o script utiliza princípios de engenharia de prompts para melhorar as 
respostas do modelo. 

## Requisitos

- Python 3.x instalado
- **Bibliotecas Python**:
  - dotenv: Para carregar variáveis de ambiente a partir de um arquivo `.env`.
  - google-generativeai: Para interagir com o modelo Gemini 1.5 Flash.

## Configuração do ambiente

- Para instalar as dependências necessárias, rode na raiz do projeto:

```bash
pip install -r requirements.txt
```

- Crie um arquivo .env na raiz do projeto com a sua chave da API do gemini:

```
GEMINI_API_KEY=SuaChaveAPIaqui
```

## Execução

1. Prepare o Arquivo de Texto com o Problema
O script lê o conteúdo de um arquivo chamado prompt_problema.txt. Coloque uma descrição do problema neste arquivo para que o modelo possa gerar soluções alternativas.
O texto já é um prompt pré configurado, ajuste os textos entre colchetes [] como desejar.

2. Execute o programa

```bash
python main.py
```

## Princípio da engenharia de prompts

- Prompt inicial: O prompt inicial é dividido entre problema, objetivo e pergunta para que a IA entenda de maneira mais eficiente oque deve ser feito.
- Temperatura: A temperatura é ajustada para controlar o grau de criatividade nas respostas. Quanto maior a temperatura, mais criativas e diversas as respostas, enquanto uma temperatura mais baixa tende a gerar respostas mais conservadoras.

## Exemplo:

![questão 4](../exemplos/questao-4.gif)