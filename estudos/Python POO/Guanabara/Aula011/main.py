from Aluno import Aluno, Pessoa
from Professos import Professor
from Visitante import Visitante
p1 = Pessoa('jose', 21, 'M')
a1 = Aluno(50406, 'informatica', 'antonio', 14, 'M')
prof1 = Professor('Literatura', 3000, 'Iara', 27, 'F')

prof1.aumento(3000)

print(p1.__dict__)
print(a1.__dict__)
print(prof1.__dict__)
