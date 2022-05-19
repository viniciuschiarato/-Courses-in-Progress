"""num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.remove(2)  # só elimina o 1° elemento
print(num)"""

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 2 in num:
    num.remove(2)
else:
    print('Não achei o número 2')
print(num)
