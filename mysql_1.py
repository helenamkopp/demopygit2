import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python_helena"
)

cursor = banco.cursor()

# o banco de dados sempre vai atualizando as informações (se eu excluir a linha de código, continua salvo no database)

comando_SQL = "DELETE FROM pessoas WHERE idade = 15"
cursor.execute(comando_SQL)

banco.commit()
