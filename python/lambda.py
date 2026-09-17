# what is lambda function in python ?
# what is comprhensions in python ? types ?
# what are map(), filter()methods in python ?
# what is while loop ?
# dict methods  in python ?


# dict methods  in python ? 
# what is dict ?
# dict methods 

# d={
#     "id":1,
#     "name":"vamsi",
#     "age":27,
#     "loc":"Hyd"
# } 
# # print(d)  # entire dict
# # print(d["id"]) # single key
# # print(d["name"]) # single key

# # get()
# a=d.get("id")
# print(a) # 1
# print(d.get("name")) # 1

# # keys()
# for i in d.keys():
#     print(i)

# # values()
# for i in d.values():
#     print(i)

# # items()
# for i in d.items():
#     print(i)
# # copy()
# copiedDict=d.copy()
# print(copiedDict)


# # pop()
# copiedDict.pop("loc")
# print(copiedDict) # 
# # popIndex() research method

# # update() add / modify
# copiedDict.update({"salary":451234}) # adding
# copiedDict.update({"age":32}) # modifying

# print(copiedDict)

# # clear()
# copiedDict.clear()
# print(copiedDict)


# while loop :

# syntax :-- 
# while condition:
# #     code 

# # 1-10 while loop 
# i=1 # 2 3
# while i<=10: #i<= 10
#     print(i) # 1
#     i+=1

# # 10-1 while loop 
# i=10
# while i>0: # i>0
#     print(i)
#     i-=1



# lambda  
# is short-hand for normal deffunctions in python 

# syntax :--
# res=lambda param : code 
# res()

# def a(*a):
#     print(a) # ()
#     for i in a:
#         print(i) # 10
# a(10,20,30,40)


# lambda  
# is short-hand for normal deffunctions in python 

# syntax :--
# res=lambda param : code 
# res()

# a=lambda *h: h
# print(a(10,20,30,"vamsi"))


# # lambda + if-else :

# a=22
# res=lambda xyz:"even" if xyz % 2 == 0  else "non-even"
# print(res(a))


# # lambda + if-else + param :

# a=22
# res=lambda xyz:("even" if xyz % 2 == 0  else "non-even",xyz)
# print(res(a))




#  comprehensions

# 4 types 
# list  :-- [for  if]
# dict  :-- { for  if}

# res=[i*2 for i in range(1,11)]
# res2=[i**2 for i in range(1,11)]
# print(res)
# print(res2)


# lambda + list comprehension :-- 
# 1-10 print 

# res=lambda x,y: [print(i) for i in range(x,y)]
# res(1,11) 

# # lambda + dict comprehension :
# res = lambda incoming_dict: {print(i) for i in incoming_dict.items()} 
# res({"id":1,"name":"vamsi"})






# lambda + map 
# map(f,iterable) :-- map obj

res=list(map(lambda a: a*a , [1,2,3,4,5]))  #  list(<map Object>)
print(res)
# [1,4,9,16,25]

# lambda +filter research method
# filter(f,iterable) :-- filter obj
