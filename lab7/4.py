employees = {}
i = 0
while i<5:
  names = input("Enter the name: ")
  salary1 = int(input("Enter the salary: "))
  employees.update({salary1:names})
  i += 1


salary = employees.keys()
salary = sorted(salary, reverse = True)
for maas in salary[0:3]:
  print(employees[maas])
