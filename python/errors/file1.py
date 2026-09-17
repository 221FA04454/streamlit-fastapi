# # # errors :-- 
# # a=10
# # abcName=20
# # _abc=200
# # abc124=2000

# # *abc =10
# # &abc 
# # @abc 
# # 123
# # abc    name =

# # for i in "vamsi","ravu":



# # errors even befpre executing the single line
# syntax error 
# 1avc=100
# print(1avc)

# errorName:- syntax error
# error_statement :-- invalid decimal literal

# indentation error 
# a=10
# print(a) 

# errorName:- indentation error
# error_statement :-- unexpected indent

# # errors at execution time :
# name error 
# a=10
# b=20
# c=a+b 
# print(d)

# errorName :-- NameError
# error_statement :-- name 'd' is not defined


# type error

# a=10
# b=10.5
# c="vamsi"
# print(c+c)
# # print(a+b+c)
# print(a*c)
# print(2 * [1,2,3])
# print(2 * {"id":1})

# # errorName :-- TypeError
# # error_statement :-- unsuppotrted opearnd types




# key error
# d={
#     "id":1,
#     "name":"vamsi"
# } 
# print(d)
# print(d["id"])
# print(d["name"])
# print(d["age"])
# print(d["loc"])

# # errorName :-- KeyError
# # error_statement :-- 'age'




# attribute error 

# class A: # class
#     name="vamsi" # var = attribute
#     def abc(self): # func = method
#         print("vamsi")
# obj=A()
# print(obj.name)
# obj.abc()
# obj.xyz()

# # errorName :-- AttributeError
# # error_statement :-- A object has no attribute 'abc'


# zeroDivsionError 

# a=10
# b=0
# c=a/b 
# print(c)

# # errorName :-- ZeroDivisonError
# # error_statement :-- division by zero





# modulenotfound error 

# from klmno import xyz 
# print(xyz)

# # errorName :-- ModuleNotFoundError
# # error_statement :-- no module named klmno



# unboundlocalError


a=10

def xyz():
    a+=10
    print(a)
xyz() 


# # errorName :-- UnboundLocalError
# # error_statement :-- cannot access local varible 'a' where it is not associated with it


# value error  # research topic


# error handling r exceptional handling

try 
except  
finally
else 


raise :-- create own custom error 


