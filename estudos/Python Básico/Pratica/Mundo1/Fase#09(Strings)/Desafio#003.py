c = input('sua cidade:')
c = c.lower().split()
print('Sua cidade começa com santo? {}'.format('santo' in c[0]))