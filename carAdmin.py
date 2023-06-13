from car import Car
from carMgnt import CarMgnt
from datetime import date
from datetime import datetime
import getpass
from prettytable import PrettyTable 
from colorama import Fore,Style

flag = "y"
choice = 0
while(flag.lower()!="n" and choice!="10"):
    print()
    admin_name = input("Please enter Admin Username: ")
    admin_pass = getpass.getpass("Please enter Admin Password: ")
    if(admin_name == "avanti1503" and admin_pass == "admin"):
        print()
        print("Hello 'Avanti Aniruddha Haval'😄")
        print()
        print(Fore.MAGENTA +"You are successfully logged in to admin page.✔️")  
        print(Style.RESET_ALL)      
        mgnt = CarMgnt()
        while(choice!="10"):
            print()
            print("---------------------------------------------------------------------------------------------------------------------------")
            print()
            print(Fore.CYAN +"\t\t _______' avanti1503 ' Section______")
            print(Style.RESET_ALL)
            print(Fore.YELLOW + Style.DIM + "\t 'Boom Car Hire'🚗💭 (The joy of 'Self-Drive') ")
            print(Style.RESET_ALL)
            print("\t\t1. Add a new car.") 
            print("\t\t2. Display all cars from portal.") 
            print("\t\t3. Display all available cars for rent.")
            print("\t\t4. Search record by car ID or by car model or by car seating capacity.")  
            print("\t\t5. Edit record by car ID.")
            print("\t\t6. Delete record by car ID.")
            print("\t\t7. View monthly car bookings and details.")
            print("\t\t8. View users details.")
            print("\t\t9. View monthly profitable report.")
            print("\t\t10. Exit.")  
            print()
            print("---------------------------------------------------------------------------------------------------------------------------")
            print()
            choice = input("Enter your choice: ")
            print()

            if(choice == "1"):
                print(Fore.MAGENTA +"Add a new car.🚕")
                print(Style.RESET_ALL)
                cmodel = input("Enter car model: ")
                cnumber = input("Enter car number: ")
                crentdate = date.today()
                costperday = int(input("Enter car cost per day: "))
                cstatus = 1
                cseat = input("Enter car seating capacity: ")
                carObj = Car(cmodel,cnumber,crentdate,costperday,cstatus,cseat)
                mgnt.addCar(carObj)
    #--------------------------------------------------------------------------------------------------------#               
            elif(choice == "2"): 
                print(Fore.MAGENTA +"Display all cars from portal.📄")
                print(Style.RESET_ALL)   
                mgnt.showAllCars()
    #--------------------------------------------------------------------------------------------------------#               
            elif(choice == "3"):
                print(Fore.MAGENTA +"Display all available cars for rent.📈")
                print(Style.RESET_ALL)
                mgnt.showAllAvailableCars()
    #--------------------------------------------------------------------------------------------------------#               
            elif(choice == "4"):
                print(Fore.MAGENTA +"Submenu of search option.🔎")
                print(Style.RESET_ALL)
                ans = input("Do you want to search car details with CarID [y/n]: ")
                if(ans.lower() == 'y'):
                    cid = int(input("Enter the car Id to search: "))
                    if(mgnt.checkCarIDPresent(cid) != 0): 
                        mgnt.searchById(cid) 
                    else:
                        print(Fore.RED +"\nYou have entered invalid carID!!👎") 
                        print(Style.RESET_ALL)   
                elif(ans.lower() == 'n'):
                    ans = input("Do you want to search car details with model name [y/n]: ")
                    if(ans.lower() == 'y'):
                        cmodel = input("Enter the car model to search: ")
                        mgnt.searchByName(cmodel)
                    elif(ans.lower() == 'n'):  
                        ans = input("Do you want to search car details with car seating capacity [y/n]: ")
                        if(ans.lower() == 'y'):
                            cseat = input("Enter the car seating capacity to search: ")
                            mgnt.searchBySeat(cseat)
                        elif(ans.lower() == 'n'):
                            print(Fore.GREEN +"\nOkay!! You dont want to search anything.👍")
                            print(Style.RESET_ALL) 
                    else:
                        print(Fore.RED +"\nInvalid input.👎")
                        print(Style.RESET_ALL)
                else:
                    print(Fore.RED +"\nInvalid input.👎")   
                    print(Style.RESET_ALL) 
    #--------------------------------------------------------------------------------------------------------#                       
            elif(choice == "5"):
                mgnt.showAllCars()
                print()
                print(Fore.MAGENTA +"Edit record by car ID.✏️")
                print(Style.RESET_ALL)
                cid = int(input("Enter the car Id to edit details: "))
                if(mgnt.checkCarIDPresent(cid) != 0): 
                    mgnt.editById(cid) 
                else:
                    print(Fore.RED +"\nYou have entered invalid carID!!👎") 
                    print(Style.RESET_ALL)   
    #--------------------------------------------------------------------------------------------------------#                   
            elif(choice == "6"):
                mgnt.showAllCars()
                print()
                print(Fore.MAGENTA +"Delete record by car ID.❌")
                print(Style.RESET_ALL)
                cid = int(input("Enter the car Id to delete details: "))
                if(mgnt.checkCarIDPresent(cid) != 0):
                    mgnt.deleteById(cid) 
                else:
                    print(Fore.RED +"\nYou have entered invalid carID!!👎")
                    print(Style.RESET_ALL)   
    #--------------------------------------------------------------------------------------------------------#                    
            elif(choice == "7"):
                print(Fore.MAGENTA +"View monthly car bookings and details.📌")
                print(Style.RESET_ALL)
                intMonth = int(input("Enter the month [1-12] to car bookings and details: "))
                if (intMonth in range(1,13)):
                    intyear = int(input("Enter the year in yyyy format: "))
                    print()
                    mgnt.showAllDetails(intMonth,intyear)
                else:
                    print(Fore.RED +"\nPlease enter month number between [1-12]👎") 
                    print(Style.RESET_ALL)    
    #--------------------------------------------------------------------------------------------------------#               
            elif(choice == "8"):  
                mgnt.showAllUserDetails()
                print()
                print(Fore.MAGENTA +"Submenu of make user inactive options.📝")
                print(Style.RESET_ALL)                
                ans = input("Press 'n' if you want to skip this part or press 'y' to continue : ")
                if(ans.lower() == 'y'):
                    ruid = input("Enter the user ID to inactivate: ")
                    mgnt.makeUserInactive(ruid)
                elif(ans.lower() == 'n') : 
                    print(Fore.GREEN +"\nOkay!! You want to skip this part.👍")
                    print(Style.RESET_ALL)   
                else:
                    print(Fore.RED +"\nInvalid input.👎")
                    print(Style.RESET_ALL)  
    #--------------------------------------------------------------------------------------------------------#                    
            elif(choice == "9"):
                print(Fore.MAGENTA +"View monthly profitable report.📊")
                print(Style.RESET_ALL)
                intMonth = int(input("Enter the month [1-12] to view profitable report: "))
                if (intMonth in range(1,13)):
                    intyear = int(input("Enter the year in yyyy format: "))
                    print()
                    mgnt.showMonthlyReport(intMonth,intyear)
                else:
                    print(Fore.RED +"\nPlease enter month number between [1-12]👎") 
                    print(Style.RESET_ALL)
    #--------------------------------------------------------------------------------------------------------#                   
            elif(choice == "10"):            
                print(Fore.MAGENTA +"============== 😀 Logged out 😀 ===============") 
                print(Style.RESET_ALL) 
    #--------------------------------------------------------------------------------------------------------#               
    else:
        print()
        print(Fore.RED +"Sorry! You have entered incorrect username and password!!👎")
        print(Style.RESET_ALL)
        flag = input("Do you want to try once again [y/n]: ")