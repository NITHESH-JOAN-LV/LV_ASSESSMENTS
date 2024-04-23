# -*- coding: utf-8 -*-
"""Internal Assessment_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WGTZUiGmpnGHEdYtglRPOTR-okx6bof4
"""

import numpy as np
import pandas as pd

# Q1.
l=[1,2,3,4,5]
l=np.array(l)
print('sum',l.sum())
print('max',l.max())
print('min',l.min())
print('mean',l.mean())
print('std',l.std())

# Q2

def normalize(data,normalized_data):
  for i in data:
    norm= np.mean(i)/max(i)-min(i)
    std= np.std(i)
    normalized_data.append([norm,std])



normalized_data=[]
health=np.array([[160,70,30],[165,65,35],[170,75,40]])
normalize(health,normalized_data)
print(normalized_data)

# Q3.
marks=np.array([[50,60,50,80],[60,60,70,90]])
marks_arr=[]
for i in marks:
  if -1 not in i:
    marks_arr.append(i)
marks=np.array(marks_arr)
avg_score=marks[:,1:].mean(axis=1)
print(avg_score)

#Q4
temp=np.linspace(15,25,24)
print(temp)

#Q5
import numpy as np
daily_closing_prices = np.array([100, 102, 98, 105, 107, 110, 108, 112, 115, 118, 120])
answer=pd.Series(daily_closing_prices)
window_size = 5
print(answer.rolling(window_size).mean())

#Q6
samples=np.linspace(0,1,100)
print(samples)

#Q7:
import numpy as np
properties_matrix = np.array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]])
print(np.linalg.det(properties_matrix))

#Q8:
array=[[1,2,3],[4,5,6],[7,8,9]]
arr=np.array(array)
print(arr[arr<5])

#Q9:
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'Age': [25, 30, 35, 40, 45, 50, 55],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Miami', 'Boston'],
        'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales', 'IT', 'HR']}
df=pd.DataFrame(data)
df=df[(df['Age']<45) & (df['Department']!='HR')]
print(df)

# Q10
data = {'Department': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Home Goods'],
        'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Sales': [70000, 50000, 30000, 40000, 60000]}
df=pd.DataFrame(data)

department_sales=df.groupby(['Department','Salesperson'])['Sales'].mean().sort_values(ascending=False)
print(department_sales)

#Q11
data = {
    'Product': ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries', 'Flour', 'Grapes'],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit', 'Bakery', 'Fruit'],
    'Price': [1.20, 0.50, 3.00, 2.50, 4.00, 1.50, 2.00],
    'Promotion': [True, False, True, True, False, True, False]
}

df=pd.DataFrame(data)
fruits=df[df['Category']=='Fruit']
category_price_avg=fruits['Price'].mean()
answer=fruits[(fruits['Price']>category_price_avg) & (fruits['Promotion']==False)]

print(answer)

#Q12
employee_data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'IT', 'Finance', 'IT'],
    'Manager': ['John', 'Rachel', 'Emily', 'Rachel']
}
project_data = {
    'Employee': ['Alice', 'Charlie', 'Eve'],
    'Project': ['P1', 'P3', 'P2']
}

employee=pd.DataFrame(employee_data)
project=pd.DataFrame(project_data)

merged=pd.merge(employee,project,on='Employee',how='left')
print(merged)

#Q13
sports_team=pd.read_csv("/content/Q13_sports_team_stats.csv")

wins=sports_team.groupby("TeamID")['Wins'].sum()
total=sports_team.groupby("TeamID")['GamesPlayed'].sum()
print("Ratio")
print()
print(wins/total)
print()
print("avg_score")
# we need game id and score to calcualte avg score per game.
avg_score=sports_team.groupby(['TeamID','Game Id'])['Score'].mean()
print(avg_score)

# Q14
customer=pd.read_csv("/content/Q14_customer_purchases.csv")
before=customer[customer['Date']<customer['LoyaltyProgramSignUp']]
before_purchase=before.groupby("CustomerID")['PurchaseAmount'].sum()
mean_before=before.groupby("CustomerID")['PurchaseAmount'].mean()
after=customer[customer['Date']>=customer['LoyaltyProgramSignUp']]
after_purchase=after.groupby("CustomerID")['PurchaseAmount'].sum()
after_mean=after.groupby("CustomerID")['PurchaseAmount'].mean()
print("Before program")
print("total",before_purchase)
print('Mean',mean_before)
print("After Program")
print("total",after_purchase)
print('Mean',after_mean)
#it can be seen that more number of customers have joined after the loyalty program and it has boosted the sales

#Q15
students=pd.read_csv("/content/Q15_student_grades.csv")
avg_score_sub=students.groupby('Subject')['Grade'].mean()
median_score_sub=students.groupby("Subject")['Grade'].median()
print("avg")
print(avg_score_sub)
print()
print('median')
print(median_score_sub)
# from the given data i would say the students are already performing good. so we can just do whatever we are doing now.





print(students)