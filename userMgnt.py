from user import User
from car import Car
from datetime import date
from prettytable import PrettyTable 
from colorama import Fore,Style

class UserMgnt:
    
    def showAllAvailableCars(self):
        try:
            with open("carRentalData.txt","r") as fp:
                #print("\t\t***Available cars for rent***\n") 
                print()
                newTable = PrettyTable(["Car ID", "Car Name", "Car Number", "Seating Capacity","Added Date","Cost per Day","Car Status"])  
                cnt = 0
                content = fp.readlines()
                for line in content:
                    line = line.strip()
                    data = line.split(",")
                    if(data[5] == '1'):  
                        newTable.add_row([data[0], data[1],data[2], data[6],data[3],data[4],"Available"]) 
                        cnt += 1 
                if(cnt == 0):
                    print(Fore.RED +"\nCar is not available for rent!! 👎")
                    print(Style.RESET_ALL)  
                else: 
                    print(newTable)                  
        except FileNotFoundError:
            print(Fore.RED +"File does not exist!!👎") 
            print(Style.RESET_ALL)

#-----------------------------------------------------------------------------------------------------------------------------------------------#  
   
    def searchByName(self,cmodel):
        try:
            with open("carRentalData.txt","r") as fp:
                #print("\t\t***Searching a car details with car Model***\n")  
                cnt = 0    
                print()
                newTable = PrettyTable(["Car ID", "Car Name", "Car Number", "Seating Capacity","Added Date","Cost per Day","Car Status"])           
                content = fp.readlines() 
                for line in content:
                    line = line.strip()
                    data = line.split(",")
                    if(data[1] == cmodel):
                        if(data[5] == '1'):
                            newTable.add_row([data[0], data[1],data[2], data[6],data[3],data[4],"Available"]) 
                            cnt += 1 
                if(cnt == 0):
                    print(Fore.RED +"\nCar is not available for rent!! 👎")  
                    print(Style.RESET_ALL)
                else: 
                    print(newTable)                  
        except FileNotFoundError:
            print(Fore.RED +"File does not exist!! 👎")
            print(Style.RESET_ALL)  

#-----------------------------------------------------------------------------------------------------------------------------------------------#  
   
    def searchBySeat(self,cseat):
        try:
            with open("carRentalData.txt","r") as fp:
                #print("\t\t***Searching a car details with car Seating Capacity***\n")  
                cnt = 0    
                print()
                newTable = PrettyTable(["Car ID", "Car Name", "Car Number", "Seating Capacity","Added Date","Cost per Day","Car Status"])          
                content = fp.readlines() 
                for line in content:
                    line = line.strip()
                    data = line.split(",")
                    if(data[6] == cseat):
                        if(data[5] == '1'):
                            newTable.add_row([data[0], data[1],data[2], data[6],data[3],data[4],"Available"]) 
                            cnt += 1 
                if(cnt == 0):
                    print(Fore.RED +"\nCar is not available for rent!!👎")
                    print(Style.RESET_ALL) 
                else: 
                    print(newTable)                   
        except FileNotFoundError:
            print(Fore.RED +"File does not exist!!👎")
            print(Style.RESET_ALL)   

#-----------------------------------------------------------------------------------------------------------------------------------------------#  
 
    def bookCarById(self,u1):
        try: 
            with open("userRentalData.txt","r") as fp: 
                 #print("\t\t***Book a car using CarID ***\n")  
                lines = fp.read().splitlines()
                last_line = lines[-1]
                line = last_line.strip()
                data1 = line.split(",")
                for i in range(len(data1)):              
                    if(i == 0):
                        data1[0] = int(data1[0])
                        data1[0] += 1
                try:
                    with open("userRentalData.txt","a") as fp:
                        ndata = str(u1)
                        ndata = ndata.strip()
                        ndata = ndata.split(",") 
                        ndata[0] = str(data1[0])
                        totaldays = int(ndata[6])
                        cid = ndata[2]
                        with open("carRentalData.txt","r") as fp:
                            content = fp.readlines()
                            for line in content:
                                data2 = line.split(",")
                                if(data2[0] == cid):
                                    amt = int(data2[4])
                                    totalamt = amt * totaldays 
                                    print("\nTo rent this car, You need to pay Rs.",totalamt,"💰 for",totaldays,"days") 
                                    i = 0        
                                    while(i<=2):        
                                        ans = input("\nTo confirm your booking, you need to pay above amount online(y/n): ") 
                                        if(ans.lower() == 'y'):    
                                            with open("userRentalData.txt","a") as fp:  
                                                paid = 1
                                                ndata[5] = str(paid)                                                              
                                                ndata[6] = str(totaldays)
                                                ndata[7] = str(totalamt)
                                                line = ",".join(ndata)                     
                                                fp.write(line)
                                                fp.write("\n")
                                                print(Fore.GREEN +"\nThank you for payment and your car is booked!!😀") 
                                                print(Style.RESET_ALL) 
                                                try:
                                                    allCar = []
                                                    found = False
                                                    with open("carRentalData.txt","r") as fp:
                                                        for line in fp:
                                                            data1 = line.split(",")
                                                            if(data1[0] == ndata[2]):
                                                                data1[5] = '0'
                                                            line = ",".join(data1) 
                                                            found = True
                                                            allCar.append(line) 
                                                        if(found):
                                                            with open("carRentalData.txt","w") as fp:
                                                                for car in allCar:
                                                                    fp.write(car) 
                                                except FileNotFoundError:
                                                     print("File does not exist!!")  
                                            break            
                                        else:
                                            print(Fore.RED +"\nSorry! To book your car, you need to pay 💰 amount first!!")  
                                            print(Style.RESET_ALL)
                                        i += 1  
                except FileNotFoundError:
                    print(Fore.RED +"File does not exist!! 👎") 
                    print(Style.RESET_ALL) 
        except FileNotFoundError:
            print(Fore.RED +"File does not exist!! 👎")
            print(Style.RESET_ALL)

#-----------------------------------------------------------------------------------------------------------------------------------------------#  
    
    def searchByUserRegID(self,ruid):
        try:
            with open("userRentalData.txt","r") as fp:
                #print("\t\t***Searching a user details with user registered ID***\n")  
                cnt = 0
                newTable = PrettyTable(["Car ID", "Car Name", "Car Number", "Booked Date","Return Date","Amount Paid","Car Status"])  
                content = fp.readlines()                  
                for line in content:
                    line = line.strip()
                    data = line.split(",")
                    if(data[1] == ruid):  
                        with open("carRentalData.txt","r") as fp:
                            content1 = fp.readlines() 
                            for line1 in content1:
                                line1 = line1.strip()
                                data1 = line1.split(",")
                                if(data1[0] == data[2] and data[5] == '2'):
                                    newTable.add_row([data1[0], data1[1],data1[2], data[3],data[4],data[7],"Paid & Returned"])    
                                elif(data1[0] == data[2] and data[5] == '1'):
                                    newTable.add_row([data1[0], data1[1],data1[2], data[3],data[4],data[7],"Paid"])  
                                elif(data1[0] == data[2] and data[5] == '3'):
                                   newTable.add_row([data1[0], data1[1],data1[2], data[3],data[4],data[7],"Cancelled & refunded"])    
                                cnt += 1                             
                if(cnt == 0):                     
                    return 0  
                else:
                    print(newTable) 
                    return 1                
        except FileNotFoundError:
            print(Fore.RED +"File does not exist!!👎")
            print(Style.RESET_ALL) 

#-----------------------------------------------------------------------------------------------------------------------------------------------#       
    
    def carReturn(self,cid,ruid,alreadyPresent):
        cnt = 0
        try:
            with open("userRentalData.txt","r") as fp:
                 #print("\t\t*** Return a car using carID and Registered UID ***\n")  
                allCar = []
                found = False 
                allCar1 = []
                found2 = False               
                for line in fp:
                    line = line.strip()
                    data = line.split(",")
                    if(data[1] == ruid and data[2] == cid and data[5] == '1'): 
                        cnt += 1
                        with open("carRentalData.txt","r") as fp:    
                            for line1 in fp:
                                #line1 = line1.strip()
                                data1 = line1.split(",")
                                if(data1[0] == cid):
                                    data1[5] = '1'
                                    line1 = ",".join(data1) 
                                    found = True
                                allCar.append(line1) 
                            if(found):
                                with open("carRentalData.txt","w") as fp:
                                    for car in allCar:
                                        fp.write(car) 
                                print(Fore.GREEN +"Thank you!!😀 ")
                                print(Style.RESET_ALL)
                                ans = input("\nHow was your experience with our 'Boom Car Hire'🚗💭 ? Hope it was good 👍 [y/n]: ")
                                if(ans.lower() == 'y'):
                                    print()
                                    print(Fore.BLUE +"Thank you for your valuable feedback!!😀")
                                    print(Style.RESET_ALL)
                                    print(Fore.BLUE+'''Here at 'Boom Car Hire'🚗💭 , the customer satisfaction is our highest priority. 
Your feedback, not only that you will help us thrive but will also help us improve our services.🎯''')
                                    print(Style.RESET_ALL)
                                elif( ans.lower() == 'n'):
                                    print()
                                    print(Fore.BLUE +"Thank you for your valuable feedback!!😀")
                                    print(Style.RESET_ALL)
                                    print(Fore.BLUE +"We want to offer our sincerest apologies for any inconvenience this may have caused.🙏")
                                    print(Style.RESET_ALL)
                        with open("userRentalData.txt","r") as fp:    
                            for line2 in fp:
                                data2 = line2.split(",")
                                if(data2[1] == ruid and data2[2] == cid and data2[5] == '1'):
                                    data2[5] = '2'
                                    line2 = ",".join(data2) 
                                    found2 = True
                                allCar1.append(line2) 
                            if(found2):
                                with open("userRentalData.txt","w") as fp:
                                    for car1 in allCar1:
                                        fp.write(car1) 
                    elif(data[1] == ruid and data[2] == cid and data[5] == '2' and alreadyPresent == 0): 
                        print(Fore.GREEN +"You have paid and returned car.!!👍")
                        print(Style.RESET_ALL)
                        cnt += 1
                    elif(data[1] == ruid and data[2] == cid and data[5] == '3' and alreadyPresent == 0): 
                        print(Fore.GREEN +"You have cancelled car booking.!!👍") 
                        print(Style.RESET_ALL)
                        cnt += 1
                if(cnt == 0):
                    print(Fore.RED +"\nYou can only return a car that has paid status for entered Car ID!!👎")    
                    print(Style.RESET_ALL)                              
        except FileNotFoundError:
            print(Fore.RED +"File does not exist!!👎")  
            print(Style.RESET_ALL) 

#-----------------------------------------------------------------------------------------------------------------------------------------------#  
    
    def carExtend(self,cid,ruid,alreadyPresent): 
        with open("userRentalData.txt","r") as fp:
             #print("\t\t***car Extend using carID and Registered UID ***\n")  
            cnt = 0  
            for line in fp:
                data = line.split(",")
                if(data[1] == ruid and data[2] == cid and data[5] == '1'):
                    cnt += 1
                    with open("carRentalData.txt","r") as fp:
                        content1 = fp.readlines() 
                        for line1 in content1:
                            line1 = line1.strip()
                            data1 = line1.split(",")
                            if(data1[0] == data[2]): 
                                print()
                                print("You have booked",data1[1],"with car number",data1[2],"on",data[3])
                                print("And you are going to return it on",data[4])
                                print("You have paid 💰 Rs",data[7])
                                ans = input("Do you want to extend car booking [y/n]: ")
                                if(ans.lower() == 'y'):
                                    datalist = []
                                    datalist.append(data[2])
                                    datalist.append(data[3])
                                    datalist.append(data1[4])
                                    datalist.append(data[6])
                                    data[7] = data[7].strip()
                                    datalist.append(data[7])
                                    datalist.append(data[4])
                                    return datalist
                                else:
                                    print(Fore.GREEN +"\nOkay!👍 we will not extend your car booking. ")
                                    print(Style.RESET_ALL) 
                                    
                elif(data[1] == ruid and data[2] == cid and data[5] == '2' and alreadyPresent == 0 ):
                    print(Fore.GREEN +"\nYou have paid and returned car already!👍 ")
                    print(Style.RESET_ALL) 
                    cnt += 1
                elif(data[1] == ruid and data[2] == cid and data[5] == '3' and alreadyPresent == 0):
                    print(Fore.GREEN +"\nYou have cancelled car booking and amount is refunded already!👍") 
                    print(Style.RESET_ALL)
                    cnt += 1            
            if(cnt == 0):
                print(Fore.RED +"\nYou can only extend a car booking that has paid status for entered Car ID!!👎")
                print(Style.RESET_ALL)
                return 0 
            else:
                return 0 

#-----------------------------------------------------------------------------------------------------------------------------------------------#  
   
    def carBookingExtend(self,cid,ruid,returndate,totaldays,newamt): 
        try:
            allCar = []
            found = False
            with open("userRentalData.txt","r") as fp:
                 #print("\t\t***Extend a car booking for entered carID and for Registered User ID ***\n")  
                for line in fp:
                    data = line.split(",")
                    if(data[2] == str(cid) and data[1] == ruid):
                        data[4] =  str(returndate)
                        data[6] =  str(totaldays)
                        data[7] =  str(newamt)+"\n"
                        line = ",".join(data)
                        found = True
                    allCar.append(line)
                if(found):
                    with open("userRentalData.txt","w") as fp:
                        for car in allCar:
                            fp.write(car)
                    print(Fore.GREEN +"Yes!! Your car booking is extended!!👍")
                    print(Style.RESET_ALL)
                else:
                    print(Fore.RED +"Record not present!!👎")
                    print(Style.RESET_ALL)
        except FileNotFoundError:
            print(Fore.RED +"File does not exist!!👎")
            print(Style.RESET_ALL)

#-----------------------------------------------------------------------------------------------------------------------------------------------#  

    def carCancel(self,cid,ruid,alreadyPresent):
        cnt = 0
        try:
            with open("userRentalData.txt","r") as fp:
                #print("\t\t***cancel a car booking for entered carID and for Registered User ID ***\n")  
                allCar = []
                found = False 
                allCar1 = []
                found2 = False               
                for line in fp:
                    line = line.strip()
                    data = line.split(",")
                    if(data[1] == ruid and data[2] == cid and data[5] == '1'):
                        cnt += 1
                        print()
                        ans = input("Do you really want to cancel this car booking [y/n]: ") 
                        if(ans.lower() == 'y'):
                            with open("carRentalData.txt","r") as fp:    
                                for line1 in fp:
                                    data1 = line1.split(",")
                                    if(data1[0] == cid):
                                        data1[5] = '1'
                                        line1 = ",".join(data1) 
                                        found = True
                                    allCar.append(line1) 
                                if(found):
                                    with open("carRentalData.txt","w") as fp:
                                        for car in allCar:
                                            fp.write(car) 

                            with open("userRentalData.txt","r") as fp:    
                                for line2 in fp:
                                    data2 = line2.split(",")
                                    if(data2[1] == ruid and data2[2] == cid and data2[5] == '1'):                                        
                                        data2[5] = '3'                                        
                                        PaidAmt = data2[7]
                                        data2[7] = int(data2[7])
                                        refundAmt =  int(data2[7] * 0.9)
                                        data2[7] = int(data2[7] * 0.1)        
                                        data2[7] = str(data2[7])+'\n'
                                        line2 = ",".join(data2)                                         
                                        found2 = True
                                    allCar1.append(line2) 
                                if(found2):
                                    with open("userRentalData.txt","w") as fp:
                                        for car1 in allCar1:
                                            fp.write(car1)
                            print()                
                            print(Fore.BLUE +"As per our car booking cancellation policies")
                            print(Fore.BLUE +"We are going to refund 90% amount from your paid amount") 
                            print(Fore.BLUE +"and 10% of the booking fee will be charged as cancellation fee.")
                            print(Style.RESET_ALL)
                            print("To rent this car, You have paid Rs.",PaidAmt)
                            print("We are refunding you Rs.",refundAmt,"in your bank account.👍") 
                            print()               
                            print(Fore.GREEN +"\nYour car booking is cancelled. Booking amount will refund to your account soon..!!👍")                             
                            print(Style.RESET_ALL)
                        else:
                            print(Fore.GREEN +"\nOkay! We will not cancel your car booking..!!👍") 
                            print(Style.RESET_ALL)                   
                    elif(data[1] == ruid and data[2] == cid and data[5] == '3'  and alreadyPresent == 0): 
                        print(Fore.GREEN +"\nYou have canceled this car already!👍")
                        print(Style.RESET_ALL)
                        cnt += 1
                    elif(data[1] == ruid and data[2] == cid and data[5] == '2'  and alreadyPresent == 0):
                       print(Fore.GREEN +"\nYou have paid and returned car already!👍")
                       print(Style.RESET_ALL) 
                       cnt += 1  
                if(cnt == 0):
                    print(Fore.RED +"\nYou can only cancel a car booking that has paid status for entered Car ID!!👎")   
                    print(Style.RESET_ALL)                        
        except FileNotFoundError:
            print(Fore.RED +"File does not exist!!👎")
            print(Style.RESET_ALL)

#-----------------------------------------------------------------------------------------------------------------------------------------------#  
    
    def searchByUserIDRentDetails(self,ruid):
        try:
            with open("userRentalData.txt","r") as fp:
                #print("\t\t***Car renting details for RUID***\n")  
                cnt = 0  
                newTable = PrettyTable(["Car ID", "Car Name", "Car Number", "Booked Date","Return Date","Amount Paid","Car Status"]) 
                content = fp.readlines()                  
                for line in content:
                    line = line.strip()
                    data = line.split(",")
                    if(data[1] == ruid):  
                        with open("carRentalData.txt","r") as fp:
                            content1 = fp.readlines() 
                            for line1 in content1:
                                line1 = line1.strip()
                                data1 = line1.split(",")
                                if(data1[0] == data[2] and data[5] == '2'):
                                    newTable.add_row([data1[0], data1[1],data1[2], data[3],data[4],data[7],"Paid & Returned"])
                                elif(data1[0] == data[2] and data[5] == '1'):
                                    newTable.add_row([data1[0], data1[1],data1[2], data[3],data[4],data[7],"Paid"])  
                                elif(data1[0] == data[2] and data[5] == '3'):
                                    newTable.add_row([data1[0], data1[1],data1[2], data[3],data[4],data[7],"Cancelled & refunded"])
                                cnt += 1                             
                if(cnt == 0):
                    print(Fore.RED +"Record not found!!👎")  
                    print(Style.RESET_ALL)
                else:
                    print(newTable) 
        except FileNotFoundError:
            print(Fore.RED +"File does not exist!!👎")
            print(Style.RESET_ALL)   

#-----------------------------------------------------------------------------------------------------------------------------------------------#  
   
    def registerUser(self,ru1):
        try:
            with open("userData.txt","r") as fp: 
                #print("\t\t***Register a user details***\n")  
                lines = fp.read().splitlines()
                last_line = lines[-1]
                line = last_line.strip()
                data1 = line.split(",")
                for i in range(len(data1)):              
                    if(i == 0):
                        data1[0] = int(data1[0])
                        data1[0] += 1
                try:
                    with open("userData.txt","a") as fp:
                        ndata = str(ru1)
                        ndata = ndata.strip()
                        ndata = ndata.split(",") 
                        ndata[0] = str(data1[0])
                        line = ",".join(ndata)                     
                        fp.write(line)
                        fp.write("\n")
                        print()
                        print(Fore.GREEN +"Your details are registered successfully!!👍")
                        print(Style.RESET_ALL)
                except FileNotFoundError:
                    print(Fore.RED +"File does not exist!!👎") 
                    print(Style.RESET_ALL) 
        except FileNotFoundError:
                print(Fore.RED +"File does not exist!! 👎")
                print(Style.RESET_ALL) 

#-----------------------------------------------------------------------------------------------------------------------------------------------#                   

    def checkUser(self,uname,upass):
        cnt = 0 
        try:
            with open("userData.txt","r") as fp:
                #print("\t\t***Checking valid user login by user name and password***\n")  
                for line in fp:
                    data = line.strip()
                    data = data.split(",")
                    if(data[1] == uname and data[2] == upass and data[6] == '1'):
                        userDataList = []
                        userDataList.append(data[0])
                        userDataList.append(data[1])
                        userDataList.append(data[3])
                        userDataList.append(data[4])
                        cnt += 1
                        return userDataList
                if(cnt == 0):
                    return 0    
        except FileNotFoundError:
                print(Fore.RED +"File does not exist!!👎") 
                print(Style.RESET_ALL) 

#-----------------------------------------------------------------------------------------------------------------------------------------------#  

    def checkCarIDPresent(self,cid):
        try:
            with open("carRentalData.txt","r") as fp:
                #print("\t\t***Checking valid carID***\n") 
                cnt = 0 
                for line in fp:
                    data = line.strip()
                    data = data.split(",")
                    if(data[0] == str(cid)):
                        cnt += 1
                if(cnt == 0):
                    return 0 
                else:
                    return 1    
        except FileNotFoundError:
            print(Fore.RED +"File does not exist!!👎")
            print(Style.RESET_ALL) 

#-----------------------------------------------------------------------------------------------------------------------------------------------#              

    def checkCarIDStatus(self,cid):
        try:
            with open("carRentalData.txt","r") as fp:
                #print("\t\t***Checking valid carID***\n") 
                cnt = 0 
                for line in fp:
                    data = line.strip()
                    data = data.split(",")
                    if(data[0] == str(cid) and data[5] == '1'):
                        cnt += 1
                if(cnt == 0):
                    return 0 
                else:
                    return 1    
        except FileNotFoundError:
            print(Fore.RED +"File does not exist!!👎")
            print(Style.RESET_ALL)  

#-----------------------------------------------------------------------------------------------------------------------------------------------#  

    def carReschedule(self,cid,ruid,alreadyPresent): 
        with open("userRentalData.txt","r") as fp:
             #print("\t\t***car reschedule using carID and Registered UID ***\n")  
            cnt = 0  
            for line in fp:
                data = line.split(",") 
                if(data[1] == ruid and data[2] == cid and data[5] == '1'):
                    cnt += 1
                    with open("carRentalData.txt","r") as fp:
                        content1 = fp.readlines() 
                        for line1 in content1:
                            line1 = line1.strip()
                            data1 = line1.split(",")
                            if(data1[0] == data[2]): 
                                print()
                                print("You have booked",data1[1],"with car number",data1[2],"on",data[3])
                                print("And you are going to return it on",data[4])
                                print("You have paid 💰 Rs",data[7])
                                ans = input("Do you want to reschedule car booking [y/n]: ")
                                if(ans.lower() == 'y'):
                                    datalist = []
                                    datalist.append(data1[4])
                                    return datalist
                                else:
                                    print(Fore.GREEN +"\nOkay!👍 we will not reschedule your car booking. ")
                                    print(Style.RESET_ALL) 
                                    
                elif(data[1] == ruid and data[2] == cid and data[5] == '2' and alreadyPresent == 0):
                    print(Fore.GREEN +"\nYou have paid and returned car already!👍 ")
                    print(Style.RESET_ALL) 
                    cnt += 1
                elif(data[1] == ruid and data[2] == cid and data[5] == '3' and alreadyPresent == 0):
                    print(Fore.GREEN +"\nYou have cancelled car booking and amount is refunded already!👍") 
                    print(Style.RESET_ALL)
                    cnt += 1            
            if(cnt == 0):
                print(Fore.RED +"\nYou can only extened a car booking that has paid status for entered Car ID!!👎")
                print(Style.RESET_ALL)
                return 0 
            else:
                return 0  

#-----------------------------------------------------------------------------------------------------------------------------------------------#  
    
    def carBookingReschedule(self,cid,ruid,bookdate3,returndate3,totaldays,finefee): 
        try:
            allCar = []
            found = False
            with open("userRentalData.txt","r") as fp:
                 #print("\t\t***Reschedule a car booking for entered carID and for Registered User ID ***\n")  
                for line in fp:
                    data = line.split(",")
                    if(data[2] == str(cid) and data[1] == ruid):
                        data[3] = str(bookdate3)
                        data[4] =  str(returndate3)
                        data[6] =  str(totaldays)
                        data[7] =  str(finefee)+"\n"
                        line = ",".join(data)
                        found = True
                    allCar.append(line)
                if(found):
                    with open("userRentalData.txt","w") as fp:
                        for car in allCar:
                            fp.write(car)
                    print(Fore.GREEN +"\nYes!! Your car booking is Rescheduled!!👍")
                    print(Style.RESET_ALL)
                else:
                    print(Fore.RED +"Record not present!!👎")
                    print(Style.RESET_ALL)
        except FileNotFoundError:
            print(Fore.RED +"File does not exist!!👎")
            print(Style.RESET_ALL)

#-----------------------------------------------------------------------------------------------------------------------------------------------#  

    def checkCIDRUIDPresent(self,cid,ruid):
        with open("userRentalData.txt","r") as fp:
            #print("\t\t***checking carID and Registered UID present or not in userRentalData.txt ***\n")  
            cnt = 0
            for line in fp:
                data = line.split(",") 
                if(data[1] == ruid and data[2] == cid and data[5] == '2'):
                    cnt += 1
                elif(data[1] == ruid and data[2] == cid and data[5] == '3'):
                    cnt += 1
            if(cnt == 0):
                return 0
            else:
                return 1           

#-----------------------------------------------------------------------------------------------------------------------------------------------#  