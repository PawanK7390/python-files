def admin():
    loginid = "18PCGBM07"
    password = "******"
    lid = input("Enter LginID:")
    pw = input("Enter Password:")
    if lid == loginid and pw == password:
        # import pandas as pd
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
        cursor.execute(f'insert into pcgbmadmin values("{g}","{p}","{m}","{gr}","{s}","{pr}","{pl}","{r}","{pc}");')
        pcgbm.commit()
        print("records added")
        exit()


admin()
