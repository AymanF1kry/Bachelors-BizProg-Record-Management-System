import json
import time

def deletemod(username):
    while True:
        try:
            time.sleep(1)
            print("\n"+"-"*(80)+"\n\n  Delete Records"+
                    " "*(57-len("  Delete Records"))+"Welcome back, "+username+"!\n\n"+
                    "-"*(80)+"\n")
            print("\n  Which records would you like to delete?\n\n" +
                            "  1. Delete customer purchase records.\n" +
                            "  2. Delete book records.\n" +
                            "  3. Go back to main menu.\n")
            print("  Please key-in a number based on the options above.\n")
            time.sleep(1)
            option=input("  Option[Example: 1]: ")
            if option=="1":
                deleteCustomer(username)
                return username
            elif option=="2":
                deleteBook(username)
                return username
            elif option=="3":
                return username
            else:
                print(  "\n  |-----------------------------------------------------|"+
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
    
def deleteCustomer(username):
    try:
        time.sleep(1)
        print("\n"+"-"*(80)+"\n\n  Delete One Customer Purchase Record"+
                " "*(57-len("  Delete One Customer Purchase Record"))+"Welcome back, "+username+"!\n\n"+
                "-"*(80)+"\n")
        with open("record_management.json", "r") as file:
            data = json.load(file)
            delete_customer=data["customer_purchases"]
            if len(delete_customer)!=0:
                while True:
                    found=False
                    time.sleep(1)
                    print("\n  Please enter the Customer's Purchase ID to delete the customer record.")
                    print(  "\n  +-------------+----------------------+----------------+---------------+"+
                            "\n  | Purchase ID | Customer Name        | Phone Number   | Purchase Date |"+
                            "\n  +-------------+----------------------+----------------+---------------+")
                    for i in range(len(delete_customer)):
                        print("  |",delete_customer[i].get("purchase_id")," "*(10-len(delete_customer[i].get("purchase_id"))),"|",
                            delete_customer[i].get("customer_name")," "*(19-len(delete_customer[i].get("customer_name"))),"|",
                            delete_customer[i].get("phone_number")," "*(13-len(delete_customer[i].get("phone_number"))),"|",
                            delete_customer[i].get("purchase_date")," "*(12-len(delete_customer[i].get("purchase_date"))),"|")
                        print("  +-------------+----------------------+----------------+---------------+")
                    time.sleep(1)
                    cust_pcID=input("\n  Customer's Purchase ID[Example: PID138]: ")
                    for i in range(len(delete_customer)):
                        if(delete_customer[i].get("purchase_id")==cust_pcID):
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
                print("\n  Customer Purchase Record #"+str(pid_index+1))
                print("  Purchase ID:"," "+delete_customer[pid_index].get("purchase_id")," "*(14-len(delete_customer[pid_index].get("purchase_id")))," ","Customer Name:","   "+delete_customer[pid_index].get("customer_name"))
                print("  Phone Number:",delete_customer[pid_index].get("phone_number")," "*(14-len(delete_customer[pid_index].get("phone_number")))," ","Date of Purchase:",delete_customer[pid_index].get("purchase_date"))
                print("  +------------------------------------------------------------------------+"+
                    "\n  |                        Purchased Product                               |"+
                    "\n  +-----+-----------------+---------------+------------------+-------------+"+
                    "\n  | No. | Book Product ID | Product Price | Product Quantity | Subtotal    |"+
                    "\n  +-----+-----------------+---------------+------------------+-------------+")
                for num in range(len(delete_customer[pid_index]["purchased_product"])):
                    print("  |",str(num+1)+"."," "*(2-len(str(num+1)+".")),"|",
                        delete_customer[pid_index]["purchased_product"][num].get("book_product")," "*(14-len(str(delete_customer[pid_index]["purchased_product"][num].get("book_product")))),"|",
                        delete_customer[pid_index]["purchased_product"][num].get("product_price")," "*(12-len(delete_customer[pid_index]["purchased_product"][num].get("product_price"))),"|",
                        delete_customer[pid_index]["purchased_product"][num].get("product_quantity")," "*(15-len(str(delete_customer[pid_index]["purchased_product"][num].get("product_quantity")))),"|",
                        delete_customer[pid_index]["purchased_product"][num].get("subtotal")," "*(10-len(delete_customer[pid_index]["purchased_product"][num].get("subtotal"))),"|")
                    print("  +-----+-----------------+---------------+------------------+-------------+")
                    if(num==(len(delete_customer[pid_index]["purchased_product"])-1)):
                        print("  |","Total","                                |",delete_customer[pid_index].get("total_quantity")," "*(15-len(str(delete_customer[pid_index].get("total_quantity")))),"|",
                            delete_customer[pid_index].get("total_price")," "*(10-len(str(delete_customer[pid_index].get("total_price")))),"|")
                        print("  +------------------------------------------------------------------------+")
                print("\n  Are you sure you want to delete the customer purchase record?\n"+
                    "\n  Press [1] if you want to delete it OR press any other key to cancel.")
                time.sleep(1)
                option=input("  Option[Example: 1]: ")
                if(option=="1"):
                    with open("record_management.json", "w") as file:
                        del delete_customer[pid_index]
                        json.dump(data, file, indent=4)
                    print(  "\n  |------------------------------------------------|"+
                            "\n  | Success Message: The customer purchase record  |"+
                            "\n  | has successfully been deleted from the system. |"+
                            "\n  |------------------------------------------------|\n")
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
       
def deleteBook(username):
    try:
        time.sleep(1)
        print("\n"+"-"*(80)+"\n\n  Delete One Book Record"+
                " "*(57-len("  Delete One Book Record"))+"Welcome back, "+username+"!\n\n"+
                "-"*(80)+"\n")
        with open("record_management.json", "r") as file:
            data = json.load(file)
            delete_book=data["books"]
            if len(delete_book)!=0:
                while True:
                    found=False
                    time.sleep(1)
                    print("\n  Please enter the Book ID to delete the book record.")
                    print("\n  +-----------+--------------------------------+----------------------+" +
                        "\n  | Book ID   | Book Title                     | Book Author          |" +
                        "\n  +-----------+--------------------------------+----------------------+")
                    for i in range(len(delete_book)):
                        print("  |",delete_book[i].get("book_id")," "*(8-len(delete_book[i].get("book_id"))),"|",
                            delete_book[i].get("book_title")," "*(29-len(delete_book[i].get("book_title"))),"|",
                            delete_book[i].get("book_author")," "*(19-len(delete_book[i].get("book_author"))),"|")
                        print("  +-----------+--------------------------------+----------------------+")
                        time.sleep(1)
                    book_ID=input("\n  Book ID[Example: BID4748]: ")
                    for i in range(len(delete_book)):
                        if(delete_book[i].get("book_id")==book_ID):
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
                print("\n  Book Record #"+str(bid_index+1))
                print("  Book ID:",delete_book[bid_index].get("book_id")," "*(8-len(delete_book[bid_index].get("book_id")))," ","    Book Title:",delete_book[bid_index].get("book_title"))
                print(  "  +------------------------------------------------------------------+"+
                    "\n  |                            Book Details                          |"+
                    "\n  +----------------------+----------------+-------------+------------+"+
                    "\n  | Book Author          | Book ISBN      | Book Price  | Book Stock |"+
                    "\n  +----------------------+----------------+-------------+------------+")
                print("  |",delete_book[bid_index].get("book_author")," "*(19-len(delete_book[bid_index].get("book_author"))),"|",
                    delete_book[bid_index].get("book_isbn")," "*(13-len(delete_book[bid_index].get("book_isbn"))),"|",
                    delete_book[bid_index].get("book_price")," "*(10-len(str(delete_book[bid_index].get("book_price")))),"|",
                    delete_book[bid_index].get("book_stock")," "*(9-len(str(delete_book[bid_index].get("book_stock")))),"|")
                print("  +----------------------+----------------+-------------+------------+")
                print("\n  Are you sure you want to delete the book record?\n"+
                    "\n  Press [1] if you want to delete it OR press any other key to cancel.")
                time.sleep(1)
                option=input("  Option: ")
                if(option=="1"):
                    with open("record_management.json", "w") as file:
                        del delete_book[bid_index]
                        json.dump(data, file, indent=4)
                    print("\n  |---------------------------------------------------|"+
                            "\n  | Success Message: The book record has successfully |"+
                            "\n  | been deleted from the system.                     |"+
                            "\n  |---------------------------------------------------|\n")
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
    
       
