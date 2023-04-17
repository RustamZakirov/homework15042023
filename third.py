# Создайте скрипт бота, который находит ответы на фразы по ключу в словаре.
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут».
# Если фраза ему неизвестна, он выводит соответствующую фразу.

def importlist():
        print('новый ключ: ')
        b = str.lower(input())
        print('новое значение: ')
        c = str.lower(input())
        list[b] = c

list = {'привет': 'hello', 'как дела?': 'нормально', 'как тебя зовут?': 'PytonTest'}
flag = True
print('Введите запрос')
while flag == True:
    a = str.lower(input())
    if a == 'стоп':
        flag = False
    elif a in list:
        print(list.get(a))
    elif a == 'добавить':
        importlist()
    else:
        print('я не знаю, что ответить')
