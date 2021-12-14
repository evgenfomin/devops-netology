#!/usr/bin/env python3

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}
def peoples (number):     #оманда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    find_people = ''
    for people in documents:
        if people['number'] == number:
            find_people = people
            print (people['name'])
    if find_people == '':
        print ('не правильно введенное значение или нет таких документов')
    return find_people

def shelfs (number):    #команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    dir = ''
    for shelf in directories:
        for num in directories[shelf]:
            if num == number:
                dir = shelf
                print (f'directory = {dir}')
    if dir == '':
        print ('не правильно введенное значение или нет таких документов')
    return dir

def list ():   #команда, которая выведет список всех документов
    for people in documents:
        print (people['type'], people['number'], people['name'])

def add ():   #команда, которая добавит новый документ в каталог и в перечень полок
    type_doc = input('Введите тип документа: ')
    number_doc = input('Введите номер документа: ')
    name_doc = input('Введите Имя Фамилию: ')
    number_shelf = input('Введите номер полки: ')
    if number_shelf in directories:
        documents.append({"type": type_doc, "number": number_doc, "name": name_doc})
        directories[number_shelf].append(number_doc)
    else:
        print ('Такой полки не существует')

if __name__ == "__main__":
    action = ''
    while action != 'q':
        print('укажите дальнейшее действие:')
        print('p - people, s - shelf, l - list, a - add, d - delete, m - move, as - add shelf,  q - exit')
        action = input()
        if action == 'p':
            number = input('Введите номер документа: ')
            peoples(number)
        elif action == 's':
            number = input('Введите номер документа: ')
            shelfs(number)
        elif action == 'l':
            list()
        elif action == 'a':
            add()
        elif action == 'd':
            number = input('Введите номер документа: ')
            documents.remove(peoples(number))
            directories[shelfs(number)].remove(number)
        elif action == 'm':
            number = input('Введите номер документа: ')
            dir = input('Введите номер полки: ')
            if dir in directories:
                dir_old = shelfs(number)
                directories[dir_old].remove(number)
                directories[dir].append(number)
        elif action == 'as':
            dir = input('Введите номер новой полки: ')
            if dir not in directories:
                directories[dir] = []
            else:
                print('такая полка уже сушествует')
        elif action == 'q':
            print ('bye')
        else:
            print ('Введите нужную команду')