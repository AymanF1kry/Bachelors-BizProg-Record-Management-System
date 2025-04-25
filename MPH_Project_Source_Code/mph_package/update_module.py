import json
import time
import datetime

def updatemod(username):
    while True:
        try:
            time.sleep(1)
            print("\n"+"-"*(80)+"\n\n  Update Records"+
                " "*(57-len("  Update Records"))+"Welcome back, "+username+"!\n\n"+
                "-"*(80)+"\n")
            print("\n  Which records would you like to update?\n\n" +
                        "  1. Update customer purchase records.\n" +
                        "  2. Update book records.\n" +
                        "  3. Go back to main menu.\n")
            print("  Please key-in a number based on the options above.\n")
            time.sleep(0.5)
            option=input("  Option[Example: 1]: ")
            if option=="1":
                time.sleep(1)
                updateCustomer(username)
                return username
            elif option=="2":
                time.sleep(1)
                updateBook(username)
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
                
def updateCustomer(username):
    try:
        time.sleep(1)
        print("\n"+"-"*(80)+"\n\n  Update Customer Purchase Records"+
            " "*(57-len("  Update Customer Purchase Records"))+"Welcome back, "+username+"!\n\n"+
            "-"*(80)+"\n")
        with open("record_management.json", "r") as file:
            data = json.load(file)
            update_customer=data["customer_purchases"]
            update_bkdetails=data["books"]
            if len(update_customer)!=0:
                total_price=0
                total_quantity=0
                while True:
                    found=False
                    time.sleep(1)
                    print("\n  Please enter the customer's Purchase ID to search for the customer record.")
                    print("\n  +-------------+----------------------+----------------+---------------+"+
                            "\n  | Purchase ID | Customer Name        | Phone Number   | Purchase Date |"+
                            "\n  +-------------+----------------------+----------------+---------------+")
                    for i in range(len(update_customer)):
                        print("  |",update_customer[i].get("purchase_id")," "*(10-len(update_customer[i].get("purchase_id"))),"|",
                                update_customer[i].get("customer_name")," "*(19-len(update_customer[i].get("customer_name"))),"|",
                                update_customer[i].get("phone_number")," "*(13-len(update_customer[i].get("phone_number"))),"|",
                                update_customer[i].get("purchase_date")," "*(12-len(update_customer[i].get("purchase_date"))),"|")
                        print("  +-------------+----------------------+----------------+---------------+")
                    time.sleep(1)
                    cust_pcID=input("\n  Customer's Purchase ID[Example: PID138]: ")
                    for i in range(len(update_customer)):
                        if(update_customer[i].get("purchase_id")==cust_pcID):
                            pid_index = i
                            found=True
                            break
                    if found==True:
                        break
                    else:
                        print("\n  |-------------------------------------------------------------|"+
                                "\n  | Error Message: The customer purchase record does not appear |"+
                                "\n  | to exist. Please choose an existing Purchase ID as above.   |"+
                                "\n  |-------------------------------------------------------------|\n")
                time.sleep(1)
                print("\n  |--------------------------------------------------------------|"+
                        "\n  | Success Message: Gotcha! Found the customer purchase result. |"+
                        "\n  |--------------------------------------------------------------|\n")
                print("\n  Customer Purchase Record #"+str(pid_index+1))
                print("  Purchase ID:"," "+update_customer[pid_index].get("purchase_id")," "*(14-len(update_customer[pid_index].get("purchase_id")))," ","Customer Name:","   "+update_customer[pid_index].get("customer_name"))
                print("  Phone Number:",update_customer[pid_index].get("phone_number")," "*(14-len(update_customer[pid_index].get("phone_number")))," ","Date of Purchase:",update_customer[pid_index].get("purchase_date"))
                print("  +------------------------------------------------------------------------+"+
                    "\n  |                        Purchased Product                               |"+
                    "\n  +-----+-----------------+---------------+------------------+-------------+"+
                    "\n  | No. | Book Product ID | Product Price | Product Quantity | Subtotal    |"+
                    "\n  +-----+-----------------+---------------+------------------+-------------+")
                for num in range(len(update_customer[pid_index]["purchased_product"])):
                    print("  |",str(num+1)+"."," "*(2-len(str(num+1)+".")),"|",
                        update_customer[pid_index]["purchased_product"][num].get("book_product")," "*(14-len(str(update_customer[pid_index]["purchased_product"][num].get("book_product")))),"|",
                        update_customer[pid_index]["purchased_product"][num].get("product_price")," "*(12-len(update_customer[pid_index]["purchased_product"][num].get("product_price"))),"|",
                        update_customer[pid_index]["purchased_product"][num].get("product_quantity")," "*(15-len(str(update_customer[pid_index]["purchased_product"][num].get("product_quantity")))),"|",
                        update_customer[pid_index]["purchased_product"][num].get("subtotal")," "*(10-len(update_customer[pid_index]["purchased_product"][num].get("subtotal"))),"|")
                    print("  +-----+-----------------+---------------+------------------+-------------+")
                    if(num==(len(update_customer[pid_index]["purchased_product"])-1)):
                        print("  |","Total","                                |",update_customer[pid_index].get("total_quantity")," "*(15-len(str(update_customer[pid_index].get("total_quantity")))),"|",
                            update_customer[pid_index].get("total_price")," "*(10-len(str(update_customer[pid_index].get("total_price")))),"|")
                        print("  +------------------------------------------------------------------------+")
                print("\n  Press [1] to update the customer purchase record OR press any other key to cancel.")
                option=input("  Option[Example: 1]: ")
                if(option!="1"):
                    input("\n  Please press enter key to go back to main menu: ")
                    return username
                else:
                    print("\n  Purchase ID[Cannot be changed]:",update_customer[pid_index].get("purchase_id"))
                    time.sleep(1)
                    print("\n  Old Customer Name: "+update_customer[pid_index].get("customer_name"))
                    while True:
                        customer_name=input("\n  New Customer Name[Example: Ali bin Abu]: ")
                        time.sleep(1)
                        if(len(customer_name)>20 or len(customer_name)<3):
                            print("\n  |--------------------------------------------------|"+
                                "\n  | Error Message: The customer name must be between |"+
                                "\n  | 3 to 20 characters only. Please try again.       |"+
                                "\n  |--------------------------------------------------|\n")
                        elif(customer_name.replace(" ", "").isalpha()):
                            customer_name=customer_name.title()
                            update_custname=update_customer[pid_index]
                            update_custname.update({"customer_name":customer_name})
                            break
                        else:
                            print("\n  |--------------------------------------------------|"+
                                    "\n  | Error Message: The customer name can only be in  |"+
                                    "\n  | alphabet letters. Please try again.              |"+
                                    "\n  |--------------------------------------------------|\n")
                    time.sleep(1)
                    print("\n  Old Phone Number: "+update_customer[pid_index].get("phone_number").replace("+",""))
                    while True:
                        phone_number=input("\n  New Phone Number[Example: 0123456789]: ")
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
                                update_custphone=update_customer[pid_index]
                                update_custphone.update({"phone_number":phone_number})
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
                    time.sleep(1)
                    for i in range(len(update_customer[pid_index]["purchased_product"])):
                        old_quantity=update_customer[pid_index]["purchased_product"][i].get("product_quantity")
                        old_bookprod=update_customer[pid_index]["purchased_product"][i].get("book_product")
                        for y in range(len(update_bkdetails)):
                            if(update_bkdetails[y].get("book_id")==old_bookprod):
                                bid_index = y
                                break
                        old_stock=update_bkdetails[bid_index].get("book_stock")
                        update_bkdetails[bid_index].update({"book_stock":old_stock+old_quantity})
                    with open("record_management.json", "w") as file:
                        for i in range(len(update_customer[pid_index]["purchased_product"])):
                            del update_customer[pid_index]["purchased_product"][0]
                        json.dump(data, file, indent=4)
                    while True:
                        while True:
                            time.sleep(1)
                            print("\n  Please key-in a number to choose a book from the options below:")
                            print(  "\n  +-----+---------------------------------+-------------+------------+" +
                                    "\n  | No. | Book Title                      | Book Price  | Book Stock |" +
                                    "\n  +-----+---------------------------------+-------------+------------+")
                            for i in range(len(update_bkdetails)):
                                print("  |",str(i+1)+"."," "*(2-len(str(i+1)+".")),"|",
                                update_bkdetails[i].get("book_title")," "*(30-len(update_bkdetails[i].get("book_title"))),"|",
                                update_bkdetails[i].get("book_price")," "*(10-len(str(update_bkdetails[i].get("book_price")))),"|",
                                update_bkdetails[i].get("book_stock")," "*(9-len(str(update_bkdetails[i].get("book_stock")))),"|")
                                print("  +-----+---------------------------------+-------------+------------+")
                            try:
                                time.sleep(1)
                                book_index=int(input("\n  Book Product Number[Example: 1]: "))
                                if(book_index<1 or book_index>(len(update_bkdetails))):
                                    print("\n  |--------------------------------------------------------|"+
                                            "\n  | Error Message: The book product number does not appear |"+
                                            "\n  | to exist. Please choose from the options above only.   |"+
                                            "\n  |--------------------------------------------------------|\n")
                                    continue
                                if(update_bkdetails[book_index-1].get("book_stock")==0):
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
                        book_product=update_bkdetails[book_index].get("book_id")
                        product_price=update_bkdetails[book_index].get("book_price")
                        product_stock=update_bkdetails[book_index].get("book_stock")
                        while True:
                            time.sleep(1)
                            print("\n  Please select the number of books.")
                            print("\n  +-----+---------------------------------+-------------+------------+" +
                                    "\n  | No. | Book Title                      | Book Price  | Book Stock |" +
                                    "\n  +-----+---------------------------------+-------------+------------+")
                            print("  |",str(book_index+1)+"."," "*(2-len(str(book_index+1)+".")),"|",
                                update_bkdetails[book_index].get("book_title")," "*(30-len(update_bkdetails[book_index].get("book_title"))),"|",
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
                        found = False
                        with open("record_management.json", "w") as file:
                            variable_update=data["customer_purchases"][pid_index]
                            variable_update.update({"total_quantity":total_quantity})
                            variable_update.update({"total_price":"RM"+"{:.2f}".format(total_price)})
                            product_add=data["customer_purchases"][pid_index]["purchased_product"]
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
                        print("\n  Do you want to add more products?\n"+
                            "  Press [1] to add more product OR press any other key to stop adding products.\n")
                        time.sleep(1)
                        select=input("  Option[Example: 1]: ")
                        if select!="1":
                            datetime_format=datetime.date.today()
                            purchase_date=datetime.datetime.strftime(datetime_format, '%d/%m/%Y')
                            purchase_date=str(purchase_date)
                            print("\n  New Purchase Date[Auto generated]:",purchase_date)
                            update_customer[pid_index].update({"purchase_date":purchase_date})
                            break
                    with open("record_management.json", "w") as file:
                        json.dump(data, file, indent=4)
                    print("\n  |----------------------------------------------------------|"+
                            "\n  | Success Message: Well done! The customer purchase record |"+
                            "\n  | has successfully been updated in the database.           |"+
                            "\n  |----------------------------------------------------------|\n")
                    input("\n  Please press enter key to go back to main menu: ")
                    return username
            else:
                print("\n  |--------------------------------------------------------------|"+
                      "\n  | Error Message: There seems to be no customer purchase record |"+
                      "\n  | in the system. Please add a customer purchase record first.  |"+
                      "\n  |--------------------------------------------------------------|\n")
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
    
def updateBook(username):
    try:
        time.sleep(1)
        print("\n"+"-"*(80)+"\n\n  Update Book Records"+
            " "*(57-len("  Update Book Records"))+"Welcome back, "+username+"!\n\n"+
            "-"*(80)+"\n")
        with open("record_management.json", "r") as file:
            data = json.load(file)
            update_book=data["books"]
            if len(update_book)!=0:
                while True:
                    found=False
                    time.sleep(1)
                    print("\n  Please enter the Book ID to search for the book record.")
                    print("\n  +-----------+--------------------------------+----------------------+" +
                            "\n  | Book ID   | Book Title                     | Book Author          |" +
                            "\n  +-----------+--------------------------------+----------------------+")
                    for i in range(len(update_book)):
                        print("  |",update_book[i].get("book_id")," "*(8-len(update_book[i].get("book_id"))),"|",
                            update_book[i].get("book_title")," "*(29-len(update_book[i].get("book_title"))),"|",
                            update_book[i].get("book_author")," "*(19-len(update_book[i].get("book_author"))),"|")
                        print("  +-----------+--------------------------------+----------------------+")
                    time.sleep(1)
                    book_ID=input("\n  Book ID[Example: BID4748]: ")
                    for i in range(len(update_book)):
                        if(update_book[i].get("book_id")==book_ID):
                            bid_index = i
                            found=True
                            break
                    if found==True:
                        break
                    else:
                        print("\n  |----------------------------------------------------|"+
                                "\n  | Error Message: The book record does not appear to  |"+
                                "\n  | exist. Please choose an existing Book ID as above. |"+
                                "\n  |----------------------------------------------------|\n")
                time.sleep(1)
                print("\n  |-------------------------------------------------|"+
                        "\n  | Success Message: Gotcha! Found the book result. |"+
                        "\n  |-------------------------------------------------|\n")
                print("\n  Book Record #"+str(bid_index+1))
                print("  Book ID:",update_book[bid_index].get("book_id")," "*(8-len(update_book[bid_index].get("book_id")))," ","    Book Title:",update_book[bid_index].get("book_title"))
                print(  "  +------------------------------------------------------------------+"+
                        "\n  |                            Book Details                          |"+
                        "\n  +----------------------+----------------+-------------+------------+"+
                        "\n  | Book Author          | Book ISBN      | Book Price  | Book Stock |"+
                        "\n  +----------------------+----------------+-------------+------------+")
                print("  |",update_book[bid_index].get("book_author")," "*(19-len(update_book[bid_index].get("book_author"))),"|",
                    update_book[bid_index].get("book_isbn")," "*(13-len(update_book[bid_index].get("book_isbn"))),"|",
                    update_book[bid_index].get("book_price")," "*(10-len(str(update_book[bid_index].get("book_price")))),"|",
                    update_book[bid_index].get("book_stock")," "*(9-len(str(update_book[bid_index].get("book_stock")))),"|")
                print("  +----------------------+----------------+-------------+------------+")
                print("\n  Press [1] to update the book record OR press any other key to cancel.")
                option=input("  Option[Example: 1]: ")
                if(option!="1"):
                    input("\n  Please press enter key to go back to main menu: ")
                    return username       
                else:
                    print("\n  Book ID[Cannot be changed]:",update_book[bid_index].get("book_id"))
                    time.sleep(1)

                    print("\n  Old Book Title: "+update_book[bid_index].get("book_title"))
                    while True:
                        book_title=input("\n  New Book Title[Example:The Story of Life #1]: ")
                        if(len(book_title)>30 or len(book_title)<3):
                            print("\n  |-----------------------------------------------|"+
                                    "\n  | Error Message: The book title must be between |"+
                                    "\n  | 3 to 30 characters only. Please try again.    |"+
                                    "\n  |-----------------------------------------------|\n")
                        else:
                            book_title=book_title.title()
                            update_bktitle=update_book[bid_index]
                            update_bktitle.update({"book_title":book_title})
                            break
                    time.sleep(1)
                    print("\n  Old Book Author: "+update_book[bid_index].get("book_author"))
                    while True:
                        book_author=input("\n  New Book Author[Example: Ali bin Abu]: ")
                        if(len(book_author)>20 or len(book_author)<3):
                            print("\n  |------------------------------------------------|"+
                                    "\n  | Error Message: The book author must be between |"+
                                    "\n  | 3 to 20 characters only. Please try again.     |"+
                                    "\n  |------------------------------------------------|\n")
                        elif(book_author.replace("&", "").replace(",", "").replace(" ", "").isalpha()):
                            book_author=book_author.title()
                            update_bkauthor=update_book[bid_index]
                            update_bkauthor.update({"book_author":book_author})
                            break
                        else:
                            print("\n  |-----------------------------------------------|"+
                                    "\n  | Error Message: The book author can only be in |"+
                                    "\n  | alphabet letters. Please try again.           |"+
                                    "\n  |-----------------------------------------------|\n")
                    time.sleep(1)
                    print("\n  Book ISBN[Cannot be changed]:",update_book[bid_index].get("book_isbn"))
                    time.sleep(1)
                    print("\n  Old Book Price: "+update_book[bid_index].get("book_price"))
                    while True:
                        try:
                            book_price=float(input("\n  New Book Price[Example: 54.96]: RM"))
                            if(book_price<=0):
                                print("\n  |---------------------------------------|"+
                                        "\n  | Error Message: The book price must be |"+
                                        "\n  | more than 0. Please try again.        |"+
                                        "\n  |---------------------------------------|\n")
                                continue
                            book_price="RM"+"{:.2f}".format(book_price)
                            update_bkprice=update_book[bid_index]
                            update_bkprice.update({"book_price":book_price})
                            break
                        except ValueError as ve:
                            print("\n  |------------------------------------------|"+
                                    "\n  | Error Message: The book price can only   |"+
                                    "\n  | be in numeral numbers. Please try again. |"+
                                    "\n  |------------------------------------------|\n")
                    time.sleep(1)
                    print("\n  Old Book Stock: "+str(update_book[bid_index].get("book_stock")))
                    while True:
                        try:
                            book_stock=int(input("\n  New Book Stock[Example: 10]: "))
                            if(book_stock<1):
                                print("\n  |---------------------------------------|"+
                                        "\n  | Error Message: The book stock must be |"+
                                        "\n  | more than 0. Please try again.        |"+
                                        "\n  |---------------------------------------|\n")
                                continue
                            update_bkstock=update_book[bid_index]
                            update_bkstock.update({"book_stock":book_stock})
                            break
                        except ValueError as ve:
                            print("\n  |-------------------------------------------|"+
                                    "\n  | Error Message: The book stock can only be |"+
                                    "\n  | in numeral numbers. Please try again.     |"+
                                    "\n  |-------------------------------------------|\n")
                    time.sleep(1)
                    with open("record_management.json", "w") as file:
                        json.dump(data, file, indent=4)

                    print("\n  |-------------------------------------------------|"+
                            "\n  | Success Message: Well done! The book record has |"+
                            "\n  | successfully been updated in the database.      |"+
                            "\n  |-------------------------------------------------|\n")
                    input("\n  Please press enter key to go back to main menu: ")
                    return username
            else:
                print("\n  |-------------------------------------------------|"+
                      "\n  | Error Message: There seems to be no book record |"+
                      "\n  | in the system. Please add a book record first.  |"+
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
    
    