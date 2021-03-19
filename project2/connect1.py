#first file create connection string : file name : connect1
#create class of connectivity means to connect mysql server with python
import pymysql
class Connection: #Connection user defined class
    def __init__(self): #constructor function
        servername="localhost"
        username="root"
        password=""
        dbname="employee_management_system"
        try:
            self.__conn=pymysql.connect(servername,username,password,dbname)
            #__conn private variable means highly secured
        except Exception :
            self.msg="Connection Error"
        else:
            self.msg="Connection successfully created"
    def show(self):
        return self.msg,self.__conn

    def __del__(self): #destructor function
        self.__conn.close()
    
    
