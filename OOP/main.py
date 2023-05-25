from employee import Employee

person_one = Employee('John', 'john.smith@gmail.com', 'DevOps Engineer', '30000')

person_one.print_info()

# There is a hidden property "company". We can get access or change it via 'getter' and 'setter'
# Usage of 'getter'
print(person_one.get_company())

# Usage of 'setter'
person_one.set_company('Luxoft')
print(person_one.get_company())

# Get information about company with help of a method 'company'
print(person_one.company)

# Set company name with method 'company'
person_one.company = 'EPAM'
print(person_one.company)