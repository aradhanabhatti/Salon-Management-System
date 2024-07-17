import mysql.connector
import datetime;

def insert(bill_master_id,service_id,employee_id,cost):
     con=mysql.connector.connect(host="localhost", user="root",
     password="students", database="dbsaloon") 

     cursor=con.cursor();
     query="insert into bill_details(bill_master_id,service_id,employee_id,cost) values ('"+str(bill_master_id)+"','"+str(service_id)+"','"+str(employee_id)+"','"+str(cost)+"')"
     cursor.execute(query)
     con.commit()

     print("RECORD INSERTED SUCCESSFULLY")

     cursor.close()
     if(con.is_connected()):
          con.close()
 

def delete(bill_master_id):
     con=mysql.connector.connect(host="localhost", user="root",
     password="students", database="dbsaloon") 

     cursor=con.cursor();
     query="delete from bill_details where bill_master_id="+str(bill_master_id)+""
     cursor.execute(query)
     con.commit()

     cursor.close()
     if(con.is_connected()):
          con.close()

def search(bill_master_id):
     con=mysql.connector.connect(host="localhost", user="root",password="students", database="dbsaloon") 

     cursor=con.cursor()
     query="select * from bill_details where bill_master_id like'%"+bill_master_id+"%'"
     cursor.execute(query)
     records=cursor.fetchall()
     for row in records:
          print("Bill Details Id:",row[0])
          print("Bill Master Id:",row[1])
          print("Service Id:",row[2])
          print("Employee Id:",row[3],"\n")

     cursor.close()
     if(con.is_connected()):
          con.close()


 
def GetByBillMasterId(bill_master_id):
     con=mysql.connector.connect(host="localhost", user="root",
     password="students", database="dbsaloon") 

     cursor=con.cursor();
     query="select b.title,a.cost,e.emp_name  from bill_details a inner join services b on a.service_id=b.service_id  inner join employees e on e.employee_id=a.employee_id where a.bill_master_id="+str(bill_master_id)+""
     cursor.execute(query)
     records=cursor.fetchall()
     for row in records:
          print("Item=",row[0], "\nCost:",row[1],"----------Done By=",row[2], "\n")
          

     cursor.close()
     if(con.is_connected()):
          con.close()
 
def getall():
     con=mysql.connector.connect(host="localhost", user="root",password="students", database="dbsaloon") 

     cursor=con.cursor()
     query="select * from bill_details"
     cursor.execute(query)
     records=cursor.fetchall()
     for row in records:
          print("Bill Details Id:",row[0])
          print("Bill Master Id:",row[1])
          print("Service Id:",row[2])
          print("Employee Id:",row[3],"\n")

     cursor.close()
     if(con.is_connected()):
          con.close()



