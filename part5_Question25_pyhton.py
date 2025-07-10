
import pandas as pd
#Ans1
d1={
    'Name':['Mayank','Dev','Rohan'],
    'Grade':['A','B','C'],
    'Roll_No':[100,101,102]
}
dt1=pd.DataFrame(d1)
print(dt1)
#Ans2
d2=pd.read_csv('sales_data_sample.csv',encoding='latin1')
print(d2.head())
#Ans3
d2={
    'Emp_Name':['Mayank','Dev','Rohan'],
    'Salary':[20000,30000,40000],
    'Emp_id':[100,101,102],
    'Age':[34,23,64]
}
dt2=pd.DataFrame(d2)
print(dt2.describe())
#Ans4
print('Shape = ',dt2.shape)
print('Column Name = ',dt2.columns)
#Ans5
dt2=dt2.rename(columns={'Salary':'Salary_emp'})
print(dt2)
#Ans6
print(dt2[dt2['Age']>25])
#Ans7
p=dt2[['Emp_Name','Salary_emp']]
print(p)
#Ans8
d3={
    'Emp_Name':['Mayank',None,'Rohan'],
    'Salary':[20000,None,40000],
    'Emp_id':[100,None,102],
    'Age':[34,None,64]
}
q1=pd.DataFrame(d3)
a1=pd.isnull(q1)
print(a1)
a2=pd.isnull(q1).sum()
print(a2)
#Ans9
w1=q1.dropna(inplace=True)
print(q1)
#Ans10
d11=q1['Salary'].isnull().sum()
print(d11)
#Ans11
data1={
    "Name":["Mayank","Dev","Keshav","Rahul","Mohan","Sohan","Rohan","Jai"],
    "Age":[22,21,34,23,23,55,35,37],
    "Salary":[20000,30000,40000,42000,23000,34000,21000,66000],
    "Performance Score":[80,85,90,92,83,88,81,99]
}
fr=pd.DataFrame(data1)
print(fr)
asq=fr.sort_values(by='Salary',ascending=True,inplace=True)
print(fr)
#Ans12
import pandas as pd
data16 = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'department': ['HR', 'IT', 'HR', 'Finance', 'IT', 'Finance'],
    'salary': [50000, 60000, 52000, 58000, 61000, 57000]
}

df23 = pd.DataFrame(data16)
print(df23)
qw=df23.groupby('department')['salary'].mean()
print(qw.reset_index())
#Ans13
aq=df23.groupby('department')['name'].count()
print(aq)
#Ans14
aq1=df23.groupby('department')['salary'].max()
print(aq1)
#Ans15
data16 = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'department': ['HR', 'IT', 'HR', 'Finance', 'IT', 'Finance'],
    'salary': [50000, 60000, 52000, 58000, 61000, 57000]
}

df23 = pd.DataFrame(data16)
print(df23)
df23['tax']=df23['salary']*0.9
print(df23)
#Ans16
import pandas as pd
df1 = pd.DataFrame({
    'employee_id': [101, 102, 103, 104],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'department': ['HR', 'IT', 'Finance', 'IT']
})
df2 = pd.DataFrame({
    'employee_id': [101, 102, 104, 105],
    'salary': [50000, 60000, 55000, 62000]
})
merge=pd.merge(df1,df2,how='outer')
print(merge)
#Ans17
df1 = pd.DataFrame({
    'employee_id': [101, 102, 103, 104],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'department': ['HR', 'IT', 'Finance', 'IT']
})
df2 = pd.DataFrame({
    'employee_id': [101, 102, 104, 105],
    'salary': [50000, 60000, 55000, 62000]
})
cocat=pd.concat([df1,df2],axis=0).reset_index(drop=True)
print(cocat)
#Ans18
def bonus(a):
    return df2['salary']*0.1
aw=bonus(df2['salary'])
df2['Bonus']=aw
print(df2)
#Ans19
import pandas as pd
df = pd.DataFrame({
    'employee': ['Alice', 'Bob', 'Charlie'],
    'joining_date': ['2021-05-10', '2022-01-15', '2020-07-22']
})

df['joining_date'] = pd.to_datetime(df['joining_date'])
df['year_joined'] = df['joining_date'].dt.year
print(df)
#ans20
df1 = pd.DataFrame({
    'employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'department': ['HR', 'IT', 'HR', 'Finance', 'IT'],
    'gender': ['F', 'M', 'M', 'M', 'F'],
    'salary': [50000, 60000, 52000, 58000, 61000]
})
pivot = pd.pivot_table(df1,values='salary',index='department',columns='gender',aggfunc='mean')
print(pivot)
#Ans21
a=df1.columns
lt=(a.str.upper())
print(lt.str.lower())
#Ans22
import numpy as np
df1['salary_level']=np.where(df1['salary']>55000,'High','Normal')
print(df1)
#Ans23
df_unique = df1.drop_duplicates(subset='employee', keep='first')
print(df_unique)
#ans24
df3 = pd.DataFrame({
    'employee': ['Alice', 'Bob', 'Charlie', 'David'],
    'experience': [3, 6, 5, 10]
})
import numpy as np
df3['experience_level'] = np.where(df3['experience'] > 5, 'Senior', 'Junior')
#ans25
df4 = pd.DataFrame({
    'employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
    'salary': [60000, 50000, 70000, 55000, 52000]
})
df_sorted = df4.sort_values(by=['department', 'salary'], ascending=[True, False])
print(df_sorted)
