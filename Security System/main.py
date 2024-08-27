import mysql.connector as my 
import time 
import os
import random
import sys
passw = input("Your SQL Password : ")
con = my.connect(host= 'localhost',\
                 user = "root",\
                 passwd  = passw)
cur = con.cursor() 

def database():
     queries = ['create database Security','use Security','create table data (Username VARCHAR(20) NOT NULL, Password VARCHAR(20) NOT NULL, Email VARCHAR(40) NOT NULL,ID int(5), Name VARCHAR(15), Phn VARCHAR(10), DOB DATE)','INSERT INTO data (Username, Password, Email,ID, Name, Phn, DOB) VALUES ("UtsavGupta99", "Utsav@1234", "utsav@gmail.com",10000 ,"Utsav Gupta", "8076043638", "2005-12-15")']
     for j in queries :
          cur.execute(j)
     con.commit()


def ID_chk() : 
     global ID_list
     cur.execute('select ID from data')
     ID_list = cur.fetchall()


def Choose(): 
      print("Welcome TO My Security System :=) ")
      time.sleep(2)
      y = int(input('''Login [Press 1 ] :\nSignUp [Press 2] :'''))
      if y == 1 : 
        login()
        os.system('cls')
      else :
        signup()
        os.system('cls')

def login() : 
    global ID
    ID_chk()
    username = input("Enter Your Username : ")
    password = input("Enter Password : ")
    cur.execute('select ID from data where Username ="{}" and Password ="{}"'.format(username,password))
    ID = cur.fetchall()
    login_check(ID)


def login_check(ID):    
        ID_chk()
        if ID != [] and ID[0] in ID_list  :
            print("Checking Your Credentials  ")
            time.sleep(3)
            print("Sucessfull login :)")
            time.sleep(2)
            print("Taking You To Your Account....")
            time.sleep(3)
            os.system('cls')
            cur.execute('select Username,Password,Email,Name,Phn,DOB from data where ID="{}"'.format(ID[0][0]))
            temp_data = cur.fetchall()
            print("Name = ",temp_data[0][3],"\n"
                "Phone Number = ",temp_data[0][4],"\n"
                "Date Of Birth = ",temp_data[0][5],"\n"
                "Username = ",temp_data[0][0],"\n"
                "Password = ",temp_data[0][1],"\n"
                "Email = ",temp_data[0][2],"\n")
            print()
            x = int(input('''Edit your Info [Press 1 ] :\nLogout[Press 2 ] : '''))
            con.commit()
            if x == 1 :
                login_Update(ID)
            elif x == 2 :
                print("Logging Out....")
                time.sleep(2)
                os.system('cls')
                Choose()
        else : 
            print("Incorrect Credentials :() ") 
            time.sleep(1)
            z = int(input("Reset Password [Press 1] :\nRetry [Press 2] :"))
            os.system('cls')
            if z == 1 :
                reset()
            else : 
                 login()

def reset(): 
    ID_chk()
    u = input("Enter Your Username :")
    m = input("Enter Your Mail : ")
    cur.execute('select ID from data where Username ="{}" and Email ="{}"'.format(u,m))
    ID_1 = cur.fetchall()
    if ID_1 != [] and ID_1[0] in ID_list  :
        print("Success")
        time.sleep(2)
        Pass = input("Enter your New Password : ")
        cur.execute('Update data Set Password = "{}" where ID ="{}"'.format(Pass,ID_1[0][0]))
        con.commit()
        print("Password Reset successfully :) ")
        time.sleep(2)
        os.system('cls')
        login()
    else : 
         print("Incorrect Mail or Username : ")
         print("RETRY ")
         time.sleep(5)
         os.system('cls')
         reset()



def login_Update(ID):
            ID_chk()
            os.system("cls")
            new_username=input("Enter Username : ")
            cur.execute('update data set Username = "{}" where ID = "{}"'.format(new_username,ID[0][0]))
            new_password=input("Enter Password : ")
            cur.execute('update data set Password = "{}" where ID = "{}"'.format(new_password,ID[0][0]))
            new_mail=input("Enter Email : ")
            cur.execute('update data set Email = "{}" where ID = "{}"'.format(new_mail,ID[0][0]))
            print("Wait Updating in Proceess.....")
            time.sleep(3)
            print("Successfull :)")
            con.commit()
            time.sleep(2)
            os.system('cls')
            login_check(ID)

def signup():
     i = 1
     j = 1
     ID_chk()
     name = input("Enter Your Name : ")
     phn = input("Enter Your Phone Number : ")
     dob = input("Enter Your Date of Birth [YYYY-MM-DD] : ")
     username = input("Set Your Username [8-12 Characters]: ")
     while i != 0 :   
        password = input("Set Your Password [8-15 Characters]: ")
        password_repeat = input("Repeat Your Password [8-15 Characters]: ")
        if password == password_repeat :
             i = 0
     email = input("Set Password Recovery Mail : ")
     while j != 0:
          ID_2 = random.randint(10000,99999)
          if (ID_2,) in ID_list :
               continue
          else : 
               j = 0
     print("Wait Creating Your Account.....")
     cur.execute('Insert into data Values ("{}","{}","{}","{}","{}","{}","{}")'.format(username,password,email,ID_2,name,phn,dob))
     con.commit()
     time.sleep(3)
     print("Account Created :)")
     print("Redirecting You to Login....")
     time.sleep(3)
     os.system('cls')
     login()
def database_chk():     
    c = 0
    cur.execute('show databases')
    abc = cur.fetchall()
    for m in abc : 
        if m[0] == 'security' or m[0] == 'Security' : 
           c = 1
    if c == 0 : 
         print("Database Not Found, Creating a New Database....")
         time.sleep(3)
         os.system('cls')
         database()
    else:
         cur.execute('use security')

database_chk()
ID_chk()
Choose() 