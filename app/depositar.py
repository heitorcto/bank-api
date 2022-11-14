import json
from app.entrar import Entrar


class Depositar(Entrar):
    valor = 0.0

    def __init__(self, token, valor):
        Depositar.validar(self, token)

        for char in valor:
            if char.isalpha():
                self.retorno = {
                    "mensagem": "A valor não pode conter letras."
                }

        if self.retorno == "":
            self.valor = self.saldo + float(valor)

    def salvar(self):
        if self.retorno == "":
            with open("usuarios.json") as f:
                usuarios = json.load(f)

            for token in usuarios:
                if token == self.token:
                    usuarios[token]['saldo'] = self.valor

            with open("usuarios.json", 'w') as file:
                pass

            usuarios = json.dumps(usuarios)
            arquivo = open("usuarios.json", "a")
            arquivo.write(usuarios)

            self.retorno = {
                "mensagem": "Depósito efetuado."
            }
