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
