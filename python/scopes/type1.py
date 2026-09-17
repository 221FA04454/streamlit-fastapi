# # # # # # functions :--
# # # # # # in :-- 
# # # # # # u :-- 


# # # # # # variables


# # # # # # global variables
# # # # # # class variables
# # # # # # local variables
# # # # # # instance variables
# # # # # fileName="typ1.py" # global var
# # # # # class Vamsi:
# # # # #     clasName="vamsi" # class var
# # # # #     def abc(self,a,b):
# # # # #         self.a=a # instance var1
# # # # #         self.b=b # instance var2
# # # # #         nameOfTheFunction="abc" # local var
# # # # # obj=Vamsi()   
# # # # # obj.abc(1,2)

# # # # # # scopes :-- 
# # # # # # scope :-- the process of accessing var r function r class in a specific area only

# # # # # # LEGB rule in python :-- 
# # # # # # local enclosed global built-in scopes 


# # # # # # global scope 

# # # # # a=10 # global var / global scoped varaible

# # # # # print(a)





# # # # local scope 
# # # def abc():
# # #     a=10
# # #     print()













































# # # # # def mno():
# # # # #     print(a)
# # # # # mno()    

# # # # # class B:
# # # # #     print(a)












# # # # # print(a)

# # m=10

# # # # print(a)


# # # # def xyz():
# # # #     a=10
# # # #     b=20
# # # #     c=a+b+abc
# # # #     print(c)



# # # local scope :

# # def abc():
# #     x=10 # LOCAL SCOPED VAR
# #     y=20 # local socped var
# #     z=x+y
# #     print(m) # global scoped var
# #     print(z)
# # abc()    

# # print(x+y) # local scoped varaibes trying to access outside of function      
# # print(m)  # global scoped var



# store_name="zepto" # global scoped var
# def shopping_cart(name):
#     cartHolder=name # enclosed scoped var

#     cart_items_count=10
#     cart_item_price=100 #local scoped var
#     print(cartHolder) # local scoped 

#     def checkout():

#         totalPrice=cart_items_count*cart_item_price # local scoped var
#         print(totalPrice) # current memory scoped var access
#         print(cartHolder) # current memeory parent scoped var access # accessing enclsoed var
#         print(store_name) # current memoey top level parent scoped var access

#     checkout()    
# shopping_cart("vamsi")

# global keyword:--

cartItems=0
print(cartItems)

def cart():
    global cartItems # abilityto modify the upper scoped var :-- unbound local varible
    cartItems+=10
    print(cartItems) # 10
cart()    

print(cartItems)