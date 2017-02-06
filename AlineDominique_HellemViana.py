#EP2-Forca
#Desenvolvedores: Aline Dominique e Hellem Viana
#Matéria: Algoritmos
#Professor: Fernando Masanori Ashikaga
# 1º Semestre A

# Importanção de funções

import random
import os
import urllib.request

# Buscando as palavras no site

pagina = urllib.request.urlopen ('http://www.ime.usp.br/~pf/dicios/br')
palavras = pagina.read().decode ("iso8859").lower()

#variáreis

print("F O R C A")
p= palavras.split()
forca = [
         '''
            | ========= |
            |           |
           ---          |
                        |
                        |
                        |
              _ _ _ _ _ |
         ''',
         '''
            | ========= |
            |           |
           ---          |
          (*_*)         |
                        |
                        |
            ____________|
          ''', 
          '''
            | ========= |
            |           |
           ---          |
          (*_*)         |
            |           |
                        |
            ____________|
         ''',
         '''| ========= |
            |           |
           ---          |
          (*_*)         |
           /|           |
                        |
            ____________|
        ''',
        ''' | ========= |
            |           |
           ---          |
          (*_*)         |
           /|\          |
                        |
            ____________|
        ''',
        '''
            | ========= |
            |           |
           ---          |
          (*_*)         |
           /|\          |
          _/            |
            ____________|
        ''',
        '''
            | ========= |
            |           |
           ---          |
          (*_*)         |
           /|\          |
          _/ \_         |
            ____________|        
        ''']

certas=''
erradas=''
letras=''

#Função que sorteia as
def sorteia():
    global p
    global palavra
    palavra = random.choice(p)
    while len(palavra) <5:
        palavra = random.choice(p)
    if len(palavra)>=5:
        desenha(certas,erradas,p)
      
#Função again ou inicial do jogo 
def jogar():    
    resposta = str(input("\ns - para sim e n - para não.\n")).lower()
    r=resposta
    global erradas
    erradas =''
    global certas
    certas = ''
    global letras
    letras = ''
    
    if r != 's' and r != 'n':
        jogar()
    elif r == 's':
        print("Antes de começarmos,alguns informações:\n1- Somente palavras com mais de 5 letras;\n2- Você só pode errar 6 vezes;\nBoa Sorte!")
        sorteia()
    elif r == 'n':
        print("Fica para próxima.")
        os._exit(0)


#Função dos Chutes
def chute(letras):
    global l
    
    while True:
        l = str(input("\nDigite uma letra:")).lower()
        if len(l) > 1:
            return chute(letras)
        elif l in letras:
            return chute(letras)
        elif l.isalpha():
            cade()

            

def cade():
    global erradas
    global certas
    global letras
    global palavra

    letras=certas+erradas
    
    if l in palavra:
        certas+=l
        desenha(certas,erradas,p)
        chute(letras)
    
    else:
        erradas+= l
        desenha(certas,erradas,p)
        chute(letras)
        
     
       
#Função desenhando a forca
def desenha(certas,erradas,p):
    global forca
    global palavra
    global letras
    
    if len(erradas)==len(forca)-1:
        print('VOCÊ PERDEU!!!')
        print('Letras erradas: '+str(len(erradas))+ ' Letras certas: '+str(len(certas))+'.\n')
        print('A palavra é: '+palavra+'.')
        jogar()
        
    elif win(palavra,certas,erradas):
        print('PARABÉNS!!!\nVocê ganhou!\nQue tal uma nova partida?')
        print('A palavra é: '+palavra+'.')
        jogar()
        
    
    print(forca[len(erradas)])
    print('Erradas: ',erradas)
    print('Certas: ',certas)
    print('Letras:',letras)
    
    for i in palavra:
        if i in certas:
            print (i, end = ' ')
        else:
            tracinho = palavra.replace(palavra, '_')
            print (tracinho, end = ' ')
            
       
    chute(letras)
    
#Função quem ganhou
def win(palavra,certas,erradas):
    ganhou =True
    for letras in palavra:
        if letras not in certas:
            ganhou = False
            break
    return ganhou
            
        
jogar()
