import requests  # importando biblioteca para solicitações HTTP e interagir com a API

# Criando um dicionario das traduções, para sair a previsao do tempo em portugues
traducoes = {
'clear sky': 'céu limpo',
    'few clouds': 'poucas nuvens',
    'scattered clouds': 'nuvens dispersas',
    'broken clouds': 'nuvens quebradas',
    'overcast clouds': 'céu nublado',
    'light rain': 'chuva leve',
    'moderate rain': 'chuva moderada'
}

# Implementando a API OpenWeatherMap
def obter_previsao_tempo(cidade, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric'  # "&units=metric" para saida da temperatura em Celsius
    response = requests.get(url)

    if response.status_code == 200:  # Se a API retornar codigo 200 significa que a solicitação foi bem-sucedida
        dados = response.json()
        temperatura = dados['main']['temp']
        descricao = dados['weather'][0]['description']
        descricao_traduzida = traducoes.get(descricao, descricao)
        return f'Previsão do tempo para {cidade}: {temperatura} ºC, {descricao_traduzida}'
    else:
        return 'Não foi possivel obter a previsão do tempo. Verifique o nome cidade e tente novamente.' # Menssagem caso a solicitação nao tenha sido bem sucedida


api_key = 'bf0d7c029fe3ed6d5727c7e85450cbd9'  # API do OpenWeatherMap
cidade = input('Digite o nome da cidade: ') # Solicitando nome da cidade
print(obter_previsao_tempo(cidade, api_key)) # Resposta ao usuario
