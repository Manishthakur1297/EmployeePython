from Emp import *;

def main():
    while(True):
        print("-"*30)
        print("1. Create")
        print("2. Display")
        print("3. Exit")
        print("-"*30)
        choice = int(input("Enter Choice : "))
        if(choice==1):
                while(True):
                    print("-"*30)
                    print("1. Clerk")
                    print("2. Programmer")
                    print("3. Manager")
                    print("4. Exit")
                    print("-"*30)
                    choice = int(input("Enter Choice : "))
                    if(choice==1):
                        Clerk()
                    elif(choice==2):
                        Programmer()
                    elif(choice==3):
                        Manager()
                    else:
                        break
        elif(choice==2):
            Emp.display()
        else:
            break

        
    print("Total Employee Created : ",Emp.count)
