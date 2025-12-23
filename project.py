if a == 1:
    while True:
        m = int(input("Enter a serial number: "))
        if 1 <= m <= len(data):
            fkp_id = data[m - 1][0]
            data2 = set7(fkp_id)

            if data2:
                faka = []
                for inx, row in enumerate(data2, start=1):
                    faka.append((inx, row[0], row[1], row[2], row[3], row[4]))  # row[0], row[1] ... etc.

                # লুপ শেষ হওয়ার পর একবারে প্রিন্ট
                print(tabulate(
                    faka,
                    headers=["Serial No", "Element", "Colour", "Kena Dam", "Resiv Date", "Future Sells Date"],
                    tablefmt="pretty"
                ))

                print("1. Back")
                print("2. Exit")
                b = int(input("Enter your choice: "))
                if b == 1:
                    break  # আবার উপরের মেনুতে যাবে
                elif b == 2:
                    exit()

                    if a ==1:
                        while True:
                            m = int(input("enter a sirial number :  "))
                            if 1 <= m <len(data):
                                fkp_id = data[m - 1][0]

                                data2 = set7(fkp_id)

                                if data2:
                                    faka = []
                                    for inx, row in enumerate(data2, start=1):
                                        faka.append((inx, row[1], row[2], row[3], row[4], row[5]))

                                        print(tabulate(faka,headers=["serial no", "element", "colour", "kena dam", "resiv date","future selse date"], tablefmt="pretty"))

                                        print("1. back")
                                        print("2. exit")
                                        b = int(input("enter your chose :  "))
                                        if b ==1:
                                            continue
                                        elif b==2:
                                            exit()






                                            elif n == 3:
                                            data = set3()
                                            faka = []
                                            if data:
                                                for inx, row in enumerate(data, start=1):
                                                    faka.append((inx, row[1], row[2], row[3], row[4], row[5]))
                                                print('\n~~~~~~~~~~~~ personal information table ~~~~~~~~~~~~~~~~~')

                                                print(tabulate(faka, headers=['Name', 'Father_name', 'City', 'velage',
                                                                              'Phon_no'], tablefmt="pretty"))

                                                print("\n1. woant you know spasifiq parson")
                                                print("2. are you show another menu")
                                                print("3. back")
                                                print("4. exit")

                                                a = int(input("enter your chose :  "))

                                                if a == 1:
                                                    while True:
                                                        m = int(input("enter a sirial number :  "))
                                                        if 1 <= m <= len(data):
                                                            fkp_id = data[m - 1][0]

                                                            data2 = set7(fkp_id)

                                                            if data2:
                                                                faka = []
                                                                for inx, row in enumerate(data2, start=1):
                                                                    faka.append(
                                                                        (inx, row[0], row[1], row[2], row[3], row[4]))

                                                                print(tabulate(faka,
                                                                               headers=["serial no", "element",
                                                                                        "colour", "kena dam",
                                                                                        "resiv date",
                                                                                        "future selse date"],
                                                                               tablefmt="pretty"))

                                                                print("1. back")
                                                                print("2. exit")
                                                                b = int(input("enter your chose :  "))
                                                                if b == 1:
                                                                    break
                                                                elif b == 2:
                                                                    exit()

                                                                    if a == 1:

                                                                        while True:

                                                                            m = int(input("enter a sirial number : "))

                                                                            if 1 <= m <= len(data):

                                                                                fkp_id = data[m - 1][0]

                                                                                data2 = set7(fkp_id)

                                                                                faka2 = []

                                                                                for inx, row in enumerate(data2,
                                                                                                          start=1):
                                                                                    faka2.append((inx, *row))

                                                                                print(tabulate(

                                                                                    faka2,

                                                                                    headers=["S.No", "Element",
                                                                                             "Colour", "Price",
                                                                                             "Receive", "Future"],

                                                                                    tablefmt="pretty"

                                                                                ))

                                                                                print("1. back")

                                                                                print("2. exit")

                                                                                b = int(input("enter your chose : "))

                                                                                if b == 1:

                                                                                    break  # 🔥 আগের personal table এ ফিরবে

                                                                                elif b == 2:

                                                                                    exit()


                                                                    elif a == 3:

                                                                        break  # 🔙 main menu


                                                                    elif a == 4:

                                                                        exit()

                                                                        elif n == 4:
                                                                        data1 = set8()
                                                                        faka = []

                                                                        for inx, row in enumerate(data1, start=1):
                                                                            faka.append(
                                                                                (inx, row[1], row[2], row[3], row[4],
                                                                                 row[5], row[6], row[8], row[9],
                                                                                 row[10], row[11], row[12], row[13]))
                                                                            print(tabulate(faka, headers=["father_name",
                                                                                                          "city",
                                                                                                          "velage",
                                                                                                          "phone",
                                                                                                          "element",
                                                                                                          "colour",
                                                                                                          "buying_price",
                                                                                                          "sales_price",
                                                                                                          "sales_date",
                                                                                                          "total_profit",
                                                                                                          "company_pro",
                                                                                                          "customer_pro"],
                                                                                           tablefmt="pretty"))

                                                                        user = int(input("enter your user id :  "))
                                                                        cursor.execute(
                                                                            "select p.parsonal_id, p.Name, p.Father_name, p.City, p.velage, p.Phon_no,"
                                                                            "d.upadan_name,  d.colur,  d.kena_mullo,  d.Resive_date from parsonal_info p"
                                                                            " join product_desc d on p.parsonal_id = d.fkp_id  "
                                                                            "where p.parsonal_id = %s", (user,))

                                                                        row = cursor.fetchall()

                                                                        sales = int(input("enter your sales price :  "))
                                                                        date = input("enter date of sales :  ")

                                                                        cursor.execute(
                                                                            "insert into sales(parsonal_id,Father_name,City,velage,Phon_no,upadan_name,colur,"
                                                                            "kena_mullo,Resive_date,sales_price,sales_date) "
                                                                            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                                            (*row[:10], sales, date))

                                                                        db.commit()

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

                        if user_id in existing_id:
                            cursor.execute("insert into sales (parsonal_id ,name ,father_name ,city, velage ,phone) "
                                           "select parsonal_id,Name,Father_name,City,velage,Phon_no from parsonal_info "
                                           "where parsonal_id =%s", (user_id,))

                            print("this parson is allrady added")
                            db.commit()

                        total_pro = sales_p - result[2]
                        cus_pro = total_pro * 0.4
                        com_pro = total_pro * 0.6

                        cursor.execute(
                            "insert into sales2 (element ,colour ,buying_price ,sales_price ,sales_date ,total_pro ,cus_pro ,com_pro ,sales2_id )"
                            "values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (result[0], result[1], result[2], sales_p, sales_d, total_pro, cus_pro, com_pro, user_id))

                        db.commit()
                        print("added successfully")













                        cursor.execute("insert into sales (parsonal_id ,name ,father_name ,city, velage ,phone) "
                                       "select parsonal_id,Name,Father_name,City,velage,Phon_no from parsonal_info "
                                       "where parsonal_id =%s",(user_id,))

                        db.commit()


                        cursor.execute("select upadan_name, colur,kena_mullo,Resive_date,future_byuing_date,buy_mullo from product_desc where fkp_id=%s",(user,))

                        result = cursor.fetchone()
                        total_pro = sales_p - result[2]
                        cus_pro = total_pro * 0.4
                        com_pro = total_pro * 0.6
