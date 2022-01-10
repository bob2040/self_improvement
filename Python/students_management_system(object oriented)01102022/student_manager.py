from student import Student


class StudentManagerSystem(object):
    def __init__(self):
        self.students = {}

    def start(self):
        self.__load_data()
        print('Student Management System is running,enjoy it yourself.')
        while True:
            self.__print_menu()
            selected_id = input('Please input a function ID:')
            if selected_id.isdigit():
                n = int(selected_id)
                if n >= 0 and n <= 7:
                    self.__operator(selected_id)
                else:
                    print('The function ID you input was out of its range,please re-input.')
            else:
                print('The function ID you input was not a number,please re-input.')

    def __print_menu(self):
        print('*' * 30)
        print('Welcome to use [Students Management System] v1.1')
        print('[1].Add student')
        print('[2].Show all students')
        print('[3].Search student')
        print('[4].Modify student')
        print('[5].Delete student')
        print('[6].Save data')
        print('[7].Load data')
        print()
        print('[0].Exit')
        print('*' * 30)

    def __operator(self, selected_id):
        func_dict = {'1': '[1].Add student.',
                     '2': '[2].Show all students.',
                     '3': '[3].Search student.',
                     '4': '[4].Modify student.',
                     '5': '[5].Delete student.',
                     '6': '[6].Save data.',
                     '7': '[7].Load data.',
                     '0': '[0].Exit.'}
        print(f'*Tip: You have just selected the function: {func_dict[selected_id]}')
        method_dict = {'1': self.__add_student,
                       '2': self.__show_all_info,
                       '3': self.__search_stu_with_id,
                       '4': self.__modify_stu_with_id,
                       '5': self.__remove_stu_with_id,
                       '6': self.__save_data,
                       '7': self.__load_data,
                       '0': exit}
        method = method_dict[selected_id]
        if selected_id == '3' or selected_id == '4' or selected_id == '5':
            stu_id = input('Please input a student ID that you want to operate:')
            method(stu_id)
        elif selected_id == '0':
            self.__save_data()
            method(0)
        else:
            method()

    def __add_student(self):
        stu_info = self.__input_stu_info()
        stu = Student(stu_info[0], stu_info[1], stu_info[2])
        self.students[stu.stu_id] = stu
        # self.students[stu_info[0]] = stu

    def __search_stu_with_id(self, stu_id):
        stu = None
        if stu_id in self.students:
            stu = self.students[stu_id]
            self.__show_stu_info(stu)
        else:
            print(f'The student whose ID is {stu_id} does not exist!')
        return stu

    def __modify_stu_with_id(self, stu_id):
        stu = self.__search_stu_with_id(stu_id)
        if stu != None:
            new_stu_info = self.__input_stu_info()
            stu.stu_id = new_stu_info[0]
            stu.stu_name = new_stu_info[1]
            stu.stu_age = new_stu_info[2]
            print('Modified successfully!')
            self.__show_stu_info(stu)
        else:
            print(f'The student whose ID is {stu_id} does not exist!')

    def __remove_stu_with_id(self, stu_id):
        stu = self.__search_stu_with_id(stu_id)
        if stu:
            self.students.pop(stu_id)
        else:
            print(f'The student whose ID is {stu_id} does not exist!')

    def __show_stu_info(self, stu):
        print(stu)

    def __show_all_info(self):
        for stu in self.students.values():
            # print(stu)
            self.__show_stu_info(stu)

    def __input_stu_info(self):
        stu_id = input('Please input student ID:')
        stu_name = input('Please input student name:')
        stu_age = input('Please input student age:')
        return stu_id, stu_name, stu_age

    def __save_data(self):
        print('Saving data......')
        file_w = open('data', 'w')
        for stu in self.students.values():
            stu_s = stu.stu_id + ' ' + stu.stu_name + ' ' + stu.stu_age + '\n'
            file_w.write(stu_s)
        file_w.close()
        print('Saved successfully!')

    def __load_data(self):
        print('Loading data......')
        file_r = None
        try:
            file_r = open('data', 'r')
        except Exception as e:
            print(e, 'File does not exist!')
        else:
            print('Loaded successfully!')
            content = file_r.readlines()
            for stu_s in content:
                split_info = stu_s.split()
                stu = Student(split_info[0], split_info[1], split_info[2])
                self.students[split_info[0]] = stu
        finally:
            if file_r != None:
                file_r.close()
