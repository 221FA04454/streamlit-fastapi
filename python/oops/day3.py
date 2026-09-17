# # # inheritance part 2 
# # # sigle level
# # # multi level 

# # # multiple inheritance # having multiple parents and having single child
# # # hierarchial inheritance # single parent class and but multiple child class



# # # multiple inheritance

# # class Father:
# #     name="srinu" 

# #     def __init__(self):
# #         print("father init method")

# #     def Iq(self):
# #         v=150
# #         print(v)    

# # class Mother:
# #     name="anjali"

# #     def __init__(self):
# #         print("mother init method")

# #     def Iq(self):
# #         v=120
# #         print(v)     
        
# # class Child(Father,Mother):
# #     name="vamsi"

# #     def __init__(self):
# #         print("child method init")  
# #         print(Father.name) # srinu / anjali
# #         print(Mother.name)
# #         Father.Iq(self)
# #         Mother.Iq(self)

# # obj=Child()




# class Srinu:
#     name="srinu"
#     surName="Enduri" 

#     def __init__(self):
#         print("father init method")

#     def Iq(self):
#         v=150
#         print(v) 

#     def properties(self):
#         land=1
#         gold=1
#         silver=1
#         print(land,gold,silver)     


# class Srilekha(Srinu):

#     def __init__(self):
#         print(super().surName)
#         super().properties()

#     def abc(self):
#         print("asdfgh")    
        

# obj1=Srilekha()
# obj1.abc()
# print(obj1.surName,"line 75") # Enduri 





# class Vamsi(Srinu):

#     def __init__(self):
#         print(super().surName)
#         super().properties()

# obj2=Vamsi() 
# print(obj2.surName  )
# obj2.Iq()
# obj2.properties() 


# # pillars of oops 

# # inheritance
# encapsulation.

# en- capsule - ation 
# closed -- all covered - process

# password 
# atm pin 
# atm cvv



class HDFCBank:
    

    def __init__(self,b,p,n,a_t,amt):
        self.name=n 
        self.pincode =p 
        self.amount=amt 
        self.account_type=a_t 
        self.branch=b

    def atm_pin_generate(self,fpin,spin):
        if fpin == spin:
            self.pin=fpin # public var
                          # protected var  #resaerch point
            self.__pin=fpin              # private var
            print(self.__pin)


        
obj=HDFCBank("kukatpally",500072,"vamsiEnduri","savings",10000)
obj.atm_pin_generate("1234" , "1234")    
print(obj.pin)
print(obj.__pin)





# # polymorhism
# # abstraction