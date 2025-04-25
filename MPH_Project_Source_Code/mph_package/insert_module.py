import json
import random
import time
import datetime

def insertmod(username):
    while True:
        try:
            time.sleep(1)
            print("\n"+"-"*(80)+"\n\n  Add New Records"+
                " "*(57-len("  Add New Records"))+"Welcome back, "+username+"!\n\n"+
                "-"*(80)+"\n")
            print("\n  Which records would you like to add?\n\n" +
                        "  1. Add new customer purchase records.\n" +
                        "  2. Add new book records.\n" +
                        "  3. Go back to main menu.\n")
            print("  Please key-in a number based on the options above.\n")
            time.sleep(0.5)
            option=input("  Option[Example: 1]: ")
            if option=="1":
                time.sleep(1)
                addCustomer(username)
                return username
            elif option=="2":
                time.sleep(1)
                addBook(username)
                return username
            elif option=="3":
                return username
            else: 
                print("\n  |-----------------------------------------------------|"+
                      "\n  | Error Message: The option does not appear to exist. |"+
                      "\n  | Please only choose option 1 to 3.                   |"+
                      "\n  |-----------------------------------------------------|\n")
        except KeyboardInterrupt:
            print("\n\n  |-----------------------------------------------------------------|"+
                    "\n  | Error Message: It looks like you accidentally pressed ctrl + C. |" +
                    "\n  | It's ok we all make mistakes sometimes.                         |"+
                    "\n  |---------------------------------------------------------------- |\n")
            time.sleep(2)
            option=input("\n  [Press 0 to exit the system] OR "+
                         "\n  [Press any other key to continue where you left off] : ")
            time.sleep(1)
            if(option=="0"):
                print("\n\n\n  Shutting down system.... in 5")
                for i in range(4,0,-1):
                    time.sleep(1)
                    print("\n  ...",i)
                print("\n  Thank you "+username+" for using the MPH Record Management System." +
                      "\n  Goodbye :)\n\n")
                exit()
   
def addCustomer(username):
    total_price=0
    total_quantity=0
    try:
        print("\n"+"-"*(80)+"\n\n  Add Customer Purchase Records"+
                " "*(57-len("  Add Customer Purchase Records"))+"Welcome back, "+username+"!\n\n"+
                "-"*(80)+"\n")
        with open("record_management.json", "r") as file:
            data = json.load(file)
            check_book=data["books"]
            insert_customer=data["customer_purchases"]
            if len(check_book)==0:
                print("\n  |--------------------------------------------------|"+
                      "\n  | Error Message: There seems to be no book records |"+
                      "\n  | in the system. Please add a book record first.   |"+
                      "\n  |--------------------------------------------------|\n")
                
                input("\n  Please press enter key to go back to main menu: ")
                return username
            else:
                print("\n  Please enter the required information for the customer purchase record.")
                select="0"
                purchase_id= "PID" + str(random.randint(100, 1000))
                for i in range(len(insert_customer)):
                    for i in range(len(insert_customer)):
                        if(insert_customer[i].get("purchase_id")==purchase_id):
                            purchase_id= "PID" + str(random.randint(100, 1000))
                print("\n  Purchase ID[Auto Generated]: "+purchase_id)
                time.sleep(1)
                while True:
                    customer_name=input("\n  Customer Name[Example: Ali bin Abu]: ")
                    time.sleep(1)
                    if(len(customer_name)>20 or len(customer_name)<3):
                        print("\n  |--------------------------------------------------|"+
                              "\n  | Error Message: The customer name must be between |"+
                              "\n  | 3 to 20 characters only. Please try again.       |"+
                              "\n  |--------------------------------------------------|\n")
                    elif(customer_name.replace(" ", "").isalpha()):
                        customer_name=customer_name.title()
                        break
                    else:
                        print("\n  |--------------------------------------------------|"+
                              "\n  | Error Message: The customer name can only be in  |"+
                              "\n  | alphabet letters. Please try again.              |"+
                              "\n  |--------------------------------------------------|\n")
                time.sleep(1)
                while True:
                    phone_number=input("\n  Phone Number[Example: 0123456789]: ")
                    time.sleep(1)
                    if(phone_number.isnumeric()):
                        if(len(phone_number)>=10 and len(phone_number)<=11):
                            while True:
                                print("\n  Is this a Malaysian number?")
                                num_type=input("\n  Type [1] for Yes OR Type [2] for No: ")
                                if(num_type=="1"):
                                    phone_number="+6"+phone_number
                                    break
                                elif(num_type=="2"):
                                    phone_number="+"+phone_number
                                    break
                                else:
                                    print("\n  |-----------------------------------------------------|"+
                                          "\n  | Error Message: The option does not appear to exist. |"+
                                          "\n  | Please choose only option 1 or 2.                   |"+
                                          "\n  |-----------------------------------------------------|\n")
                            break
                        else:
                            print("\n  |-------------------------------------------------|"+
                                  "\n  | Error Message: The phone number must be between |"+
                                  "\n  | 10 to 11 numbers only. Please try again.        |"+
                                  "\n  |-------------------------------------------------|\n")
                    else:
                        print("\n  |--------------------------------------------------|"+
                              "\n  | Error Message: The phone number can only contain |"+
                              "\n  | numeral numbers. Please try again.               |"+
                              "\n  |--------------------------------------------------|\n")
                while True:
                    while True:
                        time.sleep(1)
                        print("\n  Please key-in a number to choose a book from the options below:")
                        print(  "\n  +-----+---------------------------------+-------------+------------+" +
                                "\n  | No. | Book Title                      | Book Price  | Book Stock |" +
                                "\n  +-----+---------------------------------+-------------+------------+")
                        for i in range(len(check_book)):
                            print("  |",str(i+1)+"."," "*(2-len(str(i+1)+".")),"|",
                            check_book[i].get("book_title")," "*(30-len(check_book[i].get("book_title"))),"|",
                            check_book[i].get("book_price")," "*(10-len(str(check_book[i].get("book_price")))),"|",
                            check_book[i].get("book_stock")," "*(9-len(str(check_book[i].get("book_stock")))),"|")
                            print("  +-----+---------------------------------+-------------+------------+")
                        try:
                            time.sleep(1)
                            book_index=int(input("\n  Book Product Number[Example: 1]: "))
                            if(book_index<1 or book_index>(len(check_book))):
                                print("\n  |--------------------------------------------------------|"+
                                      "\n  | Error Message: The book product number does not appear |"+
                                      "\n  | to exist. Please choose from the options above only.   |"+
                                      "\n  |--------------------------------------------------------|\n")
                                continue
                            if(check_book[book_index-1].get("book_stock")==0):
                                print("\n  |-------------------------------------------------------|"+
                                      "\n  | Error Message: The product is currently out of stock. |"+
                                      "\n  | Please choose another product.                        |"+
                                      "\n  |-------------------------------------------------------|\n")
                                continue
                            book_index=book_index-1
                            break
                        except ValueError:
                            print("\n  |--------------------------------------------------------|"+
                                  "\n  | Error Message: The book product number does not appear |"+
                                  "\n  | to exist. Please choose from the options above only.   |"+
                                  "\n  |--------------------------------------------------------|\n")
                    book_product=check_book[book_index].get("book_id")
                    product_price=check_book[book_index].get("book_price")
                    product_stock=check_book[book_index].get("book_stock")
                    while True:
                        time.sleep(1)
                        print("\n  Please select the number of books.")
                        print("\n  +-----+---------------------------------+-------------+------------+" +
                              "\n  | No. | Book Title                      | Book Price  | Book Stock |" +
                              "\n  +-----+---------------------------------+-------------+------------+")
                        print("  |",str(book_index+1)+"."," "*(2-len(str(book_index+1)+".")),"|",
                            check_book[book_index].get("book_title")," "*(30-len(check_book[book_index].get("book_title"))),"|",
                            product_price," "*(10-len(str(product_price))),"|",
                            product_stock," "*(9-len(str(product_stock))),"|")
                        print(  "  +-----+---------------------------------+-------------+------------+")
                        try:
                            time.sleep(1)
                            product_quantity=int(input("\n  Product Quantity[Example: 1]: "))
                            if(product_quantity>product_stock):
                                print("\n  |-------------------------------------------|"+
                                      "\n  | Error Message: The quantity exceeds the   |"+
                                      "\n  | product stock. Please choose accordingly. |"+
                                      "\n  |-------------------------------------------|\n")
                                continue
                            if(product_quantity<1):
                                print("\n  |-------------------------------------------|"+
                                      "\n  | Error Message: The quantity must be more  |"+
                                      "\n  | than 0. Please choose a higher number.    |"+
                                      "\n  |-------------------------------------------|\n")
                                continue
                            break
                        except ValueError:
                            print("\n  |--------------------------------------|"+
                                  "\n  | Error Message: The quantity can only |"+
                                  "\n  | be in numerals. Please try again.    |"+
                                  "\n  |--------------------------------------|\n")
                    product_price=product_price.replace("RM","")
                    product_price=float(product_price)
                    book_stock=product_stock-product_quantity
                    update_stock=data["books"][book_index]
                    update_stock.update({"book_stock":book_stock})
                    total_quantity=total_quantity+product_quantity
                    subtotal=product_price*product_quantity
                    total_price=total_price+subtotal
                    temp_price="RM"+"{:.2f}".format(total_price)
                    print("\n  Total Price[Auto generated]:",temp_price)
                    product_data = {
                        "book_product": book_product,
                        "product_price":"RM"+"{:.2f}".format(product_price),
                        "product_quantity":product_quantity,
                        "subtotal":"RM"+"{:.2f}".format(subtotal)
                        }
                    if(select=="1"):
                        found = False
                        with open("record_management.json", "w") as file:
                            variable_update=data["customer_purchases"][len(insert_customer)-1]
                            variable_update.update({"total_quantity":total_quantity})
                            variable_update.update({"total_price":"RM"+"{:.2f}".format(total_price)})
                            product_add=data["customer_purchases"][len(insert_customer)-1]["purchased_product"]
                            for i in range(len(product_add)):
                                if(product_add[i].get("book_product")==book_product):
                                    product_add[i].update({"product_quantity":product_add[i].get("product_quantity")+product_quantity})
                                    subtotal_temp=float(product_add[i].get("subtotal").replace("RM",""))
                                    product_add[i].update({"subtotal":"RM"+"{:.2f}".format(subtotal_temp+subtotal)})
                                    found = True
                                    break
                            if found == False:    
                                product_add.append(product_data)
                            json.dump(data, file, indent=6)
                    else:
                        datetime_format=datetime.date.today()
                        purchase_date=datetime.datetime.strftime(datetime_format, '%d/%m/%Y')
                        purchase_date=str(purchase_date)
                        print("\n  Purchase Date[Auto generated]:",purchase_date)
                        customer_data =  {
                            "purchase_id": purchase_id, 
                            "customer_name": customer_name,
                            "phone_number": phone_number,
                            "purchased_product":[product_data],
                            "total_quantity":total_quantity,
                            "total_price":"RM"+"{:.2f}".format(total_price),
                            "purchase_date":purchase_date
                            }
                        with open("record_management.json", "w") as file:
                            insert_customer.append(customer_data)
                            json.dump(data, file, indent=4)
                    print("\n  Do you want to add more products?\n"+
                        "  Press [1] to add more product OR press any other key to stop adding products.\n")
                    time.sleep(1)
                    select=input("  Option[Example: 1]: ")
                    if select!="1":
                        break
        print("\n  |----------------------------------------------------------|"+
              "\n  | Success Message: Well done! The customer purchase record |"+
              "\n  | has successfully been recorded in the database.          |"+
              "\n  |----------------------------------------------------------|\n")
        input("\n  Please press enter key to go back to main menu: ")
        return username
    except KeyboardInterrupt:
        print("\n\n  |-----------------------------------------------------------------|"+
                "\n  | Error Message: It looks like you accidentally pressed ctrl + C. |" +
                "\n  | It's ok we all make mistakes sometimes.                         |"+
                "\n  |---------------------------------------------------------------- |\n")
        time.sleep(2)
        option=input("\n  [Press 0 to exit the system] OR "+
                     "\n  [Press any other key to continue where you left off] : ")
        time.sleep(1)
        if(option=="0"):
            print("\n\n\n  Shutting down system.... in 5")
            for i in range(4,0,-1):
                time.sleep(1)
                print("\n  ...",i)
            print("\n  Thank you "+username+" for using the MPH Record Management System." +
                "\n  Goodbye :)\n\n")
            exit()
    
def addBook(username):
    try:
        time.sleep(1)
        print("\n"+"-"*(80)+"\n\n  Add Book Records"+
            " "*(57-len("  Add Book Records"))+"Welcome back, "+username+"!\n\n"+
            "-"*(80)+"\n")
        print("\n  Please enter the required information for the book record.")
        with open("record_management.json", "r") as file:
            data = json.load(file)
            insert_book=data["books"]
            book_id= "BID" + str(random.randint(1000, 10000))
            for i in range(len(insert_book)):
                for i in range(len(insert_book)):
                    if(insert_book[i].get("book_id")==book_id):
                        book_id= "BID" + str(random.randint(1000, 10000))
            print("\n  Book ID[Auto Generated]: " +book_id)
            time.sleep(1)
            while True:
                book_title=input("\n  Book Title[Example:The Story of Life #1]: ")
                if(len(book_title)>30 or len(book_title)<3):
                    print("\n  |-----------------------------------------------|"+
                          "\n  | Error Message: The book title must be between |"+
                          "\n  | 3 to 30 characters only. Please try again.    |"+
                          "\n  |-----------------------------------------------|\n")
                else:
                    book_title=book_title.title()
                    break
                time.sleep(1)
            while True:
                book_author=input("\n  Book Author[Example: Ali bin Abu]: ")
                if(len(book_author)>20 or len(book_author)<3):
                    print("\n  |------------------------------------------------|"+
                          "\n  | Error Message: The book author must be between |"+
                          "\n  | 3 to 20 characters only. Please try again.     |"+
                          "\n  |------------------------------------------------|\n")
                elif(book_author.replace("&", "").replace(",", "").replace(" ", "").isalpha()):
                    book_author=book_author.title()
                    break
                else:
                    print("\n  |-----------------------------------------------|"+
                          "\n  | Error Message: The book author can only be in |"+
                          "\n  | alphabet letters. Please try again.           |"+
                          "\n  |-----------------------------------------------|\n")
            time.sleep(1)
            book_isbn= str(random.randint(9000000000000, 9999999999999))
            for i in range(len(insert_book)):
                for i in range(len(insert_book)):
                    if(insert_book[i].get("book_isbn")==book_isbn):
                        book_isbn= str(random.randint(9000000000000, 9999999999999))
            print("\n  Book ISBN[Auto Generated]: " +book_isbn)
            time.sleep(1)
            while True:
                try:
                    
                    book_price=float(input("\n  Book Price[Example: 54.96]: RM"))
                    if(book_price<=0):
                        print("\n  |---------------------------------------|"+
                              "\n  | Error Message: The book price must be |"+
                              "\n  | more than 0. Please try again.        |"+
                              "\n  |---------------------------------------|\n")
                        continue
                    book_price="RM"+"{:.2f}".format(book_price)
                    break
                except ValueError:
                    print("\n  |------------------------------------------|"+
                          "\n  | Error Message: The book price can only   |"+
                          "\n  | be in numeral numbers. Please try again. |"+
                          "\n  |------------------------------------------|\n")
            time.sleep(1)
            while True:
                try:
                    book_stock=int(input("\n  Book Stock[Example: 10]: "))
                    if(book_stock<1):
                        print("\n  |---------------------------------------|"+
                              "\n  | Error Message: The book stock must be |"+
                              "\n  | more than 0. Please try again.        |"+
                              "\n  |---------------------------------------|\n")
                        continue
                    break
                except ValueError:
                    print("\n  |-------------------------------------------|"+
                          "\n  | Error Message: The book stock can only be |"+
                          "\n  | in numeral numbers. Please try again.     |"+
                          "\n  |-------------------------------------------|\n")
            time.sleep(1)
        book_data = {
            "book_id":book_id,
            "book_title":book_title,
            "book_author":book_author,
            "book_isbn":book_isbn,
            "book_price":book_price,
            "book_stock":book_stock
        }
        with open("record_management.json", "w") as file:
            insert_book.append(book_data)
            json.dump(data, file, indent=4)
        print("\n  |-------------------------------------------------|"+
              "\n  | Success Message: Well done! The book record has |"+
              "\n  | successfully been recorded in the database.     |"+
              "\n  |-------------------------------------------------|\n")
        input("\n  Please press enter key to go back to main menu: ")
        return username
    except KeyboardInterrupt:
            print("\n\n  |-----------------------------------------------------------------|"+
                    "\n  | Error Message: It looks like you accidentally pressed ctrl + C. |" +
                    "\n  | It's ok we all make mistakes sometimes.                         |"+
                    "\n  |---------------------------------------------------------------- |\n")
            time.sleep(2)
            option=input("\n  [Press 0 to exit the system] OR "+
                         "\n  [Press any other key to continue where you left off] : ")
            time.sleep(1)
            if(option=="0"):
                print("\n\n\n  Shutting down system.... in 5")
                for i in range(4,0,-1):
                    time.sleep(1)
                    print("\n  ...",i)
                print("\n  Thank you "+username+" for using the MPH Record Management System." +
                      "\n  Goodbye :)\n\n")
                exit()
   