from video import Video
from Gafanhoto import Gafanhoto
from Visualização import Visualizacao

v1 = Video('Curso tkinter')
v1.play()
v1.pause()
v1.like()
print(v1.__dict__)

g1 = Gafanhoto('Antonio', 14, 'Masculino', 'Cripeer_Extreme')
g1.GanharExperiencia()
g1.ViuMaisUm()
g1.ViuMaisUm()
print(g1.__dict__)

visu = Visualizacao(g1, v1)
visu.avaliarNota(4)
print(visu.filme.avaliacao)
print(visu.__dict__)




