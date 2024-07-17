import mysql.connector
import datetime;
import customers;
import bill_details;
def insert(customer_id):
     con=mysql.connector.connect(host="localhost", user="root",
     password="students", database="dbsaloon") 

     cursor=con.cursor();
     query="insert into bill_master(customer_id,billing_dt) values ('"+str(customer_id)+"','"+str(datetime.date.today())+"')"
     cursor.execute(query)
     bill_master_id=str(cursor.lastrowid);
     con.commit()

 
     cursor.close()
     if(con.is_connected()):
          con.close()
     return bill_master_id;


def delete(bill_master_id):
     con=mysql.connector.connect(host="localhost", user="root",
     password="students", database="dbsaloon") 

     cursor=con.cursor();
     query="delete from bill_master where bill_master_id="+str(bill_master_id)+""
     cursor.execute(query)
     con.commit()
     cursor.close()
     if(con.is_connected()):
          con.close()

 

def getall():
     con=mysql.connector.connect(host="localhost", user="root",password="students", database="dbsaloon") 

     cursor=con.cursor()
     query="select bill_master_id,bill_master.customer_id,billing_dt,customer_name from bill_master inner join customer on customer.customer_id=bill_master.customer_id"
     cursor.execute(query)
     records=cursor.fetchall()
     for row in records:
          print("Bill Master Id=",row[0])
          print("Customer Id",row[1])
          print("Billing Date",row[2])
          print("Customer Name:",row[3],"\n")

     cursor.close()
     if(con.is_connected()):
          con.close()


def search(customer_id):
     con=mysql.connector.connect(host="localhost", user="root",password="students", database="dbsaloon") 

     cursor=con.cursor()
     query="select bill_master_id,bill_master.customer_id,billing_dt,customer_name from bill_master inner join customer on customer.customer_id=bill_master.customer_id where bill_master.customer_id like'%"+customer_id+"%'"
     cursor.execute(query)
     records=cursor.fetchall()
     for row in records:
          print("Bill Master Id:=",row[0])
          print("Customer Id:",row[1])
          print("Billing Date:",row[2])
          print("Customer Name:",row[3],"\n")

     cursor.close()
     if(con.is_connected()):
          con.close()

def GenerateReport():

     con=mysql.connector.connect(host="localhost", user="root",password="students", database="dbsaloon") 

     cursor=con.cursor()


     print("1--------------------Generate Report By Bill Date")
     print("2--------------------Generate Report By Customer")
     print("3--------------------Get All Bills")
     
     query=""

     ch=input("Enter Your Choice:")     
     if(ch=="1"):
          billing_dt=input("Enter Billing Date: ")
          query="select bill_master_id,billing_dt,customer_name from bill_master inner join customer on customer.customer_id=bill_master.customer_id where billing_dt='"+billing_dt+"'"
     elif(ch=="2"):
          customer_name=input("Search Customer: ")
          customers.search(customer_name)
          customer_id=input("Enter Customer Id:")
          query="select bill_master_id,billing_dt,customer_name from bill_master inner join customer on customer.customer_id=bill_master.customer_id where bill_master.customer_id ='"+customer_id+"'"
     elif(ch=="3"):
          query="select bill_master_id,billing_dt,customer_name from bill_master inner join customer on customer.customer_id=bill_master.customer_id"
     else:
          print("Invalid Choice")
          GenerateReport()
     cursor.execute(query)
     records=cursor.fetchall()
     if(len(records)<1):
          print("No Record Found")
          GenerateReport()
     for row in records:
          print("Bill Id=",row[0],"\nCustomer Name:",row[2],"\nBilling date",row[1],"\n")
          bill_details.GetByBillMasterId(row[0])

     cursor.close()
     if(con.is_connected()):
          con.close()
 

 
