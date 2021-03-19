import pymysql
class Connection: #Connection user defined class
    def conn(self): #constructor function
        
        #to create a connection string (between python and mysqlserver)
        
        self.servername="localhost"
        self.username="root"
        self.password=""
        self.dbname="employee_management"
        try:
            self.con=pymysql.connect(self.servername,self.username,self.password,self.dbname)
        except:
            print("Connectivity Error")
        else:
            print("Connect successfully")
            return self.con
