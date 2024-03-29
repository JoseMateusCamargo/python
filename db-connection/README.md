<img src="https://i.ibb.co/M6nBBb0/mascote.png" align="right" width="130">

# Python

## Conexões com banco de dados

#### _Let's Code!_

* Conexão MySQL usando `mysql.connector`.
* Inserindo dados `DataFrame` em MySQL usando `mysql.connector`.
* Conexão MySQL usando `pymysql`.
* Conexão SQLite usando `sqldf`.

---

**Conexão MySQL usando `mysql.connector`**

```python
import mysql.connector
from mysql.connector import Error

query = """SELECT ID, INVENTORY_ID FROM db_cadastro LIMIT 10;"""

try:

    config = {'user': 'root', 'password': '123123', 'host': '127.0.0.1', 'database': 'data_base_name',
              'raise_on_warnings': True}

    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)

        cursor = connection.cursor()
        cursor.execute(query)

        for (id_, inventory) in cursor:
            print("{}, {}".format(id_, inventory))

        cursor.execute("select database();")
        record = cursor.fetchone()
        print("\nYou're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
```

**Inserindo dados `DataFrame` em MySQL usando `mysql.connector`**

```python
import pymysql
import pandas as pd

data = pd.DataFrame({
    'book_id': [12345, 12346, 12347],
    'title': ['Python Programming', 'Learn MySQL', 'Data Science Cookbook'],
    'price': [29, 23, 27]
})

connection = pymysql.connect(host='localhost', user='root', password='123123', db='data_base_name')

# Crie um cursor usando a função cursor(). Isso nos permitirá executar a consulta SQL depois de escrevê-la.
cursor = connection.cursor()

# Criando lista atraves das colunas
cols = "`,`".join([str(i) for i in data.columns.tolist()])

# Inserindo dados.
for i, row in data.iterrows():
    sql = "INSERT INTO `book_details` (`" + cols + "`) VALUES (" + "%s," * (len(row) - 1) + "%s)"
    cursor.execute(sql, tuple(row))

    # A conexão não é confirmada automaticamente por padrão. Portanto, devemos nos comprometer a salvar nossas alterações.
    connection.commit()

connection.close()
```

**Conexão MySQL usando `pymysql`**

```python
import pymysql

try:
    connection = pymysql.connect(host='localhost', user='root', password='123123', db='data_base_name')

    # Crie um cursor usando a função cursor(). Isso nos permitirá executar a consulta SQL depois de escrevê-la.
    cursor = connection.cursor()

    sql = "INSERT INTO `employee` (`EmployeeID`, `Ename`, `DeptID`, `Salary`, `Dname`, `Dlocation`) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (1009, 'Morgan', 1, 4000, 'HR', 'Mumbai'))

    # A conexão não é confirmada automaticamente por padrão. Portanto, devemos nos comprometer a salvar nossas alterações.
    connection.commit()

    sql = "SELECT * FROM `employee`"
    cursor.execute(sql)
    result = cursor.fetchall()

    for i in result:
        print(i)

except Error as e:
    print(e)

finally:
    connection.close()
```

**Conexão SQLite usando `sqldf`**

```python
from pandasql import sqldf

query = """SELECT ID, INVENTORY_ID FROM db_cadastro LIMIT 10;"""

df_new = sqldf(query, locals())
```