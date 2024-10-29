n = input('Введите N: ')
m = input('Введите M: ')
value = input('Введите Value: ')
def get_matrix():
    matrix = []
    for i in range(int(n)):
        matrix.append([value]*int(m))
    print(matrix)

get_matrix()