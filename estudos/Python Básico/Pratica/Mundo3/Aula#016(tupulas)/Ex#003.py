lanche = ('Hambuguer', 'Suco', 'Pizza', 'Pudim', 'batata frita')
print(len(lanche))
#for c in range (0, len(lanche)):
#    print(f'Vou comer {len(lanche)} na posição {c}')

#for comida in lanche:
#    print(comida)

for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')

print('Comi p cacete')