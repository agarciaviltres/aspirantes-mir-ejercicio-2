import requests

API_KEY = 'l7u502p8v46ba3ppgvj5y2aad50lb9'            #'trnsl.1.1.20230506T211300Z.6ced1d39efdd24dc.d1c073c6b113d7755af34762ad8a9ab524a76e97'
# EasyBrocker l7u502p8v46ba3ppgvj5y2aad50lb9
traducir = 'Mi novio es muy guapo'

params = dict(key=API_KEY, text=traducir, lang='es-en')

url = 'https://api.stagingeb.com/v1/contact_requests?page=1&limit=20'          #'https://translate.yandex.net/api/v1.5/tr.json/translate'
res = requests.get(url, params=params)

#print(res.text)
print(res.headers)
###cuando el contenido es application/json en lugar de text/html  podemos hacer que Requests convierta la respuesta en un diccionario y una lista para que podamos acceder a los datos con mayor facilidad
#json = res.json()
#print(json)
#print(json['text'])
#print(json['text'][0])

#res = requests.get('https://scotch.io')

#print(res)

#if res:
#    print('Response OK')
#else:
#    print('Response Failed')

#print(res.status_code)

#print(res.headers)

#print(res.text)