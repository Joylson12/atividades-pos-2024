import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

user = input("Seu usuário do GitHub: ")
password = getpass("Digite sua chave de acesso: ")

while True:
    print("Opções:")
    print("1. Listar seguidores do usuário")
    print("2. Seguir um usuário")
    print("3. Parar de seguir um usuário")
    print("4. Voltar")
    
    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        usuario = input("Digite o Nome do usuário para ver seus seguidores: ")
        response = requests.get(
            f'https://api.github.com/users/{usuario}/followers',
            auth=HTTPBasicAuth(user, password)
        )
        
        if response.status_code == 200:
            seguidores = response.json()
            for seguidor in seguidores:
                print(seguidor['login'])
            print(f"Total de seguidores de {usuario}: {len(seguidores)}")
        else:
            print(f"Erro ao obter dados: {response.status_code}")

    elif opcao == '2':
        usuario = input("Digite o login do usuário que deseja seguir: ")
        response = requests.put(
            f'https://api.github.com/user/following/{usuario}',
            auth=HTTPBasicAuth(user, password)
        )
        
        if response.status_code == 204:
            print(f"Você agora está seguindo {usuario}.")
        else:
            print(f"Erro ao seguir o usuário: {response.status_code}")

    elif opcao == '3':
        usuario = input("Digite o login do usuário que deseja deixar de seguir: ")
        response = requests.delete(
            f'https://api.github.com/user/following/{usuario}',
            auth=HTTPBasicAuth(user, password)
        )
        
        if response.status_code == 204:
            print(f"Certo! {user} deixou de sguir:  {usuario}.")
        else:
            print(f"Erro! Não parou de seguir: {response.status_code}")

    elif opcao == '4':
        print("Valeu")
        break

    else:
        print("Opção inválida.")
