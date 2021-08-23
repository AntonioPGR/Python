from Aluno import Aluno, Pessoa
from Professos import Professor
from Funcionario import Funcionario

p1 = Pessoa('jose', 21, 'M')
a1 = Aluno(50406, 'informatica', 'antonio', 14, 'M')
prof1 = Professor('Literatura', 3000, 'Iara', 27, 'F')
f1 = Funcionario('Manutenção', True, 'Josefa', 57, 'F')

f1.nome = 'Maria'
prof1.aumento(3000)
f1.mudarTrabalho('Enfermagem')

print(p1.__dict__)
print(a1.__dict__)
print(prof1.__dict__)
print(f1.__dict__)