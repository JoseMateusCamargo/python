# How to drop rows based on column values using Pandas Dataframe
import pandas as pd

# List of Tuples
students = [('user 1', 'car', 2),
            ('user 2', 'house', 1),
            ('user 3', 'others', 3),
            ('user 4', 'car', 2),
            ('user 5', 'house', 1)]

df = pd.DataFrame(students, columns=['name', 'item', 'value'])
print(df)

df_method1 = df
df_method2 = df

# Method #1: Delete rows based on multiple column values ----------------------#
# Get indexes where name column has value john and value column equals to 0.0
indexNames = df_method1[(df_method1['name'] == 'user 1') & (df_method1['value'] == 2)].index
df_method1.drop(indexNames, inplace=True)  # Delete these row indexes from dataFrame
print(f'\n {df_method1}')

# Method #2: Delete rows based on inverse of column values --------------------#
# Get indexes where name column doesn't have value john
indexNames2 = df_method2[~(df_method2['name'] == 'user 4')].index
df_method2.drop(indexNames2, inplace=True)  # Delete these row indexes from dataFrame
print(f'\n{df_method2}')
