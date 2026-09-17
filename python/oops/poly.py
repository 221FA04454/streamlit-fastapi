# # # method - over-riding
# # class Manager:
# #     name="VamsiEnduri" 

# #     def __init__(self):
# #         print("parent init method")

# #     def role_experience(self):
# #         role="manager"
# #         exp=12
# #         print(role,exp)


# # class SrEmployee(Manager):
# #     name="ravi"

# #     def __init__(self):
# #         print("srEmployee class init method")

# #     def role_experience(self):
# #         role="srEmployee"
# #         exp=7
# #         print(role,exp)

# # obj1=SrEmployee()
# # obj1.role_experience()



        
# # class JrEmployee(Manager):
# #     name="akhil"

# #     def __init__(self):
# #         print("jrEmp init method")

# #     def role_experience(self):
# #         role="jrEmployee"
# #         exp=3
# #         print(role,exp)     

# # obj2=JrEmployee()
# # obj2.role_experience()




# # -- method overloading 

# class Manager:
#     name="VamsiEnduri" 

#     def __init__(self):
#         print("parent init method")

#     def role_experience(self):
#         role="manager"
#         exp=12
#         print(role,exp)

#     def details(self):
#         pass    


# class SrEmployee(Manager):
#     name="ravi"

#     def __init__(self):
#         print("srEmployee class init method")

#     def role_experience(self):
#         role="srEmployee"
#         exp=7
#         print(role,exp)

#     def details(self,**v):
#         print(v)    

# obj1=SrEmployee()
# obj1.role_experience()
# # obj1.details("ravi",26,"10000coders","javaTrainer&dev","3+",500072,"akhil","rakesh")
# obj1.details(name="ravi",age=26,company="10000coders",role="javaTrainer&dev",exp="3+",pincode=500072,manager="akhil",ceo="rakesh")


# duck typing

# class A:
#     def xyz(self):
#         print("hello")

# obj1=A()
# class B:
#     def xyz(self):
#         print("hi")

# obj2=B()

# def call_it(o):
#     o.xyz()

# call_it(obj1) # hello
# call_it(obj2) # hi