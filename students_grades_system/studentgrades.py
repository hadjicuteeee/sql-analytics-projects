import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="hadjilover911",
    database="dbstudents"
)
cursor = conn.cursor()
while True:
    first_name = input("Enter student name: ")
    last_name = input("Enter student last name : ")
    age = int(input("Enter student age : "))
    course = input("Enter student course: ")
    gwa = float(input("Enter student gwa : "))

    try:
        sql = "INSERT INTO tblstudents (first_name, last_name, age, course, gwa) VALUES (%s, %s, %s, %s, %s)"
        values = (first_name, last_name, age, course, gwa)
        cursor.execute(sql, values)
        conn.commit()
        print("Student was successfully addedd")
    except Exception as e:
        print("Error inserting datas")

    add = input("Want to add more? yes/no : ")
    if add == "no":
        print("Thank you for using this system!")
        exit()


        cursor.close()
        conn.close()























