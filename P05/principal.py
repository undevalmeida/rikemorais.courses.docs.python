try:
    with open('dados/nao-existe.csv', encoding='latin_1', mode='w+') as arquivo_contatos:
        for linha in arquivo_contatos:
            print(linha, end='')
except FileNotFoundError:
    print('Arquivo não encontrado.')
except PermissionError:
    print('Sem permissão para abrir o arquivo.')
    