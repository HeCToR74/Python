import psycopg2

conn = psycopg2.connect(dbname='Demo1',user='postgres',password='postgres',host='localhost',port='5433')
cursor = conn.cursor()

# table Steps
'''
file = open('steps.txt', 'r')
for row in file:
	cursor.execute(""" INSERT INTO "Steps" (step_name) VALUES ('""" + row.replace('\n','').replace("'","''") + """') """)
	conn.commit()
file.close()

cursor.execute("""SELECT * FROM "Steps" """)
for row in cursor:
	print(row)
'''

# table Courstitles
'''
row = 'WebUI_Python'
cursor.execute(""" INSERT INTO "Courstitles" (cours_name) VALUES ('""" + row.replace('\n','').replace("'","''") + """') """)
conn.commit()

cursor.execute("""SELECT * FROM "Courstitles" """)
for row in cursor:
	print(row)
'''

# table Roles

row1 = 'User'
row2 = 'Admin'
cursor.execute(""" INSERT INTO "Roles" (name) VALUES ('""" + row1 + """') """)
conn.commit()
cursor.execute(""" INSERT INTO "Roles" (name) VALUES ('""" + row2 + """') """)
conn.commit()

cursor.execute("""SELECT * FROM "Roles" """)
for row in cursor:
	print(row)

cursor.close()
conn.close()
