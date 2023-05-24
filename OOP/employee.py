class Employee:
    def __init__(self, name, email, title, salary):
        self.name = name
        self.email = email
        self.title = title
        self.salary = salary
        self.__company = 'BestSoft'


    def print_info(self):
        print(f'Employee {self.name} works as {self.title} and earns {self.salary} PLN per month. You can contact the employee via {self.email}\n')


    # Getter
    def get_company(self):
        return self.__company
    
    # Setter
    def set_company(self, value):
        if value == '':
            self.__company = 'BestSoft'
        else:
            self.__company = value

    # Decorator
    @property
    def company(self):
        return self.__company
    
    @company.setter
    def company(self, value):
        if value == '':
            self.__company = 'BestSoft'
        else:
            self.__company = value