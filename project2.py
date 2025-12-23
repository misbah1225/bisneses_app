import mysql.connector
from tabulate import tabulate

try:
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "bisnes_project"

    )
    print("DATA SERVER is sucssesfuly conncet")
except mysql.connector.Error as err:
    print("404 SERVER ~~~ ERROR ")

cursor = db.cursor()

def menu_show():
    cursor.execute("select services from main_menu")
    result = cursor.fetchall()

    return result




#function 1

def set1():
    cursor.execute("select  kenar_id, eliment,price,quantity,date,comment  from kbistarito")
    result = cursor.fetchall()
    return result




#function 2

def set2():
    cursor.execute("select stock_id,upadan_s, poriman_s  from stock_ase")
    result = cursor.fetchall()
    return result


#function 3
def set3():
    cursor.execute("SELECT parsonal_id, Name, Father_name, City, velage, Phon_no FROM parsonal_info")
    personal_data = cursor.fetchall()

    return personal_data




#function 4


def set4():
    cursor.execute("select  Name	,Father_name	,City,	velage,	Phon_no from personal_info")
    result = cursor.fetchall()
    return result




#function 5

def set5():
    cursor.execute("select lone_id ,Name	,Father_Name,	Velage,	Phone_no, Lone_amount	from lone_table")
    result = cursor.fetchall()
    return result




#function 6

def set6():
    cursor.execute("select donation_id,Name, velage,Type_of_donation,   donation_taka,donation_date  from donetion_table	")
    result = cursor.fetchall()
    return result


#function 7
def set7(fkp_id):
    cursor.execute("SELECT upadan_name, colur, kena_mullo, Resive_date, future_byuing_date, buy_mullo FROM product_desc where fkp_id=%s ",(fkp_id,))
    product_data = cursor.fetchall()

    return product_data


#function 8
def set8():
    cursor.execute("select parsonal_id ,name ,father_name ,city, velage ,phone from sales")

    sales = cursor.fetchall()
    return sales


#function 9
def set9():
    cursor.execute("select 	element,colour, buying_price, sales_price, sales_date, total_pro, cus_pro,"
                   " com_pro from sales2 where sales2_id =%s",(m,))

    sales2 = cursor.fetchall()
    return sales2


####


def limit():
    cursor.execute("""select 
            ifnull(sum(total_pro),0) 
            - ifnull((select sum(lone_amount) from lone_table ),0)
            - ifnull((select sum(donation_taka) from donetion_table),0)
            from sales2""")
    return cursor.fetchone()[0]




#main hart
def company_info():
    cursor.execute("select sum(lone_amount)from lone_table")
    total_lone = cursor.fetchone()[0]or 0



    cursor.execute("select sum(donation_taka) from donetion_table")
    total_donation = cursor.fetchone()[0] or 0


    cursor.execute("select sum(total_pro) from sales2")
    total_sales = cursor.fetchone()[0] or 0



    total_profit = total_sales-total_donation-total_lone

    cursor.execute("""
    update total_info  set total_lone =%s,total_donation = %s,total_profit = %s where com_id = 1""",(total_lone,total_donation,total_profit)

    )
    db.commit()



while True:
    menu = menu_show()

    if menu:
        faka = []
        for inx, row in enumerate(menu,start=1):
            faka.append((inx,*row))

        print(tabulate(faka, headers=["serial_no", "services"], tablefmt="pretty"))
        try:

           n = int(input("enter a valid number or exit (input 0) : "))

        except ValueError:
           print("try again")
           continue

        if n == 1:
            data = set1()
            if data:
                faka = []
                for inx, row in enumerate(data, start=1):
                    faka.append((inx, row[1],row[2],row[3],row[4],row[5]))
                print('\n~~~~~~~~~~~~~~~~~~~~~Total buying information~~~~~~~~~~~~~~~~~')
                print(tabulate(faka, headers=["serial no", "element", "price", "quentity", "date", "comment"],tablefmt="pretty"))

                print("\n~~~~~~~~~~~~~ 1. add a new element ~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~ 2. delete a element  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~ 3. back  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~ 4. exist  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")




            n = int(input("enter your choice : "))
            #add a new row
            #function 1
            if n == 1:
                try:
                    element = str(input("element name :  "))
                    price = int(input("enter element amount :  "))
                    quantity = int(input("how many pisec this element :  "))
                    date = input("enter buying date(yyyy-mm-dd) :  ")
                    comment = input("enter your comment :  ")
                    cursor.execute("insert into kbistarito (eliment,price,quantity,date,comment)values(%s,%s,%s,%s,%s)",
                                (element,price,quantity,date,comment))

                    db.commit()

                except ValueError:
                    print("try again later")
                    continue

            elif n == 2:
                try:

                    user_input = int(input("enter your delete row (s_no) :  "))

                    if 1 <= user_input <= len(data):

                        kenar_id = data[user_input - 1][0]

                        cursor.execute(

                            "delete from kbistarito where kenar_id = %s",
                            (kenar_id,)

                        )

                        db.commit()

                        print(f"\n{user_input} number row is deleted successfully")


                    else:

                        print("this serial number is not available")

                except ValueError:
                    print("K")


            elif n == 3:

                continue


            elif n == 4:
                exit()


        #function 2
        elif n == 2:
            data1=set2()
            faka = []
            if data1 :
                for inx,row in enumerate(data1,start=1):
                    faka.append((inx,row[1],row[2]))
                print('\n~~~~~~~~~~~~ stock table ~~~~~~~~~~~~~~~~~')

                print(tabulate(faka,headers=["serial_no","element","pisses"],tablefmt="pretty"))

                print("\n~~~~~~~~~~~~~ 1. add a new element ~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~ 2. delete a element  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~ 3. back  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~ 4. exist  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


                n=int(input("enter your chose : "))

                if n == 1:
                    try:
                        upadan_s  = str(input("enter your element name :  "))
                        poriman_s = int(input("how many pis this element :  "))

                        cursor.execute("insert into stock_ase(upadan_s, poriman_s)values(%s,%s)",
                                           (upadan_s, poriman_s))
                        db.commit()

                    except ValueError:
                        continue

                elif n == 2:

                    try :
                        n = int(input("enter your chose :  "))
                        if 1 <= n <= len(data1):
                            stock_id = data1[n - 1][0]
                            cursor.execute("delete from stock_ase where stock_id = %s",
                                        (stock_id,)
                            )

                            db.commit()
                            print(f"\n{n}. this row is deleted succsesfully")
                        else:
                            print(f"\n{n}. this row is not avalable")


                    except ValueError:
                        continue

                elif n == 3:
                    continue

                elif n == 4:
                    exit()

                else:
                    print("400 ~~~~~ invalid request")




        elif n == 3:
            while True:

                data = set3()
                faka = []

                for inx , row in enumerate(data,start=1):
                    faka.append((inx,row[1],row[2],row[3],row[4],row[5],row[0]))

                print(tabulate(faka,headers=[ "serial no","Name", "Father_name", "City", "velage", "Phon_no","user id"],tablefmt = "pretty"))
                print("\n1. specific person")

                print("2. another menu")

                print("3. back")

                print("4. exit")


                a = int(input("enter your chose :  "))

                if a == 1:
                    while True:
                        m = int(input("enter your chose s n :  "))
                        if 1<=m<=len(data):
                            fkp_id = data[m - 1][0]
                            data2 = set7(fkp_id)
                            faka = []

                            for inx ,row in enumerate(data2,start=1):
                                faka.append((inx,row[0],row[1],row[2],row[3],row[4]))

                            print(tabulate(faka,headers =["serial no","element","colour","buying price","resive date","future selse date"],tablefmt="pretty"))

                            print("")
                            print("1. back")
                            print("2. exit")
                            b = int(input("enter your chose :  "))

                            if b == 1:
                                break
                            elif b == 2:
                                exit()

                elif a == 3:
                    break
                elif a == 4:
                    exit()










                elif a==2:
                        print("\n~~~~~~~~~~~~~ 1. add a new element ~~~~~~~~~~~~~~~~~~~~~~~")
                        print("~~~~~~~~~~~~~ 2. delete a element  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("~~~~~~~~~~~~~ 3. back  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("~~~~~~~~~~~~~ 4. exist  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


                        n =int(input("enter your chose :  "))






                        if n == 1:
                            try:

                                name = str(input("Enter your name :  "))
                                father = str(input("Enter your father name :  "))
                                city = str(input("Enter your city name :  "))
                                velag = str(input("Enter your velage name :  "))
                                phon = input("Enter your phone number :  ")
                                element_name =input("enter element name :  ")
                                colur =input("enter your element colur :  ")
                                kena_dam= int(input("enter buying price :  "))
                                resiv_date = input("enter resave date :  ")
                                future_byuing_date = input("enter selse date :  ")
                            except ValueError:
                                continue


                            cursor.execute("insert into parsonal_info ( Name, Father_name, City, velage, Phon_no)values(%s,%s,%s,%s,%s)",
                                 (name,father,city,velag,phon ))

                            db.commit()

                            fkp_id = cursor.lastrowid

                            cursor.execute("insert into product_desc(fkp_id,upadan_name,colur,kena_mullo,Resive_date,future_byuing_date)"
                                               "values(%s,%s,%s,%s,%s,%s)",
                                    (fkp_id,element_name,colur,kena_dam,resiv_date,future_byuing_date))


                            db.commit()


                        elif n == 2:

                            c = int(input("enter your delete row of s_n :  "))
                            fkp_id = data[c-1][0]
                            cursor.execute("delete from parsonal_info where parsonal_id = %s",(fkp_id,))
                            db.commit()



                        elif n == 3:
                            continue

                        else :
                            exit()

        elif n == 4:


            while True:
                data8 = set8()
                faka = []

                if data8:
                    for inx ,row in enumerate(data8,start=1):
                        faka.append((inx,row[1],row[2],row[3],row[4],row[5],row[0]))

                    print(tabulate(faka,headers = ["name","father name","city","velage","phon no","user id"],tablefmt = "pretty"))

                    print("\n1. specific person")

                    print("2. add parson")

                    print("3. back")

                    print("4. exit")


                    try:
                        user = int(input("enter your chose :  "))
                    except ValueError:
                        continue
                    if user == 1:
                        while True:
                            try:
                                m = int(input("enter your user id :  "))
                            except ValueError:
                                continue
                            if 1<=m:

                        #        sfk_id = [m-1][0]
                                faka = []
                                data9 = set9()

                                for inx, row in enumerate(data9,start=1):
                                    faka.append((inx,row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))

                                print(tabulate(faka,headers = ['element','colour', 'buying_price',
                                                               'sales_price', 'sales_date', 'total_pro', 'cus_pro', 'com_pro']
                                               ,tablefmt = "pretty"))


                                print("1. back")
                                print("2. exit")
                                b = int(input("Enter your chose :  "))
                                if b == 1:
                                    break

                                elif b == 2:
                                    exit()

                    elif user == 2:
                        try:
                            user_id = int(input("Enter your user ID :  "))
                            sales_p = int(input("enter your sales price :  "))
                            sales_d = input("enter your sales date (yyyy-mm-dd) :  ")
                        except ValueError:
                            continue

                        cursor.execute("select upadan_name, colur,kena_mullo,fkp_id,Resive_date,"
                                       "future_byuing_date,buy_mullo from product_desc where fkp_id =%s", (user_id,))

                        result = cursor.fetchone()

                        if not result:
                            print("data null")
                            continue

                        cursor.execute("select 1 from sales where parsonal_id = %s", (user_id,))

                        already = cursor.fetchone()

                        if not already:
                            cursor.execute("insert into sales (parsonal_id ,name ,father_name ,city, velage ,phone) "
                                           "select parsonal_id,Name,Father_name,City,velage,Phon_no from parsonal_info "
                                           "where parsonal_id =%s", (user_id,))
                            db.commit()

                        elif already :
                            print("eta agei ase")

                        total_pro = sales_p - result[2]
                        cus_pro = total_pro * 0.4
                        com_pro = total_pro * 0.6

                        cursor.execute(
                            "insert into sales2 (element ,colour ,buying_price ,sales_price ,sales_date ,total_pro ,cus_pro ,com_pro ,sales2_id )"
                            "values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (result[0], result[1], result[2], sales_p, sales_d, total_pro, cus_pro, com_pro, user_id))

                        db.commit()
                        cursor.execute("delete from parsonal_info where parsonal_id=%s",(user_id,))
                        company_info()
                        db.commit()

                        print("added successfully")

                    elif user == 3:
                        break

                    elif user == 4:
                        exit()


        elif n == 5:
            data3 = set5()
            faka2 = []
            if data3:
                for inx,row in enumerate(data3,start=1):
                    faka2.append((inx,row[1],row[2],row[3],row[4],row[5]))

            print('\n~~~~~~~~~~~~ lone table ~~~~~~~~~~~~~~~~~')


            print(tabulate(faka2,headers = ["serial no","name","father name","vilage","phon no","lone amount"],tablefmt= "pretty"))

            print("\n~~~~~~~~~~~~~ 1. add a new parson ~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~ 2. delete a parson  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~ 3. back  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~ 4. exist  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


            w =int(input("enter your chose :  "))

            if w == 1:
                try:
                    name = input("enter your name :  ")
                    f_name = input("enter your father name :  ")
                    velage = input("enter your velage name :  ")
                    phone1 = input("enter your phone no :  ")


                    data2 = limit()
                    if data2<=0:
                        print("taka nei")
                        continue

                    print(f"\nyou can give {data2} taka")
                    amount = int(input("enter your lone amount :  "))
                    if amount>data2:
                        print(f"error you have {data2} taka")
                        continue





                except ValueError:
                    continue

                cursor.execute("insert into lone_table (Name	,Father_Name,	Velage,	Phone_no, Lone_amount) values(%s,%s,%s,%s,%s)",
                                (name,f_name,velage,phone1,amount))

                db.commit()
                company_info()
                print("added successfully")


            elif w == 2:
                try:
                    m = int(input("input your serial no. :  "))


                    if 1<=m<=len(data3):

                        new = data3[m-1][0]

                        cursor.execute("delete from lone_table where 	lone_id =%s",(new,))

                        db.commit()
                        company_info()
                        print(f"\n{m}. this row is deleted succsesfully")

                    else:
                        print(f"\n{m}. this row is not avalable")


                except ValueError:
                    continue


            elif w ==3:
                continue

            else:
                exit()





        elif n == 6:
            data4 = set6()
            faka = []
            if data4:
                 for inx ,row in enumerate(data4,start=1):
                        faka.append((inx,row[1],row[2],row[3],row[4],row[5]))
            print('\n~~~~~~~~~~~~ donation table ~~~~~~~~~~~~~~~~~')

            print(tabulate(faka,headers = ['serial no',"name","velage","type of donation","donation price","donation date"],tablefmt="pretty"))

            print("\n~~~~~~~~~~~~~ 1. add a new parson ~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~ 2. delete a parson  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~ 3. back  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~ 4. exist  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            v = int(input("enter your chose :  "))


            if v == 1:
                try:
                    name = input("enter your name :  ")
                    velage = input("enter you velage :  ")
                    t_o_d = input("enter your donation type :  ")
                    d_d = input("enter your donation date :  ")

                    faka = limit()
                    if faka<=0:
                        print("taka nai")
                        continue
                    print(f"\nyou can give {faka} taka")
                    do_pr = int(input("enter your donation price :  "))

                    if do_pr > faka:
                        print(f"tomar {do_pr} taka nei")
                        continue




                except ValueError:
                    continue

                cursor.execute("insert into donetion_table (Name, velage,Type_of_donation,   donation_taka,donation_date) "
                               "values (%s,%s,%s,%s,%s)",
                               (name,velage,t_o_d,do_pr,d_d))

                db.commit()
                company_info()
                print(f"{name}. parson is donation successfully !!!")


            elif v == 2:
                try:
                    f = int(input("enter your serial no :  "))

                    if 1<=f<=len(data4):

                        do_id = data4[f-1][0]
                        cursor.execute("delete from donetion_table where donation_id = %s",(do_id,))
                        db.commit()
                        print(f"\n{f}. this row is deleted succsesfully")

                    else:
                        print(f"\n{f}. this row is not avalable")

                except ValueError:
                    continue


            elif v == 3:
                continue

            else:
                exit()





        elif n == 7:
            cursor.execute("select total_profit,total_lone,total_donation from total_info")
            show = cursor.fetchall()
            print(tabulate(show,headers = ["tota profit","total lone","tota donation"],tablefmt = "pretty"))

            print("1. back")
            print("2. exit")
            b = int(input("enter your chose :  "))
            if b == 1:
                continue

            elif b == 2:
                exit()



        elif n==0:
            exit()