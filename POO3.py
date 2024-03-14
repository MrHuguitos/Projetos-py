class Funcionario:
  def __init__(self, c):
    self.__cargo = c

  def setCargo(self, c): #atributo privado cargo
    self.__cargo = c
  def setNome(self, n): #atributo privado nome
    self.__nome = n
  def setIdade(self, i): #atributo privado idade
    self.__idade = i
  def setHorasMensais(self, h): #atributo privado horas mensais trabalhadas
    self.__horasMensais = h

  def getHorasMensais(self): #recuperar o atributo privado horas mensais trabalhadas
    return self.__horasMensais
  def getCargo(self): #recuperar o atributo privado cargo
    return self.__cargo
  def getNome(self): #recuperar o atributo privado nome
    return self.__nome
  def getIdade(self): #recuperar atributo privado idade
    return self.__idade

  def salario(self): #Define o salário do funcionario
    valorPorHora = 0
    if self.__cargo == 'Dono':
      valorPorHora = 15
      return self.__horasMensais * valorPorHora
    elif self.__cargo == 'CEO':
      valorPorHora = 30
      return self.__horasMensais * valorPorHora
    elif self.__cargo == 'Estagiario':
      valorPorHora = 5
      return self.__horasMensais * valorPorHora

#Define a classe utilizada e o valor de seus atributos
eu = Funcionario(input("Qual o seu cargo? "))
if (eu.getCargo() == "Dono") or (eu.getCargo() == "CEO") or (eu.getCargo() == "Estagiario"): 
  eu.setNome(input("Qual o seu nome? "))
  eu.setIdade(int(input("Qual a sua idade? ")))
  eu.setHorasMensais(int(input("Quantas horas você trabalha por mês? ")))

  print(f"{eu.getNome()} tem {eu.getIdade()} anos, é {eu.getCargo()} da empresa, recebe R${eu.salario()}, trabalhando {eu.getHorasMensais()} horas por mês.")

else:
  print("Esta função não existe")