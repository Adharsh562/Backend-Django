import mysql.connector
from datetime import date

config = {
    'user':'root',
    'password':'Adi1605',
    'host':'localhost',
    'port':3306,
    'database':'learningdatabase'
}

def InsertUpdateDelete(sql):
   try:
       conn=mysql.connector.connect(**config)
       print("connection success")
       try:
          
           mycur=conn.cursor()
           mycur.execute(sql)
           conn.commit()
           mycur.close()
           return True
       except:
           conn.rollback()
           print("sysntext error")
           return False
       conn.close()
   except:
       print("unable to connect to db")

def DisplayTable(sql):
   try:
       conn=mysql.connector.connect(**config)
       print("connection success")
       try:
          
           mycur=conn.cursor()
           mycur.execute(sql)
           row=mycur.fetchall()
           for r in row:
               print(r)
           mycur.close()
       except:
           conn.rollback()
           print("sysntext error11")
       conn.close()
   except:
       print("unable to connect to db")

while True:
    print("Main Menu")
    print("1.book")
    print("2.user")
    print("3.loan")
    print("4.exit")

    choice=int(input("enter your choice"))

    if choice == 1:
        print("--BOOK--")
        print("1.insert")
        print("2.update")
        print("3.delete")
        print("4.display")
        print("5.exit")
        choice1= int(input("enter choice"))
        if choice1==1:
            name=input("enter book name")
            author=input("enter book author")
            price =float(input("enter book price"))
            quantity=int(input("enter book quantity"))
            sql=f"insert into book(name,author,price,quantity) values('{name}','{author}',{price},{quantity})"
            # print("sql=",sql)
            result=InsertUpdateDelete(sql)
            print("book added")


        elif choice1 == 2:
            bookid = int(input("Enter book id"))  # Prompt for book id to update
            name = input("Enter book name")
            author = input("Enter book author")
            price = float(input("Enter book price"))
            quantity = int(input("Enter book quantity"))
            sql = f"UPDATE book SET name='{name}', author='{author}', price={price}, quantity={quantity} WHERE bookid={bookid}"
            result = InsertUpdateDelete(sql)
            if result:
               print("Book updated")
            else:
               print("Failed to update book")


        elif choice1==3:
            bookid=int(input("enter book id"))
            sql=f"delete from book where bookid={bookid}"
            # print("sql=",sql)
            result=InsertUpdateDelete(sql)
            print("book deleted")
        

        elif choice1==4:
            sql="select * from book"
            DisplayTable(sql)

        elif choice1==5:
           break
        
        else:
            print("enter correct choice")
    elif choice == 2:
         print("--USER--")
         print("1.insert")
         print("2.update")
         print("3.delete")
         print("4.display")
         print("5.exit")
         choice2= int(input("enter choice"))
         if choice2==1:
            name=input("enter user name")
            address=input("enter address")
            identitynumber =float(input("enter id_number"))
            mobile=input("enter mobile_number")
            email=input("enter email")
            sql=f"insert into user(name,address,identitynumber,mobile,email) values('{name}','{address}','{identitynumber}','{mobile}','{email}')"
            # print("sql=",sql)2
            result=InsertUpdateDelete(sql)
           
            print("user added")
        


         elif choice2 == 2:
            userid = int(input("Enter user id"))  # Prompt for user id to update
            name = input("Enter user name")
            address = input("Enter address")
            identitynumber = input("Enter id_number")
            mobile = input("Enter mobile_number")
            email = input("Enter email")
            sql = f"UPDATE user SET name='{name}', address='{address}', identitynumber='{identitynumber}', mobile='{mobile}', email='{email}' WHERE userid={userid}"
            result = InsertUpdateDelete(sql)
            if result:
                print("User updated")
            else:
                print("Failed to update user")

            


         elif choice2==3:
            userid=int(input("enter user id"))
            sql=f"delete from user where userid={userid}"
            # print("sql=",sql)
            result=InsertUpdateDelete(sql)
            
            print("user deleted")
           

         elif choice2==4:
            sql="select * from user"
            DisplayTable(sql)

         elif choice2==5:
           break
    elif choice == 3:
        print("--LOAN--")
        print("1.insert")
        print("2.update")
        print("3.delete")
        print("4.display")
        print("5.exit")
        choice3= int(input("enter choice"))

        if choice3==1:
            bookid=int(input("enter book id"))
            userid=int(input("enter user id"))
            today=date.today()
            
            sql=f"insert into loan(bookid,userid,issuedate) values({bookid},{userid},'{today}')"
            # print("sql=",sql)2
            result=InsertUpdateDelete(sql)
           
            print("loan added")
        


        if choice3 == 2:
            loanid = int(input("Enter loan id"))  # Prompt for loan id to update
            bookid = int(input("Enter book id"))
            userid = int(input("Enter user id"))
            sql = f"UPDATE loan SET bookid={bookid}, userid={userid} WHERE loanid={loanid}"
            result = InsertUpdateDelete(sql)
            if result:
                print("Loan updated")
            else:
                print("Failed to update loan")

            


        elif choice3==3:
            loanid=int(input("enter loan id"))
            sql=f"delete from loan where loanid={loanid}"
            # print("sql=",sql)
            result=InsertUpdateDelete(sql)
            
            print("user deleted")
           

        elif choice3==4:
            sql="select * from loan"
            DisplayTable(sql)

        elif choice3==5:
           break
        
    elif choice == 4:
        break
    else:
        print("enter valid input")