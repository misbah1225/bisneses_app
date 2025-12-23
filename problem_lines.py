# insert into parsonal_info
cursor.execute(
    "INSERT INTO parsonal_info (Name, Father_name, City, velage, Phon_no) "
    "VALUES (%s,%s,%s,%s,%s)",
    (name, father, city, velag, phon)
)
db.commit()

# 🔥 THIS IS THE MAGIC
fkp_id = cursor.lastrowid

# insert into product_desc (FK goes here)
cursor.execute(
    """
    INSERT INTO product_desc
    (fkp_id, upadan_name, colur, kena_mullo, Resive_date)
    VALUES (%s,%s,%s,%s,%s)
    """,
    (fkp_id, element_name, colur, kena_dam, resiv_date)
)
db.commit()

faka = []
data2 = set7(fkp_id)
if data2:
    for inx, row in enumerate(data2, start=1):
        faka.append((inx, row[0], row[1], row[2], row[3]))

        print("\n~~~~~~~~~~~~~ 1. add a new element ~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~ 2. delete a element  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~ 3. back  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~ 4. exist  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")













        elif n == 3:

            while True:  # 🔥 personal list loop

                data = set3()

                faka = []

                for inx, row in enumerate(data, start=1):
                    faka.append((inx, row[1], row[2], row[3], row[4], row[5]))

                    elif n == 3:
                    while True:

                        data = set3()
                        faka = []

                        for inx, row in enumerate(data, start=1):
                            faka.append((row[1], row[2], row[3], row[4], row[5]))

                        print(tabulate(faka, headers=["serial no", "Name", "Father_name", "City", "velage", "Phon_no"],
                                       tablefmt="pretty"))
                        print("\n1. specific person")

                print('\n~~~~~~~~~~~~ personal information table ~~~~~~~~~~~~~~~~~')

                print(tabulate(

                    faka,

                    headers=['Name', 'Father_name', 'City', 'velage', 'Phon_no'],

                    tablefmt="pretty"

                ))

                print("\n1. specific person")

                print("2. another menu")

                print("3. back")

                print("4. exit")

                a = int(input("enter your chose : "))

                if a == 1:
                    while True:
                        m = int(input("enter a sirial number :  "))
                        if 1 <= m <= len(data):
                            fkp_id = data[m - 1][0]

                            data2 = set7(fkp_id)
                            faka = []
                            if data2:

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

row = cursor.fetchall()

sales = int(input("enter your sales price :  "))
date = input("enter date of sales :  ")

cursor.execute("insert into sales(parsonal_id,Father_name,City,velage,Phon_no,upadan_name,colur,"
               "kena_mullo,Resive_date,sales_price,sales_date) "
               "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
               (*row[:10], sales, date))

db.commit()



































\

sales_price = int(input("Enter sales price: "))
sales_date = input("Enter sales date (yyyy-mm-dd): ")
cursor.execute(
    "SELECT upadan_name, colur, kena_mullo, fkp_id FROM product_desc WHERE fkp_id=%s",
    (user_id,))
product = cursor.fetchone()


# profit calculation
total_pro = sales_price - product[2]  # sales_price - buying_price
cus_pro = total_pro * 0.4  # customer profit example
com_pro = total_pro * 0.6  # company profit example

cursor.execute(
    "INSERT INTO sales2 (element, colour, buying_price, sales_price, sales_date, total_pro, cus_pro, com_pro,sales2_id) "
    "VALUES  (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
    (product[0], product[1], product[2], sales_price, sales_date, total_pro, cus_pro, com_pro, product[3])
)
db.commit()
print("✅ Sale recorded in new table")

if user_id in data5[0]:
    cursor.execute("insert into sales (parsonal_id ,name ,father_name ,city, velage ,phone) "
                   "select parsonal_id,Name,Father_name,City,velage,Phon_no from parsonal_info "
                   "where parsonal_id =%s", (user_id,))

    print("this parson is allrady added")
    continue





















































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

    total_pro = sales_p - result[2]
    cus_pro = total_pro * 0.4
    com_pro = total_pro * 0.6

    cursor.execute(
        "insert into sales2 (element ,colour ,buying_price ,sales_price ,sales_date ,total_pro ,cus_pro ,com_pro ,sales2_id )"
        "values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (result[0], result[1], result[2], sales_p, sales_d, total_pro, cus_pro, com_pro, user_id))

    db.commit()
    print("added successfully")