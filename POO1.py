class Estudante:
  def __init__(self, m):
    self.matricula = m

  def setMatricula(self, m):
    self.matricula = m
  def setNome(self, n):
    self.nome = n
  def setCurso(self, c):
    self.curso = c
  def setDisciplina(self, d):
    self.disciplina = d
  def setNota1(self, n1):
    self.nota1 = n1
  def setNota2(self, n2):
    self.nota2 = n2
  def setNota3(self, n3):
    self.nota3 = n3
  def setNota4(self, n4):
    self.nota4 = n4
    
  def getMatricula(self):
    return self.matricula
  def getNome(self):
    return self.nome
  def getCurso(self):
    return self.curso
  def getDisciplina(self):
    return self.disciplina
  def getNota1(self):
    return self.nota1
  def getNota2(self):
    return self.nota2
  def getNota3(self):
    return self.nota3
  def getNota4(self):
    return self.nota4

  def media(self):
    return (self.nota1*2 + self.nota2*2 + self.nota3*3 + self.nota4*3)/10
  
  def status(self):
    if self.media() < 30:
      return "Reprovado"
    elif self.media() >= 60:
      return "Aprovado"
    else:
      return "em Prova Final"
  def info(self):
    return f'{self.matricula} e {self.nome}'

aluno = Estudante(int(input("Digite sua matrícula: ")))

aluno.setNome(input("Digite seu nome: "))
aluno.setCurso(input("Digite o nome de seu curso: "))
aluno.setDisciplina(input("Digite a disciplina de interesse: "))

aluno.setNota1(int(input("Digite a nota do 1° Bimestre: ")))
aluno.setNota2(int(input("Digite a nota do 2° Bimestre: ")))
aluno.setNota3(int(input("Digite a nota do 3° Bimestre: ")))
aluno.setNota4(int(input("Digite a nota do 4° Bimestre: ")))

print(f"O aluno cuja matricula e nome são, respectivamente, {aluno.info()}, está {aluno.status()}, na disciplina de {aluno.getDisciplina()} com média de {aluno.media()} pontos.")