'''A estrutura dos personagem é mesma para todos apenas mudando as perguntas e
os proprios personagens.
Na questão obter por usar laços e muitos returns para dar feito se usario acerte 
vai proxima assim sucessamente até que erre é volte para menu inicial onde tem a
possibilidade de sair do jogo.
'''

def escolhido():
  linha_de_espaco()
  print('''
     Parti te agora devera prova que verdadeiro,
     Jack Torrence,um ex-professor e aspirante a escritor.   
   ''')
  linha_de_espaco()
  primeira_fase()

def primeira_fase():
    linha_de_espaco()
    print("Primeira fase: Sobre a obra")
    linha_de_espaco()   
    return primeira_pergunta()

def primeira_pergunta():
   print(''' 1- O lancaçamento do seu filme foi 1980:
       [1] Verdadeiro
       [2] Falso
    ========================================================
       ''')

   while True:
       resposta = int(input("Prove que é Jack resposta corrretamente : "))

       if resposta ==1:
           print("Otimo você lembro, proxima pergunta...")
           return segunda_pergunta()
       else:
            return mensagem_do_imposto()
def segunda_pergunta():
    print(''' 2- O diretor do seu filme foi Stanley Kubrick:
            [1] Verdadeiro
            [2] Falso
         ========================================================
      ''') 

    while True:
           resposta = int(input("Prove que é Jack resposta corrretamente : "))

           if resposta ==1:
               print("Otimo você lembro, proxima pergunta...")
               return terceira_pergunta()
               
           else:
             return mensagem_do_imposto()

def terceira_pergunta():
    print(''' 3- A historia do seu filme passa no velho hotel Bates Motel:
            [1] Verdadeiro
            [2] Falso
         ========================================================
    ''')
    while True:
           resposta = int(input("Prove que é Jack resposta corrretamente : "))

           if resposta ==1:
               return mensagem_do_imposto()
               
           else: 
               print("Otimo você lembro, proxima pergunta...")
               return segunda_fase()

   
def segunda_fase():
      def linha_de_espaco():
        print("=" *50)
      linha_de_espaco()
      print("Segunda fase: Contexto Narrativo ")
      linha_de_espaco()
      return quarta_pergunta()
def quarta_pergunta():
    print(''' 
            4-Qual é nome dos seus familiares?
            [1] Hanna e Blake
            [2] Wendy e Danny
            [3] Allison e Troy
         ========================================================
    ''')    
    
    while True:
         resposta = int(input("Prove que é Jack resposta corrretamente : "))

         if resposta ==1:
            return mensagem_do_imposto()
         elif resposta ==2:
            print("Otimo você lembro, proxima fase...")
            return quinta_pergunta()
         else: 
            return mensagem_do_imposto() 
def quinta_pergunta():
      print(''' 
            5- Qual é emprego que você aceita?
            [1] Motorista
            [2] Cozinheiro
            [3] Zelador

         ========================================================
    ''')  
     
      while True:
         resposta = int(input("Prove que é Jack resposta corrretamente : "))

         if resposta ==1:
            return mensagem_do_imposto()
         elif resposta ==2:
           return mensagem_do_imposto()
            
            
         else: 
             print("Otimo você lembro, proxima fase...")
             return sexta_pergunta()
def sexta_pergunta():
     print(''' 
            6- Por quais motivo você aceita?
            [1] Pelo dinheiro afim paga dividas.
            [2] Para se torna mais proxima da sua familia.
            [3] Na esperança de curar seu bloqueio de escritor.

         ========================================================
    ''')  
     while True:
         resposta = int(input("Prove que é Jack resposta corrretamente : "))
         if resposta ==1:
            return mensagem_do_imposto()
            
         elif resposta ==2:
            return mensagem_do_imposto()
            
         else: 
             print("Otimo você lembro, proxima fase...")
             return terceira_pergunta()
def terceira_fase():
       linha_de_espaco()
       print("Terceira fase:Sobre o Você.")
       linha_de_espaco()
       return setima_pergunta()
def setima_pergunta():
      print(''' 
            7- Qual é nome do amigo imaginario do seu filho?
            [1] Tony
            [2] Christopher
            [3] Nathan

        ========================================================
    ''')  
      while True:
         resposta = int(input("Prove que é Jack resposta corrretamente : "))
         if resposta ==1:
            return mensagem_do_imposto()
         elif resposta ==2:
            return mensagem_do_imposto()  
         else: 
            print("Otimo você lembro, proxima fase...")
            return oitava_pergunta()
def oitava_pergunta():
      print(''' 
            8- Qual foi motiva banal que você machucou seu filho?
            [1] Por ele ter sido desobediência
            [2] Por ele fala sozinho
            [3] Por ele terespalhando suas folhas.
         ========================================================
    ''')  
      while True:
         resposta = int(input("Prove que é Jack resposta corrretamente : "))
         if resposta ==1:
              return mensagem_do_imposto()
         elif resposta ==2:
             return mensagem_do_imposto()
         else: 
            print("Otimo você lembro, proxima fase...")
            return nona_pergunta()
    
def nona_pergunta():
         print(''' 
            9- Por qual você transforma em um maníaco homicida?
            [1] Sonho que você mata filho e esposa.
            [2] Fica varios dias isolado e não evoluir com livro.
            [3] O fato de você descobrir coisas sombrias do hotel.

         ========================================================
    ''')  
         while True:
            resposta = int(input("Prove que é Jack resposta corrretamente : "))
            if resposta ==1:
              return mensagem_do_imposto()
            elif resposta ==2:
               print("Não vou deixa vez imposto!")
               return mensagem_do_imposto()
               
            else: 
               print("Otimo você lembro, proxima fase...")
               return 

def linha_de_espaco():
     print("-=-" *25)


def mensagem_do_imposto():
   linha_de_espaco()
   print('''
      Não vou deixa vez seu imposto.
      Fim de jogo para você!!!
   ''')
   linha_de_espaco()

def mensagem_do_vencedor():
    linha_de_espaco()
    print('''
         Você realmente é maníaco homicida e 
         alcoólatra Jack Torrence.
         Parabéns você não é imposto!!
  ''')
linha_de_espaco()