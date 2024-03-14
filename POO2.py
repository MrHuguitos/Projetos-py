nome = []
idade = []

while True:
  print('1 - Adicionar elemento')
  print('2 - Salvar e encerrar')
  print('3 - Abrir e exibir')

  op = int(input("O que deseja? "))

  if op == 1:
    n = str(input("Seu nome: "))
    i = str(input("Sua idade: "))

    nome.append(n)
    idade.append(i)
  elif op == 2:
    print('Operção Finalizada')
    #Salvando dados
    with open('Aluno.txt', 'w') as f: #'w' é usado para escrever em um arquivo
      for indice in range(0, len(nome)):
        f.write(f'{nome[indice]} : {idade[indice]}\n') #Nesse exemplo, o código vai escrever o valor no arquivo aluno
    #terminando a execução
    break
  elif op == 3:
    print('Abrindo arquivo...')
    with open('Aluno.txt', 'r') as f: #'r' é usado para ler um arquivo
      dados = f.readlines() #Nesse exemplo, o codigo vai ler os itens da lista aluno

      for d in dados:
        dado = d.split(':')
        nome.append(dado[0])
        idade.append(int(dado[1])) #Adicionando os valores do arquivo na lista

      for indice in range(0, len(nome)):
        print(f'{nome[indice]} : {idade[indice]}') #exibindo as listas

  else:
    print('Operação Invalida')