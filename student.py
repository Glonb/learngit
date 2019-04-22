class Student:
    stuCount = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.stuCount +=1
    
    def showCount(self):
        print("Total Student is:  ", Student.showCount)

    def showStu(self):
        print("Name: ", self.name, ", Age: ", self.age)
    
stu1 = Student("Daming", 18)
stu2 = Student("Xiaoming", 20)
stu1.showStu()
stu2.showStu()
print("total student is: ", Student.stuCount)