import json
import time

def searchmod(username):
    while True:
        try: 
            time.sleep(1)
            print("\n"+"-"*(80)+"\n\n  Search Records"+
                " "*(57-len("  Search Records"))+"Welcome back, "+username+"!\n\n"+
                "-"*(80)+"\n")
        
        
            print("\n  Which records would you like to search for?\n\n" +
                        "  1. Seach for customer purchase records.\n" +
                        "  2. Search for book records.\n" +
                        "  3. Go back to main menu.\n")
            print("  Please key-in a number based on the options above.\n")
            time.sleep(1)
            option=input("  Option[Example: 1]: ")
            if option=="1":
                time.sleep(1)
                searchCustomer(username)
                return username
            elif option=="2":
                time.sleep(1)
                searchBook(username)
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
                
def searchCustomer(username):
    try:
        time.sleep(1)
        print("\n"+"-"*(80)+"\n\n  Search Customer Purchase Records"+
            " "*(57-len("  Search Customer Purchase Records"))+"Welcome back, "+username+"!\n\n"+
            "-"*(80)+"\n")
        with open("record_management.json", "r") as file:
            data = json.load(file)
            search_customer=data["customer_purchases"]
            if len(search_customer)!=0:
                while True:
                    found=False
                    time.sleep(1)
                    print("\n  Please enter the customer's Purchase ID to search for the customer record.")
                    print(  "\n  +-------------+----------------------+----------------+---------------+"+
                            "\n  | Purchase ID | Customer Name        | Phone Number   | Purchase Date |"+
                            "\n  +-------------+----------------------+----------------+---------------+")
                    for i in range(len(search_customer)):
                        print("  |",search_customer[i].get("purchase_id")," "*(10-len(search_customer[i].get("purchase_id"))),"|",
                                search_customer[i].get("customer_name")," "*(19-len(search_customer[i].get("customer_name"))),"|",
                                search_customer[i].get("phone_number")," "*(13-len(search_customer[i].get("phone_number"))),"|",
                                search_customer[i].get("purchase_date")," "*(12-len(search_customer[i].get("purchase_date"))),"|")
                        print("  +-------------+----------------------+----------------+---------------+")
                    time.sleep(1)
                    cust_pcID=input("\n  Customer's Purchase ID[Example: PID138]: ")
                    for i in range(len(search_customer)):
                        if(search_customer[i].get("purchase_id")==cust_pcID):
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
                print("  Purchase ID:"," "+search_customer[pid_index].get("purchase_id")," "*(14-len(search_customer[pid_index].get("purchase_id")))," ","Customer Name:","   "+search_customer[pid_index].get("customer_name"))
                print("  Phone Number:",search_customer[pid_index].get("phone_number")," "*(14-len(search_customer[pid_index].get("phone_number")))," ","Date of Purchase:",search_customer[pid_index].get("purchase_date"))
                print("  +------------------------------------------------------------------------+"+
                    "\n  |                        Purchased Product                               |"+
                    "\n  +-----+-----------------+---------------+------------------+-------------+"+
                    "\n  | No. | Book Product ID | Product Price | Product Quantity | Subtotal    |"+
                    "\n  +-----+-----------------+---------------+------------------+-------------+")
                for num in range(len(search_customer[pid_index]["purchased_product"])):
                    print("  |",str(num+1)+"."," "*(2-len(str(num+1)+".")),"|",
                        search_customer[pid_index]["purchased_product"][num].get("book_product")," "*(14-len(str(search_customer[pid_index]["purchased_product"][num].get("book_product")))),"|",
                        search_customer[pid_index]["purchased_product"][num].get("product_price")," "*(12-len(search_customer[pid_index]["purchased_product"][num].get("product_price"))),"|",
                        search_customer[pid_index]["purchased_product"][num].get("product_quantity")," "*(15-len(str(search_customer[pid_index]["purchased_product"][num].get("product_quantity")))),"|",
                        search_customer[pid_index]["purchased_product"][num].get("subtotal")," "*(10-len(search_customer[pid_index]["purchased_product"][num].get("subtotal"))),"|")
                    print("  +-----+-----------------+---------------+------------------+-------------+")
                    if(num==(len(search_customer[pid_index]["purchased_product"])-1)):
                        print("  |","Total","                                |",search_customer[pid_index].get("total_quantity")," "*(15-len(str(search_customer[pid_index].get("total_quantity")))),"|",
                            search_customer[pid_index].get("total_price")," "*(10-len(str(search_customer[pid_index].get("total_price")))),"|")
                        print("  +------------------------------------------------------------------------+")
                input("\n  Press enter any key to go back to main menu: ")
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

def searchBook(username):
    try:
        time.sleep(1)
        print("\n"+"-"*(80)+"\n\n  Search Book Records"+
            " "*(57-len("  Search Book Records"))+"Welcome back, "+username+"!\n\n"+
            "-"*(80)+"\n")
        with open("record_management.json", "r") as file:
            data = json.load(file)
            search_book=data["books"]
            if len(search_book)!=0:
                while True:
                    found=False
                    time.sleep(1)
                    print("\n  Please enter the Book ID to search for the book record.")
                    print("\n  +-----------+--------------------------------+----------------------+" +
                            "\n  | Book ID   | Book Title                     | Book Author          |" +
                            "\n  +-----------+--------------------------------+----------------------+")
                    for i in range(len(search_book)):
                        print("  |",search_book[i].get("book_id")," "*(8-len(search_book[i].get("book_id"))),"|",
                            search_book[i].get("book_title")," "*(29-len(search_book[i].get("book_title"))),"|",
                            search_book[i].get("book_author")," "*(19-len(search_book[i].get("book_author"))),"|")
                        print("  +-----------+--------------------------------+----------------------+")
                    time.sleep(1)
                    book_ID=input("\n  Book ID[Example: BID4748]: ")
                    for i in range(len(search_book)):
                        if(search_book[i].get("book_id")==book_ID):
                            bid_index = i
                            found=True
                            break
                    if found==True:
                        break
                    else:
                        print(  "\n  |----------------------------------------------------|"+
                                "\n  | Error Message: The book record does not appear to  |"+
                                "\n  | exist. Please choose an existing Book ID as above. |"+
                                "\n  |----------------------------------------------------|\n")
                time.sleep(1)
                print(  "\n  |-------------------------------------------------|"+
                        "\n  | Success Message: Gotcha! Found the book result. |"+
                        "\n  |-------------------------------------------------|\n")
                print("\n  Book Record #"+str(bid_index+1))
                print("  Book ID:",search_book[bid_index].get("book_id")," "*(8-len(search_book[bid_index].get("book_id")))," ","    Book Title:",search_book[bid_index].get("book_title"))
                print(  "  +------------------------------------------------------------------+"+
                      "\n  |                            Book Details                          |"+
                      "\n  +----------------------+----------------+-------------+------------+"+
                      "\n  | Book Author          | Book ISBN      | Book Price  | Book Stock |"+
                      "\n  +----------------------+----------------+-------------+------------+")
                print("  |",search_book[bid_index].get("book_author")," "*(19-len(search_book[bid_index].get("book_author"))),"|",
                    search_book[bid_index].get("book_isbn")," "*(13-len(search_book[bid_index].get("book_isbn"))),"|",
                    search_book[bid_index].get("book_price")," "*(10-len(str(search_book[bid_index].get("book_price")))),"|",
                    search_book[bid_index].get("book_stock")," "*(9-len(str(search_book[bid_index].get("book_stock")))),"|")
                print("  +----------------------+----------------+-------------+------------+")
                input("\n  Press enter any key to go back to main menu: ")
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
