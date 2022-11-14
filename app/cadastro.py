import re
import hashlib
import json
import os


class Cadastro():
    nome = ""
    senha = ""
    retorno = ""

    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def tratarDados(self):
        self.nome = self.nome.replace(" ", "")
        self.nome = re.sub(r'[0-9]', '', self.nome)
        self.nome = self.nome.title()

    def validarDados(self):
        if self.nome == "":
            self.retorno = {
                "mensagem": "Nome precisa de ter ao menos uma letra."
            }

        if len(self.senha) < 4:
            self.retorno = {
                "mensagem": "Senha não pode ter menos que 4 caracteres."
            }

    def validarUsuario(self):
        arquivotamanho = os.stat('usuarios.json')

        if arquivotamanho.st_size > 0:
            with open("usuarios.json") as f:
                usuarios = json.load(f)

            if usuarios != "":
                for usuario in usuarios:
                    nomeExistente = usuarios[usuario]["nome"]
                    if nomeExistente == self.nome:
                        self.retorno = {
                            "mensagem": "Esse usuário já existe, escolha outro nome por favor."
                        }

    def salvarUsuario(self):
        if self.retorno == "":
            token = hashlib.md5(self.nome.encode('utf-8')).hexdigest()

            jsonSalvar = {
                token: {
                    "nome": self.nome,
                    "senha": self.senha,
                    "saldo": 0.00
                }
            }

            arquivotamanho = os.stat('usuarios.json')

            if arquivotamanho.st_size > 0:
                with open("usuarios.json") as f:
                    usuarios = json.load(f)
                    usuarios.update(jsonSalvar)
            else:
                usuarios = jsonSalvar

            with open("usuarios.json", 'w') as file:
                pass

            usuarios = json.dumps(usuarios)
            arquivo = open("usuarios.json", "a")
            arquivo.write(usuarios)

            self.retorno = {
                "mensagem": "Usuário cadastrado com sucesso. Salve o seu token de acesso: " + token
            }
