from Classes import *;
import array;
from Emp import Emp;

def create():
    #arr = array.array(str('Emp'),Emp("",""))
    while(True):
        print("-"*30)
        print("1. Clerk")
        print("2. Programmer")
        print("3. Manager")
        print("4. Exit")
        print("-"*30)
        choice = int(input("Enter Choice : "))
        if(choice==1):
            #arr.append(Clerk())
            Clerk()
        elif(choice==2):
            #arr.append(Programmer())
            Programmer()
        elif(choice==3):
            #arr.append(Manager())
            Manager()
        else:
            #print(arr)
            break

def display():
    f = open("employee.txt", "r")
    for line in f:
        arr = line.split("|")
        print("-"*30)
        print("Name : "+arr[0]+"\nAge : "+arr[1] + "\nSalary : "+arr[2] + "\nDesignation : "+arr[3])
        print("-"*30)
    f.close()
