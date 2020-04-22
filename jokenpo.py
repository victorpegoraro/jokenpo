#! /usr/bin/env python

#Desenvolvedor: Victor Pegoraro

#Bibliotecas
import time, random, colorama
from prettytable import PrettyTable

#Iniciando cores
colorama.init()
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
CYAN = colorama.Fore.CYAN
RED = colorama.Fore.RED
YELLOW = colorama.Fore.YELLOW

#Variaveis
pontos_player  = 0
pontos_machine = 0

#Funções

#Mostrar animação
def jokenpo():
    time.sleep(1)
    print(f"\n{YELLOW}JO")
    time.sleep(1)
    print(f"{CYAN}KEN")
    time.sleep(1)
    print(f"{GREEN}PO!{RESET}\n")
    time.sleep(1)

#Função da partida
def jogo(pontos_player,pontos_machine):

    mao = input(f"{YELLOW}[1] Pedra [2] Papel [3] Tesoura :{RESET}")#Escolher opção

    if mao.isnumeric(): #Verifica se é numero

    #Verifica escolha 
        if mao == '1':
            jokenpo() #Animação
            machine = random.randint(1,3) #Jogo da máquina
            
            #Compara jogos
            if machine == 1:
                print(f"{YELLOW}Empate !!{RESET} \n")
            elif machine == 2 :
                print(f"{RED}Perdeu !!{RESET} \n")
                pontos_machine += 1
            elif machine == 3:
                print(f"{GREEN}Ganhou !!{RESET}\n")
                pontos_player += 1

        elif mao == '2':
            jokenpo() #Animação
            machine = random.randint(1,3) #Jogo da máquina

            #Compara jogos
            if machine == 1:
                print(f"{GREEN}Ganhou !!{RESET}\n")
                pontos_player += 1
                
            elif machine == 2 :
                print(f"{YELLOW}Empate !! {RESET}\n")

            elif machine == 3:
                print(f"{RED}Perdeu !! {RESET}\n")
                pontos_machine += 1

        
        elif mao == '3':
            jokenpo() #Animação
            machine = random.randint(1,3) #Jogo da máquina

            #Compara jogos
            if machine == 1:
                print(f"{RED}Perdeu !! {RESET}\n")
                pontos_machine += 1

            elif machine == 2 :
                print(f"{GREEN}Ganhou !!{RESET}\n")
                pontos_player += 1

            elif machine == 3:
                print(f"{YELLOW}Empate !!{RESET} \n")

    #Mostrar se a opão for inválida
        else:
            print(f"{RED}Digite uma opção válida!{RESET} \n ")
            jogo(pontos_player,pontos_machine)

    else:
        print(f"{RED}Digite uma opção válida!{RESET} \n ")
        jogo(pontos_player,pontos_machine)

    return pontos_player , pontos_machine

#Jokenpo Game

start = """
        -------Jokenpo Game-------
        Dev: Victor Pegoraro
        Vesion: 1.0
        --------------------------
        """

print(f"\n{CYAN}" + start + f"{RESET}")

nome = input(f"\nQual seu nome: ")

#Rotina do jogo
while True:

    #Mostrar placar atual
    print("Seus pontos: " + str(pontos_player) + " || Machine: " + str(pontos_machine) + "\n" )

    #Opção para continuar jogando
    opcao = input(f"Próxima partida ? [1] {GREEN}Sim {RESET}[2] {RED}Não{RESET}:")

    if opcao.isnumeric(): #Verifica se é numero

        if opcao == '1':
            #Começa uma nova partida
            pontos_player, pontos_machine = jogo(pontos_player,pontos_machine)

        #Finaliza jogo e mostra  placar final
        elif opcao == '2':
            table = PrettyTable(['Nome', ' Pontos'])
            table.add_row([nome, str(pontos_player)])
            table.add_row(["Machine", str(pontos_machine)])
            print(table)
            print(f"{YELLOW}Até mais...")
            break

    #Mostrar se houver algum erro
        else:
            print(f"{RED}Digite uma opção válida!\n{RESET}")

    else:
        print(f"{RED}Digite uma opção válida! \n{RESET}")

