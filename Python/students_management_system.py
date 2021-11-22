"""
    Students Management System
"""
from typing import TYPE_CHECKING


students = []


def main():
    while True:
        show_menu()
        function_id = input('Please input a function ID:')
        operator(function_id)


def show_menu():
    print('--------------------------------')
    print('Students Management System v1.0')
    print('1:Add student')
    print('2:Delete student')
    print('3:Modify student')
    print('4:Find student')
    print('5:Show all students')
    print('6:Exit system')
    print('--------------------------------')


def operator(function_id):
    if function_id == '1':
        add_stu()
    elif function_id == '2':
        del_id = input('Please input the ID you want to delete:')
        del_stu(del_id)
    elif function_id == '3':
        modify_id = input('Please input the ID you want to modify:')
        modify_stu(modify_id)
    elif function_id == '4':
        query_stu = input('Please input the ID you want to find:')
        stu = search_stu_with_id(query_stu)
        show_stu_info(stu)
    elif function_id == '5':
        show_all_stu()
    elif function_id == '6':
        exit(0)
    else:
        print('The ID you input was wrong,please reinput.')


def input_stu_info():
    stu_id = input('Please input ID:')
    stu_name = input('Please input Name:')
    stu_age = input('Please input Age:')
    return stu_id, stu_name, stu_age


def add_stu():
    stu = {}
    stu_info = input_stu_info()
    stu['id'] = stu_info[0]
    stu['name'] = stu_info[1]
    stu['age'] = stu_info[2]
    students.append(stu)
    # print(students)


def search_stu_with_id(stu_id):
    for stu in students:
        if stu['id'] == stu_id:
            # show_stu_info(stu)
            return stu
    else:
        print(f'The ID {stu_id} does not exist!')
        return None


def show_stu_info(stu):
    print(f'ID:{stu["id"]}, Name:{stu["name"]}, Age:{stu["age"]}')


def del_stu(del_id):
    stu = search_stu_with_id(del_id)
    if stu != None:
        students.remove(stu)


def modify_stu(modify_id):
    stu = search_stu_with_id(modify_id)
    if stu != None:
        stu_info = input_stu_info()
        stu['id'] = stu_info[0]
        stu['name'] = stu_info[1]
        stu['age'] = stu_info[2]


def show_all_stu():
    for stu in students:
        show_stu_info(stu)


main()

