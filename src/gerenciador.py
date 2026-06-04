import os
import shutil
from datetime import datetime
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.simpledialog import askstring

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

BIBLIOTECA_DIR = os.path.join(
    BASE_DIR,
    "biblioteca"
)

def garantir_diretorio():
    """Cria o diretório principal da biblioteca caso não exista."""
    if not os.path.exists(BIBLIOTECA_DIR):
        os.makedirs(BIBLIOTECA_DIR)


def listar_documentos():
    print("\n=== TODOS OS DOCUMENTOS ===\n")

    encontrou = False

    for raiz, diretorios, arquivos in os.walk(BIBLIOTECA_DIR):

        for arquivo in arquivos:

            caminho = os.path.join(
                raiz,
                arquivo
            )

            extensao = os.path.splitext(
                arquivo
            )[1].replace(".", "").upper()

            data_modificacao = os.path.getmtime(
                caminho
            )

            ano = datetime.fromtimestamp(
                data_modificacao
            ).year

            print(f"Arquivo : {arquivo}")
            print(f"Tipo    : {extensao}")
            print(f"Ano     : {ano}")
            print(f"Caminho : {caminho}")
            print("-" * 50)

            encontrou = True

    if not encontrou:
        print("Nenhum documento encontrado.")


def listar_documentos_por_tipo():

    print("\n=== DOCUMENTOS POR TIPO ===\n")

    tipos = {}

    for raiz, diretorios, arquivos in os.walk(BIBLIOTECA_DIR):

        for arquivo in arquivos:

            extensao = os.path.splitext(
                arquivo
            )[1].replace(".", "").upper()

            if extensao == "":
                extensao = "SEM EXTENSÃO"

            if extensao not in tipos:
                tipos[extensao] = []

            tipos[extensao].append(arquivo)

    if not tipos:
        print("Nenhum documento encontrado.")
        return

    for tipo in sorted(tipos.keys()):

        print(f"\n[{tipo}]")

        for arquivo in sorted(tipos[tipo]):
            print(f"  - {arquivo}")


def listar_documentos_por_ano(tipo='c'):

    if tipo == 'c':
        print("\n=== DOCUMENTOS POR ANO DE CRIAÇÃO ===\n")
    else:
        print("\n=== DOCUMENTOS POR ANO DE MODIFICAÇÃO ===\n")

    anos = {}

    for raiz, diretorios, arquivos in os.walk(BIBLIOTECA_DIR):

        for arquivo in arquivos:

            caminho = os.path.join(
                raiz,
                arquivo
            )

            if tipo == 'c':
                data = os.path.getctime(
                    caminho
                )
            else:
                data = os.path.getmtime(
                    caminho
                )

            ano = datetime.fromtimestamp(
                data
            ).year

            if ano not in anos:
                anos[ano] = []

            anos[ano].append(arquivo)

    if not anos:
        print("Nenhum documento encontrado.")
        return

    for ano in sorted(anos.keys()):

        print(f"\n[{ano}]")

        for arquivo in sorted(anos[ano]):
            print(f"  - {arquivo}")


def adicionar_documento():

    root = Tk()
    root.withdraw()

    arquivo_origem = askopenfilename(
        title="Selecione um documento"
    )

    root.destroy()

    if not arquivo_origem:
        print("Operação cancelada.")
        return

    nome_arquivo = os.path.basename(
        arquivo_origem
    )

    destino = os.path.join(
        BIBLIOTECA_DIR,
        nome_arquivo
    )

    if os.path.exists(destino):
        print(f"Documento {destino} já existe.")
        return

    shutil.copy2(
        arquivo_origem,
        destino
    )

    print(f"Documento {destino} adicionado com sucesso.")

def renomear_documento():

    root = Tk()
    root.withdraw()

    arquivo = askopenfilename(
        initialdir=BIBLIOTECA_DIR,
        title="Selecione o documento"
    )

    root.destroy()

    if not arquivo:
        print("Operação cancelada.")
        return

    nome_atual = os.path.basename(
        arquivo
    )

    nome_sem_extensao, extensao = os.path.splitext(
        nome_atual
    )

    print(f"\nDocumento selecionado: {nome_atual}")

    novo_nome = input(
        "Novo nome (sem extensão): "
    ).strip()

    if not novo_nome:
        print("Nome não informado.")
        return

    novo_caminho = os.path.join(
        BIBLIOTECA_DIR,
        novo_nome + extensao
    )

    if os.path.exists(novo_caminho):
        print(
            f"Já existe um documento com esse nome: {novo_caminho}"
        )
        return

    os.rename(
        arquivo,
        novo_caminho
    )

    print(
        f"Documento renomeado para: {novo_nome + extensao}"
    )

def remover_documento():

    arquivo = askopenfilename(
        initialdir=BIBLIOTECA_DIR,
        title="Selecione o documento para remover"
    )

    if not arquivo:
        print("Operação cancelada.")
        return

    os.remove(arquivo)

    print(f"Documento {arquivo} removido com sucesso.")


def criar_diretorio():

    nome = askstring(
        "Novo Diretório",
        "Informe o nome:"
    )

    if not nome:
        print("Nome do diretório não informado.")
        return

    caminho = os.path.join(
        BIBLIOTECA_DIR,
        nome
    )

    if os.path.exists(caminho):
        print(f"Diretório {caminho} já existe.")
        return

    os.makedirs(caminho)

    print(f"Diretório {caminho} criado com sucesso.")


def remover_diretorio():

    pasta = askdirectory(
        initialdir=BIBLIOTECA_DIR,
        title="Selecione o diretório"
    )

    if not os.path.isdir(pasta):
        print(f"Diretório {pasta} não encontrado.")
        return

    shutil.rmtree(pasta)

    print(f"Diretório {pasta} removido com sucesso.")


def exibir_menu():

    print("\n")
    print("=" * 50)
    print(" BIBLIOTECA DIGITAL MANAGER ")
    print("=" * 50)

    print("1 - Listar todos os documentos")
    print("2 - Listar documentos por tipo")
    print("3 - Listar documentos por ano da criação")
    print("4 - Listar documentos por ano da última modificação")

    print()

    print("5 - Adicionar documento")
    print("6 - Renomear documento")
    print("7 - Remover documento")

    print()

    print("8 - Criar diretório")
    print("9 - Remover diretório")

    print()

    print("0 - Sair")
    print("=" * 50)


def main():

    garantir_diretorio()

    while True:

        exibir_menu()

        opcao = input(
            "Escolha uma opção: "
        ).strip()

        if opcao == "1":
            listar_documentos()

        elif opcao == "2":
            listar_documentos_por_tipo()

        elif opcao == "3":
            listar_documentos_por_ano('c')

        elif opcao == "4":
            listar_documentos_por_ano('m')

        elif opcao == "5":
            adicionar_documento()

        elif opcao == "6":
            renomear_documento()

        elif opcao == "7":
            remover_documento()

        elif opcao == "8":
            criar_diretorio()

        elif opcao == "9":
            remover_diretorio()

        elif opcao == "0":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()