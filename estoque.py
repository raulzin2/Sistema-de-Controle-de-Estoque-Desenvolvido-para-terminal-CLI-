# ==========================================
# Sistema de Controle de Estoque
# Desenvolvido para terminal (CLI)
# ==========================================

import json
import os

ARQUIVO_DADOS = "estoque.json"


def carregar_estoque():
    """Carrega o estoque salvo em disco, se existir. Se não existir, começa vazio."""
    if os.path.exists(ARQUIVO_DADOS):
        try:
            with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            print("Aviso: não foi possível ler o arquivo de dados. Iniciando estoque vazio.")
    return {}


def salvar_estoque(estoque):
    """Salva o estoque atual em disco, em formato JSON."""
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(estoque, f, ensure_ascii=False, indent=2)


def exibir_menu():
    """Exibe as opções do sistema para o usuário."""
    print("\n" + "=" * 45)
    print("      SISTEMA DE CONTROLE DE ESTOQUE")
    print("=" * 45)
    print("[1] - Cadastrar produto")
    print("[2] - Atualizar quantidade")
    print("[3] - Remover produto")
    print("[4] - Listar todos os produtos do estoque")
    print("[5] - Consultar um produto")
    print("[6] - Encerrar o sistema")
    print("=" * 45)


def cadastrar_produto(estoque):
    """Cadastra um novo produto no dicionário de estoque."""
    print("\n--- Cadastro de Produto ---")
    nome = input("Digite o nome do produto: ").strip().lower()

    if nome in estoque:
        print("Aviso: O produto '{}' já está cadastrado no sistema.".format(nome.title()))
        return

    try:
        quantidade = int(input("Digite a quantidade inicial: "))
        preco = float(input("Digite o preço unitário (R$): "))

        if quantidade < 0 or preco < 0:
            print("Erro: A quantidade e o preço devem ser valores positivos.")
            return

        estoque[nome] = {
            "quantidade": quantidade,
            "preco": preco
        }
        salvar_estoque(estoque)
        print("Sucesso: Produto '{}' cadastrado com sucesso!".format(nome.title()))

    except ValueError:
        print("Erro: Entrada inválida. Use apenas números para quantidade e preço.")


def atualizar_quantidade(estoque):
    """Atualiza a quantidade de um produto existente."""
    print("\n--- Atualizar Quantidade ---")
    nome = input("Digite o nome do produto: ").strip().lower()

    if nome not in estoque:
        print("Erro: O produto '{}' não foi encontrado no estoque.".format(nome.title()))
        return

    try:
        nova_quantidade = int(input("Digite a nova quantidade em estoque: "))

        if nova_quantidade < 0:
            print("Erro: A quantidade em estoque não pode ser negativa.")
            return

        estoque[nome]["quantidade"] = nova_quantidade
        salvar_estoque(estoque)
        print("Sucesso: A quantidade de '{}' foi atualizada para {}.".format(nome.title(), nova_quantidade))

    except ValueError:
        print("Erro: Entrada inválida. A quantidade deve ser um número inteiro.")


def remover_produto(estoque):
    """Remove um produto do estoque permanentemente."""
    print("\n--- Remover Produto ---")
    nome = input("Digite o nome do produto a ser removido: ").strip().lower()

    if nome in estoque:
        del estoque[nome]
        salvar_estoque(estoque)
        print("Sucesso: Produto '{}' removido do estoque!".format(nome.title()))
    else:
        print("Erro: O produto '{}' não foi encontrado.".format(nome.title()))


def listar_estoque(estoque):
    """Exibe todos os produtos cadastrados de forma tabular, com o valor total do estoque."""
    print("\n--- Lista de Produtos ---")

    if not estoque:
        print("O estoque está vazio no momento.")
        return

    print("-" * 45)
    print("{:<20} | {:<10} | {:<10}".format("PRODUTO", "QTD", "PREÇO"))
    print("-" * 45)

    valor_total = 0
    for nome, dados in estoque.items():
        quantidade = dados["quantidade"]
        preco = dados["preco"]
        valor_total += quantidade * preco
        print("{:<20} | {:<10} | R$ {:.2f}".format(nome.title(), quantidade, preco))

    print("-" * 45)
    print("Valor total em estoque: R$ {:.2f}".format(valor_total))


def consultar_produto(estoque):
    """Busca e exibe os dados de um único produto."""
    print("\n--- Consultar Produto ---")
    nome = input("Digite o nome do produto: ").strip().lower()

    if nome not in estoque:
        print("Erro: O produto '{}' não foi encontrado no estoque.".format(nome.title()))
        return

    dados = estoque[nome]
    subtotal = dados["quantidade"] * dados["preco"]
    print("-" * 45)
    print("Produto : {}".format(nome.title()))
    print("Qtd.    : {}".format(dados["quantidade"]))
    print("Preço   : R$ {:.2f}".format(dados["preco"]))
    print("Subtotal: R$ {:.2f}".format(subtotal))
    print("-" * 45)


def main():
    """Função principal que controla o fluxo do programa."""
    estoque = carregar_estoque()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-6): ").strip()

        if opcao == "1":
            cadastrar_produto(estoque)
        elif opcao == "2":
            atualizar_quantidade(estoque)
        elif opcao == "3":
            remover_produto(estoque)
        elif opcao == "4":
            listar_estoque(estoque)
        elif opcao == "5":
            consultar_produto(estoque)
        elif opcao == "6":
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("\nErro: Opção inválida. Por favor, escolha um número de 1 a 6.")


if __name__ == "__main__":
    main()
