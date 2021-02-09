import mysql.connector
mydb = mysql.connector.connect(
        host="HOST",
        database="DATABASE",
        user="USER",
        password="PASSWORD"
)

mycursor = mydb.cursor()

sql = "SELECT CODE from data WHERE SESSION = 'Basic Select' AND QUESTION = 'Query NAME, COUNTRY GREATER 4000'"
mycursor.execute(sql)

result = mycursor.fetchone()
print(result)