
class Employees: 
    COMPANY = 'Robosapiens'
    
    # Constructor
    def __init__(self, name, email, dept, salary):
        self.name = name
        self.email = email
        self.dept = dept
        self.salary = salary
    
    
    # Method
    def emp_info(self):
        print(f'Name is {self.name}')
        print(f'Email is {self.email}')
        print(f'Dept is {self.dept}')
        print(f'Salary is {self.salary}')
    
    def change_dept(self, new_dept):
        self.dept = new_dept
        print(f'department changed to {new_dept}')


# Object Creation
emp1 = Employees('Himanshu', 'raju@gmail.com', 'Sales', 30000)
emp2 = Employees('Kinshu', 'sham@gmail.com', 'QA', 600000)


emp1.emp_info();
emp2.emp_info();


emp1.change_dept('Devops');
emp1.emp_info()

    