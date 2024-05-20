def programb():
    cont = "y"
    if cont == "y":

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
            print("G_NAME ,storage(GB) ,price($)  ,ReviewScore(outof100),PCprice(Rs)")
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i3" and graphics="Geforce GTX 1050 Ti" and memory="4GB"')
            myresult = cursor.fetchall()
            for x in myresult:
                if (graphics == 'g1'):
                    if (processor == 'p1'):
                        if (memory == 'r1'):
                            print(x)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i5" and graphics="Geforce GTX 1060" and memory="8GB"')
            myresult = cursor.fetchall()
            for y in myresult:
                if (graphics == 'g2'):
                    if (processor == 'p2'):
                        if (memory == 'r2'):
                            print(y)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i7" and graphics="Geforce GTX 1060" and memory="4GB"')
            myresult = cursor.fetchall()
            for a in myresult:
                if (graphics == 'g2'):
                    if (processor == 'p3'):
                        if (memory == 'r1'):
                            print(a)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i7" and graphics="Geforce GTX 1060" and memory="8GB"')
            myresult = cursor.fetchall()
            for b in myresult:
                if (graphics == 'g2'):
                    if (processor == 'p3'):
                        if (memory == 'r2'):
                            print(b)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i7" and graphics="Geforce GTX 1060" and memory="16GB"')
            myresult = cursor.fetchall()
            for c in myresult:
                if (graphics == 'g2'):
                    if (processor == 'p3'):
                        if (memory == 'r3'):
                            print(c)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i5" and graphics="Geforce GTX 1060" and memory="4GB"')
            myresult = cursor.fetchall()
            for d in myresult:
                if (graphics == 'g2'):
                    if (processor == 'p2'):
                        if (memory == 'r1'):
                            print(d)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i5" and graphics="Geforce GTX 1060" and memory="16GB"')
            myresult = cursor.fetchall()
            for e in myresult:
                if (graphics == 'g2'):
                    if (processor == 'p2'):
                        if (memory == 'r3'):
                            print(e)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i3" and graphics="Geforce GTX 1060" and memory="4GB"')
            myresult = cursor.fetchall()
            for f in myresult:
                if (graphics == 'g2'):
                    if (processor == 'p1'):
                        if (memory == 'r1'):
                            print(f)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i3" and graphics="Geforce GTX 1060" and memory="8GB"')
            myresult = cursor.fetchall()
            for g in myresult:
                if (graphics == 'g2'):
                    if (processor == 'p1'):
                        if (memory == 'r2'):
                            print(g)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i3" and graphics="Geforce GTX 1060" and memory="16GB"')
            myresult = cursor.fetchall()
            for h in myresult:
                if (graphics == 'g2'):
                    if (processor == 'p1'):
                        if (memory == 'r3'):
                            print(h)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i7" and graphics="Geforce GTX 1050 Ti" and memory="4GB"')
            myresult = cursor.fetchall()
            for i in myresult:
                if (graphics == 'g1'):
                    if (processor == 'p3'):
                        if (memory == 'r1'):
                            print(i)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i7" and graphics="Geforce GTX 1050 Ti" and memory="8GB"')
            myresult = cursor.fetchall()
            for j in myresult:
                if (graphics == 'g1'):
                    if (processor == 'p3'):
                        if (memory == 'r2'):
                            print(j)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i7" and graphics="Geforce GTX 1050 Ti" and memory="16GB"')
            myresult = cursor.fetchall()
            for k in myresult:
                if (graphics == 'g1'):
                    if (processor == 'p3'):
                        if (memory == 'r3'):
                            print(k)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i5" and graphics="Geforce GTX 1050 Ti" and memory="4GB"')
            myresult = cursor.fetchall()
            for l in myresult:
                if (graphics == 'g1'):
                    if (processor == 'p2'):
                        if (memory == 'r1'):
                            print(l)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i5" and graphics="Geforce GTX 1050 Ti" and memory="8GB"')
            myresult = cursor.fetchall()
            for m in myresult:
                if (graphics == 'g1'):
                    if (processor == 'p2'):
                        if (memory == 'r2'):
                            print(m)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i5" and graphics="Geforce GTX 1050 Ti" and memory="16GB"')
            myresult = cursor.fetchall()
            for n in myresult:
                if (graphics == 'g1'):
                    if (processor == 'p2'):
                        if (memory == 'r3'):
                            print(n)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i3" and graphics="Geforce GTX 1050 Ti" and memory="8GB"')
            myresult = cursor.fetchall()
            for o in myresult:
                if (graphics == 'g1'):
                    if (processor == 'p1'):
                        if (memory == 'r2'):
                            print(o)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i3" and graphics="Geforce GTX 1050 Ti" and memory="16GB"')
            myresult = cursor.fetchall()
            for p in myresult:
                if (graphics == 'g1'):
                    if (processor == 'p1'):
                        if (memory == 'r3'):
                            print(p)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i7" and graphics="Geforce GTX 1070 Ti" and memory="4GB"')
            myresult = cursor.fetchall()
            for q in myresult:
                if (graphics == 'g3'):
                    if (processor == 'p3'):
                        if (memory == 'r1'):
                            print(q)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i7" and graphics="Geforce GTX 1070 Ti" and memory="8GB"')
            myresult = cursor.fetchall()
            for r in myresult:
                if graphics == 'g3':
                    if processor == 'p3':
                        if memory == 'r2':
                            print(r)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i7" and graphics="Geforce GTX 1070 Ti" and memory="16GB"' and
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm')
            myresult = cursor.fetchall()
            for s in myresult:
                if (graphics == 'g3'):
                    if (processor == 'p3'):
                        if (memory == 'r3'):
                            print(s)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i5" and graphics="Geforce GTX 1070 Ti" and memory="4GB"')
            myresult = cursor.fetchall()
            for t in myresult:
                if (graphics == 'g3'):
                    if (processor == 'p2'):
                        if (memory == 'r1'):
                            print(t)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i5" and graphics="Geforce GTX 1070 Ti" and memory="8GB"')
            myresult = cursor.fetchall()
            for u in myresult:
                if (graphics == 'g3'):
                    if (processor == 'p2'):
                        if (memory == 'r2'):
                            print(u)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i5" and graphics="Geforce GTX 1070 Ti" and memory="16GB"')
            myresult = cursor.fetchall()
            for v in myresult:
                if (graphics == 'g3'):
                    if (processor == 'p2'):
                        if (memory == 'r3'):
                            print(v)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i3" and graphics="Geforce GTX 1070 Ti" and memory="4GB"')
            myresult = cursor.fetchall()
            for w in myresult:
                if (graphics == 'g3'):
                    if (processor == 'p1'):
                        if (memory == 'r1'):
                            print(w)
            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i3" and graphics="Geforce GTX 1070 Ti" and memory="8GB"')
            myresult = cursor.fetchall()
            for z in myresult:
                if (graphics == 'g3'):
                    if (processor == 'p1'):
                        if (memory == 'r2'):
                            print(z)

            cursor = pcgbm.cursor()
            cursor.execute(
                'select G_name,storage_GB_,price_$_,ReviewScore_outof100,PCprice_Rs from pcgbm where processor="i3" and graphics="Geforce GTX 1070 Ti" and memory="16GB"')
            myresult = cursor.fetchall()
            for ab in myresult:
                if (graphics == 'g3'):
                    if (processor == 'p1'):
                        if (memory == 'r3'):
                            print(ab)

    rerun = input("\nDo you want run the program again \nIf yes then type y \nElse enter anything\n : ").lower()
    if rerun == 'y':
        print(programb())
    else:
        print("I wish you have a Good Day!!" )
        exit()
programb()
