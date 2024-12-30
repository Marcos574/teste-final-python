import hashlib
import hmac
from dotenv import load_dotenv
from datetime import datetime
import os
import requests
import json
import pprint

def create_url(lat, lon, api_key):


    sharedSecret = "MySharedSecret"
    query = f"/packages/basic-1h?lat={lat}&lon={lon}&apikey={api_key}"

    sig = hmac.new(sharedSecret.encode(), query.encode(), hashlib.sha256).hexdigest()

    signedUrl = f"https://my.meteoblue.com{query}&sig={sig}"

    return signedUrl

def request(url):
    response = requests.get(url)

    data = response.json()

    with open("response_data.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def data_processing():
    arquivo_json = 'response_data.json'
    chance_nevar = 0

    with open(arquivo_json, "r", encoding="utf-8") as file:
        dados = json.load(file)

    temperatura = {'max':None, 'min':None, 'media':None}

    ini_fim = [dados['data_1h']['time'][0], dados['data_1h']['time'][168]]

    ini_fim[0] = datetime.strptime(ini_fim[0], "%Y-%m-%d %H:%M")
    ini_fim[1] = datetime.strptime(ini_fim[1], "%Y-%m-%d %H:%M")

    print('\nDados sobre a previsão do tempo da cidade de Brasília entre os dias: ')
    print(f'{ini_fim[0].strftime("%d/%m/%Y")} e {ini_fim[1].strftime("%d/%m/%Y")}')

    for i in range(0, len(dados['data_1h']['time'])):
        if dados['data_1h']['snowfraction'][i] != 0:
            chance_nevar += 1

    temperatura['max'] = max(dados['data_1h']['temperature'])
    temperatura['min'] = min(dados['data_1h']['temperature'])
    temperatura['media'] = sum(dados['data_1h']['temperature']) / len(dados['data_1h']['temperature'])

        

    if chance_nevar == 0:
        print("\nNeste intervalo não deve nevar")

    media_velocidade_vento = sum(dados['data_1h']['windspeed']) / len(dados['data_1h']['windspeed'])
    print(f"A média de velocidade do vento será de {media_velocidade_vento:.2f} m/s")

    print("\nAs informações reelevantes sobre a temperatura são: ")
    print(f"Mais alta: {temperatura['max']} °C")
    print(f"Mais baixa: {temperatura['min']} °C")
    print(f"Média: {temperatura['media']:.2f} °C")








def main():

    load_dotenv()
    meteo_blue_api_key = os.getenv("METEO_BLUE_API_KEY")

    lat=-15.7797
    lon=-47.9297

    url = create_url(lat, lon, meteo_blue_api_key)

    #request(url)

    data_processing()



if __name__ == '__main__':
    main()
