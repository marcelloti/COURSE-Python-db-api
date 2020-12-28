import MySQLdb
from MySQLdb import connect

host = "127.0.0.1"
port = 3306
user = "root"
password = "root"
database = "default"

# PEP 249
db = connect(
    host=host, port=port, user=user, passwd=password, db=database, autocommit=True
)
print("Successful connection")

cursor = db.cursor()
row_affected = cursor.execute("SELECT * FROM bank_accounts")
print("Rows affected - Method 1: " + str(row_affected))
row_affected = cursor.rowcount
print("Rows affected - Method 2: " + str(row_affected))
# print(row_affected)
# print(list(cursor))

print("---------------------")
print("Fetch all")
print("---------------------")
rows = cursor.fetchall()

print("---------------------")
print("Method 1")
print("---------------------")
for row in rows:
    print(row)

print("---------------------")
print("Method 2")
print("---------------------")
for row in cursor:
    print(row)

print("---------------------")
print("Method 3")
print("---------------------")
cursor.execute("SELECT * FROM bank_accounts")
row = cursor.fetchone()
while row is not None:
    print(row)
    row = cursor.fetchone()

print("")
print("")
print("---------------------")
print("Fetch many")
print("---------------------")
cursor.execute("SELECT * FROM bank_accounts")
rows = cursor.fetchmany(2)
print(rows)
rest = cursor.fetchall()
print("---------------------")
print("Rest of rows")
print("---------------------")
print(rest)

print("---------------------")
print("Insert")
print("---------------------")
# INSERT INTO `bank_accounts` VALUES (1,'0001-01','Fulano da Silva','123456',450.50,0,1),(2,'0002-02','Jane Doe','123456',50.00,0,1),(3,'0003-03','John Doe','123456',70.00,0,2),(4,'1111-11','Admin 1','123456',1000.00,1,3);
cursor.execute(
    """INSERT INTO `bank_accounts` (
        `number`,`name`,`password`,`value`,`admin`,`agency_id`) VALUES (
        '0004-04','Richard Roe','123456', 999.50,0,1
    )"""
)

cursor.executemany(
    """INSERT INTO `bank_accounts` (`number`,`name`,`password`,`value`,`admin`,`agency_id`)
    VALUES (%s,%s,%s,%s,%s,%s)""",
    (
        ("1222-99", "Another John Doe", "123456", 450.00, 0, 1),
        ("2222-99", "Another John Doe 2", "123456", 450.00, 0, 1),
    ),
)
# db.commit()

print("---------------------")
print("Get last inserted ID")
print("---------------------")
print(cursor.lastrowid)


print("---------------------")
print("Disabling auto-commit + Commit + Rollback")
print("---------------------")
db.autocommit(False)
try:
    cursor.execute(
        """INSERT INTO `bank_accounts` (
          `number`,`name`,`password`,`value`,`admin`,`agency_id`) VALUES (
          '0004-04','Richard Roe','123456', 999.50,0,1
      )"""
    )
    db.commit()
except:
    print("Row already exists. Rollback")
    db.rollback()

# Closing connection
db.close()