import requests
from getpass import getpass
import json


def autenticar(url_api):
    try:
        nome_usuario = input("Nome de usuário: ")
        senha = getpass("Senha: ") 

        dados = {"username": nome_usuario, "password": senha}

        resposta = requests.post(url_api + "v2/autenticacao/token/", json=dados)
        resposta.raise_for_status() 

        return resposta.json()["access"]
    except requests.exceptions.RequestException as e:
        print(f"Autenticação falhou: {e}")
        return None


def obter_informacoes_usuario(url_api, token):  
    try:
        headers = {"Authorization": f"Bearer {token}"}

        resposta = requests.get(url_api + "v2/minhas-informacoes/meus-dados/", headers=headers)
        resposta.raise_for_status() 
        return resposta.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao recuperar informações do usuário: {e}")
        return None


def principal():
    url_api = "https://suap.ifrn.edu.br/api/"
    arquivo_dados = "suap_keys.json"

    try:
        with open(arquivo_dados, 'r') as arquivo:
            try:
                dados = json.load(arquivo)
                token = dados.get('token')
            except json.decoder.JSONDecodeError:
                dados = {}
                token = None

        if not token or not autenticar(url_api):
            return

        informacoes_usuario = obter_informacoes_usuario(url_api, token)
        if informacoes_usuario:
            print("Informações do Usuário:")
            print(json.dumps(informacoes_usuario, indent=4)) 
        else:
            print("Falha ao recuperar informações do usuário.")

    except FileNotFoundError:
        print(f"Arquivo '{arquivo_dados}' não encontrado.")


if __name__ == '__main__':
    principal()