immutale_var = 1,2,3,4,True,'String'
print('Immutale:',(immutale_var))
#immutale_var[1]=5 выдает ошибку "'tuple' object does not support item assignment" так как кортеж не поддерживате обращение к элементам
mutable_var = [1,2,3,False,1.5]
print('Mutale:',mutable_var)
mutable_var[2] = 5
print('New mutale:', mutable_var)