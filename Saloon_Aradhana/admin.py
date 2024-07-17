import mysql.connector


def insert(user_name,password):
              con=mysql.connector.connect(host="localhost",
              user="root",password="students",database="dbsaloon")#for connection

              cursor=con.cursor();
              query="insert into users(user_name,password) values ('"+user_name+"','"+password+"')"
              cursor.execute(query)
              con.commit()

              print("RECORD INSERTED SUCCESSFULLY")
              cursor.close()
              if(con.is_connected()):
                            con.close()
              

def delete(user_id):
              
              con=mysql.connector.connect(host="localhost",user="root",password="students",database="dbsaloon")#for connection

 
              query=("delete from users where  user_id='"+user_id+"'")
              cursor=con.cursor();
              cursor.execute(query)
              con.commit()

              print("RECORD DELETED SUCCESSFULLY")
              cursor.close()
              if(con.is_connected()):
                            con.close()
 

def update(user_name,password):
              
              con=mysql.connector.connect(host="localhost",user="root",password="students",database="dbsaloon")#for connection

              
              query="update  users set password ='"+password+"' where user_name='"+user_name+"' "
              cursor=con.cursor()
              cursor.execute(query)
              con.commit()

              print("PASSWORD CHANGED  SUCCESSFULLY")
              cursor.close()
              if(con.is_connected()):
                            con.close()


def getall():
              
              con=mysql.connector.connect(host="localhost",user="root",password="students",database="dbsaloon")#for connection
              cursor=con.cursor()
              
              query=" select * from users "
              cursor.execute(query)
              records=cursor.fetchall()
              for row in records:
                            print("User Id=",row[0])
                            print("User Name=",row[1])
                            print("Password=",row[2],"\n")
              cursor.close()
              if(con.is_connected()):
                            con.close()

def login():
              user_name=input("Enter Username:  ")
              password=input("Enter Password:  ")
              print ()
              
              con=mysql.connector.connect(host="localhost",user="root",password="students",database="dbsaloon")#for connection

              
              query="select * from users where user_name='"+user_name+"' and password='"+password+"' "
              cursor=con.cursor()
              cursor.execute(query)
              records=cursor.fetchall()
              if(len(records)>0):
                            return 1
              else :
                            print("Invalid username/password")
                            login()
              cursor.close()
              if(con.is_connected()):
                            con.close()

def search(user_name):
              
              con=mysql.connector.connect(host="localhost",user="root",password="students",database="dbsaloon")#for connection
              cursor=con.cursor()
              
              query=" select * from users where user_name like'"+user_name+"%"+"'"
              cursor.execute(query)
              records=cursor.fetchall()
              for row in records:
                            print("User Id=",row[0])
                            print("User Name=",row[1])
                            print("Password=",row[2],"\n")
              cursor.close()
              if(con.is_connected()):
                            con.close()


