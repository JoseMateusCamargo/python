import pandas as pd

technologies = {
    'Courses': ["Spark", "PySpark", "Python", "pandas", "Python", "Spark", "pandas"],
    'Fee': [20000, 25000, 22000, 30000, 22000, 20000, 30000],
    'Duration': ['30days', '40days', '35days', '50days', '35days', '30days', '50days'],
    'Discount': [1000, 2300, 1200, 2000, 1200, 1000, 2000]
}

df = pd.DataFrame(technologies)
print(df)

# Keep first duplicate row
df2 = df.drop_duplicates()
print(df2)

# Using DataFrame.drop_duplicates() to keep first duplicate row
df2 = df.drop_duplicates(keep='first')
print(df2)

# Keep last duplicate row
df2 = df.drop_duplicates(keep='last')
print(df2)

# Remove all duplicate rows
df2 = df.drop_duplicates(keep=False)
print(df2)

# Delete duplicate rows based on specific columns
df2 = df.drop_duplicates(subset=["Courses", "Fee"], keep=False)
print(df2)

# Drop duplicate rows in place
df.drop_duplicates(inplace=True)
print(df)

# Using DataFrame.apply() and lambda function
df2 = df.apply(lambda x: x.astype(str).str.lower()).drop_duplicates(subset=['Courses', 'Fee'], keep='first')
print(df2)

"""
Abaixo está a sintaxe da DataFrame.drop_duplicates() função que remove linhas duplicadas do DataFrame pandas.

# Syntax of drop_duplicates
DataFrame.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)

subset – Rótulo da coluna ou sequência de rótulos. Seu valor padrão é nenhum. Depois de passar as colunas, considere a 
identificação de linhas duplicadas.

keep – Os valores permitidos são {'first', 'last', False}, padrão 'first'.
    1° ‘first’ – Linhas duplicadas, exceto a primeira é descartada.
    2° ‘last' – Linhas duplicadas, exceto a última que é descartada.
    3° False – Todas as linhas duplicadas são descartadas.

inplace– Valor booleano. remove linhas com duplicatas no DataFrame existente quando é True. Por padrão Falso.

ignore_index– Valor booleano, por padrão False.
"""
