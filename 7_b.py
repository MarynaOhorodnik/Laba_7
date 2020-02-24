'''
Вивести дані про книги, тираж яких не перевищує 10000 примірників. Поля структури: Автор, Жанр, Назва, Тираж.
'''
bk = ['book1', 'book2', 'book3', 'book4', 'book5', 'book6', 'book7', 'book8']
ath = {j: i for (j, i) in zip(bk, ['James Joyce', 'Miguel de Cervantes', 'F. Scott Fitzgerald', 'Fyodor Dostoyevsky',\
                                  'Leo Tolstoy', 'Stendhal', 'William Shakespeare','Gustave Flaubert'])}
gnr = {j: i for (j, i) in zip(bk, ['modernist novel', 'novel', 'tragedy', 'psychological fiction',\
                                   '‎historical novel‎','‎bildungsroman', 'tragedy', 'realist novel'])}
nm = {j: i for (j, i) in zip(bk, ['Ulysses', 'Don Quixote', 'The Great Gatsby', 'Crime and Punishment',\
                                  'War and Peace', 'The Red and the Black', 'Hamlet', 'Madame Bovary'])}
edt = {j: i for (j, i) in zip(bk, [10500, 9500, 8150, 8550, 14000, 9250, 10150, 7900])}
for k in range(len(bk)):
    if edt[bk[k]] <= 10000:
        print(f'Name: "{nm[bk[k]]}", author: {ath[bk[k]]}, genre: {gnr[bk[k]]}, edition: {edt[bk[k]]}')
