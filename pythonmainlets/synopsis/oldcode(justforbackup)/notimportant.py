def main():
    c = 'y'
    while c == 'y':
        userpost = input("If you are the programme user(Enter U)\nIf you are programme admin(Enter A):").upper()
        if userpost == "A":
            admin()
        elif userpost == "U":
            program()
        else:
            print("Invalid Input")
            exit()
    else:
        print('wrong input')
# c = input('\nDo you want run the program again \nIf yes then type y \nElse enter anything\n : ').lower()


def program():
    cont = "y"
    if cont == "y":
        def pcgaming():
            import pandas as pd
            import mysql.connector
            pcgbm = mysql.connector.connect(host="localhost", user="root", passwd='abc@123', database="pcgbm")
            print("\nCan I Run It ?")
            print("System requirement application to find games that can run on your computer,\nGame Price, "
                  "Price of the PC(Based upon the configuration provided by you)\n"
                  "What games your laptop/PC can run - from our list of over 70 PC games. \n")
            print("Tell us about your PC specification from the following option's\n ")
            graphics = (input("Choose from the folLowing GRAPHICS CARD\n"
                              "   Geforce GTX 1050 Ti (ENTER g1)\n "
                              "  Geforce GTX 1060    (ENTER g2)\n "
                              "  Geforce GTX 1070 Ti (ENTER g3)\n "
                              " :  ")).lower()
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
                print(data.loc[row])
                print()
        print(pcgaming())
    rerun = input("\nDo you want run the program again \nIf yes then type y \nElse enter anything\n : ").lower()
    if rerun == 'y':
        program()
    else:
        print("I wish you have a Good Day!!")
        exit()


def admin():
    loginid = "18PCGBM07"
    password = "******"
    lid = input("Enter LginID:")
    pw = input("Enter Password:")
    if lid == loginid and pw == password:
        print("Correct ID")
        print("You will be taken to program coding")
        exit()
    else:
        print("Invalid ID!!!")
        print("Invalid Password!!!")
        print("You are being taken to the coding part!!")
        exit()


main()
