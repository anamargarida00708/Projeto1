
'''O jogo Será Que Você foi pensado nos amantes de filmes de terror classicos, 
assim tornado fãs parte da historia ser tornado os persongens principais. Objetivo jogo é prova 
que não é imposto, ou seja, jogadores tem prova que fazer parte da universo resposta as questões
correta sobre obra, contexto narrativo e personsagem.
====================================================================================================
Nessa primeira use imports pois aprende para alura achei interessante para pode acessa os
personagens e fases pela menu incial. Além de foi usa conteúdos vindos no móduloI como 
palavras reservadas, estruturas condicionais,laços/repetições e funções.
'''
import personagem1, personagem2, personagem3

def menu_incial():
  while True:
     linha_de_espaco()
     print(''''
     Seja bem vindo, ao gamer será que é você?
     Onde você tem três possiblidade de escolher
     entre clássicos do cinema:

     ===============================================

     [1] O surrado Jack Torrence do filme O Iluminado
     [2] A jovem Regan MacNeil do filme O Exorcista
     [3]O assustado Pennywise do filme IT Coisa
     [4] Sair do jog0
     ''')
     linha_de_espaco()

     personagem = int(input(" Digite o número do filme da sua preferencia: "))
     if personagem ==1:
               personagem1.escolhido()
     elif personagem ==2:
               personagem2.escolhido()
     elif personagem==3:
              personagem3.escolhido()
     elif personagem == 4:
          print("Saindo do jogo...")
          break
     else:
          print("Opção inválida")
def linha_de_espaco():
     print("-=-" *25)
menu_incial()