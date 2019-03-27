from Emp import Emp
class Clerk(Emp):
    def __init__(self):
        super().__init__(8000,"Clerk")


class Programmer(Emp):
    def __init__(self):
        Emp.__init__(self,25000,"Programmer")

class Manager(Emp):
    def __init__(self):
        Emp.__init__(self,80000,"Manager")