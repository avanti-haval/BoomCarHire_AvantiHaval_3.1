class User:
    uid = 10
    def __init__(self,ruid,cid,bookdate,returndate,ustatus,totaldays,totalamt):
        User.uid += 1
        self.uid = User.uid
        self.ruid = ruid
        self.cid = cid 
        self.bookdate = bookdate        
        self.returndate = returndate
        self.ustatus = ustatus
        self.totaldays = totaldays
        self.totalamt = totalamt

    def __str__(self):
        data = str(self.uid)+","+str(self.ruid)+","+str(self.cid)+","+str(self.bookdate)+","+str(self.returndate)+","+str(self.ustatus)+","+str(self.totaldays)+","+str(self.totalamt)
        return data    

#-----------------------------------------------------------------------------------------------------------------------------------------------#  

class RegisterUser:
    ruid = 1000
    def __init__(self,user_name,user_pass,first_name,last_name,user_date,user_status):
        RegisterUser.ruid += 1        
        self.user_name = user_name
        self.user_pass = user_pass
        self.first_name = first_name        
        self.last_name = last_name
        self.user_date = user_date
        self.user_status = user_status

    def __str__(self):
        user_data = str(self.ruid)+","+self.user_name+","+self.user_pass+","+self.first_name+","+self.last_name+","+str(self.user_date)+","+str(self.user_status)
        return user_data

#-----------------------------------------------------------------------------------------------------------------------------------------------#          