class Teacher:
    temp = 0 
    def __init__(self, name, surname, subject, age):
        Teacher.temp += 1
        self.name = name
        self.surname = surname
        self.subject = subject
        self.age = age
        self.fullname = name + ' ' + surname

    def instance_number(self):
        return Teacher.temp    



T1 = Teacher('Akash', 'Tripathi','Python', 32)

T2 = Teacher('Vibha', 'Tripathi','C', 32)

print(T1.instance_number())
print(Teacher.temp)