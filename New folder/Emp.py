class Emp:
    count = 0
    def __init__(self, salary, designation):
        self.name = input("Enter Name : ")
        self.age = int(input("Enter Age : "))
        self.salary = salary
        self.designation = designation
        f = open("employee.txt", "a")
        f.write(self.name+"|"+str(self.age)+"|"+str(self.salary)+"|"+self.designation+"\n")
        f.close()
        Emp.count+=1
