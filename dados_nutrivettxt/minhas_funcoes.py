def salvar_lista_arquivo(lista):
  with open("dados_telas.txt", 'w') as arquivo:
    for item in lista:
      arquivo.write(f'{item}\n')


def adicionar_valor_arquivo(valor):
  with open("dados_telas.txt", 'a') as arquivo:
    arquivo.write(f'{valor}\n')


def ler_arquivo():
  with open("dados_telas.txt", 'r') as arquivo:
    lista = arquivo.readlines()
  return lista
