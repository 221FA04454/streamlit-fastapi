from fastapi import FastAPI  # line meaning
import json
obj=FastAPI()

# uvicorn main:obj --reload 

# http://localhost:8080 = @obj 
# http://localhost:8080/get_all_data =@obj.get("/get_all_data")
# http://localhost:8080/post_data =@obj.post("/post_data")
# http://localhost:8080/delete_data =@obj.delete("/delete_data")
# http://localhost:8080/edit_data =@obj.put("/edit_data")
# get operation
@obj.get("/get_all_users") # this api creation in be
def get_data():
    with open("users.json","r") as r_file:
        all_users=json.load(r_file)
        print(all_users)
        return all_users
    
    # db dataget 

@obj.post("/create_user")  # http://localhost:8080/post_data
def post_data(new_user:dict): # type annotation
    # name=new_user["name"]
    # email=new_user["email"]
    # password=new_user["password"]
    # role=new_user["role"]

    with open("users.json","r") as r_file:
        all_users=json.load(r_file)
        all_users.append(new_user)

    with open("users.json","w") as w_file:
        json.dump(all_users,w_file)  
        return {
            "msg":"user created successfullyyyy......."
        }  

@obj.delete("/delete_user/{email}")
def delete_user(email:str):
    with open("users.json","r") as r_file:
        all_users=json.load(r_file)
        for user in all_users: # [{},{}]
            if user["email"] == email :
                all_users.remove(user)
                with open("users.json","w") as w_file:
                    json.dump(all_users,w_file)
                    return "successfully deleted and data updated after deletion"
                # return "successfully deleted"
            else:
                continue                    
        else:
            print("no valid user found ")


#path parameters
@obj.put("/update_user/{email}") #"edit_user/ravi@gmailcom"
def edit_user(email:str,update_data:dict): # type annotation
    with open("users.json","r") as r_file:
        all_users=json.load(r_file)
        for user in all_users:
            if user["email"] == email:
                user["name"] = update_data["name"]  # current matched dict mame key value changing
                user["password"]  = update_data["password"] # current matched dict password key value changing
                with open("users.json","w") as w_file:
                    json.dump(all_users,w_file)
                    return "user updated successfully..."
            else:
                continue
        else:
            return "no user found with provided email"            

# decorator

# query params
@obj.get("/users") # /users?email="ravi@gmail.com"
def get_single_user(email:str):
    with open("users.json","r") as r_file:
        all_users=json.load(r_file)
        for user in all_users:
            if user["email"] == email :
                return user


# @obj.get("/login")
# def login_func(email:str,password:str):


# data validation :-- pydantic 
# req-res lifecycle with fe+be 
# req body - res body 
