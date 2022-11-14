import json

import requests

class Moedas():
    dolar = 0.0
    bitcoin = 0.0
    euro = 0.0

    def buscarDados(self):
        dados = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
        moedas = json.loads(dados.content)
        self.dolar = moedas['USDBRL']['bid']
        self.bitcoin = moedas['BTCBRL']['bid']
        self.euro = moedas['EURBRL']['bid']

        retorno = {
            "Acompanhe a cotação das seguintes moedas": {
                "dolar": {
                    "valor": self.dolar,
                    "atualizado": moedas['USDBRL']['create_date']
                },
                "bitcoin": {
                    "valor": self.bitcoin,
                    "atualizado": moedas['BTCBRL']['create_date']
                },
                "euro": {
                    "valor": self.euro,
                    "atualizado": moedas['EURBRL']['create_date']
                },
            }
        }
        return retorno
