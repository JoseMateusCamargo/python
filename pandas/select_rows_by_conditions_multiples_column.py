import pandas as pd

# List of Tuples
students = [('user 1', 'car', 2),
            ('user 2', 'house', 1),
            ('user 3', 'others', 3),
            ('user 4', 'car', 2),
            ('user 5', 'house', 1)]

# Create a DataFrame object
dfObj = pd.DataFrame(students, columns=['user', 'item', 'price'])

print("Original Dataframe", dfObj, sep='\n')

print(f'\nSelect Rows based on value in column')
first_select = dfObj[dfObj['item'] == 'car']
print('1º Select table: ', first_select.head(5), sep='\n')

print(f'\nSelect Rows based on any of the multiple values in column')
second_select = dfObj[dfObj['item'].isin(['house', 'others'])]
print('2º Select table: ', second_select.head(5), sep='\n')

print(f'\nSelect DataFrame Rows Based on multiple conditions on columns')
third_select = dfObj[(dfObj['price'] > 1) & (dfObj['price'] < 3)]
print('3º Select table: ', third_select.head(5), sep='\n')
