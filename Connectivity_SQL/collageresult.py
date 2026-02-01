import mysql.connector

print("Program started...")

try:
    print("Trying to connect...")

    conn = mysql.connector.connect(
        host="localhost",  # Force IPv4
        user="root",
        password="Ram@2145",
        database="mall",
        port=3306,
        auth_plugin="mysql_native_password",
        use_pure=True,
        connection_timeout=5
    )

    print("Connection object created")

    if conn.is_connected():
        print("Connected Successfully")
    else:
        print("Not Connected")

    def insert():
        roll_no = eval(input("Enter your rollno. :"))
        name= input("Enter Your name :")
        branch = input("Enter Your Branch :")
        c = eval(input("Enter your marks of C :"))
        cpp = eval(input("Enter your marks of Cpp :"))
        python = eval(input("Enter your marks of python :"))
        total = c+cpp+python
        percentage= total*(100/300)
        cur = conn.cursor()
        sql = "INSERT INTO record (Roll_no,name,branch,c,cpp,python,total,percentage) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (roll_no,name,branch,c,cpp,python,total,percentage)
        cur.execute(sql,values)
        conn.commit()
        print("✅ Data successfully inserted into Products table!")

    insert()
    conn.close()
    print("Connection closed")

except Exception as e:
    print("ERROR:", e)