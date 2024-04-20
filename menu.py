import db_academia

menu_acoes = """- CRIAR
- VIZUALIZAR
- ATUALIZAR
- DELETAR
- VOLTAR

opção: """

menu_tabelas = """=========TABELAS=========
- ALUNO
- FUNCIONARIO
- PERSONAL
- MODALIDADES
- SAIR

opção: """


while True:
    tabelas_validas = ["aluno", "funcionario", "personal", "modalidades", "sair"]
    tabela_escolhida = input(menu_tabelas).lower().strip()
    if tabela_escolhida not in tabelas_validas:
        print("Opção invalida! Verifique a resposta passada e tente novamente.")
        continue
    elif tabela_escolhida == "sair":
        break
    else:
        print("=" * 26)
        print(f"TABELA: {tabela_escolhida.upper()}")
        op_men_validas = ["criar", "vizualizar", "atualizar", "deletar", "voltar"]
        op_menu = input(menu_acoes).lower().strip()
        if op_menu not in op_men_validas:
            print("Opção invalida! Verifique a resposta passada e tente novamente.")
            continue
        elif op_menu == "voltar":
            continue

        if op_menu == "criar":
            novo_id = db_academia.criar_registro(tabela_escolhida)
            print(f"Cadastro efetuado! Novo ID: {novo_id}")
        elif op_menu == "vizualizar":
            db_academia.ler_registro(tabela_escolhida)
        elif op_menu == "deletar":
            db_academia.apagar_registro(tabela_escolhida)
