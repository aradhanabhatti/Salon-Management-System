import mysql.connector
def insert(customer_name,address,phone_no):
              
              con=mysql.connector.connect(host="localhost",
              user="root",password="students",database="dbsaloon")#for connection

              cursor=con.cursor();
              query="insert into customer(customer_name,address,phone_no) values ('"+customer_name+"','"+address+"','"+phone_no+"')"
              cursor.execute(query)
              con.commit()

              print("RECORD INSERTED SUCCESSFULLY")
              cursor.close()
              if(con.is_connected()):
                            con.close()


def delete(customer_id):
              
              con=mysql.connector.connect(host="localhost",user="root",password="students",database="dbsaloon")#for connection

              query=("delete from customer where  customer_id=' "+customer_id+" ' ")
              cursor=con.cursor();
              cursor.execute(query)
              con.commit()

              print("RECORD DELETE SUCCESSFULLY")
              cursor.close()
              if(con.is_connected()):
                            con.close()

def update(customer_id,customer_name="",address="",phone_no=""):
              
              con=mysql.connector.connect(host="localhost",user="root",password="students",database="dbsaloon")#for connection
              query="";
              if(customer_name!="" and address!="" and phone_no!=""):
                            query="update  customer set customer_name ='"+customer_name+"', address='"+address+"', phone_no='"+phone_no+"' where customer_id='"+customer_id+"'"
              elif(customer_name!=""):
                            query="update  customer set customer_name ='"+customer_name+"'  where customer_id='"+customer_id+"'"
              elif(address!=""):
                            query="update  customer set address='"+address+"' where customer_id='"+customer_id+"'"
              elif(phone_no!=""):
                            query="update  customer set phone_no='"+phone_no+"' where customer_id='"+customer_id+"'"



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
              
              query=" select * from customer"
              cursor.execute(query)
              records=cursor.fetchall()
              for row in records:
                            print("Customer's Id=",row[0])
                            print("Customer Name=",row[1])
                            print("Address=",row[2])
                            print("Phone_no=",row[3],"\n")
              cursor.close()
              if(con.is_connected()):
                            con.close()
def search(customer_name):
              
              con=mysql.connector.connect(host="localhost",user="root",password="students",database="dbsaloon")#for connection
              cursor=con.cursor()
              
              query=" select * from customer where customer_name like '%"+customer_name+"%"+"'"
              cursor.execute(query)
              records=cursor.fetchall()
              for row in records:
                            print("Customers's Id=",row[0])
                            print("Customer Name=",row[1])
                            print("Address=",row[2])
                            print("Phone No=",row[3],"\n")
              cursor.close()
              if(con.is_connected()):
                            con.close()

