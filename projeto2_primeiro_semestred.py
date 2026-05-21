# Sistema de controle de estoque - Curso Engenharia de Software
# data 20/05/2026 1 semestre
# Projeto pratico 2


produtos =[
    {"nome": "teclado", "preço":50.0, "quantidade": 10},
    {"nome": "mouse", "preço":20.0, "quantidade": 15},
    {"nome": "microfone", "preço":30.0, "quantidade": 20}
]

#inicio do laço 
while True:
    print ("***** BEM VINDO *****")
    numero_digitado = input ("\n1 - Visualizar Estoque Atual\n"
        "2 - Registrar Entrada de Produto\n"
        "3 - Registrar Saída de Produto\n"
        "4 - Sair do Sistema\n"
        "Escolha uma das opção que desejar:")

    #opção que exibe a situação do estoque atual opção 1
    if numero_digitado == "1":
        
        print("\n--- Estoque Atual ---")
        
        for item in produtos:
            print(f"Produto: {item['nome']} | Preço: R${item['preço']} | Quantidade: {item['quantidade']}")
            
        print("---------------------\n")

    #condição para quando o usuário digitar a opção 2     
    elif numero_digitado == "2":
        # essas duas variaveis guardan o nome e quantidade para alterar, também converte a quantidade para inteiro
        nome_entrada = input("Digite o nome do produto que deseja alterar: ")
        quantidade_digitada = int(input("Digite a quantidade que deseja adicionar: "))

        produto_encontrado = False
        #laço para encontrar o produto e alterar a quantidade 
        for item in produtos: 
            if item["nome"] == nome_entrada:
                item["quantidade"] += quantidade_digitada
                produto_encontrado = True    
                print(f"Produto alterado com sucesso! Novo estoque de {item['nome']}: {item['quantidade']}")  
                break # Agora ele quebra apenas o 'for' e volta pro menu!

        # Fora do for, verificando se a bandeira continuou False
        if produto_encontrado == False:
            print("Produto não encontrado.")

    #Logica para dar saida no produto opção 3
    elif numero_digitado == "3":

        #variaveis que recebem nome e quantidade para dar saida
        nome_entrada = input("Digite o nome do produto que deseja dar saída: ")
        quantidade_digitada = int(input("Digite a quantidade que deseja dar saída: "))

        #variavel de controle para verificar se o produto foi encontrado
        produto_encontrado = False

        #Laço para buscar o produto e validar quantidades
        for item in produtos:
            if item["nome"] == nome_entrada:
                produto_encontrado = True  

                #esse if verifica se o estoque é suficiente para aceitar a saída
                if item["quantidade"] >= quantidade_digitada:
                    item["quantidade"] -= quantidade_digitada
                    print(f"Produto alterado com sucesso! Novo estoque de {item['nome']}: {item['quantidade']}")
                else:
                    print("Quantidade em estoque é menor que a saída.")
                
                break  

        if produto_encontrado == False:
            print("Produto não encontrado.")




        
    elif numero_digitado == "4": #saida do laço opção 4
        print("Muito obrigado por usar nosso sistema de estoque. ")
        break
# validação para caso o usuário digite outro numero ou uma letra e o codigo não quebrar
    else:
        print("\nDigite uma opção válida, apenas opções (1-2-3-4)\n")

print("Saindo....")


