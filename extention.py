import http
import requests
import json

class APIWorker:
    @staticmethod
    def get_price(curIn, curOut, amount):
        key = '918d1b8e7f1c3f2055d53466170e092d353d6a9a18236f2999efdf2a863f51af'
        res = requests.get(
            'https://min-api.cryptocompare.com/data/pricemulti?fsyms=' + curIn + '&tsyms=' + curOut + '&api_key=' + key)
        print(res.status_code)
        print(res.text)
        if (len(json.loads(res.text)) >= 2):
            if (json.loads(res.text)['Response'] == 'Error'):
                return 'Ощибка ввода: введена несуществующая валюта, для справки наберите команду /values'
        return format(float(format(float(json.loads(res.text)[curIn][curOut]), '.8f')) * amount, '.8f')

    def getValuesList():
        key = '918d1b8e7f1c3f2055d53466170e092d353d6a9a18236f2999efdf2a863f51af'
        res = requests.get('https://min-api.cryptocompare.com/data/blockchain/list?api_key=' + key)
        print(res.status_code)
        valuesList = 'Всего в списке ' + str(len(json.loads(res.text)['Data'])) + ' цифровых валют \n'

        for k in json.loads(res.text)['Data'].keys():
            valuesList += k + '\n'
        return valuesList