
# # a=10
# # b=0
# # print(a/b)


# # def abc():
# #     a=10
# #     b=20
# #     print(a+b)

# # abc()
# # abc()
# # abc()
# # abc()
# # abc()




# # try-except 

# # try:
# #     a=10
# #     b=0
# #     print(a/b)
# # except ZeroDivisionError:
# #     print("you cant divide a integer with 0")  


# # def abc():
# #     a=10
# #     b=20
# #     print(a+b)

# # abc()
# # abc()
# # abc()
# # abc()
# # abc()    

# # try-except-multiple

# try:
#     # a=10
#     # b=0
#     # print(a/b)
#     a=10.5
#     b=dict(a)
#     print(b)
# except ZeroDivisionError:
#     print("you cant divide a integer with 0")  
# except ValueError:
#     print("yiu cant convert that value into naother value") 
# except NameError:
#     print("you have not defined a name and tryng access it")
# except ModuleNotFoundError:
#     print("yiu are trying import unnown moudle") 
# except TypeError:
#     print("cant combvert one type to anoteher type")              


# def abc():
#     a=10
#     b=20
#     print(a+b)

# abc()
# abc()
# abc()
# abc()
# abc()   


# users=[{"id":1,"name":"vamsi","password":"12345678"}]

foodItems=["pizza","burger","momos","juice"]
email="vamsi@gmail.com"
password="12345678"

class foodNotAvailable(Exception):
    pass 

def login(e,p):

    if email == e and password == p:
        print("login successful")
        item_name=input("enter food item name here :-- ")
        try:
            if item_name not in foodItems:
                raise foodNotAvailable(item_name,"is not availble in food item slist")
        except foodNotAvailable:
            return {
                "msg":"search for only avaibl items" 
            }      
    else:
        print("invalid credentials")

login("vamsi@gmail.com","12345678")    