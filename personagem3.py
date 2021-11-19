


def escolhido():
  linha_de_espaco()
  print('''
    Parti te agora devera prova que verdadeiro,
    Pennywise, um palhaço cruel que se alimenta de seus
    medos e cuja violência teve origem há vários séculos. 
   ''')
  linha_de_espaco()
  primeira_fase()

def primeira_fase():
    linha_de_espaco()
    print("Primeira fase: Sobre a obra")
    linha_de_espaco()   
    return primeira_pergunta()

def primeira_pergunta():
   print('''1- Seu filme foi baseado no livro mesmo nome:
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
    print(''' 2- O autor desse livro é Stephen King:
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
    print(''' 3- A historia do seu filme passa na cidade Nova York e no bairro Manhattan:
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
            4-Qual é o nome do grupo de criança que lhe derrota?
            [1] Os salvadores
            [2] Os perdedores
            [3] Os vencedores
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
            5- Onde é sua primeira aparição no seu filme?
            [1]No banheiro
            [2]Na biblioteca
            [3]No poço

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
            6- O que geralmente surgir quando você aparece?
            [1] Balão azul
            [2] Balão verde
            [3] Balão vermelho

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
            7- Qual é seu poder?
            [1] Se transforma nos piores medos das pessoas
            [2] Entra nos sonhos da pessoas.
            [3] Atravessa paredes.

        ========================================================
    ''')  
      while True:
         resposta = int(input("Prove que é Jack resposta corrretamente : "))
         if resposta ==1:
           print("Otimo você lembro, proxima fase...")
           return oitava_pergunta()
         elif resposta ==2:
            return mensagem_do_imposto()  
         else: 
            return mensagem_do_imposto()
def oitava_pergunta():
      print(''' 
            8- Qual é sua verdadeira forma?
            [1]Uma espécie de aranha gigante.
            [2]Um Palhaço
            [3]Um ser humano comum
         ========================================================
    ''')  
      while True:
         resposta = int(input("Prove que é Jack resposta corrretamente : "))
         if resposta ==1:
             print("Otimo você lembro, proxima fase...")
             return nona_pergunta()
         elif resposta ==2:
             return mensagem_do_imposto()
         else: 
             return mensagem_do_imposto()
    
def nona_pergunta():
         print(''' 
            9- Qual tempo média de sua hibernaçãoW?
            [1] 10 a 20 anos
            [2] 27 a 30 anos
            [3] 25 a 35 anos

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

   