
# добавляем импортирование функции для переноса данных
from logger import input_data, print_data, transfer_data

# В функцию добавляем функционал выбора для переноса данных
def interface():
    print('Добрый день! Это бот-помощник. \n'
          'Что вы хотите сделать? \n'
          '1 - Записать данные \n'
          '2 - Вывести данные, \n'
          '3 - Перенести данные') # добавленный функционал для выбора варианта переноса
    command = int(input('Ваш выбор: '))

    while command < 1 or command > 3: # корректируем с 2 на 3
        command = int(input('Ошибка! Ваш выбор: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()

    # добавляем функцию для переноса данных
    # перенос данных будет осуществляться из файла first в файл second
    elif command == 3:
        transfer_data()

interface()
