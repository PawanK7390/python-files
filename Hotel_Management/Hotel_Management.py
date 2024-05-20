def main():
    c = 'y'
    while c == 'y':
        loginwindow = input("TO Login as USER (Enter U)\nTO Login as ADMIN (Enter A) \n: ").upper()
        print()
        if loginwindow == "A":
            adminwindow()
        elif loginwindow == "U":
            program()
        else:
            print("Invalid Input")
            exit()
    else:
        print('wrong input')


def program():
    cont = "y"
    if cont == "y":
        def Hotel_Management():
            import mysql.connector
            hm = mysql.connector.connect(host="localhost", user="root", passwd='abc@123', database="hm")
            print("Welcome to Hotel Transylvania!")

            sql_select_query = 'select * from hm'
            cursor = hm.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            book_condition = 10 - cursor.rowcount

            if book_condition != 0:
                print(
                    "Human-free since 1898.,\nYour safest destination."
                    "We have 10 luxurious Room for your stay\n")

                print("Please Enter necessary details for booking a room \n")
                g = str(input("Name :  "))
                p = str(input("Mobile : "))
                m = str(input("Address : "))
                gr = str(input("Email : "))
                cursor = hm.cursor()
                cursor.execute(f'insert into hm values("{p}","{g}","{m}","{gr}");')
                hm.commit()
                print("Room Booked!!")
                print("Enjoy your Stay!")
            else:
                print()
                print("Sorry for the inconvenience, All rooms are booked!")
                exit()

        print(Hotel_Management())
    rerun = input("\nDo you want run the program again \nIf yes then type y \nElse enter anything\n: ").lower()
    print()
    if rerun == 'y':
        main()
        print()
    else:
        print("I wish you have a Good Day!!")
        exit()


def adminwindow():
    loginid = "Hm"
    password = "****"
    lid = input("Enter LoginID : ")
    passwd = input("Enter Password : ")

    if lid == loginid and passwd == password:
        print("Access Granted!!\n")
        print("1. Add Record")
        print("2. Delete record")
        print("3. Show records")
        print("4. Update records")
        print("5. Number of rooms Left")
        print("6. Exit")
        print()
        choice = int(input("Enter choice : "))
        if choice == 1:
            adddata()
        elif choice == 2:
            deldata()
        elif choice == 3:
            fetchdata()
        elif choice == 4:
            print("What do you want to Update ?\n")
            print("1. Name")
            print("2. Mobile")
            print("3. Address")
            print("4. Email")
            choice = int(input("Enter Choice : "))
            if choice == 1:
                update_name()
            elif choice == 2:
                update_Mobile()
            elif choice == 3:
                update_Address()
            elif choice == 4:
                update_Email()
            else:
                print("wrong input")
        elif choice == 5:
            rooms_left()
            print()
        elif choice == 6:
            print("Exiting")
            exit()

        else:
            print("wrong input")
    else:
        print("Exiting")
        exit()


def adddata():
    import mysql.connector
    hm = mysql.connector.connect(host="localhost", user="root", passwd='abc@123', database="hm")
    g = str(input("Name :  "))
    p = str(input("Mobile : "))
    m = str(input("Address : "))
    gr = str(input("Email : "))
    cursor = hm.cursor()
    cursor.execute(f'insert into hm values("{p}","{g}","{m}","{gr}");')
    hm.commit()
    print("records added")

    r1 = input("Do you want to ADD more records : ")
    if r1 == "y":
        adddata()

    print()
    ad1 = input("Do you want to return to Admin Window : ")
    if ad1 == "y":
        adminwindow()
    else:
        exit()


def deldata():
    import mysql.connector
    hm = mysql.connector.connect(host="localhost", user="root", passwd='abc@123', database="hm")
    gr = str(input("Email :  "))
    cursor = hm.cursor()
    cursor.execute(f'delete from hm where Email="{gr}"')
    hm.commit()
    print("records deleted")
    r2 = input("Do you want to DELETE more records : ")
    if r2 == "y":
        deldata()

    print()
    ad2 = input("Do you want to return to Admin Window : ")
    if ad2 == "y":
        adminwindow()
    else:
        exit()


def fetchdata():
    import mysql.connector
    from mysql.connector import Error

    try:
        hm = mysql.connector.connect(host='localhost',
                                        database='hm',
                                        user='root',
                                        password='abc@123')

        sql_select_query = "select * from hm"
        cursor = hm.cursor()
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        print("Total number of rows in database is : ", cursor.rowcount)

        print("\nPrinting each record")
        for row in records:
            print("Mobile = ", row[0], )
            print("Name = ", row[1])
            print("Address = ", row[2])
            print("Email  = ", row[3],"\n")
    except Error as e:
        print("Error reading data from MySQL table", e)

    print()
    ad13 = input("Do you want to return to Admin Window : ")
    if ad13 == "y":
        adminwindow()
    else:
        exit()


def update_name():
    import mysql.connector
    hm = mysql.connector.connect(host="localhost", user="root", passwd='abc@123', database="hm")
    g = str(input("Email :  "))
    g1 = str(input("New Name : "))
    cursor = hm.cursor()
    cursor.execute(f'update hm set Name="{g1}" where Email="{g}"')
    hm.commit()
    print("records updated")
    print()
    r3 = input("Do you want to UPDATE more Name's : ")
    if r3 == "y":
        update_name()

    print()
    ad23 = input("Do you want to return to Admin Window : ")
    if ad23 == "y":
        adminwindow()
    else:
        exit()


def update_Mobile():
    import mysql.connector
    hm = mysql.connector.connect(host="localhost", user="root", passwd='abc@123', database="hm")
    g = str(input("Email :  "))
    p1 = int(input("New Mobile Number:"))
    cursor = hm.cursor()
    cursor.execute(f'update pcgbm set Mobile="{p1}" where Email="{g}"')
    hm.commit()
    print("records updated")

    r4 = input("Do you want to UPDATE Number of more records : ")
    if r4 == "y":
        update_Mobile()

    print()
    a1d2 = input("Do you want to return to Admin Window : ")
    if a1d2 == "y":
        adminwindow()
    else:
        exit()


def update_Address():
    import mysql.connector
    hm = mysql.connector.connect(host="localhost", user="root", passwd='abc@123', database="hm")
    g = str(input("Mobile :  "))
    gr1 = str(input("New Address : "))
    cursor = hm.cursor()
    cursor.execute(f'update hm set Address="{gr1}" where Mobile="{g}"')
    hm.commit()
    print("records updated")

    r5 = input("Do you want to UPDATE Address of more Records : ")
    if r5 == "y":
        update_Address()

    print()
    a2d2 = input("Do you want to return to Admin Window : ")
    if a2d2 == "y":
        adminwindow()
    else:
        exit()


def update_Email():
    import mysql.connector
    hm = mysql.connector.connect(host="localhost", user="root", passwd='abc@123', database="hm")
    g = str(input("Mobile :  "))
    m1 = str(input("New Email:"))
    cursor = hm.cursor()
    cursor.execute(f'update hm set Email="{m1}" where Mobile="{g}"')
    hm.commit()
    print("records updated")

    r6 = input("Do you want to UPDATE Email of more Clients : ")
    if r6 == "y":
        update_Email()

    print()
    a3d2 = input("Do you want to return to Admin Window : ")
    if a3d2 == "y":
        adminwindow()
    else:
        exit()


def rooms_left():
    import mysql.connector
    from mysql.connector import Error

    try:
        hm = mysql.connector.connect(host='localhost',
                                        database='hm',
                                        user='root',
                                        password='abc@123')

        sql_select_query = "select * from hm"
        cursor = hm.cursor()
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        print("Total number of Rooms Left is : ", 10 - cursor.rowcount)

        print()
        a34d2 = input("Do you want to return to Admin Window : ")
        if a34d2 == "y":
            adminwindow()
        else:
            exit()


    except Error as e:
        print("Error reading data from MySQL table", e)


main()
