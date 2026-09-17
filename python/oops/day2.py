# # phase 1 :-- 

# # vars 
# # global 
# # class 
# # function # local
# # instance var
# # enclosed scoped var


# i_name="10000coders" # gloabl var
# i_loc="kphb phase rd no 1" #global var

# class ABC: # class is b_p of obj
#     a=10 # class var

#     #default method - inbuilt method
#     # a is default param
#     #self - instance of class
#     def __init__(self,x,y): #parms # identifiers which we use to recive incoming data
#         print(x+y)

#     def abc(self):
#         xyz=100 # function / local var
#     # vars + functions
#     # attributes + methods
# obj=ABC(10,20)   # args = data whhich we pass dutring calling  
# # obj is instacne of the class
    

# inherutance : 
# the process of acquring properties of parent class by the child class  is called as 
# inherutance




class Srinu:
    # vars + functions
    surName="Enduri" # clas var

    def __init__(self,inc_v1,inc_v2):
        print(inc_v1,inc_v2)
        self.v1=inc_v1
        self.v2=inc_v2
    

    def color(self): # defined method
        c="white" #local var
        print(c) 

    def Iq(self):
        iq=170 # local var
        print(iq)   


class Vamsi(Srinu):
    
    def __init__(self,x,y):
        super().__init__(x,y) # = Srinu()
        print(super().surName) # accessing parent class var in child class
        super().color()
        super().Iq()


class VamsiChild(Vamsi):
    def __init__(self,x,y):
        super().__init__(x,y)


obj=VamsiChild(10,20)
print(obj.v1)
print(obj.v2)


# 10 20
# Enduri
# white
# 170
