'''
Дана послідовність n, що складається з символів s1, s2, .... Обрахувати загальну
кількість входжень символів +, -, * у послідовність.
'''
while True:
    n = input('Enter the symbols: ')
    if ' ' not in set(n):
        a, b, c = '+', '-', '*'
        print(f'Amount of +: {list(n).count(a)} \nAmount of -: {list(n).count(b)} \nAmount of *: {list(n).count(c)} \n'
              f'The total amount: {list(n).count(a) + list(n).count(b) + list(n).count(c)}')
    else:
        print('The sequence must be without spaces')

    answer = input('Do you want to run the program again? Yes (+), No (anything) ')
    if answer == '+':
        continue
    else:
        break
