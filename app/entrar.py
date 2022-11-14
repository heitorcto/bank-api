import json
import os

from app.moedas import Moedas


class Entrar(object):
    nome = ""
    saldo = 0.0
    token = ""
    retorno = ""

    def validar(self, token):
        arquivotamanho = os.stat('usuarios.json')
        existe = False
        self.token = token

        if arquivotamanho.st_size > 0:
            with open("usuarios.json") as f:
                usuarios = json.load(f)

            for usuario in usuarios:
                if usuario == self.token:
                    self.nome = usuarios[usuario]['nome']
                    self.saldo = usuarios[usuario]['saldo']
                    existe = True

            if existe == False:
                self.retorno = {
                    "mensagem": "Token inválido, por favor verifique-o e tente novamente."
                }
        else:
            self.retorno = {
                "mensagem": "Nenhum usuário cadastrado ainda."
            }

    def exibir(self):
        moedas = Moedas()
        d = moedas.buscarDados()


        self.retorno = {
            "usuario": self.nome,
            "saldo": self.saldo,
            "moedas": d
        }
