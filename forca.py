import random

palavras = ["Carro", "Moto", "Bicicleta"]
escolha = random.choice(palavras)
game = list(escolha)
letras_usadas = []
erros = 0
acertos = 0

representacao_lista = ['_' for _ in game] # Criando uma lista com o mesmo número de elementos que game, mas todos os elementos são inicializados como '_'.
print(" ".join(representacao_lista)) #Unir os elementos da lista, sem as aspas

while erros < 5:
    letra = str(input("Digite uma letra: "))
    if letra in letras_usadas:
        print("Essa letra já foi usada!")
    else:
        letras_usadas.append(letra) # Adiciona a letra na lista de listas já usadas
        if letra in game: # Caso a letra esteja na palavra
            posicoes = [index for index, item in enumerate(game) if item == letra] # Encontre todas as posições do valor na lista
            for posicao in posicoes: # Substitua o "_" nas posições pelos valores correspondentes
                representacao_lista[posicao] = letra 
            print(" ".join(representacao_lista))
            acertos += len(posicoes) #Quantidade de posições que a letra estava
            if acertos == len(game): #Se a quantidade de letras certas for igual a quantidade de letras no jogo, o jogo será encerrado
                print("Você ganhou!")
                break
        else:
            print("Tente novamente!")
            erros += 1

if erros >= 5:
    print("Você Perdeu!")
print("Encerrando...") 