nums = [[], []]
for c in range(0,7):
    num = int(input(f'Digite o {c}o. Numero:'))
    if num%2 == 0:
        nums[0].append(num)
    else:
        nums[1].append(num)

nums[0].sort()
nums[1].sort()
print(f'pares: {nums[0]}')
print(f'impares: {nums[1]}')