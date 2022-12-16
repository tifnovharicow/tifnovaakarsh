import os,getpass as g
print("Welcome to Cloth Store")
print("1)Sign Up\n2)Login\n3)Admin\nChoose your option:")
cld={1:['Jeans', 500],2:['cordruoy',600]}
userdict={'Aakarsh376':'your_mom',  'Chinzxzmai':'qwerty','Tivon':'qwerty'}
a=int(input())
os.system('cls')
if a==1:
    login_id=input("Sign in ID:")
    pswd=input("Password:")
    userdict[login_id]=pswd
    print("user id created")
    os.system('cls')
elif a==2:
    login_id=input("Login ID:")
    pswd = g.getpass("Password:")
    if login_id in userdict and userdict[login_id] == pswd:
        print("Login successful!")
        os.system('cls')
    v_gender=input("enter gender:")
    v_phone_no=int(input("enter your phone no:"))
    os.system('cls')
    print("Products\n1.",cld[1][0],"\t",cld[1][1],"\n2.",cld[2][0],"\t",cld[2][1],"\n")
    c=int(input("enter your choice"))
    for r in range(1,3):
          if (c==r):
              print(cld[r][0])
              
    v_qty=int(input("enter quantity:"))
    v_payment=int(input("make payment:"))
