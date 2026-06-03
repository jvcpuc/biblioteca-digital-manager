# gerenciador.py

import os
import shutil
from datetime import datetime

BIBLIOTECA_DIR = "biblioteca"


def garantir_diretorio():
    """Cria o diretório principal da biblioteca caso não exista."""
    if not os.path.exists(BIBLIOTECA_DIR):
        os.makedirs(BIBLIOTECA_DIR)


def listar_documentos():
    print("\n=== DOCUMENTOS DA BIBLIOTECA ===\n")

    encontrou = False

    for raiz, diretorios, arquivos in os.walk(BIBLIOTECA_DIR):
        for arquivo in arquivos:
            caminho = os.path.join(raiz, arquivo)

            extensao = os.path.splitext(arquivo)[1].replace(".", "").upper()

            data_modificacao = os.path.getmtime(caminho)
            ano = datetime.fromtimestamp(data_modificacao).year

            print(f"Arquivo : {arquivo}")
            print(f"Tipo    : {extensao}")
            print(f"Ano     : {ano}")
            print(f"Caminho : {caminho}")
            print("-" * 50)

            encontrou = True

    if not encontrou:
        print("Nenhum documento encontrado.")


def adicionar_documento():

    nome = input(
        "Nome do documento: "
    ).strip()

    if not nome:
        print(
            "Nome do documento não informado."
        )
        return

    caminho = os.path.join(
        BIBLIOTECA_DIR,
        nome
    )

    if os.path.exists(caminho):
        print(
            "Documento já existe."
        )
        return

    with open(
        caminho,
        "w",
        encoding="utf-8"
    ) as arquivo:
        arquivo.write("")

    print(
        "Documento criado com sucesso."
    )


def renomear_documento():

    nome_atual = input(
        "Nome atual: "
    ).strip()

    if not nome_atual:
        print(
            "Nome atual não informado."
        )
        return

    novo_nome = input(
        "Novo nome: "
    ).strip()

    if not novo_nome:
        print(
            "Novo nome não informado."
        )
        return

    origem = os.path.join(
        BIBLIOTECA_DIR,
        nome_atual
    )

    destino = os.path.join(
        BIBLIOTECA_DIR,
        novo_nome
    )

    if not os.path.exists(origem):
        print(
            "Documento não encontrado."
        )
        return

    os.rename(
        origem,
        destino
    )

    print(
        "Documento renomeado com sucesso."
    )

def remover_documento():

    nome = input(
        "Nome do documento: "
    ).strip()

    if not nome:
        print(
            "Nome do documento não informado."
        )
        return

    caminho = os.path.join(
        BIBLIOTECA_DIR,
        nome
    )

    if not os.path.isfile(caminho):
        print(
            "Documento não encontrado."
        )
        return

    os.remove(caminho)

    print(
        "Documento removido com sucesso."
    )

def criar_diretorio():

    nome = input(
        "Nome do diretório: "
    ).strip()

    if not nome:
        print(
            "Nome do diretório não informado."
        )
        return

    caminho = os.path.join(
        BIBLIOTECA_DIR,
        nome
    )

    if os.path.exists(caminho):
        print(
            "Diretório já existe."
        )
        return

    os.makedirs(caminho)

    print(
        "Diretório criado com sucesso."
    )

def remover_diretorio():

    nome = input(
        "Nome do diretório: "
    ).strip()

    if not nome:
        print(
            "Nome do diretório não informado."
        )
        return

    caminho = os.path.join(
        BIBLIOTECA_DIR,
        nome
    )

    if not os.path.isdir(caminho):
        print(
            "Diretório não encontrado."
        )
        return

    shutil.rmtree(caminho)

    print(
        "Diretório removido com sucesso."
    )

def exibir_menu():
    print("\n")
    print("=" * 40)
    print(" BIBLIOTECA DIGITAL MANAGER ")
    print("=" * 40)
    print("1 - Listar documentos")
    print("2 - Adicionar documento")
    print("3 - Renomear documento")
    print("4 - Remover documento")
    print("5 - Criar diretório")
    print("6 - Remover diretório")
    print("0 - Sair")
    print("=" * 40)


def main():
    garantir_diretorio()

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_documentos()

        elif opcao == "2":
            adicionar_documento()

        elif opcao == "3":
            renomear_documento()

        elif opcao == "4":
            remover_documento()

        elif opcao == "5":
            criar_diretorio()

        elif opcao == "6":
            remover_diretorio()

        elif opcao == "0":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()