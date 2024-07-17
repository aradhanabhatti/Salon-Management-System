import login;
import admin
import customers
import employees
import services
import bill_master 
import bill_details
import datetime
def  ShowMenuOptions(choice):
    if(choice=="MainMenu"):
        print("********    MAIN   MENU  **********")
        print("1.-----------  MANAGE  USERS  -----------")
        print("2.---------  MANAGE  CUSTOMERS  ------")
        print("3.-------- MANAGE  EMPLOYEES  ---------")
        print("4.-------- MANAGE  SERVICES  ---------")
        print("5.----------- GENERATE  BILLS  --------")
        ch=input("Enter your Choice:  ")
        if(ch=="1"):
            ShowMenuOptions("Users");
        elif(ch=="2"):
            ShowMenuOptions("Customers");
        elif(ch=="3"):
            ShowMenuOptions("Employees");
        elif(ch=="4"):
            ShowMenuOptions("Services");
        elif(ch=="5"):
            ShowMenuOptions("Bills");
        else:
            print("Invalid choice! \nPlease enter valid choice")
            print ()
            ShowMenuOptions("MainMenu")
            print ()
              
    elif(choice=="Users"):
        try:
            print("****MANAGE  USERS   ***")
            print("1.--------ADD  USERS------------")
            print("2.-----------UPDATE  USERS------")
            print("3.------- DELETE  USERS-----------")
            print("4.------ SHOW  ALL  USERS ------")
            print("5.------- SEARCH  USERS  ---------")
            print("6.------- MAIN  MENU------------")
            print ()
            ch=input("Enter your Choice:  ")
            if(ch=="1"):
                user_name=input("Enter your Name:  ")
                password=input("Enter Password:  ")
                admin.insert(user_name,password);
                ShowMenuOptions("Users");
            elif(ch=="2"):
                user_name=input("Enter User Name:  ")
                admin.search(user_name)
                user_name=input("User name:  ")
                password=input("Password:  ")
                admin.update(user_name,password)
                ShowMenuOptions("Users");
            elif(ch=="3"):
                user_name=input("Enter User Name:  ")
                admin.search(user_name)
                user_id=input("Enter User Id  ")
                admin.delete(user_id)
                ShowMenuOptions("Users");
            elif(ch=="4"):
                admin.getall()
                ShowMenuOptions("Users");
            elif(ch=="5"):
                user_name=input("Enter User Name:  ")
                admin.search(user_name)            
                ShowMenuOptions("Users");
            elif(ch=="6"):
                ShowMenuOptions("MainMenu");
                                          
            else:
                print("Invalid choice! \nPlease enter valid choice")
                print ()
                ShowMenuOptions("MainMenu")
        except Exception as e:
                print(e)
                obj=open("errorLog.txt","a");
                obj.write("Error: "+str(e)+"_Time: "+str(datetime.datetime.now()))
                obj.close()
                ShowMenuOptions("MainMenu")

    elif(choice=="Customers"):
        try:
            print("**********************  MANAGE  CUSTOMERS  *****************************")
            print("1.------------------ADD  CUSTOMERS----------------------")
            print("2.----------------UPDATE  CUSTOMERS-----------------------")
            print("3.----------------DELETE  CUSTOMERS-------------------------")
            print("4.-----------------SHOW  ALL  CUSTOMERS---------------------")
            print("5.--------------SEARCH  CUSTOMERS-----------------------------")
            print("6.--------------------MAIN  MENU--------------------")
            print ()
            ch=input("Enter your Choice:  ")
            if(ch=="1"):
                customer_name=input("Enter your Name:  ")
                address=input("Enter Address:  ")
                phone_no=input("Enter Phone no:  ")
                customers.insert(customer_name,address,phone_no);
                ShowMenuOptions("Customers");
            elif(ch=="2"):
                customer_name=input("Customer Name:  ")
                customers.search(customer_name)
                customer_id=input("Ënter Customer ID: ")

                print("1----------------------Update Customer Name")
                print("2----------------------Update Address")
                print("3----------------------Update Phone")
                print("4----------------------Update All")
                ch=input("Enter Your Choice: ")
                if(ch=="1"):
                    customer_name=input("Updated Customer name:  ")
                    customers.update(customer_id,customer_name)
                    ShowMenuOptions("Customers")
                elif(ch=="2"):
                    address=input("Address:  ")
                    customers.update(customer_id,address=address)
                    ShowMenuOptions("Customers")
                elif(ch=="3"):
                    phone_no=input("Phone no:  ")
                    customers.update(customer_id,phone_no=phone_no)
                    ShowMenuOptions("Customers")
                elif(ch=="4"):
                    customer_name=input("Updated Customer name:  ")
                    address=input("Address:  ")
                    phone_no=input("Phone no:  ")
                    customers.update(customer_id,customer_name,address,phone_no)
                    ShowMenuOptions("Customers")
                else:
                    print("Invalid Choice")
                    ShowMenuOptions("Customers")
                                                        
                                                        
            elif(ch=="3"):
                customer_name=input("Enter Custome Name:  ")
                customers.search(customer_name)
                customer_id=input("Enter Customer Id:  ")
                customers.delete(customer_id)
                ShowMenuOptions("Customers");
            elif(ch=="4"):
                customers.getall()
                ShowMenuOptions("Customers");
            elif(ch=="5"):
                customer_name=input("Enter Custome Name:  ")
                customers.search(customer_name)
                ShowMenuOptions("Customers");
            elif(ch=="6"):
                ShowMenuOptions("MainMenu");
                                         
            else:
                print("Invalid choice! \nPlease enter valid choice")
                print ()
                ShowMenuOptions("MainMenu")
        except Exception as e:
                print(e)
                obj=open("errorLog.txt","a");
                obj.write("Error: "+str(e)+"_Time: "+str(datetime.datetime.now()))
                obj.close()
                ShowMenuOptions("MainMenu")
              
    elif(choice=="Employees"):
        try:
            print("-************************   MANAGE  EMPLOYEES  *****************************************")
            print("1.------------------------ADD   EMPLOYEES-------------------------------------------------")
            print("2.------------------------UPDATE  EMPLOYEES-------------------------------------------")
            print("3.------------------------DELETE  EMPLOYEES--------------------------------------------")
            print("4.------------------------SHOW  ALL  EMPLOYEES-----------------------------------------------")
            print("5.------------------------SEARCH  EMPLOYEES-----------------------------------------------")
            print("6.------------------------MAIN  MENU--------------------------------------------------------")
            print ()
            ch=input("Enter your Choice:  ")
            if(ch=="1"):
                emp_code=input("Enter your code: ")
                emp_name=input("Enter name: ")
                address=input("Enter address: ")
                phone_no=input("Enter phone no: ")
                employees.insert(emp_code,emp_name,address,phone_no);
                ShowMenuOptions("Employees");
            elif(ch=="2"):
                emp_name=input("Enter Employee Name:  ")
                employees.search(emp_name)
                employee_id=input("Ënter Employee Id: ")

                print("1----------------------Update Employee Code")
                print("2----------------------Update Employee Name")
                print("3----------------------Update Address")
                print("4----------------------Update Phone")
                print("5----------------------Update All")
                ch=input("Enter Your Choice: ")
                if(ch=="1"):
                    emp_code=input("New Employee Code:  ")
                    employees.update(employee_id,emp_code)
                    ShowMenuOptions("Employees")


                                                        
                elif(ch=="2"):
                    emp_name=input("New Employee name:  ")
                    employees.update(employee_id,emp_name=emp_name)
                    ShowMenuOptions("Employees")
                elif(ch=="3"):
                    address=input("Address:  ")
                    employees.update(employee_id,address=address)
                    ShowMenuOptions("Employees")
                elif(ch=="4"):
                    phone_no=input("Phone no:  ")
                    employees.update(employee_id,phone_no=phone_no)
                    ShowMenuOptions("Employees")
                elif(ch=="5"):
                    emp_name=input("Updated Customer name:  ")
                    address=input("Address:  ")
                    phone_no=input("Phone no:  ")
                    employees.update(employee_id,emp_name,address,phone_no)
                    ShowMenuOptions("Employees")
                else:
                    print("Invalid Choice")
                    ShowMenuOptions("Employees")
                                                        
            elif(ch=="3"):
                emp_name =input("Enter Employee Name: ")
                employees.search(emp_name);
                emp_id=input("Enter Employee Id: ")
                employees.delete(emp_id)
                ShowMenuOptions("Employees");
            elif(ch=="4"):
                                                      
                employees.getall()
                ShowMenuOptions("Employees");
            elif(ch=="5"):
                emp_name =input("Enter Employee Name: ")
                employees.search(emp_name);
                ShowMenuOptions("Employees");
                                          
            elif(ch=="6"):
                    ShowMenuOptions("MainMenu");
            else:
                print("Invalid choice! \nPlease enter valid choice")
                print ()
                ShowMenuOptions("MainMenu")

        except Exception as e:
            print(e)
            obj=open("errorLog.txt","a");
            obj.write("Error: "+str(e)+"_Time: "+str(datetime.datetime.now()))
            obj.close()
            ShowMenuOptions("MainMenu")
                            

    elif(choice=="Services"):
        try:
            print("**************************  MANAGE  SERVICES  ******************************************")
            print("1.------------------------------ADD  SERVICES------------------------------------------------------")
            print("2.------------------------------UPDATE  SERVICES-------------------------------------------------")
            print("3.------------------------------DELETE  SERVICES--------------------------------------------------")
            print("4.------------------------------SHOW  ALL  SERVICES---------------------------------------------")
            print("5.------------------------------SEARCH  SERVICES--------------------------------------------------")
            print("6.------------------------------MAIN  MENU----------------------------------------------------------")
            print ()
            ch=input("Enter your Choice:  ")
            if(ch=="1"):
                title=input("Enter Service:  ")
                cost=input("Enter Cost:  ")
                services.insert(title,cost);
                ShowMenuOptions("Services");
            elif(ch=="2"):
                title=input("Enter Service Name:  ")
                services.search(title)
                service_id=input("Enter Service Id:  ")
                title=input("Enter Title:  ")
                cost=input("Enter Cost:  ")
                services.update(service_id,title,cost)
                ShowMenuOptions("Services");
            elif(ch=="3"):
                title=input("Enter Service Name: ")
                services.search(title)
                service_id=input("Enter Service Id: ")
                services.delete(service_id)
                ShowMenuOptions("Services");
            elif(ch=="4"):
                services.getall()
                ShowMenuOptions("Services");
            elif(ch=="5"):
                title=input("Enter Service Name: ")
                services.search(title)
                ShowMenuOptions("Services");
                                       
            elif(ch=="6"):
                ShowMenuOptions("MainMenu");
            else:
                print("Invalid choice! \nPlease enter valid choice")
                print ()
                ShowMenuOptions("MainMenu")

        except Exception as e:
            print(e)
            obj=open("errorLog.txt","a");
            obj.write("Error: "+str(e)+"_Time: "+str(datetime.datetime.now()))
            obj.close()
            ShowMenuOptions("MainMenu")
                            
    elif(choice=="Bills"):
        try:
            print("******************************   MANAGE  BILLS  ******************************************* ")
            print("1.------------------------GENERATE  BILLS-----------------------------------------------------------")
            print("2.------------------------DELETE  BILLS------------------------------------------------------")
            print("3.------------------------GENERATE  REPORT------------------------------------------------------")
            print("4.------------------------MAIN  MENU--------------------------------------------------------")
            print ()
            ch=input("Enter your Choice:  ")
            if(ch=="1"):
                customer_name=input("Enter Customer Name:  ")
                customers.search(customer_name) 
                customer_id=input("Enter Customer Id:  ")
                bill_master_id=bill_master.insert(customer_id);

                while(True):
                    title=input("Enter Service Name: ")
                    services.search(title)
                    service_id=input("Enter Service Id: ")
                                                                        
                    emp_name =input("Enter Employee Name: ")
                    employees.search(emp_name);
                    emp_id=input("Enter Employee Id: ")
                    cost=input("Enter Service Cost: ")
                    bill_details.insert(bill_master_id,service_id,emp_id,cost)
                    x=input("Press N to Stop");
                    if(x=="N" or x=="n"):
                        ShowMenuOptions("Bills")
                                                                      
                ShowMenuOptions("Bills");
            elif(ch=="2"):
                customer_name=input("Enter Customer Name:  ")
                customers.search(customer_name)
                customer_id=input("Enter Customer Id:  ")
                bill_master.search(customer_id)
                bill_master_id=input("Enter Bill Master Id:  ")
                bill_details.delete(bill_master_id)
                bill_master.delete(bill_master_id)
                print("Bill Deleted Successfully!")
                ShowMenuOptions("Bills");

            elif(ch=="3"):
                bill_master.GenerateReport();
                ShowMenuOptions("Bills");
                                                        
            elif(ch=="4"):
                ShowMenuOptions("MainMenu");
            else:
                print("Invalid choice!\n Please enter valid choice")
                print ()
                ShowMenuOptions("MainMenu")
                print ()
        except Exception as e:
            print(e)
            obj=open("errorLog.txt","a");
            obj.write("Error: "+str(e)+"_Time: "+str(datetime.datetime.now()))
            obj.close()
            ShowMenuOptions("MainMenu")
ShowMenuOptions("MainMenu")
