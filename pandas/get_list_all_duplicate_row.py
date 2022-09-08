import pandas as pd

technologies = {
    'Courses': ["Spark", "PySpark", "Python", "pandas", "Python", "Spark", "pandas"],
    'Fee': [20000, 25000, 22000, 30000, 22000, 20000, 30000],
    'Duration': ['30days', '40days', '35days', '50days', '40days', '30days', '50days'],
    'Discount': [1000, 2300, 1200, 2000, 2300, 1000, 2000]
}

df = pd.DataFrame(technologies)
print(df)

# Select duplicate rows except first occurrence based on all columns
df2 = df[df.duplicated()]

# Select duplicate row based on all columns
df2 = df[df.duplicated(keep=False)]
print(df2)

# Get duplicate last rows based on all columns
df2 = df[df.duplicated(keep='last')]
print(df2)

# Get list Of duplicate rows using single columns
df2 = df[df['Courses'].duplicated() == True]
print(df2)

# Get list of duplicate rows based on 'Courses' column
df2 = df[df.duplicated('Courses')]
print(df2)

# Get list Of duplicate rows using multiple columns
df2 = df[df[['Courses', 'Fee', 'Duration']].duplicated() == True]
print(df2)

# Get list of duplicate rows based on list of column names
df2 = df[df.duplicated(['Courses', 'Fee', 'Duration'])]
print(df2)

# Get list Of duplicate rows using sort values
df2 = df[df.duplicated(['Discount']) == True].sort_values('Discount')
print(df2)

# Using sort values
df2 = df[df.Discount.duplicated(keep=False)].sort_values("Discount")
print(df2)
