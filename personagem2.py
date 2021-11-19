

def escolhido():
  linha_de_espaco()
  print('''
     Parti te agora devera prova que verdadeira,
      Regan MacNeil a garota possuída
   ''')
  linha_de_espaco()
  primeira_fase()

def primeira_fase():
    linha_de_espaco()
    print("Primeira fase: Sobre a obra")
    linha_de_espaco()   
    return primeira_pergunta()

def primeira_pergunta():
   print(''' 1- O nome diretor do seu é William Friedkin :
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
    print('''2- A historia do seu se passa em no bairro Georgetown em Washington DC :
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
    print(''' 3- A data do seu é foi 7 de setembro 1993:
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
            4-Qual é nome do demononio que se possuir seu corpo?
            [1] Astaroth 
            [2] Abraxas
            [3] Pazuzu
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
            return quinta_pergunta()
def quinta_pergunta():
      print(''' 
            5- Quais principais mudanças que ocorreu sua transformação?
            [1] Convulsão e demonstra poderes sobrenaturais 
                como levitação e grande força.
            [2] Mudança de forma pode ser transforma no bem quiser.
            [3] Super inteligência. 

         ========================================================
    ''')  
     
      while True:
         resposta = int(input("Prove que é Jack resposta corrretamente : "))

         if resposta ==1:
            print("Otimo você lembro, proxima fase...")
            return sexta_pergunta()
         elif resposta ==2:
            return mensagem_do_imposto()
         else: 
            return mensagem_do_imposto()
def sexta_pergunta():
     print(''' 
            6- Qual nome e profissão da sua mãe?
            [1] Chris MacNeil, atriz
            [2] Clary MacNeil, pianista
            [3] Loren MacNeil, cantora

         ========================================================
    ''')  
     while True:
         resposta = int(input("Prove que é Jack resposta corrretamente : "))
         if resposta ==1:
            print("Não vou deixa vez imposto!")
            return mensagem_do_imposto()
         elif resposta ==2:
            print("Não vou deixa vez imposto!")
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
            7- O que medicos supeita ser seu problema?
            [1] Entrada na puberdade
            [2] Questões religiosos
            [3] Uma lesão em seu cérebro

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
            8- Depois de varios exames desgraveis o que acusa?
            [1] Lesão no cerebro
            [2] Problemas psiquiátricos
            [3] Nada de anormal
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
            9- No final do seu filme que salva sua vida?
            [1] Sua mãe Chris
            [2] O médico Roberto.
            [3] O padre e também psiquiatra Karras.

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

   