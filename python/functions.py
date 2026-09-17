# a="vamsi"
# b=27
# skills=["pf","mern","ds","da","genai","agenticai"]

# if 10 == 10:
#     print(True)
# else :
#     print(False)

# def add():
#     a=10
#     b=20
#     print(a+b)
   
# add()    

# # function without any args and params and return keyword
# def mul():
#     a=10
#     b=20
#     print(a*b)

# mul()   # 



# # function with params and args 

# # # args / arguments :-- 
# # the values which we pass during function calling
# # # params 
# # the identifiers which recieve the incoming args data

# # def details(x,y):
# #     print(123)
# # details(10,20)    



# # function with only return keyword but not with args and params

# rEmail="vamsi@gmail.com"
# rPassword="vamsi@123"

# def login():

#     lEmail=input("enter email to login :-   ")
#     lPassword=input("enter password to login :--  ")

#     if rEmail == lEmail and rPassword == lPassword :
#         print("login successfull")
#         return True
#     else:
#         print("invalid credentials") 
#         return False      

# op=login() #True


# if op == True :
#     print("dashboard")
# else:
#     print("login")    





# function with *args -- variable lenth arguments

def abc(*p):
    print(p)

abc(1,2,3)    

# function with  :-- keyword length args

def details(name,age):
    print(name,age)
details(name="vamsi",age=31)    

# function with  **args:-- keyword length args
def details(**p):
    print(p)
details(name="vamsi",age=31)