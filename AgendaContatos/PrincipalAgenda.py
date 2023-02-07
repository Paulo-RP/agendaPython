from FuncoesAgenda.AgendaFunction import *
contatos = {}

opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(contatos)
    if opcao == "P":
        buscar(contatos, input("Digite o nome que queira buscar na agenda: "))
    if opcao == "E":
        excluir(contatos, input("Digite o contato que precisa excluir: "))
    if opcao == "L":
        listar(contatos)
    opcao = perguntar()

print("****** OBRIGADO POR UTILIZAR A NOSSA AGENDA ******")