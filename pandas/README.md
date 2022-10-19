<img src="https://i.ibb.co/M6nBBb0/mascote.png" align="right" width="130">

# Python

## Pandas

#### _Let's Code!_

- Como excluir linhas com base em valores de coluna
    - Excluir linhas com base em vários valores de coluna.
    - Excluir linhas com base no inverso dos valores das colunas.
- Selecionar linhas usando **múltiplas de condições** em valores nas colunas.
- Trabalhando com **datas**.
- Lendo arquivo Excel `.xlsx`
- [`drop_duplicates` Excluir linhas duplicadas.](https://github.com/JoseMateusCamargo/python/blob/main/pandas/how_to_drop_duplicate_rows.py)
- [Selecionando linhas duplicadas.](https://github.com/JoseMateusCamargo/python/blob/main/pandas/get_list_all_duplicate_row.py)

---

**Como excluir linhas com base em valores de coluna**

```python
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
```

**Selecionar linhas usando múltiplas de condições em valores nas colunas**

```python
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
```

```python
import pandas as pd

data = {
    'data1': ['20191009', '20190910', '20211001'],
    'data2': ['01-07-2019', '10-09-2019', '01-10-2021'],
    'data3': ['01jul2021', '10sep2019', '01jan2021'],
    'data4': [20191008, 20210910, 20001001]
}

df = pd.DataFrame(data, columns=['data1', 'data2', 'data3', 'data4'])

df['data_1'] = pd.to_datetime(df['data1'], format='%Y%m%d')
df['data_2'] = pd.to_datetime(df['data2'], format='%d-%m-%Y')
df['data_3'] = pd.to_datetime(df['data3'], format='%d%b%Y')
df['data_4'] = pd.to_datetime(df['data4'], format='%Y%m%d')

# Get month and year
df['month'] = pd.DatetimeIndex(df['data1']).month
df['year'] = pd.DatetimeIndex(df['data2']).year

# Return year and month
# Documentation: https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_period.html#
df['year_month'] = pd.to_datetime(df['data_3']).dt.to_period('M')

print(df)
```

**Lendo arquivo Excel `.xlsx`**

```Python
df = pd.DataFrame(pd.read_excel(r"C:/Users/jleva/Downloads/acesso hv.xlsx"))
df.head(5)
```

---

Utilidade publica




