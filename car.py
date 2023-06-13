class Car:
    cid = 100
    def __init__(self,cmodel,cnumber,crentdate,costperday,cstatus,cseat):
        Car.cid += 1
        self.cid = Car.cid
        self.cmodel = cmodel
        self.cnumber = cnumber
        self.crentdate = crentdate
        self.costperday = costperday
        self.cstatus = cstatus
        self.cseat = cseat

    def __str__(self):
        data = str(self.cid)+","+self.cmodel+","+str(self.cnumber)+","+str(self.crentdate)+","+str(self.costperday)+","+str(self.cstatus)+","+str(self.cseat)
        return data  
        
#-----------------------------------------------------------------------------------------------------------------------------------------------#            