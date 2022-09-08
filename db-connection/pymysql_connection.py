import pymysql

try:
    connection = pymysql.connect(host='localhost', user='root', password='12345', db='employee')

    # Crie um cursor usando a função cursor(). Isso nos permitirá executar a consulta SQL depois de escrevê-la.
    cursor = connection.cursor()

    sql = "INSERT INTO `employee` (`EmployeeID`, `Ename`, `DeptID`, `Salary`, `Dname`, `Dlocation`) " \
          "VALUES (%s, %s, %s, %s, %s, %s)"
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
