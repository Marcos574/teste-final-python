import json
from datetime import datetime

def load_data(json_file):
    """Carrega os dados do arquivo json"""
    with open(json_file, "r", encoding="utf-8") as file:
        return json.load(file)

def calculate_temperature(data):
    """Calcula os dados referentes à temperatura: média, máxima e miníma"""
    temperature = {'max': max(data['data_1h']['temperature']),
                  'min': min(data['data_1h']['temperature']),
                  'average': sum(data['data_1h']['temperature']) / len(data['data_1h']['temperature'])}
    return temperature

def calculate_wind_speed(data):
    """Calcula a média de velocidade do vento"""
    return sum(data['data_1h']['windspeed']) / len(data['data_1h']['windspeed'])

def calculate_precipitation(data):
    """Calcula informações referentes à precipitação: média e momentos com maior probabilidade"""
    precipitation = {"average": '', "times": []}
    precipitation['average'] = sum(data['data_1h']['precipitation_probability']) / len(data['data_1h']['precipitation_probability'])
    
    max_precip = max(data['data_1h']['precipitation_probability'])
    for i, prob in enumerate(data['data_1h']['precipitation_probability']):
        if prob == max_precip:
            precipitation['times'].append(data['data_1h']['time'][i])
    
    return precipitation

def calculate_uv_index(data):
    """Calcula informações referentes ao índice uv: momentos que o índice é extremo (maior que 11)"""
    uv_index = {"extreme": []}
    for i, uv in enumerate(data['data_1h']['uvindex']):
        if uv >= 11:
            uv_index['extreme'].append(data['data_1h']['time'][i])
    return uv_index

def calculate_relative_humidity(data):
    """Calcula informações referentes à umidade relativa do ar: média, máxima e mínima"""
    relative_humidity = {"average": "", "max": "", "min": ""}
    relative_humidity['max'] = max(data['data_1h']['relativehumidity'])
    relative_humidity['min'] = min(data['data_1h']['relativehumidity'])
    relative_humidity['average'] = sum(data['data_1h']['relativehumidity']) / len(data['data_1h']['relativehumidity'])
    return relative_humidity

def calculate_snow_chance(data):
    """Calcula os momentos que há probabilidade de nevar"""
    snow_chance = sum(1 for snow in data['data_1h']['snowfraction'] if snow != 0)
    return snow_chance

def format_time_period(data):
    """Formata o tempo de acordo com o formato brasileiro"""
    start_end = [data['data_1h']['time'][0], data['data_1h']['time'][168]]
    start_end[0] = datetime.strptime(start_end[0], "%Y-%m-%d %H:%M")
    start_end[1] = datetime.strptime(start_end[1], "%Y-%m-%d %H:%M")
    return start_end

def display_weather_data(start_end, temperature, average_wind_speed, precipitation, uv_index, relative_humidity, snow_chance):
    """Mostra os dados relevantes calculados"""
    
    print('\n============================ Relatório de Previsão do Tempo de Brasília ============================\n')
    print(f'Período: {start_end[0].strftime("%d/%m/%Y")} a {start_end[1].strftime("%d/%m/%Y")}\n')
    
    if snow_chance == 0:
        print("Não há previsão de neve para este período.")
    else:
        print("Há possibilidade de neve durante este período.\n")
    
    print(f"Média de Velocidade do Vento: {average_wind_speed:.2f} m/s\n")
    
    print("---------- Informações sobre Temperatura ----------")
    print(f"Temperatura Mais Alta: {temperature['max']} °C")
    print(f"Temperatura Mais Baixa: {temperature['min']} °C")
    print(f"Temperatura Média: {temperature['average']:.2f} °C\n")
    
    print("---------- Informações sobre Precipitação ----------")
    print(f"Média de Probabilidade de Precipitação: {precipitation['average']:.2f}%")
    print("Momentos com Maior Chance de Precipitação:")
    for time in precipitation['times']:
        print(f"   - {time}")
    print()
    
    print("---------- Informações sobre Índice UV ----------")
    print("Momentos com Índice UV Extremo:")
    for time in uv_index['extreme']:
        print(f"   - {time}")
    print("Recomenda-se proteção contra raios UV nesses momentos.\n")
    
    print("---------- Informações sobre Umidade Relativa ----------")
    print(f"Umidade Relativa Mais Alta: {relative_humidity['max']} %")
    print(f"Umidade Relativa Mais Baixa: {relative_humidity['min']} %")
    print(f"Umidade Relativa Média: {relative_humidity['average']:.2f}%\n")
    
    print("============================================= Fim do Relatório =============================================\n")


def weather_data_processing():
    """Função principal que orquestra as outras"""
    json_file = 'dados/response_data.json'
    
    data = load_data(json_file)
    
    start_end = format_time_period(data)
    temperature = calculate_temperature(data)
    average_wind_speed = calculate_wind_speed(data)
    precipitation = calculate_precipitation(data)
    uv_index = calculate_uv_index(data)
    relative_humidity = calculate_relative_humidity(data)
    snow_chance = calculate_snow_chance(data)
    
    display_weather_data(start_end, temperature, average_wind_speed, precipitation, uv_index, relative_humidity, snow_chance)
