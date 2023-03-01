from random import randint
nums = (randint(0, 9), randint(0, 9), randint(
    0, 9), randint(0, 9), randint(0, 9))

print('Os valores sorteados foram:', end=' ')
for count in nums:
    print(count, end=' ')
print('')
print(f'O maior valor sorteado foi: {max(nums)}')
print(f'O menor valor sorteado foi: {min(nums)}')
