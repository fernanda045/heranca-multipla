class Funcionario:
    def __init__(self, nome):
        self.nome = nome
    
    def mostrar_tarefas(self):
        print("Faz tarefas gerais.")

class Desenvolvedor(Funcionario):  # Herda de Funcionario
    def __init__(self, nome, linguagem):
        super().__init__(nome)  # Chama o construtor da classe pai
        self.linguagem = linguagem
    
    def programar(self):
        print(f"Programando em {self.linguagem}.")
    
    def mostrar_tarefas(self):  # Sobrescreve o método da classe pai
        print(f"{self.nome} está desenvolvendo em {self.linguagem}.")

class Testador(Funcionario):  # Herda de Funcionario
    def __init__(self, nome):
        super().__init__(nome)  # Chama o construtor da classe pai
    
    def testar(self):
        print("Testando o sistema.")
    
    def mostrar_tarefas(self):  # Sobrescreve o método da classe pai
        print(f"{self.nome} está testando o sistema.")

# Exemplo de uso:
dev = Desenvolvedor("João", "Python")
dev.mostrar_tarefas()  # João está desenvolvendo em Python.
dev.programar()        # Programando em Python.

tester = Testador("Maria")
tester.mostrar_tarefas()  # Maria está testando o sistema.
tester.testar()           # Testando o sistema.