from data_create import input_user_data

def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком формате записать данные? \n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор: '))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write( f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')

def print_data():
    print('1 файл:')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))
        
    print('2 файл:')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))

"""
Пояснения к работе функции переноса данных transfer_data.
Перенос информации будет осуществляться из файла first в файл second.
Учитывая алгоритм добавления новой информации в файл, можно сделать вывод, что блок данных в отношении определенного
клиента будет всегда занимать четко определенную позицию. В отношении первого клиента это будут четыре подряд 
идущие строки, начиная с первой. В отношении второго клиента - четыре строки, начиная с шестой. В отношении 
3-го - с 11-ой строки и т.д. 
Таким образом, в отношении определенного клиента под номером N из потока data необходимо будет взять срез из 4-х
элементов со смещением, начиная с (N-1)*5 до (N-1)*5 + 4.
Далее из списка data выбранную информацию нужно исключить и файл перезаписать.
Выбранную информацию в отношении клиента в соответствующем формате добавляем во второй файл.
При разработке программы будем исходить из того, что пользователь вводит корректное значение номера данных (проверку
на корректность номера и физического существования таких строк в файле не делаем).
Специальные модули Python, позволяющие сразу обращаться к информации по номеру строки, не использовал. 
"""

def transfer_data():
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        number_data = int(input("Информацию о каком клиенте необходимо перенести (порядковый номер клиента)? "))
        transfer_data_value = data[(number_data - 1) * 5: (number_data - 1) * 5 + 4]
        data_new = data[:(number_data - 1) * 5] + data[number_data * 5:]
    with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
        file.write(f'{transfer_data_value[0][:-1]};{transfer_data_value[1][:-1]};{transfer_data_value[2][:-1]};{transfer_data_value[3][:-1]}\n\n')
    with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
        file.write(''.join(data_new))
