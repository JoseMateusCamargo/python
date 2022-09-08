import pymysql
import pandas as pd

data = pd.DataFrame({
    'book_id': [12345, 12346, 12347],
    'title': ['Python Programming', 'Learn MySQL', 'Data Science Cookbook'],
    'price': [29, 23, 27]
})

connection = pymysql.connect(host='localhost', user='root', password='12345', db='book')

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
