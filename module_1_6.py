#  "Словари и множества"
my_dict = {'Anastasiia': 1995, 'Danila': 1997, 'Fedor': 2005}
print ('Словарь:', my_dict)

print ('Дата рождения Anastasiia:', my_dict['Anastasiia'])

print ('Дата рождения Lena:', my_dict.get('Lena'))

my_dict.update ({'Alex': 1974,
                'Galina': 1958})
print ('Добавили две произвольные пары:', my_dict)

print ('Удалена дата рождения Anastasiia:', my_dict.pop('Anastasiia'))
print ('Новый словарь:', my_dict)


my_set = {1, 2, 3, 0, 1, 2, 455, 456, 'Яблоко', 'Лес', 'Лес'}
print ('Моё множество:', my_set)
my_set.add(5)
my_set.add((1,2,3))
my_set.discard(2)
print ('Новое множество:', my_set)
