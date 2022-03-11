import pandas as pd
student = pd.DataFrame([['dhanush',1],['sameer',2],['pradeep',3]] ,columns=['name','rollno'])
student.to_csv("mystudents.csv")