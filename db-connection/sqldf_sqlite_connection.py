from pandasql import sqldf

query = """SELECT ID, INVENTORY_ID FROM db_cadastro LIMIT 10;"""

df_new = sqldf(query, locals())
