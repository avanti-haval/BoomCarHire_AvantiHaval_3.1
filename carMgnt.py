from car import Car
from datetime import date
from prettytable import PrettyTable 
from colorama import Fore,Style
from datetime import datetime

class CarMgnt:
    
    def addCar(self,c1):
        try: 
            with open("carRentalData.txt","r") as fp: 
                #print("\t\t***Adding new car***\n")  
                lines = fp.read().splitlines()
                last_line = lines[-1]
                #print (last_line)
                line = last_line.strip()
                data1 = line.split(",")
                for i in range(len(data1)):               
                    if(i == 0):
                        data1[0] = int(data1[0])
                        data1[0] += 1
                try:
                    with open("carRentalData.txt","a") as fp:
                        ndata = str(c1)
                        ndata = ndata.strip()
                        ndata = ndata.split(",") 
                        ndata[0] = str(data1[0])
                        line = ",".join(ndata)                     
                        fp.write(line)
                        fp.write("\n")
                        print(Fore.GREEN +"\n New car details added successfully!!👍")
                        print(Style.RESET_ALL)
                except FileNotFoundError:
                    print(Fore.RED +"File does not exist!! 👎") 
                    print(Style.RESET_ALL)        
        except FileNotFoundError:
                print(Fore.RED +"File does not exist!! 👎") 
                print(Style.RESET_ALL) 

#-----------------------------------------------------------------------------------------------------------------------------------------------# 
  
    def showAllCars(self):
        try:
            with open("carRentalData.txt","r") as fp:
                #print("\t\t***Cars on portal***\n")  
                newTable = PrettyTable(["Car ID", "Car Name", "Car Number", "Seating Capacity","Added Date","Cost per Day","Car Status"])  
                content = fp.readlines()
                for line in content:
                    line = line.strip()
                    data = line.split(",")
                    if(data[5] == '0'):
                       newTable.add_row([data[0], data[1],data[2], data[6],data[3],data[4],"Booked"])  
                    elif(data[5] == '1'):
                        newTable.add_row([data[0], data[1],data[2], data[6],data[3],data[4],"Available"]) 
                print(newTable) 
        except FileNotFoundError:
            print(Fore.RED +"File does not exist!! 👎") 
            print(Style.RESET_ALL) 

#-----------------------------------------------------------------------------------------------------------------------------------------------#              

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
                print(newTable)
                if(cnt == 0):
                    print(Fore.RED +"\nCar is not available for rent!! 👎") 
                    print(Style.RESET_ALL)               
        except FileNotFoundError:
            print(Fore.RED +"File does not exist!! 👎") 
            print(Style.RESET_ALL)   

#-----------------------------------------------------------------------------------------------------------------------------------------------#  

    def searchById(self,cid):
        try:
            with open("carRentalData.txt","r") as fp:
                #print("\t\t***Searching a car details with car ID***\n") 
                print()
                cnt = 0
                newTable = PrettyTable(["Car ID", "Car Name", "Car Number", "Seating Capacity","Added Date","Cost per Day","Car Status"])  
                content = fp.readlines()
                for line in content:
                    line = line.strip()
                    data = line.split(",")
                    if(data[0] == str(cid)):
                        if(data[5] == '0'):
                            newTable.add_row([data[0], data[1],data[2], data[6],data[3],data[4],"Booked"])  
                        elif(data[5] == '1'):
                            newTable.add_row([data[0], data[1],data[2], data[6],data[3],data[4],"Available"]) 
                        cnt += 1    
                        break
                if(cnt == 0):
                    print(Fore.RED +"Record not found!!👎") 
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
                print()
                newTable = PrettyTable(["Car ID", "Car Name", "Car Number", "Seating Capacity","Added Date","Cost per Day","Car Status"])  
                content = fp.readlines() 
                cnt = 0
                for line in content:
                    line = line.strip()
                    data = line.split(",")
                    if(data[1] == cmodel):
                        if(data[5] == '0'):
                            newTable.add_row([data[0], data[1],data[2], data[6],data[3],data[4],"Booked"])                            
                        elif(data[5] == '1'):
                             newTable.add_row([data[0], data[1],data[2], data[6],data[3],data[4],"Available"])
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
 
    def searchBySeat(self,cseat):
        try:
            with open("carRentalData.txt","r") as fp:
                #print("\t\t***Searching a car details with car Seating Capacity***\n") 
                print()
                newTable = PrettyTable(["Car ID", "Car Name", "Car Number", "Seating Capacity","Added Date","Cost per Day","Car Status"]) 
                content = fp.readlines() 
                cnt = 0
                for line in content:
                    line = line.strip()
                    data = line.split(",")
                    if(data[6] == cseat):
                        if(data[5] == '0'):
                           newTable.add_row([data[0], data[1],data[2], data[6],data[3],data[4],"Booked"])
                        elif(data[5] == '1'):
                            newTable.add_row([data[0], data[1],data[2], data[6],data[3],data[4],"Available"])
                        cnt += 1
                if(cnt == 0):
                    print(Fore.RED +"Record not found!! 👎")  
                    print(Style.RESET_ALL) 
                else:
                    print(newTable)             
        except FileNotFoundError:
            print(Fore.RED +"File does not exist!! 👎")  
            print(Style.RESET_ALL)         

#-----------------------------------------------------------------------------------------------------------------------------------------------#  
    
    def editById(self,id):
        try:
            allCar = []
            found = False
            with open("carRentalData.txt","r") as fp:
                #print("\t\t***Editing a car details with car ID***\n") 
                for line in fp:
                    data = line.split(",")
                    if(data[0] == str(id) and data[5] == '1'):
                        ans = input("Do you wish to change model name(y/n): ")
                        if(ans.lower() == 'y'):
                            data[1] = input("Enter new model name: ")
                        ans = input("Do you wish to change car number(y/n): ")
                        if(ans.lower() == 'y'):
                            data[2] = input("Enter new car number:")     
                        ans = input("Do you wish to cost per day(y/n): ")
                        if(ans.lower() == 'y'):
                            data[4] = input("Enter new cost per day:") 
                        line = ",".join(data)
                        found = True
                    allCar.append(line)
                if(found):  
                    print()
                    print(Fore.GREEN +"\nThe car details edited successfully!!👍")
                    print(Style.RESET_ALL)
                    newTable = PrettyTable(["Car ID", "Car Name", "Car Number", "Seating Capacity","Added Date","Cost per Day","Car Status"])    
                    for line in allCar:
                        line = line.strip()
                        data = line.split(",")
                        if(data[0] == str(id)):
                            if(data[5] == '0'):
                                newTable.add_row([data[0], data[1],data[2], data[6],data[3],data[4],"Booked"])
                            elif(data[5] == '1'):
                                newTable.add_row([data[0], data[1],data[2], data[6],data[3],data[4],"Available"])  
                    print(newTable)                              
                if(found):
                    with open("carRentalData.txt","w") as fp:
                        for car in allCar:
                            fp.write(car)
                else:
                    print(Fore.RED +"\nYou can't edit this car details as it is rented by user!! 👎")
                    print(Style.RESET_ALL)
        except FileNotFoundError: 
            print(Fore.RED +"File does not exist!! 👎")
            print(Style.RESET_ALL)

#-----------------------------------------------------------------------------------------------------------------------------------------------#                                       
    
    def deleteById(self,id):
        try:
            allCar = []
            found = False
            with open("carRentalData.txt","r") as fp:
                #print("\t\t***Deleting a car details with car ID***\n")
                for line in fp:
                    data = line.split(",")
                    if(data[0] == str(id) and data[5] == '1'):
                        found = True
                    else:
                        allCar.append(line)

                if(found):
                    print(Fore.GREEN +"\ncar ID -",id,"record deleted successfully!!👍")
                    print(Style.RESET_ALL)
                    with open("carRentalData.txt","w") as fp:
                        for car in allCar:
                            fp.write(car)
                else:
                    print(Fore.RED +"\n You can't delete this record as it is renterd by user!! 👎")
                    print(Style.RESET_ALL)

        except FileNotFoundError:
            print(Fore.RED +"File does not exist!! 👎") 
            print(Style.RESET_ALL)

#-----------------------------------------------------------------------------------------------------------------------------------------------#  
   
    def showAllDetails(self,intMonth,intyear):  
        try:
            with open("userRentalData.txt","r") as fp:
                #print("\t\t***Showing all cars renting details ***\n")  
                cnt = 0
                newTable = PrettyTable(["ID","User ID","User Name","Car ID","Booked Date", "Return Date", "Amount Paid","Car Status"]) 
                content = fp.readlines()
                for line in content:
                    line = line.strip()
                    data = line.split(",")
                    date1 = data[4]
                    format = "%Y-%m-%d"
                    returndate = datetime.strptime(date1, format).date()
                    getMonth = returndate.month
                    getYear = returndate.year
                    with open("userData.txt","r") as fp:
                        content1 = fp.readlines()
                        for line1 in content1:
                            line1 = line1.strip()
                            data1 = line1.split(",")
                            if(data1[0] == data[1] and getMonth == intMonth and getYear ==  intyear):
                                if(data[5] == '1'):
                                    newTable.add_row([data[0], data1[0],data1[1],data[2],data[3],data[4],data[7],"Paid"])
                                elif(data[5] == '2'):
                                    newTable.add_row([data[0], data1[0],data1[1],data[2],data[3],data[4],data[7],"Paid & Returned"])
                                elif(data[5] == '3'):
                                    newTable.add_row([data[0], data1[0],data1[1],data[2],data[3],data[4],data[7],"Cancelled & refunded"])    
                                cnt += 1    
                if(cnt == 0):
                    print(Fore.RED +"\nThis month has no car bookings!!☹️")  
                    print(Style.RESET_ALL) 
                else:
                    print(newTable)                    
        except FileNotFoundError:
            print(Fore.RED +"File does not exist!! 👎") 
            print(Style.RESET_ALL)

#-----------------------------------------------------------------------------------------------------------------------------------------------#  
    
    def showAllUserDetails(self):
        try:     
            with open("userData.txt","r") as fp:
                 #print("\t\t***Showing all user details ***\n")  
                cnt = 0
                newTable = PrettyTable(["User ID","User Name","User Password","First Name ","Last Name", "Added Date", "User Status"]) 
                content = fp.readlines()
                for line in content:
                    line = line.strip()
                    data = line.split(",")   
                    if(data[6] == '1'):
                        newTable.add_row([data[0], data[1],data[2],data[3],data[4],data[5],"Active"])
                    elif(data[6] == '0'):
                        newTable.add_row([data[0], data[1],data[2],data[3],data[4],data[5],"Inactive"])
                    cnt += 1 
                if(cnt == 0):
                    print(Fore.RED +"Record not found!! 👎") 
                    print(Style.RESET_ALL)  
                else:
                    print(newTable)       
        except FileNotFoundError:
            print(Fore.RED +"File does not exist!! 👎")  
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
            print(Fore.RED +"File does not exist!! 👎")  
            print(Style.RESET_ALL) 

#-----------------------------------------------------------------------------------------------------------------------------------------------#  
  
    def showMonthlyReport(self,intMonth,intyear):                                                   
        try:
            with open("userRentalData.txt","r") as fp:
                #print("\t\t***Monthly profitable report ***\n") 
                cnt = 0
                profAmt = 0
                newTable = PrettyTable(["ID","User ID","Car ID","Booked Date", "Return Date", "Number of days","Amount Paid","Car Status"])
                content = fp.readlines()
                for line in content:
                    line = line.strip()
                    data = line.split(",")                    
                    date1 = data[4]
                    format = "%Y-%m-%d"
                    returndate = datetime.strptime(date1, format).date()
                    getMonth = returndate.month
                    getYear = returndate.year
                    if(getMonth == intMonth and getYear ==  intyear):
                        profAmt += int(data[7])
                        if(data[5] == '1'):
                            newTable.add_row([data[0],data[1],data[2],data[3],data[4],data[6],data[7],"Paid"])
                        elif(data[5] == '2'):
                            newTable.add_row([data[0],data[1],data[2],data[3],data[4],data[6],data[7],"Paid & Returned"])
                        elif(data[5] == '3'):
                            newTable.add_row([data[0],data[1],data[2],data[3],data[4],data[6],data[7],"Cancelled & refunded"])   
                        cnt += 1
                if(cnt == 0):
                    print(Fore.RED +"\nThis month has no profit!!☹️")  
                    print(Style.RESET_ALL) 
                else:
                    print(newTable)
                    print(Fore.GREEN +"\nHureeyy!! 🤑 This month our company got total Rs.",profAmt,"profit 💰")
                    print(Style.RESET_ALL)
        except FileNotFoundError:
            print(Fore.RED +"File does not exist!! 👎")  
            print(Style.RESET_ALL) 

#-----------------------------------------------------------------------------------------------------------------------------------------------#  
    
    def makeUserInactive(self,ruid):
        try:
            with open("userRentalData.txt","r") as fp:
                #print("\t\t***Inactivate User ***\n")  
                cnt = 0
                flag = 0
                newTable = PrettyTable(["ID","User ID","User Name","Car ID","Booked Date", "Return Date", "Amount Paid","Car Status"]) 
                content = fp.readlines()
                for line in content:
                    line = line.strip()
                    data = line.split(",")
                    with open("userData.txt","r") as fp:
                        content1 = fp.readlines()
                        for line1 in content1:
                            line1 = line1.strip()
                            data1 = line1.split(",")
                            if(data1[0] == ruid and data1[6]=='1'):
                                if(data[1] == ruid and data[5] == '1'):
                                    newTable.add_row([data[0], data1[0],data1[1],data[2],data[3],data[4],data[7],"Paid"])
                                    cnt += 1  
                                elif(data[1] == ruid and data[5] == '2'):
                                    newTable.add_row([data[0], data1[0],data1[1],data[2],data[3],data[4],data[7],"Paid & Returned"])
                                elif(data[1] == ruid and data[5] == '3') :
                                    newTable.add_row([data[0], data1[0],data1[1],data[2],data[3],data[4],data[7],"Cancelled & refunded"])
                            elif(data1[0] == ruid and data1[6] =='0'):
                                flag = 1 
                if(cnt == 0 and flag == 0):
                    allCar = []
                    found = False
                    with open("userData.txt","r") as fp:
                        for line in fp:
                            data = line.split(",")
                            if(data[0] == ruid and data[6] == '1\n'):
                                data[6] = '0\n'                             
                                line = ",".join(data)
                                found = True
                            allCar.append(line)
                        if(found):  
                            with open("userData.txt","w") as fp:
                                for car in allCar:
                                    fp.write(car)  
                                print(Fore.GREEN +"\nUser is inactivated successfully!!👍")
                                print(Style.RESET_ALL)
                elif(cnt != 0 and flag == 0):
                    print(Fore.RED +"\nThis user rented a car currently so You can't inactivate this user!! 👎")  
                    print(Style.RESET_ALL) 
                    print(newTable) 
                elif(flag == 1):
                    print(Fore.RED +"\nThis user inactivated already!! 👎")  
                    print(Style.RESET_ALL)                                                                          
        except FileNotFoundError:
            print(Fore.RED +"File does not exist!! 👎")  
            print(Style.RESET_ALL) 

#-----------------------------------------------------------------------------------------------------------------------------------------------#                                 