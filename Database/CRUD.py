import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user='root',
    password='root',
    port='3306',
    database='python_mysql'
)

cursor = db.cursor()
#cursor.execute('INSERT INTO users(id,userName,password)VALUES(4,"Vinay","VINAY23")')
#db.commit()

# cursor.execute("select * from users")
# users = cursor.fetchall()
# for user in users:
#     print(user)

# q2 = "create table scores (userId int primary key, foreign key(userId) references users(id),  game1 int default 0, game2 int default 0)"
#cursor.execute(q2)
# db.commit()

cursor.execute("show tables")

for x in cursor:
    print(x)