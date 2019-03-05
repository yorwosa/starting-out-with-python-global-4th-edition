import employee

employee1 = employee.Employee('Susan Meyers','47899','Accounting','Vice President')
employee2 = employee.Employee('Mark Jones', '39119','IT','Programmer')
employee3 = employee.Employee('Joy Rogers', '81774','Manufacturing','Engineer')

print('Name\t\tID Number\t\tDepartment\t\tJob Title')
print('-------------------------------------------------------')
print(employee1.get_name() + "\t\t" + employee1.get_id_number()+ "\t\t" + \
      employee1.get_department()+ "\t\t" + employee1.get_job_title())
print(employee2.get_name() + "\t\t" + employee2.get_id_number()+ "\t\t" + \
      employee2.get_department()+ "\t\t" + employee2.get_job_title())
print(employee3.get_name() + "\t\t" + employee3.get_id_number()+ "\t\t" + \
      employee3.get_department()+ "\t\t" + employee3.get_job_title())
print('-------------------------------------------------------')