#Create connectivity with python and mysqlserver
import pymysql
class College:  #College user defined class name
    def __init__(self): #constructor function
        self.__servername="localhost"  #private variable
        self.__username="root"
        self.__password=""
        self.__dbname="college1"  #dbname means databasename
        try:
            self.con=pymysql.connect(self.__servername,self.__username,self.__password,self.__dbname)
            #con user defined connection name
            print("Connect successfully")
        except:
            print("connectivity not work")
    def __del__(self): #destrcutor function 
        self.con.close()
        print("Connection close")
    def insertrecord(self):
       q1="insert into student(enroll,name,age,city)values(110,'seema pandey',23,'bhopal')"
       #Creating Cursor
       cursor = self.con.cursor()#cursor() inbuilt function
       #Execute(run) the Query
       cursor.execute(q1)
       #Commit changes in the database.
       self.con.commit()
       print("Record save successfully")

       




        
