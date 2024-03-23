import time # biblioteca que porta a função time.sleep()

# Bem vindo ao primeiro projeto do meu curso de Ciência da Computação no Unilassale

# Criando a função principal do jogo, o objetivo dela é armazenar o menu do jogo, o sistema de respostas, e as perguntas.
def iniciojogo(): # função que inicia o jogo


    nome_usuario = input("\nMe informe seu nome: \t")  # Pedindo o nome do usuário
    pontos = 0  ## Contador de pontos que vai ser usado mais tarde
    print("Seja bem vindo ao Jogo ! ", nome_usuario)  # Comprimentando o usuário
    time.sleep(5) # pausa o console durante 5 segundos
    print("\nCaro (a)", nome_usuario, ", escolha seu destino apertando uma opção abaixo:")
    print("1. Jogar " "\n2. Consultar respostas " "\n3. Sair do jogo") # Opçoes
    opcao_menu = input("\n Digite a opção: \t") # Lendo a opção que o usuario digitar

    if opcao_menu == '1': #Se o usuario digitar 1, então o jogo vai começar

        # Pede ao usuario para completar os quadros vazios

        print("\nVamos começar então", nome_usuario, "Complete as frases em Português do Brasil!")
        resposta_linha1 = input("1.Tina escolhe _________ no jardim: \t ")
        resposta_linha2 = input("2.Madrid é ----------- da Espanha: \t" )
        resposta_linha3 = input("3.Mãe compra pão no ________ : \t")
        resposta_linha4 = input("4.Gosto de ___________ um copo de leite :\t")
        resposta_linha5 = input("5.Um filme emocionante será exibido no ________ :\t")
        resposta_linha6 = input("6.O médico _________ um remédio : \t")
        resposta_linha7 = input("7.Na __________ vamos a praia :\t")
        resposta_linha8 = input("8.Um cavaleiro usa_______ \t : ")
        resposta_linha9 = input("9.A bandeira _________ no vento :  \t")

        if resposta_linha1 == "flores":  # se o usuario escrever a resposta certa, ganha um ponto
            pontos = pontos + 1

        if resposta_linha2 == "capital":
            pontos = pontos + 1

        if resposta_linha3 == "mercado":
            pontos = pontos + 1

        if resposta_linha4 == "beber":
            pontos = pontos + 1

        if resposta_linha5 == "cinema":
            pontos = pontos + 1

        if resposta_linha6 == "receitou":
            pontos = pontos + 1

        if resposta_linha7 == "sexta":
            pontos = pontos + 1

        if resposta_linha8 == "armadura de aço":
            pontos = pontos + 1

        if resposta_linha9 == "tremula":
            pontos = pontos + 1

        if pontos >= 8: # testando quantos pontos o usuario fez, se sua pontuação foi maior que oito, então ele passou no jogo
            print("\nVoce fez ", pontos, " pontos ! Parabéns, zerou o jogo!") # congratulando o usuario e mostrando quantos pontos ele fez

            print ("\nSuas respostas foram:") # devolvendo as respostas do usuario

            print ("\n1.Tina escolhe", resposta_linha1 , "no jardim")
            print("2.Madrid é", resposta_linha2 , "da Espanha:")
            print("3.Mãe compra pão no", resposta_linha3)
            print("4.Gosto de ", resposta_linha4 ,"um copo de leite")
            print("5.Um filme emocionante será exibido no", resposta_linha5)
            print("6.O médico", resposta_linha6 , "um remédio")
            print("7.Na", resposta_linha7 ,"vamos a praia")
            print("8.Um cavaleiro usa", resposta_linha8 )
            print("9.A bandeira", resposta_linha9 , "no vento")

            time.sleep(5) # deixando o console pausado por 5 segundos

            opcaomenu2 = input(("\nDeseja jogar de novo? Se sim, aperte s, senão, aperte n : \t")) # perguntando oque o usuario quer fazer

            if opcaomenu2 == 's':  # se ele apertar s, o jogo reinicia
                iniciojogo()

            if opcaomenu2 == 'n': # se ele apertar n, o jogo fecha
                exit()
        else:
            print("\nVoce fez ", pontos, " pontos! Não foi o suficiente, tente de novo!") # se o usuario teve pontuação menor que 8, ele precisa jogar de novo.

            time.sleep(5) # pondo o console pra descansar por 5 segundos

            print("\nSuas respostas foram:") # devolvendo as respostas do usuario

            print("\n1.Tina escolhe", resposta_linha1 , "no jardim")
            print("2.Madrid é", resposta_linha2 , "da Espanha:")
            print("3.Mãe compra pão no", resposta_linha3)
            print("4.Gosto de ", resposta_linha4 , "um copo de leite")
            print("5.Um filme emocionante será exibido no", resposta_linha5)
            print("6.O médico", resposta_linha6 , "um remédio")
            print("7.Na",  resposta_linha7 ,  "vamos a praia")
            print("8.Um cavaleiro usa", resposta_linha8)
            print("9.A bandeira", resposta_linha9, "no vento")

            opcaomenu3 = input(("\nDeseja jogar de novo? Se sim, aperte s, senão, aperte n: \t")) # convidando o usuario a fazer algo

            if opcaomenu3 == 's':
                time.sleep(5)
                iniciojogo()

            if opcaomenu3 == 'n':
                print("\nFechando jogo....")
                time.sleep(10)
                exit()


    # se o usuario apertou 2, então ele ganha de mão beijada as respostas

    if opcao_menu == '2':
        print("\nflores, capital, mercado, beber, cinema, receitou, sexta, armadura de aço, tremula")

        #convidando o usuario a escolher algo
        opcaomenu4 = input(("\nDeseja voltar? Se sim, aperte s, senão, aperte n: \t"))

        if opcaomenu4 == 's':
            time.sleep(5)
            iniciojogo()

        if opcaomenu4 == 'n':
            print("\nFechando jogo....")
            time.sleep(10)
            exit()

    #se apertar 3, o jogo fechs
    if opcao_menu == '3':
        exit()

# enquanto esse laço while for verdadeiro, tudo acima vai se repetir infinitamente, a menos que o usuario encerre
while True:
    iniciojogo() # chamando a função que carrega o jogo
