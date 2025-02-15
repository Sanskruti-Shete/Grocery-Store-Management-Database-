while True:
    print()
    print("WELCOME TO THE GROCERY STORE")
    print("|| आपका हार्दिक स्वागत है ||")
    print(""" Follow the given instructions:
    Press the respective numbers to carry out the given functions:

    1. Add Customer details
    2. Add Product details
    3. Add Employee details
    4. Create Grocery List
    5. Display all customer details
    6. Display all product details
    7. Display all employee details
    8. Delete customer details
    9. Delete Product details
    10.Delete Employee details
    11. Exit""")

    choice=int(input("Enter your choice: ")) 
    if choice==1:  #Adding Customer Details
        import csv
        customer=open("Customer.csv",'a')
        cuswriter=csv.writer(customer)
        cuswriter.writerow(['Customer Name','Customer ID','Phone Number','Address'])
        count1=int(input("How many customers do you want to add: "))
        for i in range(count1):
            C_name=input("Enter the name of customer: ")
            C_ID=int(input("Enter customer Id: "))
            C_No=int(input("Enter customer's phone number: "))
            C_Address=input("Enter customer address: ")
            rec1=[C_name,C_ID,C_No,C_Address]
            cuswriter.writerow(rec1)
        customer.close()

    if choice==2:   #Adding Product Details
        import csv
        product=open("Product.csv",'a')
        prowriter=csv.writer(product)
        prowriter.writerow(['Product Name','Product ID','Product Cost','Stock'])
        count2=int(input("How many products do you want to add: "))
        for i in range(count2):
            P_name=input("Enter name of the product: ")
            P_ID=int(input("Enter product code: "))
            P_cost=float(input("Enter cost of 1 unit of product: "))
            P_stock=int(input("Enter the stock of the product: "))
            rec2=[P_name,P_ID,P_cost,P_stock]
            prowriter.writerow(rec2)
        product.close()

    if choice==3:  #Adding Employee Details
        import csv
        employee=open("Employee.csv",'a')
        empwriter=csv.writer(employee)
        empwriter.writerow(['Employee Name','ID','Age','Post','Monthly Salary'])
        count3=int(input("How many employees do you want to add: "))
        for i in range(count3):
            E_name=input("Enter name of the employee: ")
            E_ID=int(input("Enter Employee ID: "))
            E_age=int(input("Enter age of the employee: "))
            E_post=input("Enter the post of the employee: ")
            E_salary=int(input("Enter monthly salary of the employee: "))
            rec3=[E_name,E_ID,E_age,E_post,E_salary]
            empwriter.writerow(rec3)
        employee.close()

    if choice==4:  #Making Grocery List
        grocery_list=open("Grocery List.txt",'w')
        print("Enter * to stop adding items to the list and complete the list")
        while True:
            item=input("Enter the item to be added: ")
            rec4=item+'\n'
            grocery_list.write(rec4)
            if item=='*':
                break
        grocery_list.close()

    if choice==5:  #Display data of all customers
        import csv
        with open("Customer.csv",'r') as f1:
            creader=csv.reader(f1)
            for rec in creader:
                print(rec)

    if choice==6:  #Display data of all products
        import csv
        with open("Product.csv",'r') as f2:
            preader=csv.reader(f2)
            for rec in preader:
                print(rec)

    if choice==7:   #Display data of all employees
        import csv
        with open("Employee.csv",'r') as f3:
            ereader=csv.reader(f3)
            for rec in ereader:
                print(rec)

    if choice==8:  #Deleting customer details
        import csv
        lines = list()
        members= input("Please enter a customer's ID to be deleted.")
        with open('Customer.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                     if field == members:
                         lines.remove(row)
        with open('Customer.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)


    if choice==9: #Deleting product details
        import csv
        lines=list()
        members=input("Please enter a product's ID to be deleted: ")
        with open('Product.csv','r') as readFile:
             reader=csv.reader(readFile)
             for row in reader:
                 lines.append(row)
                 for field in row:
                     if field==members:
                         lines.remove(row)
        with open("Product.csv",'w') as writeFile:
            writer=csv.writer(writeFile)
            writer.writerows(lines)
        


    if choice==10:  #Deleting employee details
        import csv
        lines=list()
        members=input("Please enter a product's ID to be deleted: ")
        with open('Employee.csv','r') as readFile:
            reader=csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                     if field==members:
                         lines.remove(row)
        with open("Employee.csv",'w') as writeFile:
             writer=csv.writer(writeFile)
             writer.writerows(lines)

    if choice==11:  #Terminating the loop
        break

                  
                      
        
         
        


        
    



         
