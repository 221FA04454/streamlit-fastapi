import json 

i=int(input("choose 1.register   2.login   3.logout")) # 1

def read_json_file():
     with open("reg_user_data.json","r") as r_file:
        users=json.load(r_file) # reading json file / loading json file into python object 
        print(type(users))
        return users

def register():
    n=input("enter name")
    e=input("enter emial")
    p=input("enter password")
    c_p=input("enter c_password")
    new_reg_user_data={
        "name":n,
        "email":e,
        "password":p,
        "c_password":c_p
    }

    try:
       users=read_json_file()
    except FileNotFoundError:
        print("you are trying to read un-defined file")

    if new_reg_user_data["password"] == new_reg_user_data["c_password"]:
        users.append(new_reg_user_data)
        print(users)
        with open("reg_user_data.json","w") as w_file: # writing data to file
            json.dump(users,w_file)

        print("user added successfully to db")    

def login():
    e=input("enter emial")
    p=input("enter password")

    users=read_json_file()

    for index,user in enumerate(users):
        if e == user["email"] and p == user["password"]:
            print(index)
            print("login successful")
            print("1. edit yr profile 2.delete yr profile")
            i1=input("choose 1 edit r 2 delete ")
            if i1=="1":
                pass
                # users.remove
            elif i1=="2"  :
                users.pop(index)

                with open("reg_user_data.json","w") as w_file:
                    json.dump(users,w_file)
            break
        else:
            continue 
    else:
        print("user not founs")           



    






















if i == 1:
    register()
elif i==2:
    login()
else:
    logout()       