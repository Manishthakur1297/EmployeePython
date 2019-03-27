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


    @staticmethod
    def display():
        f = open("employee.txt", "r")
        for line in f:
            arr = line.split("|")
            print("-"*30)
            print("Name : "+arr[0]+"\nAge : "+arr[1] + "\nSalary : "+arr[2] + "\nDesignation : "+arr[3])
            print("-"*30)
        f.close()


class Clerk(Emp):
    def __init__(self):
        super().__init__(8000,"Clerk")


class Programmer(Emp):
    def __init__(self):
        super().__init__(self,25000,"Programmer")

class Manager(Emp):
    def __init__(self):
        super().__init__(self,80000,"Manager")

