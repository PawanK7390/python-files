def main():
    c = 'y'
    while c == 'y':
        loginwindow = input("TO Login as USER (Enter U)\nTO Login as ADMIN(Enter A) \n:").upper()
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
        def pcgaming():
            import pandas as pd
            import mysql.connector
            pcgbm = mysql.connector.connect(host="localhost", user="root", passwd='abc@123', database="pcgbm")
            print("\nCan I Run It ?")
            print(
                "System requirement application to find games that can run on your computer,\nAnd to ptovide you with Game Price, "
                "Price of the PC(Based upon the configuration provided by you + other important parts required to build the PC)\n"
                "What games your laptop/PC can run - from our list of over 70 PC games. \n")
            print("Tell us about your PC specification from the following option's\n ")
            graphics = (input("Choose from the folLowing GRAPHICS CARD\n"
                              "   Geforce GTX 1050 Ti (ENTER g1)\n "
                              "  Geforce GTX 1060    (ENTER g2)\n "
                              "  Geforce GTX 1070 Ti (ENTER g3)\n "
                              " :  ")).lower()
            print()
            g1 = "Geforce GTX 1050 Ti"
            g2 = "Geforce GTX 1060"
            g3 = "Geforce GTX 1070 Ti"
            if graphics == "g1":
                g = g1
            elif graphics == "g2":
                g = g2
            elif graphics == "g3":
                g = g3
            else:
                return "ERROR"
            processor = (input("Choose from the folLowing PROCESSOR\n"
                               "  Intel core i3 (ENTER p1)\n "
                               " Intel core i5 (ENTER p2)\n "
                               " Intel core i7 (ENTER p3)\n "
                               " :  ")).lower()
            print()
            p1 = "i3"
            p2 = "i5"
            p3 = "i7"
            if processor == "p1":
                p = p1
            elif processor == "p2":
                p = p2
            elif processor == "p3":
                p = p3
            else:
                return "ERROR"
            memory = (input("Choose from the folLowing MEMORY\n"
                            " 4GB RAM (ENTER r1)\n"
                            " 8GB RAM (ENTER r2)\n"
                            "16GB RAM (ENTER r3)\n"
                            " :  ")).lower()
            r1 = "4GB"
            r2 = "8GB"
            r3 = "16GB"
            if memory == "r1":
                r = r1
            elif memory == "r2":
                r = r2
            elif memory == "r3":
                r = r3
            else:
                return "ERROR"
            cursor = pcgbm.cursor()
            cursor.execute(
                f'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="{p}" and graphics="{g}" and memory="{r}"')
            myresult = cursor.fetchall()
            data = pd.DataFrame(myresult, columns=['Game Name', 'Storage(GB)', 'Price($)', 'ReviewScore(out of 100)',
                                                   'PCprice(Rs)'])
            pd.set_option('display.max_rows' and 'display.max_columns', None)
            for row in range(len(data)):
                print()
                print(data.loc[row])
            import matplotlib.pyplot as mat

            def mypie1():
                label1 = ['Geforce GTX 1050 Ti', 'Geforce GTX 1060', 'Geforce GTX 1070 Ti']
                # labels=list(label1)
                sizes = [23, 27, 21]
                print(sizes)
                colors1 = ['yellowgreen', 'lightskyblue', 'magenta']
                # SPLIT_OF_GRAPH=(0,0,0,0,0.1,0,0,0,0)
                mat.title("Games in PCGBM for various Graphics card")
                mat.pie(sizes, explode=None, labels=label1, colors=colors1, shadow=True, autopct='%1.1f%%',
                        startangle=140)
                mat.axis('equal')
                a = mat.show()
                print(a)

            def mypie2():
                label1 = ['i3', 'i5', 'i7']
                # labels=list(label1)
                sizes = [25, 22, 24]
                print(sizes)
                colors1 = ['red', 'blue', 'magenta']
                # SPLIT_OF_GRAPH=(0,0,0,0,0.1,0,0,0,0)
                mat.title("Games in PCGBM for various Processors")
                mat.pie(sizes, explode=None, labels=label1, colors=colors1, shadow=True, autopct='%1.1f%%',
                        startangle=140)
                mat.axis('equal')
                b = mat.show()
                print(b)

            def mypie3():
                label1 = ['4GB', '8GB', '16GB']
                # labels=list(label1)
                sizes = [24, 19, 28]
                print(sizes)
                colors1 = ['lightskyblue', 'yellowgreen', 'brown']
                # SPLIT_OF_GRAPH=(0,0,0,0,0.1,0,0,0,0)
                mat.title("Games in PCGBM for various RAM")
                mat.pie(sizes, explode=None, labels=label1, colors=colors1, shadow=True, autopct='%1.1f%%',
                        startangle=140)
                mat.axis('equal')
                c = mat.show()
                print(c)

            def mypie4():
                label1 = ['Free', '1 to 20', '$21 to $40', '$41 to $60', '$61 to $100']
                # labels=list(label1)
                sizes = [14, 22, 20, 12, 3]
                print(sizes)
                colors1 = ['red', 'blue', 'magenta', 'yellowgreen', 'brown']
                # SPLIT_OF_GRAPH=(0,0,0,0,0.1,0,0,0,0)
                mat.title("Games in PCGBM for various prices($)\n")
                mat.pie(sizes, explode=None, labels=label1, colors=colors1, shadow=True, autopct='%1.1f%%',
                        startangle=140)
                mat.axis('equal')
                d = mat.show()
                print(d)

            def mypie5():
                label1 = ['40 to 60', '61 to 80', '81 to 100']
                # labels=list(label1)
                sizes = [3, 19, 48]
                print(sizes)
                colors1 = ['red', 'blue', 'cyan', ]
                # SPLIT_OF_GRAPH=(0,0,0,0,0.1,0,0,0,0)
                mat.title("Games in PCGBM for various Review Score out of 100\n")
                mat.pie(sizes, explode=None, labels=label1, colors=colors1, shadow=True, autopct='%1.1f%%',
                        startangle=140)
                mat.axis('equal')
                d = mat.show()
                print(d)

            def bar1():
                import numpy as np
                import matplotlib.pyplot as mat15
                objects = ('Geforce GTX 1050 Ti', 'Geforce GTX 1060', 'Geforce GTX 1070 Ti')
                y_pos = np.arange(len(objects))
                types = (23, 27, 21)
                mat15.bar(y_pos, types, align='center', color='yellowgreen')
                mat15.xticks(y_pos, objects)
                mat15.ylabel('Number Of Games')
                mat15.title('Number Of Games According to Graphics Card')
                mat15.show()

            def bar2():
                import numpy as np
                import matplotlib.pyplot as mat14
                objects = ('i3', 'i5', 'i7')
                y_pos = np.arange(len(objects))
                types = (25, 22, 24)
                mat14.bar(y_pos, types, align='center', color='lightgreen')
                mat14.xticks(y_pos, objects)
                mat14.ylabel('Number Of Games')
                mat14.title('Number Of Games According to processor')
                mat14.show()

            def bar3():
                import numpy as np
                import matplotlib.pyplot as mat13
                objects = ('4GB', '8GB', '16GB')
                y_pos = np.arange(len(objects))
                types = (24, 19, 28)
                mat13.bar(y_pos, types, align='center', color='lightskyblue')
                mat13.xticks(y_pos, objects)
                mat13.ylabel('Number Of Games')
                mat13.title('Number Of Games According to RAM')
                mat13.show()

            def bar4():
                import numpy as np
                import matplotlib.pyplot as mat12
                objects = ('Free', '1 to 20', '$21 to $40', '$41 to $60', '$61 to $100')
                y_pos = np.arange(len(objects))
                types = (14, 22, 20, 12, 3)
                mat12.bar(y_pos, types, align='center', color='brown')
                mat12.xticks(y_pos, objects)
                mat12.ylabel('Number Of Games')
                mat12.title('Number Of Games According to Various prices($)')
                mat12.show()

            def bar5():
                import numpy as np
                import matplotlib.pyplot as mat11
                objects = ('40 to 60', '61 to 80', '81 to 100')
                y_pos = np.arange(len(objects))
                types = (3, 19, 48)
                mat11.bar(y_pos, types, align='center', color='magenta')
                mat11.xticks(y_pos, objects)
                mat11.ylabel('Number Of Games')
                mat11.title('Number Of Games According to Various review score(out of 100)')
                mat11.show()

            def line1():
                label1 = ['Geforce GTX 1050 Ti', 'Geforce GTX 1060', 'Geforce GTX 1070 Ti']
                sizes = [23, 27, 21]
                import matplotlib.pyplot as mat10
                mat10.plot(label1, sizes)
                mat10.title("Games in PCGBM for various Graphics card")
                mat10.xlabel('Graphics card')
                mat10.ylabel('No. Of Games')
                mat10.show()

            def line2():
                label1 = ['i3', 'i5', 'i7']
                sizes = [25, 22, 24]
                import matplotlib.pyplot as mat9
                mat9.plot(label1, sizes)
                mat9.title("Games in PCGBM for various Processors")
                mat9.xlabel('Processors')
                mat9.ylabel('No. Of Games')
                mat9.show()

            def line3():
                label1 = ['4GB', '8GB', '16GB']
                sizes = [24, 19, 28]
                import matplotlib.pyplot as mat8
                mat8.plot(label1, sizes)
                mat8.title("Games in PCGBM for various RAM")
                mat8.xlabel('Ram')
                mat8.ylabel('No. Of Games')
                mat8.show()

            def line4():
                label1 = ['Free', '1 to 20', '$21 to $40', '$41 to $60', '$61 to $100']
                sizes = [14, 22, 20, 12, 3]
                import matplotlib.pyplot as mat7
                mat7.plot(label1, sizes)
                mat7.title("Games in PCGBM for various prices($)\n")
                mat7.xlabel('Prices($)')
                mat7.ylabel('No. Of Games')
                mat7.show()

            def line5():
                label1 = ['40 to 60', '61 to 80', '81 to 100']
                sizes = [3, 19, 48]
                import matplotlib.pyplot as mat6
                mat6.plot(label1, sizes)
                mat6.title("Games in PCGBM for various Review Score out of 100\n")
                mat6.xlabel('Review score')
                mat6.ylabel('No. Of Games')
                mat6.show()

            def scatter1():

                import matplotlib.pyplot as mat5
                label1 = ['Geforce GTX 1050 Ti', 'Geforce GTX 1060', 'Geforce GTX 1070 Ti']
                sizes = [23, 27, 21]
                mat5.scatter(label1, sizes, c="blue")
                mat5.show()

            def scatter2():
                import matplotlib.pyplot as mat4
                label1 = ['i3', 'i5', 'i7']
                sizes = [25, 22, 24]
                mat4.scatter(label1, sizes, c="green")
                mat4.show()

            def scatter3():
                import matplotlib.pyplot as mat3
                label1 = ['4GB', '8GB', '16GB']
                sizes = [24, 19, 28]
                mat3.scatter(label1, sizes, c="green")
                mat3.show()

            def scatter4():
                import matplotlib.pyplot as mat2
                label1 = ['Free', '1 to 20', '$21 to $40', '$41 to $60', '$61 to $100']
                sizes = [14, 22, 20, 12, 3]
                mat2.scatter(label1, sizes, c="green")
                mat2.show()

            def scatter5():
                import matplotlib.pyplot as mat1
                label1 = ['40 to 60', '61 to 80', '81 to 100']
                sizes = [3, 19, 48]
                mat1.scatter(label1, sizes, c="green")
                mat1.show()

            forgraphs = input("IF YOU WANT TO SEE GRAPHS (ENTER Y) : ").lower()
            if forgraphs == "y":
                print('Select the graph you want to see')
                print('1.Pie chart')
                print('2.Bar graph')
                print('3.Line Graph')
                print('4.Scatter plot')
                choice = int(input('Enter choice of graphs : '))
                if choice == 1:
                    print('1.Games in PCGBM for various Graphics card')
                    print('2.Games in PCGBM for various Processors')
                    print('3.Games in PCGBM for various RAM')
                    print('4.Games in PCGBM for various prices($)')
                    print("5.Games in PCGBM for various Review Score out of 100\n")

                    choice1 = int(input('Enter choice of Pie Charts : '))
                    if choice1 == 1:
                        mypie1()
                    elif choice1 == 2:
                        mypie2()
                    elif choice1 == 3:
                        mypie3()
                    elif choice1 == 4:
                        mypie4()
                    elif choice1 == 5:
                        mypie5()
                elif choice == 2:
                    print('1.Number Of Games According to Graphics Card')
                    print('2.Number Of Games According to processor')
                    print('3.Number Of Games According to RAM')
                    print('4.Number Of Games According to Various prices($)')
                    print('5.Number Of Games According to Various review score(out of 100)')
                    choice3 = int(input('Enter the choice of Bar Graphs : '))
                    if choice3 == 1:
                        bar1()
                    elif choice3 == 2:
                        bar2()
                    elif choice3 == 3:
                        bar3()
                    elif choice3 == 4:
                        bar4()
                    elif choice3 == 5:
                        bar5()
                elif choice == 3:
                    print('1.Number Of Games According to Graphics Card')
                    print('2.Number Of Games According to processor')
                    print('3.Number Of Games According to RAM')
                    print('4.Number Of Games According to Various prices($)')
                    print('5.Number Of Games According to Various review score(out of 100)')
                    choice3 = int(input('Enter the choice of Line Graphs : '))
                    if choice3 == 1:
                        line1()
                    elif choice3 == 2:
                        line2()
                    elif choice3 == 3:
                        line3()
                    elif choice3 == 4:
                        line4()
                    elif choice3 == 5:
                        line5()

                if choice == 4:
                    print('1.Games in PCGBM for various Graphics card')
                    print('2.Games in PCGBM for various Processors')
                    print('3.Games in PCGBM for various RAM')
                    print('4.Games in PCGBM for various prices($)')
                    print("5.Games in PCGBM for various Review Score out of 100\n")

                    choice1 = int(input('Enter choice of Pie Charts : '))
                    if choice1 == 1:
                        scatter1()
                    elif choice1 == 2:
                        scatter2()
                    elif choice1 == 3:
                        scatter3()
                    elif choice1 == 4:
                        scatter4()
                    elif choice1 == 5:
                        scatter5()

                else:
                    print("exiting")
            else:
                print("exiting")

        print(pcgaming())
    rerun = input("\nDo you want run the program again \nIf yes then type y \nElse enter anything\n: ").lower()
    print()
    if rerun == 'y':
        main()
        print()
    else:
        print("I wish you have a Good Day!!")
        exit()


def adminwindow():
    loginid = "pcgbm"
    password = "**"
    lid = input("Enter LginID:")
    passwd = input("Enter Password:")
    if lid == loginid and passwd == password:
        print("Access Granted!!\n")
        print("1. Add Record")
        print("2. Delete record")
        print("3. Show records")
        print("4. Update records")
        print("5. Graphs")
        print("6. Exit")
        print()
        choice = int(input("Enter choice:"))
        if choice == 1:
            adddata()
        elif choice == 2:
            deldata()
        elif choice == 3:
            fetchdata()
        elif choice == 6:
            print("Exiting")
            exit()
        elif choice == 5:
            graphs()

        elif choice == 4:
            print("What do you want to Update?:\n")
            print("1. Game name")
            print("2. Processor")
            print("3. Memory")
            print("4. Storage")
            print("5. Price")
            print("6. Review Score")
            print("7. Graphics")
            print("8. PC price")
            choice = int(input("Enter Choice:"))
            if choice == 1:
                updateG_name()
            elif choice == 2:
                updateprocessor()
            elif choice == 3:
                updatememory()
            elif choice == 4:
                updatestorage()
            elif choice == 5:
                updateprice()
            elif choice == 6:
                updateReviewScore()
            elif choice == 7:
                updategraphics()
            elif choice == 8:
                updatePCprice()
            else:
                print("wrong input")

        else:
            print("wrong input")
    else:
        print("Exiting")
        exit()


def adddata():
    import mysql.connector
    pcgbm = mysql.connector.connect(host="localhost", user="root", passwd='abc@123', database="pcgbm")
    g = str(input("game name :  "))
    p = str(input("processor from Intel core i3, Intel core i5 and Intel core i7 : "))
    m = str(input("memory from 4GB, 8GB and 16GB : "))
    gr = str(input("graphics from Geforce GTX 1050 Ti, Geforce GTX 1060 and Geforce GTX 1070 Ti : "))
    s = int(input("storage_GB_ : "))
    pr = int(input("price_$_ : "))
    pl = str(input("platform : "))
    r = str(input("ReviewScore_outof100 : "))
    pc = int(input("PCprice_Rs : "))
    cursor = pcgbm.cursor()
    cursor.execute(f'insert into pcgbm values("{g}","{p}","{m}","{gr}","{s}","{pr}","{pl}","{r}","{pc}");')
    pcgbm.commit()
    print("records added")
    exit()


def deldata():
    import mysql.connector
    pcgbm = mysql.connector.connect(host="localhost", user="root", passwd='abc@123', database="pcgbm")
    g = str(input("game name :  "))
    cursor = pcgbm.cursor()
    cursor.execute(f'delete from pcgbm where G_name="{g}"')
    pcgbm.commit()
    print("records deleted")
    exit()


def fetchdata():
    import mysql.connector
    from mysql.connector import Error

    try:
        pcgbm = mysql.connector.connect(host='localhost',
                                        database='pcgbm',
                                        user='root',
                                        password='abc@123')

        sql_select_query = "select * from pcgbm"
        cursor = pcgbm.cursor()
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        print("Total number of rows in database is : ", cursor.rowcount)

        print("\nPrinting each record")
        for row in records:
            print("G_name = ", row[0], )
            print("processor = ", row[1])
            print("memory = ", row[2])
            print("graphics  = ", row[3])
            print("storage_GB_ = ", row[4])
            print("price_$_ = ", row[5])
            print("platform = ", row[6])
            print("ReviewScore_outof100 = ", row[7])
            print("PCprice_Rs = ", row[8], "\n")
    except Error as e:
        print("Error reading data from MySQL table", e)
    exit()


def updateG_name():
    import mysql.connector
    pcgbm = mysql.connector.connect(host="localhost", user="root", passwd='abc@123', database="pcgbm")
    g = str(input("game name :  "))
    g1 = str(input("New Game Name:"))
    cursor = pcgbm.cursor()
    cursor.execute(f'update pcgbm set G_name="{g1}" where G_name="{g}"')
    pcgbm.commit()
    print("records updated")

    exit()


def updateprocessor():
    import mysql.connector
    pcgbm = mysql.connector.connect(host="localhost", user="root", passwd='abc@123', database="pcgbm")
    g = str(input("game name :  "))
    p1 = str(input("New processor:"))
    cursor = pcgbm.cursor()
    cursor.execute(f'update pcgbm set processor="{p1}" where G_name="{g}"')
    pcgbm.commit()
    print("records updated")

    exit()


def updategraphics():
    import mysql.connector
    pcgbm = mysql.connector.connect(host="localhost", user="root", passwd='abc@123', database="pcgbm")
    g = str(input("game name :  "))
    gr1 = str(input("New graphics:"))
    cursor = pcgbm.cursor()
    cursor.execute(f'update pcgbm set graphics="{gr1}" where G_name="{g}"')
    pcgbm.commit()
    print("records updated")

    exit()


def updatememory():
    import mysql.connector
    pcgbm = mysql.connector.connect(host="localhost", user="root", passwd='abc@123', database="pcgbm")
    g = str(input("game name :  "))
    m1 = str(input("New memory:"))
    cursor = pcgbm.cursor()
    cursor.execute(f'update pcgbm set memory="{m1}" where G_name="{g}"')
    pcgbm.commit()
    print("records updated")

    exit()


def updatestorage():
    import mysql.connector
    pcgbm = mysql.connector.connect(host="localhost", user="root", passwd='abc@123', database="pcgbm")
    g = str(input("game name :  "))
    s1 = str(input("New storage:"))
    cursor = pcgbm.cursor()
    cursor.execute(f'update pcgbm set storage_GB_="{s1}" where G_name="{g}"')
    pcgbm.commit()
    print("records updated")

    exit()


def updateprice():
    import mysql.connector
    pcgbm = mysql.connector.connect(host="localhost", user="root", passwd='abc@123', database="pcgbm")
    g = str(input("game name :  "))
    pr1 = str(input("New price:"))
    cursor = pcgbm.cursor()
    cursor.execute(f'update pcgbm set price_$_="{pr1}" where G_name="{g}"')
    pcgbm.commit()
    print("records updated")

    exit()


def updateReviewScore():
    import mysql.connector
    pcgbm = mysql.connector.connect(host="localhost", user="root", passwd='abc@123', database="pcgbm")
    g = str(input("game name :  "))
    r1 = str(input("New ReviewScore:"))
    cursor = pcgbm.cursor()
    cursor.execute(f'update pcgbm set ReviewScore_outof100="{r1}" where G_name="{g}"')
    pcgbm.commit()
    print("records updated")

    exit()


def updatePCprice():
    import mysql.connector
    pcgbm = mysql.connector.connect(host="localhost", user="root", passwd='abc@123', database="pcgbm")
    g = str(input("game name :  "))
    pc1 = str(input("New PCprice:"))
    cursor = pcgbm.cursor()
    cursor.execute(f'update pcgbm set PCprice_Rs="{pc1}" where G_name="{g}"')
    pcgbm.commit()
    print("records updated")

    exit()


def graphs():
    import matplotlib.pyplot as mat

    def mypie1():
        label1 = ['Geforce GTX 1050 Ti', 'Geforce GTX 1060', 'Geforce GTX 1070 Ti']
        # labels=list(label1)
        sizes = [23, 27, 21]
        print(sizes)
        colors1 = ['yellowgreen', 'lightskyblue', 'magenta']
        # SPLIT_OF_GRAPH=(0,0,0,0,0.1,0,0,0,0)
        mat.title("Games in PCGBM for various Graphics card")
        mat.pie(sizes, explode=None, labels=label1, colors=colors1, shadow=True, autopct='%1.1f%%', startangle=140)
        mat.axis('equal')
        a = mat.show()
        print(a)

    def mypie2():
        label1 = ['i3', 'i5', 'i7']
        # labels=list(label1)
        sizes = [25, 22, 24]
        print(sizes)
        colors1 = ['red', 'blue', 'magenta']
        # SPLIT_OF_GRAPH=(0,0,0,0,0.1,0,0,0,0)
        mat.title("Games in PCGBM for various Processors")
        mat.pie(sizes, explode=None, labels=label1, colors=colors1, shadow=True, autopct='%1.1f%%', startangle=140)
        mat.axis('equal')
        b = mat.show()
        print(b)

    def mypie3():
        label1 = ['4GB', '8GB', '16GB']
        # labels=list(label1)
        sizes = [24, 19, 28]
        print(sizes)
        colors1 = ['lightskyblue', 'yellowgreen', 'brown']
        # SPLIT_OF_GRAPH=(0,0,0,0,0.1,0,0,0,0)
        mat.title("Games in PCGBM for various RAM")
        mat.pie(sizes, explode=None, labels=label1, colors=colors1, shadow=True, autopct='%1.1f%%', startangle=140)
        mat.axis('equal')
        c = mat.show()
        print(c)

    def mypie4():
        label1 = ['Free', '1 to 20', '$21 to $40', '$41 to $60', '$61 to $100']
        # labels=list(label1)
        sizes = [14, 22, 20, 12, 3]
        print(sizes)
        colors1 = ['red', 'blue', 'magenta', 'yellowgreen', 'brown']
        # SPLIT_OF_GRAPH=(0,0,0,0,0.1,0,0,0,0)
        mat.title("Games in PCGBM for various prices($)\n")
        mat.pie(sizes, explode=None, labels=label1, colors=colors1, shadow=True, autopct='%1.1f%%', startangle=140)
        mat.axis('equal')
        d = mat.show()
        print(d)

    def mypie5():
        label1 = ['40 to 60', '61 to 80', '81 to 100']
        # labels=list(label1)
        sizes = [3, 19, 48]
        print(sizes)
        colors1 = ['red', 'blue', 'cyan', ]
        # SPLIT_OF_GRAPH=(0,0,0,0,0.1,0,0,0,0)
        mat.title("Games in PCGBM for various Review Score out of 100\n")
        mat.pie(sizes, explode=None, labels=label1, colors=colors1, shadow=True, autopct='%1.1f%%', startangle=140)
        mat.axis('equal')
        d = mat.show()
        print(d)

    def bar1():
        import numpy as np
        import matplotlib.pyplot as mat15
        objects = ('Geforce GTX 1050 Ti', 'Geforce GTX 1060', 'Geforce GTX 1070 Ti')
        y_pos = np.arange(len(objects))
        types = (23, 27, 21)
        mat15.bar(y_pos, types, align='center', color='yellowgreen')
        mat15.xticks(y_pos, objects)
        mat15.ylabel('Number Of Games')
        mat15.title('Number Of Games According to Graphics Card')
        mat15.show()

    def bar2():
        import numpy as np
        import matplotlib.pyplot as mat14
        objects = ('i3', 'i5', 'i7')
        y_pos = np.arange(len(objects))
        types = (25, 22, 24)
        mat14.bar(y_pos, types, align='center', color='lightgreen')
        mat14.xticks(y_pos, objects)
        mat14.ylabel('Number Of Games')
        mat14.title('Number Of Games According to processor')
        mat14.show()

    def bar3():
        import numpy as np
        import matplotlib.pyplot as mat13
        objects = ('4GB', '8GB', '16GB')
        y_pos = np.arange(len(objects))
        types = (24, 19, 28)
        mat13.bar(y_pos, types, align='center', color='lightskyblue')
        mat13.xticks(y_pos, objects)
        mat13.ylabel('Number Of Games')
        mat13.title('Number Of Games According to RAM')
        mat13.show()

    def bar4():
        import numpy as np
        import matplotlib.pyplot as mat12
        objects = ('Free', '1 to 20', '$21 to $40', '$41 to $60', '$61 to $100')
        y_pos = np.arange(len(objects))
        types = (14, 22, 20, 12, 3)
        mat12.bar(y_pos, types, align='center', color='brown')
        mat12.xticks(y_pos, objects)
        mat12.ylabel('Number Of Games')
        mat12.title('Number Of Games According to Various prices($)')
        mat12.show()

    def bar5():
        import numpy as np
        import matplotlib.pyplot as mat11
        objects = ('40 to 60', '61 to 80', '81 to 100')
        y_pos = np.arange(len(objects))
        types = (3, 19, 48)
        mat11.bar(y_pos, types, align='center', color='magenta')
        mat11.xticks(y_pos, objects)
        mat11.ylabel('Number Of Games')
        mat11.title('Number Of Games According to Various review score(out of 100)')
        mat11.show()

    def line1():
        label1 = ['Geforce GTX 1050 Ti', 'Geforce GTX 1060', 'Geforce GTX 1070 Ti']
        sizes = [23, 27, 21]
        import matplotlib.pyplot as mat10
        mat10.plot(label1, sizes)
        mat10.title("Games in PCGBM for various Graphics card")
        mat10.xlabel('Graphics card')
        mat10.ylabel('No. Of Games')
        mat10.show()

    def line2():
        label1 = ['i3', 'i5', 'i7']
        sizes = [25, 22, 24]
        import matplotlib.pyplot as mat9
        mat9.plot(label1, sizes)
        mat9.title("Games in PCGBM for various Processors")
        mat9.xlabel('Processors')
        mat9.ylabel('No. Of Games')
        mat9.show()

    def line3():
        label1 = ['4GB', '8GB', '16GB']
        sizes = [24, 19, 28]
        import matplotlib.pyplot as mat8
        mat8.plot(label1, sizes)
        mat8.title("Games in PCGBM for various RAM")
        mat8.xlabel('Ram')
        mat8.ylabel('No. Of Games')
        mat8.show()

    def line4():
        label1 = ['Free', '1 to 20', '$21 to $40', '$41 to $60', '$61 to $100']
        sizes = [14, 22, 20, 12, 3]
        import matplotlib.pyplot as mat7
        mat7.plot(label1, sizes)
        mat7.title("Games in PCGBM for various prices($)\n")
        mat7.xlabel('Prices($)')
        mat7.ylabel('No. Of Games')
        mat7.show()

    def line5():
        label1 = ['40 to 60', '61 to 80', '81 to 100']
        sizes = [3, 19, 48]
        import matplotlib.pyplot as mat6
        mat6.plot(label1, sizes)
        mat6.title("Games in PCGBM for various Review Score out of 100\n")
        mat6.xlabel('Review score')
        mat6.ylabel('No. Of Games')
        mat6.show()

    def scatter1():

        import matplotlib.pyplot as mat5
        label1 = ['Geforce GTX 1050 Ti', 'Geforce GTX 1060', 'Geforce GTX 1070 Ti']
        sizes = [23, 27, 21]
        mat5.scatter(label1, sizes, c="blue")
        mat5.show()

    def scatter2():
        import matplotlib.pyplot as mat4
        label1 = ['i3', 'i5', 'i7']
        sizes = [25, 22, 24]
        mat4.scatter(label1, sizes, c="green")
        mat4.show()

    def scatter3():
        import matplotlib.pyplot as mat3
        label1 = ['4GB', '8GB', '16GB']
        sizes = [24, 19, 28]
        mat3.scatter(label1, sizes, c="green")
        mat3.show()

    def scatter4():
        import matplotlib.pyplot as mat2
        label1 = ['Free', '1 to 20', '$21 to $40', '$41 to $60', '$61 to $100']
        sizes = [14, 22, 20, 12, 3]
        mat2.scatter(label1, sizes, c="green")
        mat2.show()

    def scatter5():
        import matplotlib.pyplot as mat1
        label1 = ['40 to 60', '61 to 80', '81 to 100']
        sizes = [3, 19, 48]
        mat1.scatter(label1, sizes, c="green")
        mat1.show()

    forgraphs = "y"
    if forgraphs == "y":
        print('Select the graph you want to see')
        print('1.Pie chart')
        print('2.Bar graph')
        print('3.Line Graph')
        print('4.Scatter plot')
        choice = int(input('Enter choice of graphs : '))
        if choice == 1:
            print('1.Games in PCGBM for various Graphics card')
            print('2.Games in PCGBM for various Processors')
            print('3.Games in PCGBM for various RAM')
            print('4.Games in PCGBM for various prices($)')
            print("5.Games in PCGBM for various Review Score out of 100\n")

            choice1 = int(input('Enter choice of Pie Charts : '))
            if choice1 == 1:
                mypie1()
            elif choice1 == 2:
                mypie2()
            elif choice1 == 3:
                mypie3()
            elif choice1 == 4:
                mypie4()
            elif choice1 == 5:
                mypie5()
        elif choice == 2:

            print('1.Number Of Games According to Graphics Card')
            print('2.Number Of Games According to processor')
            print('3.Number Of Games According to RAM')
            print('4.Number Of Games According to Various prices($)')
            print('5.Number Of Games According to Various review score(out of 100)')
            choice3 = int(input('Enter the choice of Bar Graphs : '))
            if choice3 == 1:
                bar1()
            elif choice3 == 2:
                bar2()
            elif choice3 == 3:
                bar3()
            elif choice3 == 4:
                bar4()
            elif choice3 == 5:
                bar5()

        if choice == 3:
            print('1.Games in PCGBM for various Graphics card')
            print('2.Games in PCGBM for various Processors')
            print('3.Games in PCGBM for various RAM')
            print('4.Games in PCGBM for various prices($)')
            print("5.Games in PCGBM for various Review Score out of 100\n")

            choice1 = int(input('Enter choice of Line Charts : '))
            if choice1 == 1:
                line1()
            elif choice1 == 2:
                line2()
            elif choice1 == 3:
                line3()
            elif choice1 == 4:
                line4()
            elif choice1 == 5:
                line5()

        if choice == 4:
            print('1.Games in PCGBM for various Graphics card')
            print('2.Games in PCGBM for various Processors')
            print('3.Games in PCGBM for various RAM')
            print('4.Games in PCGBM for various prices($)')
            print("5.Games in PCGBM for various Review Score out of 100\n")

            choice1 = int(input('Enter choice of Pie Charts : '))
            if choice1 == 1:
                scatter1()
            elif choice1 == 2:
                scatter2()
            elif choice1 == 3:
                scatter3()
            elif choice1 == 4:
                scatter4()
            elif choice1 == 5:
                scatter5()

        else:
            print("exiting")
    else:
        print("exiting")
        exit()


main()
