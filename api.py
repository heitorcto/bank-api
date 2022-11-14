# Importando e instanciando FastApi
from fastapi import FastAPI

app = FastAPI()

# Importando minhas classes
from app.cadastro import Cadastro
from app.entrar import Entrar
from app.depositar import Depositar
from app.sacar import Sacar


@app.get("/")
async def inicio():
    return {
        "mensagem": "Olá, cadastre-se através da rota (/cadastrar/seuNome/suaSenha) ou entre com seu token (/entrar/seuToken)."
    }


@app.post("/cadastrar/{nome}/{senha}")
async def cadastrar(nome, senha):
    cad = Cadastro(nome, senha)
    cad.tratarDados()
    cad.validarDados()
    cad.validarUsuario()
    cad.salvarUsuario()

    return cad.retorno


@app.get("/entrar/{token}")
async def entrar(token):
    ent = Entrar()
    ent.validar(token)
    ent.exibir()

    return ent.retorno


@app.put("/entrar/{token}/depositar/{valor}")
async def depositar(token, valor):
    dep = Depositar(token, valor)
    dep.salvar()
    return dep.retorno


@app.put("/entrar/{token}/sacar/{valor}")
async def sacar(token, valor):
    sac = Sacar(token, valor)
    sac.salvar()

    return sac.retorno
