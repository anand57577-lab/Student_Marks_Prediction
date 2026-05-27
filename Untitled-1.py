# %%
import pandas as pd

# %%
data = pd.read_csv('Final_Marks_Data.csv')
df = pd.DataFrame(data)




# %%
df.loc[23]

# %%
df.describe()

# %%
df.info()

# %%
#finding Null Values count
df.isna().sum()

# %%
# finding the duplicates
df.duplicated().sum()

# %%
#feature engineering
# finding the most important features using filter method

df = df.drop('Student_ID', axis=1)

# %%
df.head()

# %%
print(df.columns)

# %%
correlation = df.corr()['Final Exam Marks (out of 100)']
correlation

# %%
absoluate = correlation.abs()
sorted_values = absoluate.sort_values(ascending=False)
sorted_values

# %%
df.rename(columns = {'Internal Test 1 (out of 40)': 'Sessional_1', 'Internal Test 2 (out of 40)': 'Sessional_2', 'Assignment Score (out of 10)  ': 'Assignment_score','Final Exam Marks (out of 100)':'target'}, inplace = True)

# %%
print(df.columns)

# %%
#Train and test Split
from sklearn.model_selection import train_test_split
x = df.drop('target', axis = 1)
y = df['target']


# %%
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size = 0.3, random_state = 42)

len(y_train), len(y_test)

# %%
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)


# %%
prediction = model.predict(x_test)

# %%
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
mae = mean_absolute_error(y_test, prediction)
mse = mean_squared_error(y_test, prediction)
r2 = r2_score(y_test, prediction)

print(mae)
print(mse)
print(r2)



# %%
Attendance = 80 
Sessional_1 = 45
Sessional_2 = 50
Assignment_score =15 
Dail_study_hours = 3
user_data = [[Attendance, Sessional_1, Sessional_2, Assignment_score, Dail_study_hours]]
predicted_marks = model.predict(user_data)
print(predicted_marks)


