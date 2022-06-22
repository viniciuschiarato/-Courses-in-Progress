import requests

response = requests.get('https://translate.google.com.br/?hl=pt-BR&sl=en&tl=pt&op=translate')

print('Status code:',response.status_code)  # cód. de status referente a requisição feita
print('Header:')
print(response.headers)
print('content:')
print(response.content)
