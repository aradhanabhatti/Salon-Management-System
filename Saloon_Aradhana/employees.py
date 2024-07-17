import mysql.connector
def insert(emp_code,emp_name,address,phone_no):
              
              con=mysql.connector.connect(host="localhost",
              user="root",password="students",database="dbsaloon")#for connection

              cursor=con.cursor();
              query="insert into employees(emp_code,emp_name,address,phone_no) values ('"+emp_code+"','"+emp_name+"','"+address+"','"+phone_no+"')"
              cursor.execute(query)
              con.commit()

              print("RECORD INSERTED SUCCESSFULLY")
              cursor.close()
              if(con.is_connected()):
                            con.close()


def delete(employee_id):
              
              con=mysql.connector.connect(host="localhost",user="root",password="students",database="dbsaloon")#for connection

              query=("delete from employees where  employee_id=' "+str(employee_id)+" ' ")
              cursor=con.cursor();
              cursor.execute(query)
              con.commit()

              print("RECORD DELETE SUCCESSFULLY")
              cursor.close()
              if(con.is_connected()):
                            con.close()
                            

def update(employee_id,emp_code="",emp_name="",address="",phone_no=""):
              
              con=mysql.connector.connect(host="localhost",user="root",password="students",database="dbsaloon")#for connection


              query="";
              if(emp_name!="" and address!="" and phone_no!=""):
              
                            query="update  employees set emp_name ='"+emp_name+"',emp_code='"+emp_code+"' ,address='"+address+"', phone_no='"+phone_no+"' where employee_id='"+employee_id+"'"
              elif(emp_code!=""):
                            query="update  employees set emp_code ='"+emp_code+"'  where employee_id='"+employee_id+"'"
              elif(emp_name!=""):
                            query="update  employees set emp_name ='"+emp_name+"'  where employee_id='"+employee_id+"'"
              elif(address!=""):
                            query="update  employees set address ='"+address+"'  where employee_id='"+employee_id+"'"
              elif(phone_no!=""):
                            query="update  employees set phone_no ='"+phone_no+"'  where employee_id='"+employee_id+"'"

              cursor=con.cursor()
              cursor.execute(query)
              con.commit()

              print("RECORDS CHANGED  SUCCESSFULLY")
              cursor.close()
              if(con.is_connected()):
                            con.close()




def search(emp_name):
              
              con=mysql.connector.connect(host="localhost",user="root",password="students",database="dbsaloon")#for connection
              cursor=con.cursor()
              
              query=" select * from employees where emp_name like '%"+emp_name+"%'"
              cursor.execute(query)
              records=cursor.fetchall()
              for row in records:
                            print("Employee id=",row[0])
                            print("Emp Code=",row[1])
                            print("Emp Name=",row[2])
                            print("Address=",row[3])
                            print("Phone No=",row[4],"\n")
              cursor.close()
              if(con.is_connected()):
                            con.close()


def getall():
              
              con=mysql.connector.connect(host="localhost",user="root",password="students",database="dbsaloon")#for connection
              cursor=con.cursor()
              
              query=" select * from employees"
              cursor.execute(query)
              records=cursor.fetchall()
              for row in records:
                            print("Employee Id=",row[0])
                            print("Emp Code=",row[1])
                            print("Emp Name=",row[2])
                            print("Address=",row[3])
                            print("Phone No=",row[4],"\n")
              cursor.close()
              if(con.is_connected()):
                            con.close()
