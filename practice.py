import pandas as pd
myemployee = pd.DataFrame([[21,'dhanush','software',45000,'ABC'],
                           [32,'SAMEER','MANAGER',50000,'CSS'],
                           [45,'PRADEEP','OWNER',10000,'CCA'],
                           [66,'RILWAN','ASSOCIATE',44000,'GFD'],
                           [41,'ABI','DEVELOPER',58000,'FRE']],
                          columns=['Employeecode','EmployeeName','Designation','Salary','CompanyName'])
myemployee.to_csv("EMPLOYEE.csv")