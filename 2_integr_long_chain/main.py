import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

def config_ai_model():
    load_dotenv()
    global together_api_key, model

    together_api_key = os.getenv("TOGETHER_API_KEY")

    model = ChatOpenAI(
        base_url="https://api.together.xyz/v1",
        api_key=together_api_key,
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    )

def ai_message_to_dict(ai_message):
    """
    Converte um objeto AIMessage para um dicionário serializável.
    """

    if hasattr(ai_message, 'text'):
        return {'text': ai_message.text}
    
    return vars(ai_message)

def make_prompt(question):

    with open('dados/user_text.txt', 'r', encoding='utf-8') as file:
        user_text = file.read()

    prompt = {"context": user_text, "question": question}

    prompt_string = f"Contexto: {prompt['context']} \n\nPergunta: {prompt['question']}"

    return prompt_string


def ai_interation():

    question = input("Digite a sua pergunta sobre o texto: \n")
    prompt = make_prompt(question)
    data = model.invoke(prompt)

    if isinstance(data, list):
        data = [ai_message_to_dict(item) for item in data]
    else:
        data = ai_message_to_dict(data)

    print("\nResposta do modelo: \n")
    print(data["content"])


def main():

    config_ai_model()
    ai_interation()


if __name__ == '__main__':
    main()