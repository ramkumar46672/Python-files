import mysql.connector

print("Program started...")

try:
    print("Trying to connect..")

    conn = mysql.connector.connect(
        host="localhost",  # Force IPv4
        user="root",
        password="Enter",
        database="my_database",
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
    cursor = conn.cursor()

    # Database create query
    cursor.execute("CREATE DATABASE mydatabase")


    conn.close()
    print("Connection closed")

except Exception as e:
    print("ERROR:", e)