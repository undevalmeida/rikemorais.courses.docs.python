arquivo_contatos = open('dados/contatos.csv', encoding='latin-1')

for linha in arquivo_contatos:
    print(linha, end='')
    