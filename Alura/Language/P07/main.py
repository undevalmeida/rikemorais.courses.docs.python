url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

# Sanitizando a URL
url = url.strip()

# Validando a URL
if url == "":
    raise ValueError("URL está vazia!")

# Separa a Base e os Parâmetros
indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca o Valor de um Parâmetro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)