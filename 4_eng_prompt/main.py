import os
import google.generativeai as genai
from dotenv import load_dotenv

def config_api():
    global model 

    load_dotenv()
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=gemini_api_key)

    model = genai.GenerativeModel('gemini-1.5-flash')

def consult_gemini_api():
    with open('dados/prompt_problema.txt', 'r', encoding='utf-8') as file:
        prompt_problema = file.read()

    messages = []

    for i in range(3):
        temperature = 0.7 + i * 0.1  
        response = model.generate_content(
            prompt_problema,
            generation_config={"temperature": temperature}
        )
        messages.append(response.text)

    
    print("Resposta 1:")
    print(messages[0])
    print('-----------------------------')

    print("Resposta 2:")
    print(messages[1])
    print('-----------------------------')

    print("Resposta 3:")
    print(messages[2])


    return messages

def main():

    config_api()
    consult_gemini_api()

if __name__ == '__main__':
    main()
