class Student(object):
    def __init__(self, stu_id, stu_name, stu_age):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_age = stu_age

    def __str__(self):
        return '%s %s %s' % (self.stu_id, self.stu_name, self.stu_age)


if __name__ == '__main__':
    tom = Student('1', 'Tom', '12')
    print(tom)

