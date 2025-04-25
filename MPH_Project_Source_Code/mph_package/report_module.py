import json
import time

def report_viewmod(username):
    while True:
        try:
            time.sleep(1)
            print("\n"+"-"*(80)+"\n\n  View Record Reports"+
                    " "*(57-len("  View Record Reports"))+"Welcome back, "+username+"!\n\n"+
                    "-"*(80)+"\n")
            print("\n  Which record reports would you want to view?\n\n" +
                "  1. View customer purchase records.\n" +
                "  2. View book records.\n" +
                "  3. Go back to main menu.\n")
            print("  Please key-in a number based on the options above.\n")
            time.sleep(1)
            option=input("  Option[Example: 1]: ")
            if option=="1":
                viewCustomer(username)
                return username
            elif option=="2":
                viewBook(username)
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
        
def report_exportmod(username):
    while True:
        try:
            time.sleep(1)
            print("\n"+"-"*(80)+"\n\n  Generate & Export Records"+
            " "*(57-len("  Generate & Export Records"))+"Welcome back, "+username+"!\n\n"+
            "-"*(80)+"\n")
            
            print("\n  Which records would you want to export?\n\n" +
                "  1. Generate & Export customer purchase records.\n" +
                "  2. Generate & Export book records.\n" +
                "  3. Go back to main menu.\n")
            print("  Please key-in a number based on the options above.\n")
            time.sleep(1)
            option=input("  Option[Example: 1]: ")
            if option=="1":
                exportCustomer(username)
                return username
            elif option=="2":
                exportBook(username)
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
        
def viewCustomer(username):
    try:
        time.sleep(1)
        print("\n"+"-"*(80)+"\n\n  View Customer Purchase Records"+
                    " "*(57-len("  View Customer Purchase Records"))+"Welcome back, "+username+"!\n\n"+
                    "-"*(80)+"\n")
        with open("record_management.json", "r") as file:
            data = json.load(file)
            view_customer=data["customer_purchases"]
            if len(view_customer)!=0:
                time.sleep(1)
                for i in range(len(view_customer)):
                    print("\n  Customer Purchase Record #"+str(i+1))                           
                    print("  Purchase ID:"," "+view_customer[i].get("purchase_id")," "*(14-len(view_customer[i].get("purchase_id")))," ","Customer Name:","   "+view_customer[i].get("customer_name"))
                    print("  Phone Number:",view_customer[i].get("phone_number")," "*(14-len(view_customer[i].get("phone_number")))," ","Date of Purchase:",view_customer[i].get("purchase_date"))
                    print("  +------------------------------------------------------------------------+"+
                        "\n  |                        Purchased Product                               |"+
                        "\n  +-----+-----------------+---------------+------------------+-------------+"+
                        "\n  | No. | Book Product ID | Product Price | Product Quantity | Subtotal    |"+
                        "\n  +-----+-----------------+---------------+------------------+-------------+")
                    for booknum in range(len(view_customer[i]["purchased_product"])):
                        print("  |",str(booknum+1)+"."," "*(2-len(str(booknum+1)+".")),"|",
                            view_customer[i]["purchased_product"][booknum].get("book_product")," "*(14-len(str(view_customer[i]["purchased_product"][booknum].get("book_product")))),"|",
                            view_customer[i]["purchased_product"][booknum].get("product_price")," "*(12-len(view_customer[i]["purchased_product"][booknum].get("product_price"))),"|",
                            view_customer[i]["purchased_product"][booknum].get("product_quantity")," "*(15-len(str(view_customer[i]["purchased_product"][booknum].get("product_quantity")))),"|",
                            view_customer[i]["purchased_product"][booknum].get("subtotal")," "*(10-len(view_customer[i]["purchased_product"][booknum].get("subtotal"))),"|")
                        print("  +-----+-----------------+---------------+------------------+-------------+")
                        if(booknum==(len(view_customer[i]["purchased_product"])-1)):
                            print("  |","Total","                                |",view_customer[i].get("total_quantity")," "*(15-len(str(view_customer[i].get("total_quantity")))),"|",
                                view_customer[i].get("total_price")," "*(10-len(str(view_customer[i].get("total_price")))),"|")
                            print("  +------------------------------------------------------------------------+")
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
       
def viewBook(username):
    try:
        time.sleep(1)
        print("\n"+"-"*(80)+"\n\n  View Book Records"+
                " "*(57-len("  View Book Records"))+"Welcome back, "+username+"!\n\n"+
                "-"*(80)+"\n")
        with open("record_management.json", "r") as file:
            data = json.load(file)
            view_book=data["books"]
            if len(view_book)!=0:
                time.sleep(1)
                for i in range(len(view_book)):
                    print("\n  Book Record #"+str(i+1))
                    print("  Book ID:",view_book[i].get("book_id")," "*(8-len(view_book[i].get("book_id")))," ","    Book Title:",view_book[i].get("book_title"))
                    print(  "  +------------------------------------------------------------------+"+
                        "\n  |                            Book Details                          |"+
                        "\n  +----------------------+----------------+-------------+------------+"+
                        "\n  | Book Author          | Book ISBN      | Book Price  | Book Stock |"+
                        "\n  +----------------------+----------------+-------------+------------+")
                    print("  |",view_book[i].get("book_author")," "*(19-len(view_book[i].get("book_author"))),"|",
                        view_book[i].get("book_isbn")," "*(13-len(view_book[i].get("book_isbn"))),"|",
                        view_book[i].get("book_price")," "*(10-len(str(view_book[i].get("book_price")))),"|",
                        view_book[i].get("book_stock")," "*(9-len(str(view_book[i].get("book_stock")))),"|")
                    print("  +----------------------+----------------+-------------+------------+")
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
       
def exportCustomer(username):
    try:
        time.sleep(1)
        print("\n"+"-"*(80)+"\n\n  Export Customer Purchase Records"+
                " "*(57-len("  Export Customer Purchase Records"))+"Welcome back, "+username+"!\n\n"+
                "-"*(80)+"\n")
        with open("record_management.json", "r") as file:
            data = json.load(file)
            export_customer=data["customer_purchases"]
            if len(export_customer)!=0:
                while True:
                    time.sleep(1)
                    for i in range(len(export_customer)):
                        print("\n  Customer Purchase Record #"+str(i+1))                           
                        print("  Purchase ID:"," "+export_customer[i].get("purchase_id")," "*(14-len(export_customer[i].get("purchase_id")))," ","Customer Name:","   "+export_customer[i].get("customer_name"))
                        print("  Phone Number:",export_customer[i].get("phone_number")," "*(14-len(export_customer[i].get("phone_number")))," ","Date of Purchase:",export_customer[i].get("purchase_date"))
                        print("  +------------------------------------------------------------------------+"+
                            "\n  |                        Purchased Product                               |"+
                            "\n  +-----+-----------------+---------------+------------------+-------------+"+
                            "\n  | No. | Book Product ID | Product Price | Product Quantity | Subtotal    |"+
                            "\n  +-----+-----------------+---------------+------------------+-------------+")
                        for booknum in range(len(export_customer[i]["purchased_product"])):
                            print("  |",str(booknum+1)+"."," "*(2-len(str(booknum+1)+".")),"|",
                                export_customer[i]["purchased_product"][booknum].get("book_product")," "*(14-len(str(export_customer[i]["purchased_product"][booknum].get("book_product")))),"|",
                                export_customer[i]["purchased_product"][booknum].get("product_price")," "*(12-len(export_customer[i]["purchased_product"][booknum].get("product_price"))),"|",
                                export_customer[i]["purchased_product"][booknum].get("product_quantity")," "*(15-len(str(export_customer[i]["purchased_product"][booknum].get("product_quantity")))),"|",
                                export_customer[i]["purchased_product"][booknum].get("subtotal")," "*(10-len(export_customer[i]["purchased_product"][booknum].get("subtotal"))),"|")
                            print("  +-----+-----------------+---------------+------------------+-------------+")
                            if(booknum==(len(export_customer[i]["purchased_product"])-1)):
                                print("  |","Total","                                |",export_customer[i].get("total_quantity")," "*(15-len(str(export_customer[i].get("total_quantity")))),"|",
                                    export_customer[i].get("total_price")," "*(10-len(str(export_customer[i].get("total_price")))),"|")
                                print("  +------------------------------------------------------------------------+")
                    print("\n  Are you sure you want to export all customer purchase records?\n"+
                        "  Press [1] if you want to export them OR press any other key to cancel.")
                    time.sleep(1)
                    option=input("\n  Option[Example: 1]: ")
                    if(option=="1"):
                        print('\n  What do you want to name the file?'+
                              '\n  The filename cannot contain any of these *|\/:"?><')
                        filename=input("  Filename[Example: myFile ]: ")
                        filename=filename.replace('*|\/:"?><','')
                        time.sleep(1)
                        filetype=".json"
                        with open(str("Exported_custpurchasefiles/"+filename+filetype), "w") as file:
                            json.dump(export_customer, file, indent=4)
                        print(  "\n  |---------------------------------------------------|"+
                                "\n  | Success Message: All customer purchase records    |"+
                                "\n  | have successfully been exported to the JSON file. |"+
                                "\n  |---------------------------------------------------|\n")
                        input("\n  Please press enter key to go back to main menu: ")
                        return username
                    else:
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
       
def exportBook(username):
    try:
        time.sleep(1)
        print("\n"+"-"*(80)+"\n\n  Export Book Records"+
                " "*(57-len("  Export Book Records"))+"Welcome back, "+username+"!\n\n"+
                "-"*(80)+"\n")
        with open("record_management.json", "r") as file:
            data = json.load(file)
            export_book=data["books"]
            if len(export_book)!=0:
                time.sleep(1)
                for i in range(len(export_book)):
                    print("\n  Book Record #"+str(i+1))
                    print("  Book ID:",export_book[i].get("book_id")," "*(8-len(export_book[i].get("book_id")))," ","    Book Title:",export_book[i].get("book_title"))
                    print(  "  +------------------------------------------------------------------+"+
                            "\n  |                            Book Details                          |"+
                        "\n  +----------------------+----------------+-------------+------------+"+
                        "\n  | Book Author          | Book ISBN      | Book Price  | Book Stock |"+
                        "\n  +----------------------+----------------+-------------+------------+")
                    print("  |",export_book[i].get("book_author")," "*(19-len(export_book[i].get("book_author"))),"|",
                        export_book[i].get("book_isbn")," "*(13-len(export_book[i].get("book_isbn"))),"|",
                        export_book[i].get("book_price")," "*(10-len(str(export_book[i].get("book_price")))),"|",
                        export_book[i].get("book_stock")," "*(9-len(str(export_book[i].get("book_stock")))),"|")
                    print("  +----------------------+----------------+-------------+------------+")
                time.sleep(1)
                print("\n  Are you sure you want to export all book records?\n"+
                    "\n  Press [1] if you want to export them OR press any other key to cancel.")
                time.sleep(1)
                option=input("  Option[Example: 1]: ")
                if(option=="1"):
                    print('\n  What do you want to name the file?'+
                            '\n  The filename cannot contain any of these *|\/:"?><')
                    filename=input("  Filename[Example: myFile ]: ")
                    filename=filename.replace('*|\/:"?><','')
                    time.sleep(1)
                    filetype=".json"
                    with open(str("Exported_bookfiles/"+filename+filetype), "w") as file:
                        json.dump(export_book, file, indent=4)
                    print(  "\n  |-----------------------------------------------------|"+
                            "\n  | Success Message: All book records have successfully |"+
                            "\n  | been exported to the JSON file.                     |"+
                            "\n  |-----------------------------------------------------|\n")
                    input("\n  Please press enter key to go back to main menu: ")
                    return username
                else:
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
       









