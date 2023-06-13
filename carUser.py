from user import User
from user import RegisterUser
from userMgnt import UserMgnt
from datetime import date
from datetime import datetime
from prettytable import PrettyTable 
from colorama import Fore,Style
import getpass

ch = 0
umgnt = UserMgnt()
while(ch != "3"):
    print()
    print("---------------------------------------------------------------------------------------------------------------------------")
    print()
    print(Fore.CYAN +"\t\t _______User's Section______")
    print(Style.RESET_ALL)
    print(Fore.YELLOW + Style.DIM + "\t 'Boom Car Hire'🚗💭 (The joy of 'Self-Drive') ")
    print(Style.RESET_ALL)
    print("\t\t1. sign-up to get registered.")
    print("\t\t2. Login to your account.")
    print("\t\t3. Exit")
    print() 
    print("---------------------------------------------------------------------------------------------------------------------------")
    print()
    ch = input("Enter your choice: ")
    print()
    if(ch == "1"):
        print(Fore.GREEN +"Enter details to Sign-up.✔️")
        print(Style.RESET_ALL)
        first_name = input("Please enter your name: ")
        last_name = input("Please enter your surname: ")
        if(first_name.isalpha() and last_name.isalpha()):
            user_name = input("Please enter your user name: ")
            user_pass = input("Please enter your user password: ")
            user_city = input("Please enter your city: ")
            user_date = date.today() 
            user_status = 1
            userDataObj = RegisterUser(user_name,user_pass,first_name,last_name,user_date,user_status)
            umgnt.registerUser(userDataObj) 
        else:
            print(Fore.RED +"\nPlease enter valid first and last name!!👎")
            print(Style.RESET_ALL)       
    if(ch == '2'):
        print(Fore.GREEN +"Enter details to Login.✔️")
        print(Style.RESET_ALL)
        uname = input("Please enter your username: ")
        upass = getpass.getpass("Please enter your password: ")
        userDataList = umgnt.checkUser(uname,upass)        
        if(userDataList ==  0):
            print()
            print(Fore.RED +"Invalid login Details!! 👎 Please try again..." )
            print(Style.RESET_ALL)
        else:
            choice = 0
            ruid =  userDataList[0]
            uname = userDataList[1]
            name = userDataList[2]
            surname = userDataList[3]  
            print()          
            print("Hello '",name,surname,"'😄")
            print()
            print(Fore.MAGENTA +"You are successfully logged in to user page.✔️")
            print(Style.RESET_ALL)
            while(choice!="10"):
                print()
                print("---------------------------------------------------------------------------------------------------------------------------")
                print()
                print(Fore.CYAN +"\t\t _______'",uname,"' Section_______")
                print(Style.RESET_ALL)
                print(Fore.YELLOW + Style.DIM + "\t 'Boom Car Hire'🚗💭 (The joy of 'Self-Drive') ")
                print(Style.RESET_ALL)
                print("\t\t1. Display all available cars for rent.")
                print("\t\t2. Search car by car model or by car seating capacity.")
                print("\t\t3. Your car renting details.")
                print("\t\t4. Book a car for rent.")
                print("\t\t5. Extend a car booking.")
                print("\t\t6. Reschedule a car booking.")    
                print("\t\t7. Cancel a car booking.")
                print("\t\t8. Return a car.")
                print("\t\t9. Post Your feedback.")
                print("\t\t10. Logout.") 
                print()  
                print("---------------------------------------------------------------------------------------------------------------------------")
                print()
                choice = input("Enter your choice: ")
                print()

                if(choice == "1"):
                    print(Fore.MAGENTA +"Display all available cars for rent.📄")
                    print(Style.RESET_ALL)
                    umgnt.showAllAvailableCars()
            #--------------------------------------------------------------------------------------------------------#   
                elif(choice == "2"):
                    print(Fore.MAGENTA +"Submenu of search option.🔎")
                    print(Style.RESET_ALL)
                    ans = input("Do you want to search car details with car model [y/n]: ")
                    if(ans.lower() == 'y'):
                        cmodel = input("Enter the car model to search: ")
                        umgnt.searchByName(cmodel) 
                    elif(ans.lower() == 'n'):
                        ans = input("Do you want to search car details with car seating capacity [y/n]: ")  
                        if(ans.lower() == 'y'): 
                            cseat = input("Enter the car seating capacity to search: ")
                            if(cseat.isnumeric()):
                                umgnt.searchBySeat(cseat) 
                            else:     
                                print(Fore.RED +"\nYou have entered invalid format for seating capacity!!👎")  
                                print(Style.RESET_ALL) 
                        elif(ans.lower() == 'n'):  
                            print(Fore.GREEN +"\nOkay!! You dont want to search anything.👍")
                            print(Style.RESET_ALL)      
                    else:
                        print(Fore.RED +"\nInvalid input.👎")
                        print(Style.RESET_ALL)   
            #--------------------------------------------------------------------------------------------------------#  
                elif(choice == "3"):
                    print(Fore.MAGENTA +"Your car renting details.📊")
                    print(Style.RESET_ALL)
                    umgnt.searchByUserIDRentDetails(ruid)    
            #--------------------------------------------------------------------------------------------------------#  
                elif(choice == "4"):
                    umgnt.showAllAvailableCars()
                    print()
                    print(Fore.MAGENTA +"Book a car for rent.📌")
                    print(Style.RESET_ALL)
                    ruid = ruid
                    cid = input("Enter the carID to book the car: ")
                    if(cid.isnumeric()):
                        if(umgnt.checkCarIDPresent(cid) != 0): 
                            if(umgnt.checkCarIDStatus(cid) != 0):
                                today = date.today()  
                                bookdate = input("Enter car booking date in dd-mm-yyyy format: ")
                                bookdate = bookdate.split("-")
                                bookdate = date(int(bookdate[2]),int(bookdate[1]),int(bookdate[0]))                                              
                                returndate = input("Enter car returning date in dd-mm-yyyy format: ")
                                returndate = returndate.split("-")
                                returndate = date(int(returndate[2]),int(returndate[1]),int(returndate[0]))
                                if(bookdate > today and returndate > today):
                                    if(returndate > bookdate):
                                        ustatus = 0 
                                        totaldays = (returndate-bookdate).days
                                        totalamt = 0
                                        userObj = User(ruid,cid,bookdate,returndate,ustatus,totaldays,totalamt)
                                        umgnt.bookCarById(userObj)
                                    else:
                                        print(Fore.RED +"\nYou should enter returning date from booking date onwords!!👎")  
                                        print(Style.RESET_ALL)
                                else:
                                    print(Fore.RED +"\nEnter a booking and returning date from today onwards!!👎")  
                                    print(Style.RESET_ALL) 
                            else:
                                print(Fore.RED +"\nThis Car is already booked!!👎")  
                                print(Style.RESET_ALL)          
                        else:
                            print(Fore.RED +"\nYou have entered invalid carID!!👎")  
                            print(Style.RESET_ALL) 
                    else:     
                        print(Fore.RED +"\nYou have entered invalid format for carID!!👎")  
                        print(Style.RESET_ALL) 
            #--------------------------------------------------------------------------------------------------------#             
                elif(choice == "5"):
                    print(Fore.MAGENTA +"Extend a car booking.📈")
                    print(Style.RESET_ALL)
                    if(umgnt.searchByUserRegID(ruid) == 1):
                        print()
                        cid = input("Enter the carID to extend the car booking: ")
                        if(cid.isnumeric()):
                            if(umgnt.checkCarIDPresent(cid) != 0): 
                                alreadyPresent = umgnt.checkCIDRUIDPresent(cid,ruid)
                                datalist = umgnt.carExtend(cid,ruid,alreadyPresent)
                                if(datalist != 0):
                                    bookdate1 = datalist[1]
                                    returndate1 =  datalist[5]
                                    format = "%Y-%m-%d"
                                    bookdate = datetime.strptime(bookdate1, format).date()
                                    returndate = datetime.strptime(returndate1, format).date()
                                    costperday = int(datalist[2])
                                    prevdays = int(datalist[3])
                                    amtpaid = int(datalist[4])
                                    returndate_extended = input("Enter returning date in dd-mm-yyyy format to extend the car booking: ")
                                    returndate_extended = returndate_extended.split("-")
                                    returndate_extended = date(int(returndate_extended[2]),int(returndate_extended[1]),int(returndate_extended[0]))
                                    if(returndate_extended > returndate and returndate_extended > bookdate):
                                        totaldays = (returndate_extended-bookdate).days
                                        addedday = totaldays - prevdays
                                        newamt = totaldays * costperday
                                        remainingamt = newamt - amtpaid
                                        print("\nTo extend your car booking, you need pay 💰 Rs.",remainingamt,"remaining amount for extra",addedday,"days.")
                                        ans = input("\nYou need to pay remaining amount online(y/n): ") 
                                        if(ans.lower() == 'y'):
                                            umgnt.carBookingExtend(cid,ruid,returndate_extended,totaldays,newamt)
                                        else:
                                            print(Fore.GREEN +"\nOkay! we will not extend your car booking.👍") 
                                            print(Style.RESET_ALL)
                                    else:
                                        print(Fore.RED +"\nPlease enter extended date from previous returndate onwards!!👎") 
                                        print(Style.RESET_ALL)    
                            else:
                                print(Fore.RED +"\nYou have entered invalid carID!!👎") 
                                print(Style.RESET_ALL)  
                        else:     
                            print(Fore.RED +"\nYou have entered invalid format for carID!!👎")  
                            print(Style.RESET_ALL)        
                    else:
                        print(Fore.RED +"Record not found!! 👎")  
                        print(Style.RESET_ALL) 
            #--------------------------------------------------------------------------------------------------------#                         
                elif(choice == "6"):
                    print(Fore.MAGENTA +"Reschedule a car booking.📝")
                    print(Style.RESET_ALL)
                    if(umgnt.searchByUserRegID(ruid) == 1):
                        print()
                        cid = input("Enter the carID to reschedule the car booking: ")
                        if(cid.isnumeric()):
                            if(umgnt.checkCarIDPresent(cid) != 0):
                                alreadyPresent = umgnt.checkCIDRUIDPresent(cid,ruid)
                                datalist = umgnt.carReschedule(cid,ruid,alreadyPresent)
                                if(datalist != 0):
                                    costperday = int(datalist[0])
                                    bookdate3 = input("Enter new booking date in dd-mm-yyyy format: ")
                                    bookdate3 = bookdate3.split("-")
                                    bookdate3 = date(int(bookdate3[2]),int(bookdate3[1]),int(bookdate3[0]))
                                    returndate3 = input("Enter new returning date in dd-mm-yyyy format: ")
                                    returndate3 = returndate3.split("-")
                                    returndate3 = date(int(returndate3[2]),int(returndate3[1]),int(returndate3[0]))
                                    today = date.today()
                                    if(bookdate3 > today and returndate3 > today):
                                        if(returndate3 > bookdate3):
                                            totaldays = (returndate3-bookdate3).days
                                            newamt = totaldays * costperday
                                            finefee = newamt + 200
                                            print()
                                            print(Fore.BLUE +"As per our car rescheduling policies")
                                            print(Fore.BLUE +"A small fee (INR 200) is charged if the modification is done.") 
                                            print(Style.RESET_ALL)
                                            print("\nTo reschedule your car booking, you need pay 💰 Rs.",finefee,"(",newamt,"+ 200 modifications fee)")                                            
                                            print("\nYour previous booking amount will refund to your account!!") 
                                            ans = input("\n Do you want to reschedule your car booking? amount should pay online(y/n): ") 
                                            if(ans.lower() == 'y'):
                                                umgnt.carBookingReschedule(cid,ruid,bookdate3,returndate3,totaldays,finefee)
                                            else:
                                                print(Fore.GREEN +"\nOkay! we will not reschedule your car booking.👍") 
                                                print(Style.RESET_ALL)
                                        else:
                                            print(Fore.RED +"\nPlease enter return date from booking date onwards!!👎") 
                                            print(Style.RESET_ALL)    
                                    else:
                                        print(Fore.RED +"\nEnter a booking and returning date from today onwards!!👎")  
                                        print(Style.RESET_ALL)         
                            else:
                                print(Fore.RED +"\nYou have entered invalid carID!!👎") 
                                print(Style.RESET_ALL)  
                        else:     
                            print(Fore.RED +"\nYou have entered invalid format for carID!!👎")  
                            print(Style.RESET_ALL)        
                    else:
                        print(Fore.RED +"Record not found!! 👎")  
                        print(Style.RESET_ALL)          
            #--------------------------------------------------------------------------------------------------------#                                        
                elif(choice == "7"):
                    print(Fore.MAGENTA +"Cancel a car booking.❌")
                    print(Style.RESET_ALL)
                    if(umgnt.searchByUserRegID(ruid) == 1):
                        print()
                        cid = input("Enter the carID to cancel the car booking: ")  
                        if(cid.isnumeric()):  
                            if(umgnt.checkCarIDPresent(cid) != 0): 
                                alreadyPresent = umgnt.checkCIDRUIDPresent(cid,ruid)
                                umgnt.carCancel(cid,ruid,alreadyPresent)
                            else:
                                print(Fore.RED +"\nYou have entered invalid carID!!👎") 
                                print(Style.RESET_ALL)  
                        else:     
                            print(Fore.RED +"\nYou have entered invalid format for carID!!👎")  
                            print(Style.RESET_ALL)
                    else:
                        print(Fore.RED +"Record not found!! 👎")  
                        print(Style.RESET_ALL)          
            #--------------------------------------------------------------------------------------------------------#                               
                elif(choice == "8"):
                    print(Fore.MAGENTA +"Return a car.🚕")
                    print(Style.RESET_ALL)
                    if(umgnt.searchByUserRegID(ruid) == 1):
                        print()
                        cid = input("Enter the carID to return the car: ") 
                        if(cid.isnumeric()):   
                            if(umgnt.checkCarIDPresent(cid) != 0): 
                                alreadyPresent = umgnt.checkCIDRUIDPresent(cid,ruid)
                                umgnt.carReturn(cid,ruid,alreadyPresent)
                            else:
                                print(Fore.RED +"\nYou have entered invalid carID!!👎")   
                                print(Style.RESET_ALL)  
                        else:     
                            print(Fore.RED +"\nYou have entered invalid format for carID!!👎")  
                            print(Style.RESET_ALL)
                    else:
                        print(Fore.RED +"Record not found!! 👎")  
                        print(Style.RESET_ALL) 
            #--------------------------------------------------------------------------------------------------------#                    
                elif(choice == "9"):
                    print(Fore.MAGENTA +"Post Your feedback.🚩")
                    print(Style.RESET_ALL)
                    ans = input("How was your experience with our 'Boom Car Hire'🚗💭 ? Hope it was good [y/n]: ")
                    if(ans.lower() == 'y'):
                        print()
                        print(Fore.BLUE +"Thank you,",uname,"for your valuable feedback!!😀")
                        print(Style.RESET_ALL)
                        print(Fore.BLUE +'''Here at 'Boom Car Hire'🚗💭 , the customer satisfaction is our highest priority. 
Your feedback, not only that you will help us thrive but will also help us improve our services.🎯''')
                    elif( ans.lower() == 'n'):
                        print()
                        print(Fore.BLUE +"Thank you,",uname,"for your valuable feedback!!😀")
                        print(Style.RESET_ALL)
                        print(Fore.BLUE +"We want to offer our sincerest apologies for any inconvenience this may have caused.🙏")
                        print(Style.RESET_ALL)
            #--------------------------------------------------------------------------------------------------------#               
                elif(choice == "10"):            
                    print(Fore.MAGENTA +"============== 😀 Logged out 😀 ===============") 
                    print(Style.RESET_ALL)
            #--------------------------------------------------------------------------------------------------------#           
    if(ch == '3'):
        print(Fore.MAGENTA +"============== 😀 Thank You 😀 ===============")
        print(Style.RESET_ALL)              