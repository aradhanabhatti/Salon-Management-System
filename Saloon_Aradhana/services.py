import mysql.connector
def insert(title,cost):
              
              con=mysql.connector.connect(host="localhost",
              user="root",password="students",database="dbsaloon")#for connection

              cursor=con.cursor();
              query="insert into services(title,cost) values ('"+title+"','"+str(cost)+"')"
              cursor.execute(query)
              con.commit()

              print("RECORD INSERTED SUCCESSFULLY")
              cursor.close()
              if(con.is_connected()):
                            con.close()

def delete(service_id):
              
              con=mysql.connector.connect(host="localhost",user="root",password="students",database="dbsaloon")#for connection

              query=("delete from services where service_id=' "+service_id+" ' ")
              cursor=con.cursor();
              cursor.execute(query)
              con.commit()

              print("RECORD DELETE SUCCESSFULLY")
              cursor.close()
              if(con.is_connected()):
                            con.close()
                            

def update(service_id,title,cost):
              
              con=mysql.connector.connect(host="localhost",user="root",password="students",database="dbsaloon")#for connection

              
              query="update  services set title='"+title+"',cost='"+str(cost)+"' where service_id='"+service_id+"'"
              cursor=con.cursor()
              cursor.execute(query)
              con.commit()

              print("RECORDS CHANGED  SUCCESSFULLY")
              cursor.close()
              if(con.is_connected()):
                         con.close()

def getall():
              
              con=mysql.connector.connect(host="localhost",user="root",password="students",database="dbsaloon")#for connection
              cursor=con.cursor()
              
              query=" select * from services"
              cursor.execute(query)
              records=cursor.fetchall()
              for row in records:
                            print("Service Id=",row[0])
                            print("Title=",row[1])
                            print("Cost=",row[2],"\n")
              cursor.close()
              if(con.is_connected()):
                            con.close()
def search(title):
              
              con=mysql.connector.connect(host="localhost",user="root",password="students",database="dbsaloon")#for connection
              cursor=con.cursor()
              
              query=" select * from services where title like'%"+title+"%'"
              cursor.execute(query)
              records=cursor.fetchall()
              for row in records:
                            print("Service Id=",row[0])
                            print("Title=",row[1])
                            print("Cost=",row[2],"\n")
              cursor.close()
              if(con.is_connected()):
                            con.close()


