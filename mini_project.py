import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Employee_Salary_Dataset.csv")
#print(df.head())

#print(df.info())
#print(df.describe())

#KEY INSIGHTS
#Total Employees

#total_emp = df.shape[1]
#print(total_emp)

#Average Salary

#avg_sal = df["Salary"].mean()
#print(avg_sal)

#Highest Salary

#higH_sal = df["Salary"].max()
#print(higH_sal)

#Lowest Salary

#low_sal = df["Salary"].min()
#print(low_sal)

#Average Salary by Gender

#avg_gender = df.groupby("Gender")["Salary"].mean()
#print(avg_gender)

#Average Salary by Experience

#avg_exp = df.groupby("Experience_Years")["Salary"].mean()
#print(avg_exp)

#VISUALIZATION
#Salary by Gender
#avg_gender = df.groupby("Gender")["Salary"].mean().plot(kind="bar")
#plt.title("Salary by Gender")
#plt.xlabel("Gender")
#plt.ylabel("Salary")
#plt.show()


#Experience vs Salary
#plt.scatter(df["Experience_Years"], df["Salary"])
#plt.title("Experience vs Salary")
#plt.xlabel("Experience Years")
#plt.ylabel("Salary")
#plt.show()

#Save Insights

#df.to_csv("cleaned_employee_salary.csv", index=False)


#######OTHERS###########

#import matplotlib.pyplot as plt
#
#groups = df.groupby("Gender")
#
#for gender, data in groups:
#    plt.scatter(data["Experience_Years"], data["Salary"], label=gender)
#
#plt.title("Experience vs Salary by Gender")
#plt.xlabel("Experience Years")
#plt.ylabel("Salary")
#plt.legend()
#plt.show()

import seaborn_practice as sns

sns.scatterplot(data=df, x="Experience_Years", y="Salary", hue="Gender")
plt.show()