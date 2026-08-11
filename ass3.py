# import pandas as pd

# marks = pd.Series([80, 90, 75, 88])
# print(marks)

# question 1
import pandas as pd

data = {
    "Tid": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Refund": ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No"],
    "Marital Status": [
        "Single", "Married", "Single", "Married", "Divorced",
        "Married", "Divorced", "Single", "Married", "Single"
    ],
    "Taxable Income": [
        "125K", "100K", "70K", "120K", "95K",
        "60K", "220K", "85K", "75K", "90K"
    ],
    "Cheat": ["No", "No", "No", "No", "Yes", "No", "No", "Yes", "No", "Yes"]
}
df = pd.DataFrame(data)

# print(df)

# question 2
# print(df.iloc[[0, 4, 7, 8]])


# question 3
# print(df.iloc[3:8])

# 3.2
# print(df.iloc[4:9, 2:5])

# 3.3
# print(df.iloc[:, 1:4])

# question 4

# import pandas as pd

# df = pd.read_csv("Iris.csv")

# print(df.head())

# question 5
# df = pd.read_csv("Iris.csv")

# df = df.drop(index=4)
# df = df.drop(df.columns[3], axis=1)

# print(df)

#question 6
import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": [
        "2020-03-15",
        "2017-07-19",
        "2013-06-01",
        "2021-02-10",
        "2010-11-25"
    ],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5]
}

employees = pd.DataFrame(data)

# print(employees)
employees.to_csv("employees.csv", index=False)
#question 6 a
# print(employees.shape)
#question 6b 
# print(employees.info())
#6c
# print(employees.describe())

#6d
# print(employees.head(5))
# print(employees.tail(3))

#6e 
# average_salary = employees["Salary"].mean()

# print("Average Salary:", average_salary)
#6e2
# total_bonus = employees["Bonus"].sum()

# print("Total Bonus:", total_bonus)

#6e3
# youngest_age = employees["Age"].min()

# print("Youngest Age:", youngest_age)

#6e4
# highest_rating = employees["Rating"].max()

# print("Highest Rating:", highest_rating)

#6e5
sorted_df = employees.sort_values(by="Salary", ascending=False)

print(sorted_df)