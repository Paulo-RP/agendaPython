def perguntar():
    opcao = input("\nO que deseja realizar? \n" +
                  "<I> - Para inserir um contato \n" +
                  "<P> - Para pesquisar um contato \n" +
                  "<E> - Para excluir um contato \n" +
                  "<L> - Para listar contatos \n" +
                  "\nDigite conforme informado acima: \n").upper()
    return opcao

def inserir(dicionario):
    chave = input("Digite o nome: ")
    dicionario[chave] = [input("Digite o número: "),
                         input("Digite o e-mail: ")]

def buscar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print("Número: " + lista[0])
        print("E-mail: " + lista[1])

def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print("Contato excluído: ")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("\nContato............. ")
        print("Nome: ", chave)
        print("Dados: ", valor)