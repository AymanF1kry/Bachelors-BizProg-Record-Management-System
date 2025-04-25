import json
import time
from mph_package.insert_module import insertmod
from mph_package.search_module import searchmod
from mph_package.update_module import updatemod
from mph_package.delete_module import deletemod
from mph_package.report_module import report_viewmod
from mph_package.report_module import report_exportmod

def mphSystem():
    username=loginSystem()
    username=mainMenu(username)
    time.sleep(1)
    print("\n\n\n  Shutting down system.... in 5")
    for i in range(4,0,-1):
        time.sleep(1)
        print("\n  ...",i)
    print("\n  Thank you "+username+" for using the MPH Record Management System." +
          "\n  Goodbye :)\n\n")
    exit()
    
def loginSystem():
    while True:
        try:
            print("\n"+"-"*(80)+"\n\n  MPH Staff Login"+" "*(64-len("  MPH Record Management"))+"Welcome, MPH Staff!\n\n"+"-"*(80)+"\n")
            print("  Please enter user credentials to login to the system.")
            username = input("\n  Username: ")
            password = input("\n  Password: ")
            with open("record_management.json", "r") as file:
                data = json.load(file)
                validation=data["staffs"]
                for i in range(len(validation)):
                    if(validation[i].get("username")==username and validation[i].get("password")==password):
                        time.sleep(1)
                        print("\n  |-----------------------------------------------------------------------|"+
                              "\n  | Success Message: Everything checks out. Logging into the system now.. |"+
                              "\n  |-----------------------------------------------------------------------|")
                        time.sleep(1)
                        return username
            print("\n  |---------------------------------------------------------------------|"+
                  "\n  | Error Message: It seems you've entered the wrong Username/Password. |"+
                  "\n  | Please enter the correct Username and Password to login.            |"+
                  "\n  |---------------------------------------------------------------------|")
            time.sleep(2)
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
                print("\n  Thank you for using the MPH Record Management System." +
                      "\n  Goodbye :)\n\n")
                exit()
                
def mainMenu(username):
    while True:
        try:
            time.sleep(1)
            print("\n"+"-"*(80)+"\n\n  MPH Record Management"+
                " "*(57-len("  MPH Record Management"))+"Welcome back, "+username+"!\n\n"+
                "-"*(80)+"\n")
            print("  Welcome to MPH Record Management System. This is the Main Menu.\n\n"+
                  "  What would you like to do today?\n" +
                  "  1. Add new records.\n" +
                  "  2. Search records.\n" +
                  "  3. Update records.\n" +
                  "  4. Delete records.\n" +
                  "  5. View record reports.\n" +
                  "  6. Generate & Export records.\n" +
                  "  7. Log Out the system.\n" +
                  "  8. Exit the system.\n")
            print("  Please key-in a number based on the options above.\n")
            time.sleep(0.5)
            option=input("  Option[Example: 1]: ")
            if option=="1":
                time.sleep(1)
                insertmod(username)
            elif option=="2":
                time.sleep(1)
                searchmod(username)
            elif option=="3":
                time.sleep(1)
                updatemod(username)
            elif option=="4":
                time.sleep(1)
                deletemod(username)
            elif option=="5":
                time.sleep(1)
                report_viewmod(username)
            elif option=="6":
                time.sleep(1)
                report_exportmod(username)
            elif option=="7":
                time.sleep(1)
                print("\n  Logging out...")
                time.sleep(2)
                mphSystem()
            elif option=="8":
                return username
            else:
                print("\n  |-----------------------------------------------------|"+
                      "\n  | Error Message: The option does not appear to exist. |"+
                      "\n  | Please only choose option 1 to 8.                   |"+
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
mphSystem()

