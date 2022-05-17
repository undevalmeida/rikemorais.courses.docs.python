arquivo = open('dados/contatos.csv', encoding='latin-1', mode='a+')

print(type(arquivo.buffer))

texto_em_bytes = bytes('Esse é um texto em bytes', 'latin-1')
# print(texto_em_bytes)
# print(type(texto_em_bytes))

contato = bytes('15,Verônica,veronica@veronica.com.br\n', 'latin-1')
arquivo.buffer.write(contato)

arquivo.close()